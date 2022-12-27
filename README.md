# Pysaurus 0.1.0

A sophisticated English thesaurus with definitions, synonyms, antonyms, and word proximity measures.

The application currently provides definitions, synonyms and antonyms based on the New Academic Word List [(Coxhead, 2012)](https://onlinelibrary.wiley.com/doi/abs/10.2307/3587951), the Academic Vocabulary List (AVL) [(Gardner & Davies, 2014)](https://academic.oup.com/applij/article/35/3/305/146569), as well as high-frequency verbs, adjectives, adverbs, and conjunctions from the [British National Corpus](http://www.natcorp.ox.ac.uk/corpus/index.xml).

Version 0.1.0 wordcount: 5,035 English terms

## Usage

    from pysaurus import synonyms

    my_word = "write"

    data = synonyms.get_synonyms(my_word)

The `get_synonyms` function returns a dictionary with the following structure:

    {
        "term": "write",
        "class": "verb"
        "definition": "put language in written form",
        "synonyms": [
            ("compose", 100),
            ("draft", 100),
            ("note", 100),
            ("create", 100),
            ...
        ]
    }

