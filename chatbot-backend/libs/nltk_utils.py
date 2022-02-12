from numpy import zeros, float32
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize

tokenize = lambda sentence: word_tokenize(sentence)

def stem(word):

    stemmer = PorterStemmer()
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):

    tokenized_sentence = [stem(word) for word in tokenized_sentence]
    bag = zeros(len(all_words), dtype=float32)
    
    for w in all_words:
        bag[w == tokenized_sentence] = 1.0

    return bag
