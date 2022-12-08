import spacy
nlp = spacy.load('en_core_web_sm')

sentence1 = nlp("The old man the boat")
sentence2 = nlp("The horse raced past the barn fell")
sentence3 = nlp("Since Jay always jogs a mile seems like a short distance")
sentence4 = nlp("I convinced her children are noisy")
sentence5 = nlp("The man who whistles tunes pianos")

gardenpathSentences = [sentence1, sentence2, sentence3, sentence4, sentence5]

for sentence in gardenpathSentences:
    print(f"{sentence}\n{[(w.text, w.pos_) for w in sentence]}")
    print()
input()

"""
In the first example, "man" should be a verb because 'The elderly, man the boat' is what is meant here.

In the second sentence about the horse, it seems that the barn fell, however it means the horse (that raced past the barn) fell.

I expected some of the 'pos tags' to be incorrect due to the nature of 'garden-path sentences'.
But, I spent more time trying to figure out some of the sentences myself :)
"""