# from unittest import TestCase, main
import unittest
from .node import Node
from .linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()
        self.ll1 = LinkedList()
        self.ll2 = LinkedList()

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

    def test_find_mid_odd_number_of_elements(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.ll.insert_at_tail(30)
        self.assertEqual(self.ll.find_mid(), 20)

    @unittest.skip('postponed')
    def test_find_mid_two_elements(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_tail(20)
        self.assertEqual(self.ll.find_mid(), 10)

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

    # ------- after code optimization --------

    def test_is_empty(self):
        self.assertTrue(self.ll.is_empty())
        self.ll.insert_at_head(1)
        self.assertFalse(self.ll.is_empty())

    def test_insert_at_head(self):
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        self.assertEqual(self.ll.head.data, 2)
        self.assertEqual(self.ll.head.next.data, 1)

    @unittest.skip('postponed')
    def test_insert_at_tail(self):
        self.ll.insert_at_tail(1)
        self.ll.insert_at_tail(2)
        self.assertEqual(self.ll.tail.data, 2)
        self.assertEqual(self.ll.head.next.data, 2)

    def test_search(self):
        self.ll.insert_at_head(1)
        self.assertTrue(self.ll.search(1))
        self.assertFalse(self.ll.search(2))

    def test_delete(self):
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        self.assertTrue(self.ll.delete(1))
        self.assertFalse(self.ll.search(1))
        self.assertFalse(self.ll.delete(3))

    def test_length(self):
        self.assertEqual(self.ll.length(), 0)
        self.ll.insert_at_head(1)
        self.assertEqual(self.ll.length(), 1)
        self.ll.insert_at_tail(2)
        self.assertEqual(self.ll.length(), 2)

    def test_reverse(self):
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        self.ll.reverse()
        self.assertEqual(self.ll.head.data, 1)
        self.assertEqual(self.ll.head.next.data, 2)

    # ------ remove duplicate --------
    def test_remove_duplicates_empty_list(self):
        # Boundary case: empty list
        self.ll.remove_duplicates()
        self.assertIsNone(self.ll.head)

    def test_remove_duplicates_single_node(self):
        # Boundary case: single node
        self.ll.insert_at_head(1)
        self.ll.remove_duplicates()
        self.assertEqual(self.ll.head.data, 1)
        self.assertIsNone(self.ll.head.next)

    def test_remove_duplicates_no_duplicates(self):
        # Case: no duplicates
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        self.ll.insert_at_head(3)
        self.ll.remove_duplicates()
        self.assertEqual(self.ll.head.data, 3)
        self.assertEqual(self.ll.head.next.data, 2)
        self.assertEqual(self.ll.head.next.next.data, 1)
        self.assertIsNone(self.ll.head.next.next.next)

    def test_remove_duplicates_with_duplicates(self):
        # Case: list with duplicates
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        self.ll.insert_at_head(2)
        self.ll.insert_at_head(3)
        self.ll.remove_duplicates()
        self.assertEqual(self.ll.head.data, 3)
        self.assertEqual(self.ll.head.next.data, 2)
        self.assertEqual(self.ll.head.next.next.data, 1)
        self.assertIsNone(self.ll.head.next.next.next)

    def test_remove_duplicates_multiple_duplicates(self):
        # Edge case: multiple duplicates
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        self.ll.insert_at_head(2)
        self.ll.insert_at_head(3)
        self.ll.insert_at_head(3)
        self.ll.remove_duplicates()
        self.assertEqual(self.ll.head.data, 3)
        self.assertEqual(self.ll.head.next.data, 2)
        self.assertEqual(self.ll.head.next.next.data, 1)
        self.assertIsNone(self.ll.head.next.next.next)

    def test_remove_duplicates_all_nodes_same(self):
        # Edge case: all nodes the same
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(1)
        self.ll.remove_duplicates()
        self.assertEqual(self.ll.head.data, 1)
        self.assertIsNone(self.ll.head.next)

    # ------------ intersection -----------
    def test_empty_lists(self):
        # Boundary case: Both lists are empty
        self.assertEqual(self.ll1.intersection(self.ll2), [])

    def test_one_empty_list(self):
        # Boundary case: One list is empty
        self.ll1.insert_at_head(1)
        self.assertEqual(self.ll1.intersection(self.ll2), [])
        self.assertEqual(self.ll2.intersection(self.ll1), [])

    def test_no_intersection(self):
        # Case: No intersection between lists
        self.ll1.insert_at_head(1)
        self.ll2.insert_at_head(2)
        self.assertEqual(self.ll1.intersection(self.ll2), [])
        self.assertEqual(self.ll2.intersection(self.ll1), [])

    def test_one_element_intersection(self):
        # Case: One element in common
        self.ll1.insert_at_head(1)
        self.ll2.insert_at_head(1)
        self.assertEqual(self.ll1.intersection(self.ll2), [1])
        self.assertEqual(self.ll2.intersection(self.ll1), [1])

    def test_multiple_elements_intersection(self):
        # Case: Multiple elements in common
        self.ll1.insert_at_head(3)
        self.ll1.insert_at_head(2)
        self.ll1.insert_at_head(1)
        self.ll2.insert_at_head(3)
        self.ll2.insert_at_head(4)
        self.ll2.insert_at_head(1)
        self.assertEqual(sorted(self.ll1.intersection(self.ll2)), [1, 3])
        self.assertEqual(sorted(self.ll2.intersection(self.ll1)), [1, 3])

    def test_all_elements_intersection(self):
        # Edge case: All elements are common
        self.ll1.insert_at_head(1)
        self.ll1.insert_at_head(2)
        self.ll2.insert_at_head(2)
        self.ll2.insert_at_head(1)
        self.assertEqual(sorted(self.ll1.intersection(self.ll2)), [1, 2])
        self.assertEqual(sorted(self.ll2.intersection(self.ll1)), [1, 2])

    def test_duplicates_in_list(self):
        # Edge case: Lists contain duplicates
        self.ll1.insert_at_head(1)
        self.ll1.insert_at_head(2)
        self.ll1.insert_at_head(2)
        self.ll2.insert_at_head(2)
        self.ll2.insert_at_head(2)
        self.ll2.insert_at_head(3)
        # self.assertEqual(sorted(self.ll1.intersection(self.ll2)), [2])
        # self.assertEqual(sorted(self.ll2.intersection(self.ll1)), [2])
        self.assertEqual((self.ll1.intersection(self.ll2)), [2])
        self.assertEqual((self.ll2.intersection(self.ll1)), [2])

    # ------ union ------

    def test_empty_lists_union(self):
        # Boundary case: Both lists are empty
        self.assertEqual(self.ll1.union(self.ll2), [])

    def test_one_empty_list_union(self):
        # Boundary case: One list is empty
        self.ll1.insert_at_head(1)
        self.assertEqual(sorted(self.ll1.union(self.ll2)), [1])
        self.assertEqual(sorted(self.ll2.union(self.ll1)), [1])

    def test_no_union(self):
        # Case: No intersection between lists
        self.ll1.insert_at_head(1)
        self.ll2.insert_at_head(2)
        self.assertEqual(sorted(self.ll1.union(self.ll2)), [1, 2])
        self.assertEqual(sorted(self.ll2.union(self.ll1)), [1, 2])

    def test_one_element_union(self):
        # Case: One element in common
        self.ll1.insert_at_head(1)
        self.ll2.insert_at_head(1)
        self.assertEqual(self.ll1.union(self.ll2), [1])
        self.assertEqual(self.ll2.union(self.ll1), [1])

    def test_multiple_elements_union(self):
        # Case: Multiple elements in common
        self.ll1.insert_at_head(3)
        self.ll1.insert_at_head(2)
        self.ll1.insert_at_head(1)
        self.ll2.insert_at_head(3)
        self.ll2.insert_at_head(4)
        self.ll2.insert_at_head(1)
        self.assertEqual(sorted(self.ll1.union(self.ll2)), [1, 2, 3, 4])
        self.assertEqual(sorted(self.ll2.union(self.ll1)), [1, 2, 3, 4])

    def test_all_elements_union(self):
        # Edge case: All elements are common
        self.ll1.insert_at_head(1)
        self.ll1.insert_at_head(2)
        self.ll2.insert_at_head(2)
        self.ll2.insert_at_head(1)
        self.assertEqual(sorted(self.ll1.union(self.ll2)), [1, 2])
        self.assertEqual(sorted(self.ll2.union(self.ll1)), [1, 2])

    def test_duplicates_in_list_union(self):
        # Edge case: Lists contain duplicates
        self.ll1.insert_at_head(1)
        self.ll1.insert_at_head(2)
        self.ll1.insert_at_head(2)
        self.ll2.insert_at_head(2)
        self.ll2.insert_at_head(2)
        self.ll2.insert_at_head(3)
        self.assertEqual(sorted(self.ll1.union(self.ll2)), [1, 2, 3])
        self.assertEqual(sorted(self.ll2.union(self.ll1)), [1, 2, 3])

    # ---------------- find nth ----------------
    def test_empty_list(self):
        self.assertEqual(self.ll.find_nth(1), -1)

    def test_single_node_list(self):
        self.ll.insert_at_tail(10)
        self.assertEqual(self.ll.find_nth(1), 10)
        self.assertEqual(self.ll.find_nth(2), -1)

    def test_two_node_list(self):
        self.ll.insert_at_tail(20)
        self.ll.insert_at_tail(30)
        self.assertEqual(self.ll.find_nth(1), 30)
        self.assertEqual(self.ll.find_nth(2), 20)
        self.assertEqual(self.ll.find_nth(3), -1)

    def test_n_greater_than_list_length(self):
        self.ll.insert_at_tail(40)
        self.ll.insert_at_tail(50)
        self.ll.insert_at_tail(60)
        self.assertEqual(self.ll.find_nth(4), -1)

    def test_n_equals_list_length(self):
        self.ll.insert_at_tail(70)
        self.ll.insert_at_tail(80)
        self.ll.insert_at_tail(90)
        self.assertEqual(self.ll.find_nth(3), 70)

    def test_middle_of_the_list(self):
        self.ll.insert_at_tail(100)
        self.ll.insert_at_tail(110)
        self.ll.insert_at_tail(120)
        self.assertEqual(self.ll.find_nth(2), 110)

    def test_end_of_the_list(self):
        self.ll.insert_at_tail(130)
        self.ll.insert_at_tail(140)
        self.ll.insert_at_tail(150)
        self.assertEqual(self.ll.find_nth(1), 150)

    def test_list_with_duplicates(self):
        self.ll.insert_at_tail(160)
        self.ll.insert_at_tail(170)
        self.ll.insert_at_tail(170)
        self.ll.insert_at_tail(180)
        self.assertEqual(self.ll.find_nth(3), 170)

    def test_negative_n(self):
        self.ll.insert_at_tail(190)
        self.ll.insert_at_tail(200)
        self.assertEqual(self.ll.find_nth(-1), -1)


if __name__ == '__main__':
    unittest.main()
