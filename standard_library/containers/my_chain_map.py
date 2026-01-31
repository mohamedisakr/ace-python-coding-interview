class MyChainMap:
    def __init__(self, *maps):
        # We store the underlying mappings as a list (the 'chain')
        # f_1, f_2, ... f_n
        self.maps = list(maps) if maps else [{}]

    def __getitem__(self, key):
        # The core search logic: f_chain(x) = f_i(x) for min(i)
        for mapping in self.maps:
            if key in mapping:
                return mapping[key]
        raise KeyError(f"Key {key} not found in any layer.")

    def __setitem__(self, key, value):
        """
        Use "Search-and-Update" if Underlying layers are "Mutable", or use Standard __setitem__
        if Underlying layers are "Read-Only"

        :param self: Description
        :param key: Description
        :param value: Description
        """
        # Mutations are restricted to the first mapping (the local scope)
        # for mapping in self.maps:
        #     if key in mapping:
        #         mapping[key] = value
        #         return
        self.maps[0][key] = value

    def __delitem__(self, key):
        # Attempting to delete from the root; math dictates
        # we can't delete what isn't in the top layer.
        try:
            del self.maps[0][key]
        except KeyError:
            # raise KeyError(f"Key {key} not found in the first layer.")
            # raise KeyError(f"Key 'secret_key' not found in the first layer.") from exc
            raise KeyError(f"Key {key} not found in the first layer.")

    def new_child(self, m=None):
        # Creates a new scope (S_0) above the current ones
        return MyChainMap(m or {}, *self.maps)

    def __iter__(self):
        seen = set()
        for mapping in self.maps:
            for key in mapping:
                if key not in seen:
                    yield key
                    seen.add(key)

    @property
    def parents(self):
        # Returns the 'tail' of the list (all layers except the first)
        return MyChainMap(*self.maps[1:])

    def __repr__(self):
        return f"MyChainMap({', '.join(map(str, self.maps))})"
