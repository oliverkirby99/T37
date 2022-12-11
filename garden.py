import spacy
nlp = spacy.load('en_core_web_sm')

sentence1 = nlp("The old man the boat")
sentence2 = nlp("The horse raced past the barn fell")
sentence3 = nlp("Since Jay always jogs a mile seems like a short distance")
sentence4 = nlp("I convinced her children are noisy")
sentence5 = nlp("The man who whistles tunes pianos")



gardenpathSentences = [sentence1, sentence2, sentence3, sentence4, sentence5]

for sentence in gardenpathSentences:
    print("######################################################################")

    # Print original sentence:
    print(sentence)

    # SPLIT THE SENTENCE INTO UNIQUE ELEMENTS
    [token.orth_ for token in sentence]

    # PRINT THE TOKENIZED SENTENCES
    print(f"Sentence 'Tokenized")
    print([(token, token.orth_, token.orth) for token in sentence])  # For each element in the sentence
    print()

    # PRINT THE ENTITY RECOGNITION FOR EACH SENTENCE
    print(f"Sentence 'entity recognition'")
    print([(i, i.label_, i.label) for i in sentence.ents])  # Search for recognised elements such as people, events and places
    print()
    print("######################################################################")

input()


"""
In the sentences I chose, it only found 1 'entity recognition' which was "Jay". It detected this as a 'person'.

I thought it would possibly detect more entities. But most of my examples included common nouns rather than specific people/places.
"""