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


#take in key with the plaintext to encrypt the message
def encrypt(string, startIndex):

        #string to hold plain text
        plain = ""

        startIndex = int(startIndex)

        #startIndex is the shift applied for the cipher. Get a shifted alph
        #that has the new order
        shiftedAlph = alph[startIndex:] + alph[:startIndex]
        
        for val in string:

                #check if a non-alphabetic symbol is present
                if(not (val in alph)):
                        plain += val

                else:
                        #to encrypt, find the index of the val in the original alphabet. That will be the index
                        #of the correct letter in the shifted alphabet
                        index = alph.index(val)
                        plain += shiftedAlph[index]
                        
                        print (val + " " + str(alph.index(val)))

        #send resulting plaintext to stdout
        #print (newText(plain))
        print plain


#take in key with ciphertext to decrypt the message
def decrypt(string, startIndex):

        #string to hold plain text
        plain = ""

        startIndex = int(startIndex)

        #startIndex is the shift applied for the cipher. Get a shifted alph
        #that has the new order
        shiftedAlph = alph[startIndex:] + alph[:startIndex]
        
        for val in string:

                #check if a non-alphabetic symbol is present
                if(not (val in alph)):
                        plain += val

                else:
                        #to decrypt, find the index of the val in the shifted alphabet. That will be the index
                        #of the correct letter in the original alphabet
                        index = shiftedAlph.index(val)
                        plain += alph[index]
                        
                        print (val + " " + str(alph.index(val)))

        #send resulting plaintext to stdout
        #print (newText(plain))
        print plain

        
#confirm proper usage of program
if(len(sys.argv) < 3):
	print("Usage: ./vigener-cipher.py -[d or e] startIndex")
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
	print("Usage: ./vigener-cipher.py -[d or e] startIndex")
