# https: // stackoverflow.com/questions/25894948/make-an-array-work-like-a-circle

class CircularList(list):
    def __getitem__(self, index):
        return super().__getitem__(index % len(self))

    def __setitem__(self, index, value):
        super().__setitem__(index % len(self), value)

    def get_item_with_distance(self, item, distance):
        index = self.index(item)
        return self[index + distance]

    def set_item_with_distance(self, item, distance, value):
        index = self.index(item)
        self[index + distance] = value


# class CircularList(list):
#     def __init__(self, *args):
#         super().__init__(*args)
#         self.item_to_index = {item: idx for idx, item in enumerate(self)}

#     def __getitem__(self, index):
#         return super().__getitem__(index % len(self))

#     def __setitem__(self, index, value):
#         original_index = index % len(self)
#         original_value = super().__getitem__(original_index)
#         super().__setitem__(original_index, value)
#         if original_value in self.item_to_index:
#             del self.item_to_index[original_value]
#         self.item_to_index[value] = original_index

#     def get_item_with_distance(self, item, distance):
#         index = self.item_to_index[item]
#         return self[index + distance]

#     def set_item_with_distance(self, item, distance, value):
#         index = self.item_to_index[item]
#         target_index = (index + distance) % len(self)
#         original_value = self[target_index]
#         self[target_index] = value
#         if original_value in self.item_to_index:
#             del self.item_to_index[original_value]
#         self.item_to_index[value] = target_index

#     def __delitem__(self, index):
#         original_index = index % len(self)
#         original_value = super().__getitem__(original_index)
#         super().__delitem__(original_index)
#         if original_value in self.item_to_index:
#             del self.item_to_index[original_value]
#         self.item_to_index = {item: idx for idx, item in enumerate(self)}

#     def append(self, value):
#         super().append(value)
#         self.item_to_index[value] = len(self) - 1

#     def extend(self, iterable):
#         super().extend(iterable)
#         self.item_to_index = {item: idx for idx, item in enumerate(self)}


"""
Optimized Circular List 
"""


# class CircularList(list):
#     def __init__(self, *args):
#         super().__init__(*args)
#         self.item_to_index = {item: idx for idx, item in enumerate(self)}

#     def __getitem__(self, index):
#         return super().__getitem__(index % len(self))

#     def __setitem__(self, index, value):
#         original_index = index % len(self)
#         original_value = super().__getitem__(original_index)
#         # Update the list
#         super().__setitem__(original_index, value)
#         # Update the index mapping
#         if original_value in self.item_to_index:
#             del self.item_to_index[original_value]
#         self.item_to_index[value] = original_index

#     def get_item_with_distance(self, item, distance):
#         index = self.item_to_index[item]
#         return self[index + distance]

#     def set_item_with_distance(self, item, distance, value):
#         index = self.item_to_index[item]
#         self[index + distance] = value

#     def __delitem__(self, index):
#         original_index = index % len(self)
#         original_value = super().__getitem__(original_index)
#         super().__delitem__(original_index)
#         # Update the index mapping
#         if original_value in self.item_to_index:
#             del self.item_to_index[original_value]
#         # Rebuild the index map
#         self.item_to_index = {item: idx for idx, item in enumerate(self)}

#     def append(self, value):
#         super().append(value)
#         # Update the index mapping
#         self.item_to_index[value] = len(self) - 1

#     def extend(self, iterable):
#         super().extend(iterable)
#         # Update the index mapping
#         self.item_to_index = {item: idx for idx, item in enumerate(self)}
