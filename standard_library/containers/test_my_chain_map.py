from .my_chain_map import MyChainMap

import unittest


class TestMyChainMap(unittest.TestCase):
    def setUp(self):
        self.global_layer = {'a': 1, 'b': 2}
        self.local_layer = {'b': 99}
        self.cm = MyChainMap(self.local_layer, self.global_layer)

    def test_priority_lookup(self):
        """Math: f_chain(b) should return f_local(b) because it shadows."""
        self.assertEqual(self.cm['b'], 99)
        self.assertEqual(self.cm['a'], 1)

    def test_mutation_isolation(self):
        """Math: Writes only affect the first set (S_0)."""
        self.cm['c'] = 42
        self.assertEqual(self.local_layer['c'], 42)
        self.assertNotIn('c', self.global_layer)

    def test_new_child_scope(self):
        """Math: new_child adds a layer at index 0."""
        child = self.cm.new_child({'d': 100})
        self.assertEqual(child['d'], 100)
        self.assertEqual(child['b'], 99)  # Still sees parent's shadow

    def test_empty_initialization(self):
        """Math: Ensure the map is never empty (Avoids IndexError)."""
        empty_cm = MyChainMap()
        try:
            empty_cm['key'] = "Safe"
        except IndexError:
            self.fail("MyChainMap raised IndexError with empty initialization!")

    def test_missing_key(self):
        """Math: Key lookup on a key not in the Union should raise KeyError."""
        with self.assertRaises(KeyError):
            _ = self.cm['non_existent']

    def test_iteration_uniqueness(self):
        """Math: Iteration should represent the Union (S1 ∪ S2) without duplicates."""
        # self.local_layer = {'b': 99}
        # self.global_layer = {'a': 1, 'b': 2}
        keys = list(self.cm)

        # We expect 'a' and 'b', but 'b' should only appear ONCE.
        self.assertEqual(len(keys), 2)
        self.assertIn('a', keys)
        self.assertIn('b', keys)

        # Verify the order (optional, but ChainMap usually preserves it)
        # The first 'b' seen is the one from local_layer
        self.assertEqual(keys, ['b', 'a'])


if __name__ == '__main__':
    unittest.main()

# def test_my_chain_map():
#     # Setup layers
#     global_layer = {'a': 1, 'b': 2}
#     local_layer = {'b': 99}

#     # Initialize
#     cm = MyChainMap(local_layer, global_layer)

#     # --- Test 1: Priority Lookup (Shadowing) ---
#     # b exists in both, but local_layer should win.
#     assert cm['b'] == 99, "Error: Shadowing logic failed. Should get value from first layer."
#     assert cm['a'] == 1, "Error: Fall-through lookup failed."

#     # --- Test 2: Mutation Invariant ---
#     # Writing to the ChainMap should only affect the first dictionary.
#     cm['c'] = 42
#     assert local_layer['c'] == 42, "Error: Write didn't go to the top layer."
#     assert 'c' not in global_layer, "Error: Write leaked into a deeper layer."

#     # --- Test 3: New Child (Scoping) ---
#     # Create a deeper nested scope
#     child = cm.new_child({'d': 100})
#     assert child['d'] == 100, "Error: Child lookup failed."
#     assert child['b'] == 99, "Error: Child failed to see parent layers."

#     # --- Test 4: Boundary Condition (Empty Init) ---
#     # This addresses your concern about the IndexError
#     empty_cm = MyChainMap()
#     try:
#         empty_cm['new_key'] = "Safe"
#         assert empty_cm['new_key'] == "Safe"
#     except IndexError:
#         print("Test 4 Failed: IndexError on empty initialization!")
#         return

#     # --- Test 5: Missing Keys ---
#     try:
#         _ = cm['non_existent']
#         assert False, "Error: Should have raised KeyError."
#     except KeyError:
#         pass  # Expected behavior

#     print("✅ All Knuthian tests passed!")


# # Run the tests
# test_my_chain_map()
