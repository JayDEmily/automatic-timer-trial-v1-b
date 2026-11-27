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
        self.assertEqual(normalize(['  North  ', '\twest\n']), ['North', 'west'])

    def test_omits_blank_entries_after_trimming(self):
        self.assertEqual(normalize(['', ' \t ', 'North', '\n', '  ', 'west']), ['North', 'west'])

    def test_preserves_order_duplicates_case_and_internal_whitespace(self):
        self.assertEqual(
            normalize(['  North ', ' west\t', 'North', '  A  b  ', '\tA  b']),
            ['North', 'west', 'North', 'A  b', 'A  b'],
        )
