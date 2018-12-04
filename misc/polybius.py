class polybius_square(object):
    table = [[] for i in range(5)]
    for i in range(5):
        row = []
        for j in range(5):
            alphabet_index = (j + i * 5)
            row.append(chr(alphabet_index + 97))
        table[i] = row

    def decipher(self, c_text):
        p_text = ""
        if len(c_text) % 2 != 0:
            print("unequal length, adding additional 1")
            c_text += "1"

        for i in range(0, len(c_text), 2):
            x, y = (int(c_text[i]), int(c_text[i + 1]))
            p_text += self.table[y - 1][x - 1]

        return p_text
