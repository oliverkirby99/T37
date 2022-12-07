# T37

To run this you will need to perform the following actions:

- Open Command Line (as an administrator)
- Type the following lines

- pip3 install spacy

# For the next line, if you have multiple versions of Python, you might need to specify "python3"
- python
- import spacy

# If you don't get any errors
- exit()

# Install the appropriate language (English in this case)
- python -m spacy download en_core_web_sm

- python
- import spacy
- nlp = spacy.load('en_core_web_sm')

- doc = nlp("this is a test sentence")
- print([(w.text, w.pos_) for w in doc])

# If you get an output with no errors, you have setup spaCy correctly
