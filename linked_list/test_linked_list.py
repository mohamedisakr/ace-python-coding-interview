# from unittest import TestCase, main
import unittest
from .node import Node
from .linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_is_empty_on_empty_list(self):
        self.assertTrue(self.ll.is_empty())

    def test_insert_at_head_1(self):
        self.ll.insert_at_head(10)
        self.assertEqual(self.ll.get_head().data, 10)

    def test_insert_at_head_2(self):
        self.ll.insert_at_head(20)
        self.assertEqual(self.ll.get_head().data, 20)

    def test_insert_at_tail_1(self):
        self.ll.insert_at_tail(10)
        self.assertEqual(self.ll.get_head().data, 10)

    def test_insert_at_tail_2(self):
        self.ll.insert_at_tail(20)
        self.assertEqual(self.ll.get_head().data, 20)

    def test_search_existing_element(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.assertTrue(self.ll.search(10))
        self.assertTrue(self.ll.search(20))

    def test_search_non_existing_element(self):
        self.ll.insert_at_head(10)
        self.assertFalse(self.ll.search(20))

    def test_delete_head(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.assertTrue(self.ll.delete(10))
        self.assertEqual(self.ll.get_head().data, 20)

    def test_delete_tail(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.assertTrue(self.ll.delete(20))
        self.assertEqual(self.ll.get_head().next, None)

    def test_delete_non_existing_element(self):
        self.ll.insert_at_head(10)
        self.assertFalse(self.ll.delete(20))

    def test_delete_from_empty_list(self):
        self.assertFalse(self.ll.delete(10))

    # Additional edge and boundary test cases

    def test_insert_at_head_on_empty_list(self):
        self.ll.insert_at_head(10)
        self.assertEqual(self.ll.get_head().data, 10)

    def test_insert_at_tail_on_empty_list(self):
        self.ll.insert_at_tail(10)
        self.assertEqual(self.ll.get_head().data, 10)

    def test_insert_multiple_elements(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.ll.insert_at_head(30)
        self.assertEqual(self.ll.get_head().data, 30)
        self.assertEqual(self.ll.get_head().next.data, 10)
        self.assertEqual(self.ll.get_head().next.next.data, 20)

    def test_delete_middle_element(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.ll.insert_at_tail(30)
        self.assertTrue(self.ll.delete(20))
        self.assertEqual(self.ll.get_head().next.data, 30)

    def test_delete_only_element(self):
        self.ll.insert_at_head(10)
        self.assertTrue(self.ll.delete(10))
        self.assertTrue(self.ll.is_empty())

    def test_search_empty_list(self):
        self.assertFalse(self.ll.search(10))

    def test_delete_non_existing_element_in_non_empty_list(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.assertFalse(self.ll.delete(30))

    # ----- length test cases
    def test_length_empty_list(self):
        self.assertEqual(self.ll.length(), 0)

    def test_length_single_element(self):
        self.ll.insert_at_head(10)
        self.assertEqual(self.ll.length(), 1)

    def test_length_multiple_elements(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.ll.insert_at_tail(30)
        self.assertEqual(self.ll.length(), 3)

    def test_length_after_insert_at_head(self):
        self.ll.insert_at_head(10)
        self.assertEqual(self.ll.length(), 1)
        self.ll.insert_at_head(20)
        self.assertEqual(self.ll.length(), 2)

    def test_length_after_insert_at_tail(self):
        self.ll.insert_at_tail(10)
        self.assertEqual(self.ll.length(), 1)
        self.ll.insert_at_tail(20)
        self.assertEqual(self.ll.length(), 2)

    def test_length_after_delete_head(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.ll.delete(10)
        self.assertEqual(self.ll.length(), 1)

    def test_length_after_delete_tail(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.ll.delete(20)
        self.assertEqual(self.ll.length(), 1)

    def test_length_after_delete_middle_element(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.ll.insert_at_tail(30)
        self.ll.delete(20)
        self.assertEqual(self.ll.length(), 2)

    def test_length_after_delete_non_existing_element(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.ll.delete(30)
        self.assertEqual(self.ll.length(), 2)

    def test_length_after_delete_from_empty_list(self):
        self.ll.delete(10)
        self.assertEqual(self.ll.length(), 0)

    # --------- reverse ------
    def test_reverse_empty_list(self):
        self.ll.reverse()
        self.assertTrue(self.ll.is_empty())

    def test_reverse_single_element(self):
        self.ll.insert_at_head(10)
        self.ll.reverse()
        self.assertEqual(self.ll.get_head().data, 10)

    def test_reverse_two_elements(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.ll.reverse()
        self.assertEqual(self.ll.get_head().data, 20)
        self.assertEqual(self.ll.get_head().next.data, 10)

    def test_reverse_multiple_elements(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.ll.insert_at_tail(30)
        self.ll.reverse()
        self.assertEqual(self.ll.get_head().data, 30)
        self.assertEqual(self.ll.get_head().next.data, 20)
        self.assertEqual(self.ll.get_head().next.next.data, 10)

    def test_reverse_after_insert_at_head(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_head(20)
        self.ll.reverse()
        self.assertEqual(self.ll.get_head().data, 10)
        self.assertEqual(self.ll.get_head().next.data, 20)

    def test_reverse_after_insert_at_tail(self):
        self.ll.insert_at_tail(10)
        self.ll.insert_at_tail(20)
        self.ll.reverse()
        self.assertEqual(self.ll.get_head().data, 20)
        self.assertEqual(self.ll.get_head().next.data, 10)

    def test_reverse_twice(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.ll.insert_at_tail(30)
        self.ll.reverse()
        self.ll.reverse()
        self.assertEqual(self.ll.get_head().data, 10)
        self.assertEqual(self.ll.get_head().next.data, 20)
        self.assertEqual(self.ll.get_head().next.next.data, 30)

    # ------- detect loop (cycle) ----------
    def test_detect_loop_empty_list(self):
        self.assertFalse(self.ll.detect_loop())

    def test_detect_loop_single_element_no_loop(self):
        self.ll.insert_at_head(10)
        self.assertFalse(self.ll.detect_loop())

    def test_detect_loop_single_element_with_loop(self):
        node = Node(10)
        self.ll.head = node
        node.next = node  # Creating a loop
        self.assertTrue(self.ll.detect_loop())

    def test_detect_loop_multiple_elements_no_loop(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.ll.insert_at_tail(30)
        self.assertFalse(self.ll.detect_loop())

    def test_detect_loop_multiple_elements_with_loop_at_end(self):
        node1 = Node(10)
        node2 = Node(20)
        node3 = Node(30)
        self.ll.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node1  # Creating a loop
        self.assertTrue(self.ll.detect_loop())

    def test_detect_loop_multiple_elements_with_loop_in_middle(self):
        node1 = Node(10)
        node2 = Node(20)
        node3 = Node(30)
        node4 = Node(40)
        self.ll.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2  # Creating a loop
        self.assertTrue(self.ll.detect_loop())

    # --- middle node ---
    def test_find_mid_empty_list(self):
        self.assertIsNone(self.ll.find_mid())

    def test_find_mid_single_element(self):
        self.ll.insert_at_head(10)
        self.assertEqual(self.ll.find_mid(), 10)

    @unittest.skip('postponed')
    def test_find_mid_two_elements(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.assertEqual(self.ll.find_mid(), 10)

    def test_find_mid_odd_number_of_elements(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.ll.insert_at_tail(30)
        self.assertEqual(self.ll.find_mid(), 20)

    @unittest.skip('postponed')
    def test_find_mid_even_number_of_elements(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.ll.insert_at_tail(30)
        self.ll.insert_at_tail(40)
        self.assertEqual(self.ll.find_mid(), 20)

    def test_find_mid_large_list(self):
        for i in range(1, 1001):
            self.ll.insert_at_tail(i)
        self.assertEqual(self.ll.find_mid(), 501)

    # ------- middle node adjusted test cases


    # def test_print_list(self):
    #     self.ll.insert_at_head(10)
    #     self.ll.insert_at_tail(20)
    #     self.ll.insert_at_tail(30)
    #     self.ll.print_list()  # Expected output: 10 -> 20 -> 30 -> NULL
if __name__ == '__main__':
    unittest.main()
