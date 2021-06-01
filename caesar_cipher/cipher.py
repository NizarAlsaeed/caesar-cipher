import nltk
import re

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names
word_list = words.words()
name_list = words.words()

def encrypt(text, key):
    shifted = ''
    text = re.sub(r'[^A-Za-z\s]','',text)
    for char in list(text):
        if ord(char) in range(97,123) or ord(char) in range(65,91):
            if key > 0:
                if char.lower() == 'z':
                    char=chr(ord('z')-26)
                shifted += chr(ord(char) + key%26)    
            elif key < 0:
                if char.lower() == 'a':
                    char=chr(ord('a')+26)
                shifted += chr(ord(char) - abs(key)%26)
        else: shifted += ' '
    return shifted.lower()

def decrypt(text, key):
    return encrypt(text,-key)

def crack(text):
    """will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key."""
    # we will try every key from 1 to 26 and after each shift we will check if all the words inside the 
    # text is acutually correct English words.
    for key in range(1,27):
        counter = 0
        possible_result = decrypt(text,key)

        for word in possible_result.split(' '):
            if not (word.lower() in word_list or word in name_list):
                continue
            counter += 1
        if counter == len(possible_result.split(' ')):
                return possible_result
    return None


print(encrypt('i did not find it, please go back!',5))
print(decrypt('n ini sty knsi ny uqjfxj lt gfhp',5))
print(crack('n ini sty knsi ny uqjfxj lt gfhp'))

