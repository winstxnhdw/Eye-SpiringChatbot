from numpy import zeros
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize

tokenize = lambda sentence: word_tokenize(sentence)

def stem(word):

    stemmer = PorterStemmer()
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):

    tokenized_sentence = [stem(word) for word in tokenized_sentence]
    bag = zeros(len(all_words))
    
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0

    return bag



