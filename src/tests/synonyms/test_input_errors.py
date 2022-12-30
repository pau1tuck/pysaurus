# content of test_sample.py
import pytest
from pysaurus import synonyms

class SynonymInputErrors:
    nonsense_word = 'flumpalump'
    numerals = 123456

    def get_synonyms(self,x):
        return synonyms.get_synonyms(x)

    def test_nonsense(self):
        assert self.get_synonyms(self.nonsense_word) == None

    def test_numerals(self):
        assert self.get_synonyms(self.numerals) == None