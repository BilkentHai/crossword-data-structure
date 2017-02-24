import string

from letter import Letter


class Alphabet:

    def __init__(self):
        self.letters = [Letter(c) for c in string.ascii_lowercase]

    def getLetter(self, c):
        return self.letters[c - 'a']