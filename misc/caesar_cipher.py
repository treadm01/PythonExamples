import string


class CaesarCipher(object):
    def __init__(self):
        self.alphabet_size = 26
        self.first_letter = 'a'

    def change_string(self, c_text, shift):
        n_string = ""  # string to re-shift and return
        for character in c_text:
            n_string += self._shift_alphabet(character, shift)
        return n_string

    def _shift_alphabet(self, first, second):
        shift_letter = (string.ascii_lowercase.index(first) + second) % self.alphabet_size
        shift_letter = chr(shift_letter + (ord(self.first_letter) - 1))
        return shift_letter
