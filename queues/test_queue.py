import unittest
from .queue import MyQueue


class TestMyQueue(unittest.TestCase):

    def setUp(self):
        self.empty_queue = MyQueue()
        self.single_item_queue = MyQueue()
        self.single_item_queue.enqueue(1)
        self.multi_item_queue = MyQueue()
        for i in range(1, 6):
            self.multi_item_queue.enqueue(i)

    def test_is_empty_on_empty_queue(self):
        self.assertTrue(self.empty_queue.is_empty(), "Queue should be empty.")

    def test_is_empty_on_non_empty_queue(self):
        self.assertFalse(self.single_item_queue.is_empty(),
                         "Queue should not be empty.")

    def test_front_on_empty_queue(self):
        self.assertIsNone(self.empty_queue.front(),
                          "Front of an empty queue should be None.")

    def test_front_on_single_item_queue(self):
        self.assertEqual(self.single_item_queue.front().data, 1,
                         "Front of single-item queue should be the first item.")

    def test_front_on_multi_item_queue(self):
        self.assertEqual(self.multi_item_queue.front().data, 1,
                         "Front of multi-item queue should be the first item.")

    def test_rear_on_empty_queue(self):
        self.assertIsNone(self.empty_queue.rear(),
                          "Rear of an empty queue should be None.")

    def test_rear_on_single_item_queue(self):
        self.assertEqual(self.single_item_queue.rear().data, 1,
                         "Rear of single-item queue should be the only item.")

    def test_rear_on_multi_item_queue(self):
        self.assertEqual(self.multi_item_queue.rear().data, 5,
                         "Rear of multi-item queue should be the last item.")

    def test_size_on_empty_queue(self):
        self.assertEqual(self.empty_queue.size(), 0,
                         "Size of an empty queue should be 0.")

    def test_size_on_single_item_queue(self):
        self.assertEqual(self.single_item_queue.size(), 1,
                         "Size of single-item queue should be 1.")

    def test_size_on_multi_item_queue(self):
        self.assertEqual(self.multi_item_queue.size(), 5,
                         "Size of multi-item queue should be 5.")

    def test_enqueue_in_empty_queue(self):
        self.empty_queue.enqueue(10)
        self.assertEqual(self.empty_queue.front().data, 10,
                         "Front should be updated after enqueue.")
        self.assertEqual(self.empty_queue.rear().data, 10,
                         "Rear should be updated after enqueue.")
        self.assertEqual(self.empty_queue.size(), 1,
                         "Size should be updated after enqueue.")

    def test_dequeue_on_empty_queue(self):
        self.empty_queue.dequeue()
        self.assertIsNone(self.empty_queue.front(
        ), "Front should be None after dequeue from an empty queue.")
        self.assertIsNone(self.empty_queue.rear(
        ), "Rear should be None after dequeue from an empty queue.")
        self.assertEqual(self.empty_queue.size(
        ), 0, "Size should remain 0 after dequeue from an empty queue.")

    def test_dequeue_on_single_item_queue(self):
        self.single_item_queue.dequeue()
        self.assertIsNone(self.single_item_queue.front(
        ), "Front should be None after dequeueing the only item.")
        self.assertIsNone(self.single_item_queue.rear(),
                          "Rear should be None after dequeueing the only item.")
        self.assertEqual(self.single_item_queue.size(), 0,
                         "Size should be 0 after dequeueing the only item.")

    def test_dequeue_on_multi_item_queue(self):
        self.multi_item_queue.dequeue()
        self.assertEqual(self.multi_item_queue.front().data, 2,
                         "Front should be updated to next item after dequeue.")
        self.assertEqual(self.multi_item_queue.size(), 4,
                         "Size should decrease by one after dequeue.")

    # def test_print_list(self):
        # Assuming print_list outputs the queue in order
        # import sys
        # from io import StringIO
        # captured_output = StringIO()
        # sys.stdout = captured_output
        # self.single_item_queue.print_list()
        # sys.stdout = sys.__stdout__
        # self.assertEqual(captured_output.getvalue().strip(),
        #                  "1", "Queue printout should match inserted items.")

    @unittest.skip('fix later')
    def test_print_list(self):
        expected_output = "1"  # Single item in queue
        self.assertEqual(self.single_item_queue.print_list(
        ), expected_output, "Queue printout should match inserted items.")


if __name__ == '__main__':
    unittest.main()
