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
###############################################################
alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def newString(c):
        result = ""
        for num in c:
                if(isinstance(num, int)):
                   result += alph[num]
                else:
                   result += num[0]

                
        return result
#function to take spaces out of key
def cleanKey(key):
        key = key.split()
        key = "".join(key)
        return key

#take in key with the plaintext to encrypt the message
def encrypt(string, key):
        key = cleanKey(key)
        nonAlph = 0
        cipher = []
        for i in range(len(string)):
                ###encryption algorithim, if char is not in alph array
                #print (not (string[i] in alph))
                if(not (string[i] in alph)):
                        cipher.append([string[i]])
                        nonAlph += 1
                        
                else:
                        
                        index = ((alph.index(string[i]) + alph.index(key[((i-nonAlph) % len(key))])) % 26)
                        if(string[i].isupper()):
                                index += 26
                        cipher.append(index)
        print (newString(cipher))

#take in key with ciphertext to decrypt the message
def decrypt(string, key):
        key = cleanKey(key)
        nonAlph = 0
        plain = []
        for i in range(len(string)):
                ###encryption algorithim, if char is not in alph array
                #print (not (string[i] in alph))
                if(not (string[i] in alph)):
                        plain.append([string[i]])
                        nonAlph += 1
                        
                else:
                        
                        index = ((26 + alph.index(string[i]) - alph.index(key[((i-nonAlph) % len(key))])) % 26)
                        if(string[i].isupper()):
                                index += 26
                        plain.append(index)
        print (newString(plain))




#confirm proper usage of program
if(len(sys.argv) < 3):
	print("Usage: python vigener-cipher.py -[d or e] KEY")
	exit()

#determine mode
if(sys.argv[1] == "-d"):
	#process all inputs from stdin as ciphertext
	####need to add ability to loop until interrupt
	text = sys.stdin.readline().split('\n')
	decrypt(text[0], sys.argv[2])

elif(sys.argv[1] == "-e"):
	#process all inputs from stdin as plaintext
	####looping here too
	text = sys.stdin.readline().split('\n')
	encrypt(text[0], sys.argv[2])

#report improper usage
else:
	print("Usage: python vigener-cipher.py -[d or e] KEY")
