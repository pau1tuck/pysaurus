# content of test_sample.py
import unittest
from pysaurus import synonyms

class FaultyInput(unittest.TestCase):
    nonsense_word = 'flumpalump'
    non_english = '写'
    numerals = 123456

    def test_nonsense_word(self):
        result = synonyms.get_synonyms(self.nonsense_word)
        self.assertIsNone(result)

    def test_non_english(self):
        result = synonyms.get_synonyms(self.non_english)
        self.assertIsNone(result)