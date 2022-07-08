from PyDictionary import PyDictionary

dictionary = PyDictionary()

def get_hint(word):

    key = dictionary.meaning(word)
    value = dictionary.meaning(word)
    return "{} - {}".format(key, value)
    
