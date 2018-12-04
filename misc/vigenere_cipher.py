import string


class VigenereCipher(object):
    table = [[] for i in range(26)]
    for i in range(26):
        row = []
        for j in range(26):
            alphabet_index = (j + i) % 26
            row.append(chr(alphabet_index + 97))
        table[i] = row

    def decipher(self, codeword, c_text):
        codeword_index = 0
        p_text = ""
        for symbol in c_text:
            p_text += chr(self.table[string.ascii_lowercase.index(codeword[codeword_index])].index(symbol) + 97)
            codeword_index += 1
            if codeword_index == len(codeword):
                codeword_index = 0
        return p_text
