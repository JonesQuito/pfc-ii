import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords


def word_tokenizer(texto):
    return word_tokenize(texto)


def sent_tokenizer(texto):
    return sent_tokenize(texto)


def toLower(texto):
    return texto.lower()


def only_stopwords(texto):
    words = word_tokenize(texto)
    stpwd = stopwords.words('portuguese')
    resources = []
    size = 0
    for w in words:
        if w in stpwd:
            resources.append(w)
            size += 1
            if size == 300:
                break
    return ' '.join(resources), size
    
                         
                  
    