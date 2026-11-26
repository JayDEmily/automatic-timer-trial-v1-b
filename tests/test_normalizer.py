import unittest
from normalizer import normalize


class NormalizeTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(normalize([]), [])

    def test_order_duplicates_and_case(self):
        self.assertEqual(normalize(["North", "west", "North"]), ["North", "west", "North"])

    def test_internal_whitespace(self):
        self.assertEqual(normalize(["a b", "C  d"]), ["a b", "C  d"])

    def test_trim_ends(self):
        self.assertEqual(normalize(["  North ", "\twest\n", "  C  d\t"]), ["North", "west", "C  d"])

    def test_omit_blank_entries(self):
        self.assertEqual(normalize(["", " \t\n", " keep ", "\t"]), ["keep"])

    def test_preserve_order_duplicates_case_and_internal_whitespace_after_trimming(self):
        self.assertEqual(
            normalize(["  North ", " ", " west ", "\tNorth", " C  d ", "north"]),
            ["North", "west", "North", "C  d", "north"],
        )
