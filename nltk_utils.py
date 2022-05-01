import nltk
import torch
import numpy as np
from nltk.stem.porter import PorterStemmer

# nltk.download('punkt') # For downloading the 'punkt' package in case it doesn't exist

stemmer = PorterStemmer()

def tokenize(sentence): # To split the sentence into tokens
    return nltk.word_tokenize(sentence)

def stem(word): # To make the words (tokens) in a lower case form
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32) # [0, 0, 0, 0, 0, 0, 0, 0, , , , , to the total different number of words]
    for index, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[index] = 1.0
    return bag
