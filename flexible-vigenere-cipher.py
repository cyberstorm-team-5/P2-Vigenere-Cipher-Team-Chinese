#!/usr/bin/env python2.7
################################################################
# Authors: Team Chinese (Lane Arnold, Christopher Boquet,
# 	   Christopher Bouton, Darrell Durousseaux, Clay Fonseca,
#	   Rebecca Grantham, Andrew Maurice)
# Class: CSC 442
# Date: 3-29-2019
# Github Repo: https://github.com/cyberstorm-team-5/P2-Vigenere-Cipher-Team-Chinese
# Description: Program 2: Vigenere Cipher
#              The Python code will read either a plaintext or
#              ciphertext from stdin and send the generated
#              output file to stdout. The mode (-e to encrypt or
#              -d to decrypt) and the key must be provided via
#              the command line for the code to work properly.
################################################################
import sys
from array import *
import string
import re
###############################################################

#array of all lowercase and uppercase letters (in that order)
#TO USE CUSTOM: HAVE ALPH BE THE ARRAY WITH THE DESIRED VALUES IN THE DESIRED ORDER,
#THEN CONVERT THAT ARRAY TO A STRING (or just use string in first place like shown)
alph = string.ascii_letters



#take an array of numbers (and non-alphabet symbols) to convert to
#the new text (either plain or cipher)
def newText(code):
        result = ""
        for num in code:
        
                if(isinstance(num, int)):
                        #ints in the code array match to indexes of corresponding letters in alph,
                        #so that letter is appended to the text
                        result += alph[num]
                        
                else:
                        #all other indexes in code array will be another array that holds a
                        #non-alphabetic symbol from the inputted text that is preserved to
                        #insert directly into the new text
                        result += num[0]
                        
        return result


#take spaces out of key
def cleanKey(key):
        key = key.split()
        key = "".join(key)
        return key



###############ENCRYPT NOT ADJUSTED##################
#take in key with the plaintext to encrypt the message
def encrypt(string, key):

        #int showing how many non-alphabetic symbols have been processed. Because
        #those symbols are not modified in Vigenere cipher, the key should not advance
        #an index after processing one, so this int compensates for the offset between
        #the index used for the key and the one used for the index of the string
        nonAlph = 0
        cipher = []
        key = cleanKey(key)

        #encrypt one index of the inputted string at a time
        for i in range(len(string)):
                
                #check if a non-alphabetic symbol is present
                if(not (string[i] in alph)):
                
                        #append the non-alphabetic symbol and increment
                        #the counter to keep the key index accurate
                        cipher.append([string[i]])
                        nonAlph += 1
                        
                else:

                        #use encryption equation for vigenere
                        #[ciphertext at index i =(plaintext at i + key at i)%26]
                        #where, to compensate for the key possibly being shorter than the text, the
                        #modulus of the key's length is taken to loop back around, but before that the
                        #amount of non-alphabetic symbols is subtracted from it to compensate for
                        #symboles liek numbers and spacing not advancing the key index
                        index = ((alph.index(string[i]) + alph.index(key[((i-nonAlph) % len(key))])) % 26)

                        #for uppercase letter, add 26 to go from lowercase's index to uppercase's
                        if(string[i].isupper()):
                                index += 26
                                
                        cipher.append(index)

        #send resulting ciphertext to stdout
        print (newText(cipher))


#take in key with ciphertext to decrypt the message
def decrypt(string, key):

        #SHOW HOW MANY NON ALPHABETIC (WHERE ALPHABETIC MEANS NOT IN OUR ALPH VARIABLE, NOT
        #THE LITERAL ALPHABET) SYMBOLS HAVE BEEN PROCESSED BECAUSE THOSE SYMBOLS ARE IGNORED (LIKE
        #EXPLAINED ABOVE FOR ENCRYPT)
        nonAlph = 0
        plain = []
        key = cleanKey(key)


        #make array with the position number for each letter in the key
        keyPositions = []
        for val in key:
                keyPositions.append(alph.index(val))

        keyIndex = 0
        for val in string:

                if keyIndex == len(keyPositions):
                        keyIndex = 0

                #check if a non-alphabetic symbol is present
                if(not (val in alph)):
                        plain.append(val)
                        #nonAlph += 1

                else:
                        myKeyPos = ((len(alph) + alph.index(val)) - keyPositions[keyIndex]) % len(alph)
                        plain.append(alph[myKeyPos])
                        keyIndex += 1
                        print (val + " " + str(alph.index(val)))
                

        '''
        #decrypt one index of the inputted string at a time
        for i in range(len(string)):
                
                #check if a non-alphabetic symbol is present
                if(not (string[i] in alph)):
                        plain.append([string[i]])
                        nonAlph += 1
                        
                else:
                        #use decryption equation for vigenere
                        #[plaintext at index i =(26 + ciphertext at i - key at i)%26]
                        #where the same compensation for non-alphabetic symbols is applied to the
                        #key, and 26 is added overall to ensure teh result of the subtraction will
                        #never be negative without impacting modulus
                        #index = ((26 + alph.index(string[i]) - alph.index(key[((i-nonAlph) % len(key))])) % 26)

                        #for uppercase letter, add 26 to go from lowercase's index to uppercase's
                        #if(string[i].isupper()):
                                #index += 26


                        

                                
                        plain.append(index)'''

        #send resulting plaintext to stdout
        #print (newText(plain))
        print plain

        
#confirm proper usage of program
if(len(sys.argv) < 3):
	print("Usage: ./vigener-cipher.py -[d or e] KEY")
	exit()


#determine mode
if(sys.argv[1] == "-d"):

	#process all inputs from stdin as ciphertext
        text = sys.stdin.readline()
        while(text):
        
                #split off the newline before sending to decrypt
                text = text.split('\n')
                decrypt(text[0], sys.argv[2])
                text = sys.stdin.readline()

elif(sys.argv[1] == "-e"):

	#process all inputs from stdin as plaintext
	text = sys.stdin.readline()
        while(text):
        
                #split off the newline before sending to encrypt
                text = text.split('\n')
                encrypt(text[0], sys.argv[2])
                text = sys.stdin.readline()

#report improper usage
else:
	print("Usage: ./vigener-cipher.py -[d or e] KEY")
