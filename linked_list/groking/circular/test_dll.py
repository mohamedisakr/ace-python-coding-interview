import unittest
from dll import DLLSentinel


class TestCircularDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.dll = DLLSentinel()

    def test_initialization(self):
        self.assertIsNotNone(self.dll.sentinel)
        self.assertEqual(self.dll.sentinel.next, self.dll.sentinel)
        self.assertEqual(self.dll.sentinel.prev, self.dll.sentinel)

    def test_prepend(self):
        node = self.dll.prepend(10)
        self.assertEqual(self.dll.sentinel.next.data, 10)
        self.assertEqual(self.dll.sentinel.prev.data, 10)
        self.assertEqual(node.next, self.dll.sentinel)
        self.assertEqual(node.prev, self.dll.sentinel)

    def test_append(self):
        node = self.dll.append(20)
        self.assertEqual(self.dll.sentinel.next.data, 20)
        self.assertEqual(self.dll.sentinel.prev.data, 20)
        self.assertEqual(node.next, self.dll.sentinel)
        self.assertEqual(node.prev, self.dll.sentinel)

    def test_insert(self):
        self.dll.append(30)
        self.dll.prepend(10)
        middle_node = self.dll.sentinel.next
        new_node = self.dll.insert(20, middle_node)
        self.assertEqual(middle_node.next, new_node)
        self.assertEqual(new_node.next.data, 30)
        self.assertEqual(new_node.prev.data, 10)

    def test_delete(self):
        first = self.dll.append(10)
        second = self.dll.append(20)
        self.dll.delete(first)
        self.assertEqual(self.dll.sentinel.next.data, 20)
        self.assertEqual(self.dll.sentinel.prev.data, 20)
        self.dll.delete(second)
        self.assertEqual(self.dll.sentinel.next, self.dll.sentinel)
        self.assertEqual(self.dll.sentinel.prev, self.dll.sentinel)

    def test_delete_all(self):
        self.dll.append(10)
        self.dll.append(20)
        self.dll.delete_all()
        self.assertEqual(self.dll.sentinel.next, self.dll.sentinel)
        self.assertEqual(self.dll.sentinel.prev, self.dll.sentinel)

    def test_search(self):
        self.dll.append(10)
        self.dll.append(20)
        self.dll.append(30)
        node = self.dll.search(20)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 20)
        node = self.dll.search(40)
        self.assertIsNone(node)

    def test_iterator(self):
        self.dll.append(10)
        self.dll.append(20)
        self.dll.append(30)
        values = [data for data in self.dll.iterator()]
        self.assertEqual(values, [10, 20, 30])

    def test_copy(self):
        self.dll.append(10)
        self.dll.append(20)
        copied_dll = self.dll.copy()
        copied_values = [data for data in copied_dll.iterator()]
        self.assertEqual(copied_values, [10, 20])
        original_values = [data for data in self.dll.iterator()]
        self.assertEqual(original_values, [10, 20])

    def test_str(self):
        self.dll.append(10)
        self.dll.append(20)
        self.assertEqual(str(self.dll), "[10, 20, None]")

    def test_edge_cases(self):
        # Insert at boundaries
        with self.assertRaises(RuntimeError):
            self.dll.delete(self.dll.sentinel)
        self.dll.prepend(1)
        self.dll.append(2)
        self.assertEqual(str(self.dll), "[1, 2, None]")

        # Search in an empty list
        self.dll.delete_all()
        self.assertIsNone(self.dll.search(1))

        # Delete all nodes
        self.dll.append(1)
        self.dll.append(2)
        self.dll.delete_all()
        self.assertIsNone(self.dll.search(1))
        self.assertIsNone(self.dll.search(2))
