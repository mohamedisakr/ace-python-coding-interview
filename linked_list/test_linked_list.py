from unittest import TestCase, main
from .linked_list import LinkedList


class TestLinkedList(TestCase):

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

    # def test_print_list(self):
    #     self.ll.insert_at_head(10)
    #     self.ll.insert_at_tail(20)
    #     self.ll.insert_at_tail(30)
    #     self.ll.print_list()  # Expected output: 10 -> 20 -> 30 -> NULL


if __name__ == '__main__':
    main()
