import sys

if __name__ == "__main__":
    encrypt_or_decrypt = sys.argv[1][1:]
    key_input = sys.argv[2][2:].upper()
    encrypt_file = sys.argv[3]
    output_file = sys.argv[4]

alphabet = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
alphabet_rev = ["ZYXWVUTSRQPONMLKJIHGFEDCBA"] 
dict_alpha = {' ': ' ', '.': '.', '\n': '\n'} 
dict_alpha_rev = {' ': ' ', '.': '.', '\n': '\n'}

def remove_duplicate(s):
    temp = ""
    for i in range(len(s)):
        if s[i] not in temp:
            temp += s[i]
    return temp

key = remove_duplicate(key_input) # generate key from input by removing duplicates
crypt_alphabet = remove_duplicate(key+alphabet_rev[0]) #add reverse alphabet

#map regular alphabet to crypt alphabet and vice versa
for i in range(len(alphabet[0])):
    dict_alpha[alphabet[0][i]] = crypt_alphabet[i]
    dict_alpha_rev[crypt_alphabet[i]] = alphabet[0][i]

#takes input file and outputfile and required alphabet both for encoding or decoding
def file_write(source, output, alpha):
    readfile = open(source, "r")
    writefile = open(output, "w")
    for line in readfile:
        for i in range(len(line)):
            writefile.write(alpha[line[i].upper()])
    readfile.close()
    writefile.close()

#checks program arguments for encoding or decoding - decoding just creates a new file
if encrypt_or_decrypt == "e":
    file_write(encrypt_file, output_file, dict_alpha)
elif encrypt_or_decrypt == "d":
    file_write(output_file, "decoded.txt", dict_alpha_rev)
