import unittest
from .doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()

        self.empty_list = DoublyLinkedList()
        self.single_item_list = DoublyLinkedList()
        self.single_item_list.insert_at_tail(10)
        self.multi_item_list = DoublyLinkedList()
        self.multi_item_list.insert_at_tail(20)
        self.multi_item_list.insert_at_tail(30)
        self.multi_item_list.insert_at_tail(40)

    # ----- insert tail ------
    def test_empty_list(self):
        # Insert into an empty list
        self.dll.insert_at_tail(10)
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.tail.data, 10)
        self.assertEqual(self.dll.head.next, None)
        self.assertEqual(self.dll.tail.prev, None)

    def test_single_node_list(self):
        # Insert into a list with one node
        self.dll.insert_at_tail(10)
        self.dll.insert_at_tail(20)
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.tail.data, 20)
        self.assertEqual(self.dll.head.next.data, 20)
        self.assertEqual(self.dll.tail.prev.data, 10)

    def test_multiple_node_list(self):
        # Insert into a list with multiple nodes
        self.dll.insert_at_tail(10)
        self.dll.insert_at_tail(20)
        self.dll.insert_at_tail(30)
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.tail.data, 30)
        self.assertEqual(self.dll.head.next.data, 20)
        self.assertEqual(self.dll.tail.prev.data, 20)
        self.assertEqual(self.dll.head.next.next.data, 30)
        self.assertEqual(self.dll.tail.prev.prev.data, 10)

    def test_insert_multiple_times(self):
        # Insert multiple values sequentially
        for i in range(1, 6):
            self.dll.insert_at_tail(i * 10)
        current = self.dll.head
        expected_values = [10, 20, 30, 40, 50]
        for value in expected_values:
            self.assertEqual(current.data, value)
            current = current.next
        self.assertEqual(self.dll.tail.data, 50)
        self.assertEqual(self.dll.count, 5)

    # -------- insert head --------

    def test_empty_list_head(self):
        # Insert into an empty list
        self.dll.insert_at_head(10)
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.tail.data, 10)
        self.assertEqual(self.dll.head.next, None)
        self.assertEqual(self.dll.tail.prev, None)

    def test_single_node_list_head(self):
        # Insert into a list with one node
        self.dll.insert_at_head(20)
        self.dll.insert_at_head(10)
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.tail.data, 20)
        self.assertEqual(self.dll.head.next.data, 20)
        self.assertEqual(self.dll.tail.prev.data, 10)

    def test_multiple_node_list_head(self):
        # Insert into a list with multiple nodes
        self.dll.insert_at_head(30)
        self.dll.insert_at_head(20)
        self.dll.insert_at_head(10)
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.tail.data, 30)
        self.assertEqual(self.dll.head.next.data, 20)
        self.assertEqual(self.dll.tail.prev.data, 20)
        self.assertEqual(self.dll.head.next.next.data, 30)
        self.assertEqual(self.dll.tail.prev.prev.data, 10)

    def test_insert_multiple_times_head(self):
        # Insert multiple values sequentially
        for i in range(1, 6):
            self.dll.insert_at_head(i * 10)
        current = self.dll.head
        expected_values = [50, 40, 30, 20, 10]
        for value in expected_values:
            self.assertEqual(current.data, value)
            current = current.next
        self.assertEqual(self.dll.tail.data, 10)
        self.assertEqual(self.dll.count, 5)

    # ---- delete -----

    def test_empty_list_delete(self):
        # Delete from an empty list
        self.dll.delete(10)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)

    def test_single_node_list_delete(self):
        # Delete the only node in the list
        self.dll.insert_at_tail(10)
        self.dll.delete(10)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)

    def test_delete_head(self):
        # Delete the head node in a list with multiple nodes
        self.dll.insert_at_tail(10)
        self.dll.insert_at_tail(20)
        self.dll.insert_at_tail(30)
        self.dll.delete(10)
        self.assertEqual(self.dll.head.data, 20)
        self.assertEqual(self.dll.head.next.data, 30)
        self.assertIsNone(self.dll.head.prev)
        self.assertEqual(self.dll.tail.data, 30)

    def test_delete_tail(self):
        # Delete the tail node in a list with multiple nodes
        self.dll.insert_at_tail(10)
        self.dll.insert_at_tail(20)
        self.dll.insert_at_tail(30)
        self.dll.delete(30)
        self.assertEqual(self.dll.tail.data, 20)
        self.assertEqual(self.dll.tail.prev.data, 10)
        self.assertIsNone(self.dll.tail.next)
        self.assertEqual(self.dll.head.data, 10)

    def test_delete_middle_node(self):
        # Delete a node that is neither head nor tail in a list with multiple nodes
        self.dll.insert_at_tail(10)
        self.dll.insert_at_tail(20)
        self.dll.insert_at_tail(30)
        self.dll.insert_at_tail(40)
        self.dll.delete(20)
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.head.next.data, 30)
        self.assertEqual(self.dll.head.next.prev.data, 10)
        self.assertEqual(self.dll.tail.data, 40)

    def test_delete_non_existent_node(self):
        # Attempt to delete a value that does not exist in the list
        self.dll.insert_at_tail(10)
        self.dll.insert_at_tail(20)
        self.dll.insert_at_tail(30)
        self.dll.delete(40)
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.tail.data, 30)
        self.assertEqual(self.dll.count, 3)

    # ---------- delete head -----------

    def test_empty_list_delete_at_head(self):
        # Delete from an empty list
        self.dll.delete_at_head()
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)

    def test_single_node_list_delete_at_head(self):
        # Delete the only node in the list
        self.dll.insert_at_tail(10)
        self.dll.delete_at_head()
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)

    def test_multiple_node_list_delete_at_head(self):
        # Delete the head node in a list with multiple nodes
        self.dll.insert_at_tail(10)
        self.dll.insert_at_tail(20)
        self.dll.insert_at_tail(30)
        self.dll.delete_at_head()
        self.assertEqual(self.dll.head.data, 20)
        self.assertIsNone(self.dll.head.prev)
        self.assertEqual(self.dll.head.next.data, 30)
        self.assertEqual(self.dll.tail.data, 30)
        self.assertEqual(self.dll.tail.prev.data, 20)

    def test_consecutive_deletes(self):
        # Consecutively delete head nodes
        self.dll.insert_at_tail(10)
        self.dll.insert_at_tail(20)
        self.dll.insert_at_tail(30)
        self.dll.insert_at_tail(40)

        self.dll.delete_at_head()
        self.assertEqual(self.dll.head.data, 20)
        self.assertEqual(self.dll.tail.data, 40)

        self.dll.delete_at_head()
        self.assertEqual(self.dll.head.data, 30)
        self.assertEqual(self.dll.tail.data, 40)

        self.dll.delete_at_head()
        self.assertEqual(self.dll.head.data, 40)
        self.assertEqual(self.dll.tail.data, 40)

        self.dll.delete_at_head()
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)

    # ----- get head -------

    def test_get_head_empty_list(self):
        self.assertIsNone(self.empty_list.get_head(),
                          "Head of an empty list should be None.")

    def test_get_head_single_item_list(self):
        self.assertEqual(self.single_item_list.get_head(
        ).data, 10, "Head of a single item list should be the first item inserted.")

    def test_get_head_multi_item_list(self):
        self.assertEqual(self.multi_item_list.get_head(
        ).data, 20, "Head of a multi-item list should be the first item inserted.")

    def test_get_head_after_insertion(self):
        self.single_item_list.insert_at_tail(20)
        self.assertEqual(self.single_item_list.get_head().data,
                         10, "Head should not change after insertion at the end.")

    def test_get_head_after_deletion(self):
        self.single_item_list.delete_at_head()
        self.assertIsNone(self.single_item_list.get_head(
        ), "Head of list should be None after deleting the only item.")

    def test_get_head_after_clearing_list(self):
        self.multi_item_list.clear()
        self.assertIsNone(self.multi_item_list.get_head(),
                          "Head should be None after clearing the list.")

    # -------- reverse ------

    def test_single_node(self):
        self.dll.insert_at_tail(1)
        self.dll.reverse()
        self.assertEqual(str(self.dll), "1")

    # @unittest.skip('slow')
    def test_multiple_nodes(self):
        for i in range(1, 6):
            self.dll.insert_at_tail(i)
        self.dll.reverse()
        self.assertEqual(str(self.dll), "5 -> 4 -> 3 -> 2 -> 1")

    # @unittest.skip('slow')
    def test_empty_list_reverse(self):
        self.dll.reverse()
        self.assertEqual(str(self.dll), "")

    # @unittest.skip('slow')
    def test_two_nodes(self):
        self.dll.insert_at_tail(1)
        self.dll.insert_at_tail(2)
        self.dll.reverse()
        self.assertEqual(str(self.dll), "2 -> 1")

    # @unittest.skip('slow')
    def test_large_list(self):
        for i in range(1, 1001):
            self.dll.insert_at_tail(i)
        self.dll.reverse()
        self.assertEqual(
            str(self.dll), " -> ".join(map(str, range(1000, 0, -1))))

    def test_head_and_tail_pointers(self):
        self.dll.insert_at_tail(1)
        self.dll.insert_at_tail(2)
        self.dll.insert_at_tail(3)
        self.dll.reverse()
        self.assertEqual(self.dll.head.data, 3)
        self.assertEqual(self.dll.tail.data, 1)

    # @unittest.skip('slow')
    def test_prev_and_next_pointers(self):
        self.dll.insert_at_tail(1)
        self.dll.insert_at_tail(2)
        self.dll.insert_at_tail(3)
        self.dll.reverse()
        node = self.dll.head
        prev = None
        while node:
            self.assertEqual(node.prev, prev)
            prev = node
            node = node.next

    # @unittest.skip('slow')
    def test_multiple_reversals(self):
        for i in range(1, 6):
            self.dll.insert_at_tail(i)
        self.dll.reverse()
        self.dll.reverse()
        self.assertEqual(str(self.dll), "1 -> 2 -> 3 -> 4 -> 5")

    # Optional: Cyclic list test if applicable
    # def test_cyclic_list(self):
    #     # Implement cyclic list test if necessary


if __name__ == '__main__':
    unittest.main()

'''


'''
