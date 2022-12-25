import json
from data.wordlist_0_1_0 import words, length

def wordcount():
    return length

# If the search term exists, return the full thesaurus payload:
def retrieve_data(word):
    if word not in words:
        return False
    else:
        json_data = []
        thesaurus_data = []
        first_letter = word[0]

        data = open("../data/thesauri/0_1_0/" + first_letter + ".json", "r")
        json_data = json.load(data)

        for entry in json_data:
            if entry["term"] == word:
                thesaurus_data = entry["data"]

        return thesaurus_data

def get_synonyms(word):
    thesaurus_data = retrieve_data(word)
    if thesaurus_data == False:
        return False
    else:
        data = []
        for entry in thesaurus_data:
            definition = entry["definition"]
            pos = entry["pos"]
            synonyms = []
            for synonym in entry["synonyms"]:
                synonyms.append(synonym)
            result = {
                "term": word,
                "definition": definition,
                "class": pos,
                "synonyms": synonyms
            }
            data.append(result)
    return data