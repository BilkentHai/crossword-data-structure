from alphabet import Alphabet
from word import Word


class CWDS:

    def __init__(self, max_len):
        self.max_len = max_len
        self.alphabets = [Alphabet() for i in range(max_len)]
        self.words = []


    def add_word(self, wordStr):
        self.words.append(Word(wordStr))
        # TODO: do something