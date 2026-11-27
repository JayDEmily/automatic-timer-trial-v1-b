import unittest
from normalizer import normalize


class NormalizeTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(normalize([]), [])

    def test_order_duplicates_and_case(self):
        self.assertEqual(normalize(["North", "west", "North"]), ["North", "west", "North"])

    def test_internal_whitespace(self):
        self.assertEqual(normalize(["a b", "C  d"]), ["a b", "C  d"])

    def test_trims_leading_and_trailing_whitespace(self):
        self.assertEqual(normalize(["  North ", "\twest\n"]), ["North", "west"])

    def test_omits_empty_and_whitespace_only_entries(self):
        self.assertEqual(normalize(["", " \t ", "\n", "keep", ""]), ["keep"])
        self.assertEqual(normalize(["", "\t\n", " "]), [])

    def test_preserves_order_and_duplicates_after_trimming(self):
        self.assertEqual(normalize([" x ", "", " y", "x", "  y "]), ["x", "y", "x", "y"])

    def test_preserves_case_and_internal_whitespace_when_trimming(self):
        self.assertEqual(normalize([" A  b ", "\tC\tD\n", "a  B"]), ["A  b", "C\tD", "a  B"])
