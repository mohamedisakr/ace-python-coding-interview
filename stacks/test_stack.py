import unittest
from .stack import MyStack


class TestMyStack(unittest.TestCase):
    def setUp(self):
        self.stack = MyStack()

    def test_is_empty(self):
        # Boundary case: Initially empty stack
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)

        self.assertFalse(self.stack.is_empty())
        self.stack.pop()

        self.assertTrue(self.stack.is_empty())

    def test_push(self):
        # Normal case: Push elements to stack
        self.stack.push(1)
        self.assertEqual(self.stack.capacity(), 1)

        self.stack.push(2)
        self.assertEqual(self.stack.capacity(), 2)

        self.assertEqual(self.stack.peek(), 2)

    @unittest.skip("step by step")
    def test_pop(self):
        # Edge case: Pop from empty stack
        self.assertIsNone(self.stack.pop())

        # Normal case: Pop elements from stack
        self.stack.push(1)
        self.stack.push(2)

        # print(self.stack.pop())
        self.assertEqual(self.stack.pop(), 2)

        # print(self.stack.pop())
        self.assertEqual(self.stack.pop(), 1)
        self.assertIsNone(self.stack.pop())

    # def test_pop(self):
    #     # Edge case: Pop from empty stack
    #     self.assertIsNone(self.stack.pop())

    #     # # Normal case: Pop elements from stack
    #     self.stack.push(10)
    #     self.stack.push(20)
    #     self.assertEqual(self.stack.capacity(), 2)

    #     # print(self.stack.pop())
    #     self.assertEqual(self.stack.pop(), 20)

    #     # # print(self.stack.pop())
    #     # self.assertEqual(self.stack.pop(), 1)
    #     # self.assertIsNone(self.stack.pop())

    def test_peek(self):
        # Edge case: Peek on empty stack
        self.assertIsNone(self.stack.peek())

        # Normal case: Peek elements in stack
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)

        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)

        self.stack.pop()
        self.assertEqual(self.stack.peek(), 1)

    def test_capacity(self):
        # Boundary case: capacity of empty stack
        self.assertEqual(self.stack.capacity(), 0)

        # Normal case: capacity after pushing elements
        self.stack.push(1)
        self.assertEqual(self.stack.capacity(), 1)

        self.stack.push(2)
        self.assertEqual(self.stack.capacity(), 2)

        # Normal case: capacity after popping elements
        self.stack.pop()
        self.assertEqual(self.stack.capacity(), 1)

        self.stack.pop()
        self.assertEqual(self.stack.capacity(), 0)


if __name__ == '__main__':
    unittest.main()
