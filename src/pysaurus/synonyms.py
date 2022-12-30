from thesaurus import get_data

def get_synonyms(word):
    word = 'academic'
    thesaurus_data = get_data(word)
    if thesaurus_data == False:
        return None
    else:
        data = []
        for entry in thesaurus_data:
            definition = entry["definition"]
            pos = entry["pos"]
            synonyms = []
            for synonym in entry["synonyms"]:
                synonyms.append((synonym["term"], synonym["similarity"]))
            result = {
                "term": word,
                "definition": definition,
                "class": pos,
                "synonyms": synonyms
            }
            data.append(result)
        print(data)
    return data