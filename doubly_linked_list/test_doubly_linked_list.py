import unittest
from .doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()

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


if __name__ == '__main__':
    unittest.main()
