from unittest import TestCase, main
from collections import defaultdict
from .inverted_index import inverted_index  # Adjust import path as needed


class TestInvertedIndex(TestCase):
    def test_basic_input(self):
        text = "the quick brown fox jumps over the lazy dog"
        expected = {
            'the': [0, 6],
            'quick': [1],
            'brown': [2],
            'fox': [3],
            'jumps': [4],
            'over': [5],
            'lazy': [7],
            'dog': [8]
        }
        result = inverted_index(text)
        for word, positions in expected.items():
            self.assertEqual(result[word], positions)

    def test_repeated_words(self):
        text = "hello hello world hello"
        expected = {
            'hello': [0, 1, 3],
            'world': [2]
        }
        self.assertEqual(inverted_index(text), expected)

    def test_case_sensitivity(self):
        text = "Hello hello HeLLo"
        result = inverted_index(text)
        self.assertEqual(result['Hello'], [0])
        self.assertEqual(result['hello'], [1])
        self.assertEqual(result['HeLLo'], [2])

    def test_empty_string(self):
        self.assertEqual(inverted_index(""), {})

    def test_punctuation(self):
        text = "hello, world! hello."
        result = inverted_index(text)
        self.assertIn("hello,", result)
        self.assertIn("world!", result)
        self.assertIn("hello.", result)

    def test_large_input(self):
        text = "word " * 10000 + "unique"
        result = inverted_index(text.strip())
        self.assertEqual(result['word'], list(range(10000)))
        self.assertEqual(result['unique'], [10000])


if __name__ == '__main__':
    main()
