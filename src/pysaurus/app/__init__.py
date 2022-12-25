from data.wordlist_0_1_0 import words

def check_for_word(word):
    if word not in words:
        return "Not found"

def collect_data(word):
    json_data = []
    thesaurus_data = []
