# content of test_sample.py
import unittest
from pysaurus import synonyms

class FaultyInput(unittest.TestCase):
    nonsense_word = 'flumpalump'
    numerals = 123456
    non_English = '写'

    def test_nonsense(self):
        result = synonyms.get_synonyms(self.nonsense_word)
        self.assertIsNone(result)

    def test_numerals(self):
        result = synonyms.get_synonyms(self.non_English)
        self.assertIsNone(result)