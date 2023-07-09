# This line imports the spacy library, which provides natural language 
# processing capabilities.
# if spacy below is installed din your virtual environment with all modules
# and still give the error import "spacy" could not be resolved,
# just press Ctrl + Shift + P (win)/ cmd + Shift + P(macOS)
# to open command pellet.
# type "Python: Select Interpreter" and select this option when it appears. 
# It will open a list of available Python interpreters.
# Look for your virtual environment in the list and select it. 
# It will typically be located in the .venv folder within your project directory
# This will solve your issue, just work on the python interpreter with the
# virtual environment with all modules installed

import spacy

# Loading the medium-sized English model

nlp = spacy.load('en_core_web_md')

# Defining word objects and measuring similarity

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("Sock")
word5 = nlp("Shoe")

# md vs sm model
# These lines define word objects using the loaded model and measure the 
# similarity between pairs of words using the similarity method. 
# The similarity values range between 0 and 1, with 1 indicating high
# similarity. The results are printed in the console.

print(word1.similarity(word2)) # 0.5929930274321619 / 0.6770565478895127
print(word3.similarity(word2)) # 0.40415016164997786 / 0.7276309976205778
print(word3.similarity(word1)) # 0.22358825939615987 / 0.6806929391210822
print(word4.similarity(word5)) # 1.0000000454174354 / 0.8340204086971004
print(word5.similarity(word1)) # 0.06612196296041711 / 0.5784117082522696


# explanation and observations of similarity using the MD & SM language model

# MD bigger model with higher vocabulary for sentences
# the results are printed as floating point number between 0 & 1, 
# o is low similarity and 1 is high similarity
# the similarity makes sense based on value
# Cat & monkey highest similarity
# banana & monkey higher similarity than banana & Cat
# added sock and shoe, highest similarity, shoe and cat lowest
# Finally, the semantic similarities makes sense

# SM, smaller language model
# user warning user smaller model:
# UserWarning: [W007] The model you're using has no word vectors loaded, 
# so the result of the Doc.similarity method will be based on the tagger, 
# parser and NER, which may not give useful similarity judgments.
# This may happen if you're using one of the small models, e.g. `en_core_web_sm`, 
# which don't ship with word vectors and only use context-sensitive tensors.
# You can always add your own word vectors,
# or use one of the larger models instead if available.
# Finally, comparing sm with md, sm gives higher similarity values than md model, 
# one value
# is lower for show and cat for sm than md model. sm model is not a
# good fit for semantic similarity


# vectors & MD language model
# This code demonstrates how to work with word vectors.
# It creates word objects for the words "human," "alien," "shoe," and "sock" 
# and measures the similarity between all pairs of words. 
# The results are printed to the console.

tokens = nlp('human alien shoe sock ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# Comparing similarity between a given sentence and multiple other sentences

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

# This code compares the similarity between a given sentence
# and a list of other sentences. It uses the loaded model to
# calculate the similarity and prints the sentences along with
# their respective similarity scores.

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


# Please note the UserWarning mentioned in the comments about 
# the smaller language model (en_core_web_sm) not having word vectors.
# This warning indicates that the similarity judgments might not be
# as accurate when using that model.
# Overall, the code demonstrates the usage of spacy for measuring word
# and sentence similarity using word vectors provided by the medium-sized 
# English model (en_core_web_md).



