# -*- coding: utf-8 -*-
from tkinter import *

# The first two lines of program title

window = Tk()
window.title("Ceasar Şifreleme Yöntemi")

# Encryption algorithm
def Encryption():
    # First clean if we have encrypted text
    encryptiontext.delete(0.0, END)
    # We define to which alphabet we want to use
    # If you want you can change the alphabet
    alphabet = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r",
             "s",
             "ş", "t", "u", "ü", "v", "y", "z"]
    lengthalphabet = len(alphabet)
    # we get entry from interface
    text = list(entrytext.get(0.0, END))
    # We took the length so that it would process up to the number of letters in the text and we would process it with the for loop
    textlength = int(len(text))
    for i in range(textlength):
        # We are looking at the text string as this is the text string, so we can get it as a char (character) array
        # we found letter
        character = str(text[i])
        #we check character is in the alphabet and if there is:
        try:
            # we found the character and repair the change
            location = int(alphabet.index(character)) + 3
            if location>lengthalphabet:
                location=location-lengthalphabet
            # define the new character
                newcharacter = str(alphabet[location])
            # change the old character from the new
                text[i] = newcharacter
            # if we get error we do this :
        except:
            # if character is not in the alpahabet don't change it
            text[i] = character
            # And final process we read this the interface
    for characters in text:
        encryptiontext.insert(INSERT,characters)

# Decoding algorithm : Same logic encryption but we just change the +3
def Decode():
    entrytext.delete(0.0, END)
    alphabet = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r",
              "s",
              "ş", "t", "u", "ü", "v", "y", "z"]
    encryptionentry = list(encryptiontext.get(0.0, END))
    length = int(len(encryptionentry))
    for i in range(length):
        character = str(encryptionentry[i])
        try:
            locate = int(alphabet.index(character)) -3
            newcharacter = str(alphabet[locate])
            encryptionentry[i] = newcharacter
        except:
            encryptionentry[i] = character
    for characters in encryptionentry:
        entrytext.insert(INSERT, characters)

labeltext = Label(text="Metni Giriniz : ")
labeltext.pack()

# Entry text config.

entrytext = Text()
entrytext.config(width=30, height=5, font="arial 12")
entrytext.pack()

labeltext2= Label(text="Şifreli Metin: ")
labeltext2.pack()

# encryption text config.

encryptiontext= Text()
encryptiontext.config(width=30, height=5, font="arial 12")
encryptiontext.pack()

# encrption button config.
encryption= Button(text=" Şifrele ", command=Encryption)
encryption.pack()

# decoding button config

decoding= Button(text="Şifre çöz", command=Decode)
decoding.pack()

mainloop()