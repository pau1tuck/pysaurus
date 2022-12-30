# content of test_sample.py
import pytest
from pysaurus import synonyms

def func(x):
    return synonyms.get_synonyms(x)

def test_nonsense():
    nonsense_word = 'flumpalump'
    assert func(nonsense_word) == None

def test_numerals():
    numerals = 123456
    assert func(numerals) == None