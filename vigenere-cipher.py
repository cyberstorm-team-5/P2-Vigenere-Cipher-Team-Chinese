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
###############################################################

#take in key with the plaintext to encrypt the message
def encrypt(string, key):
	return "encrypt " + string + " " + key

#take in key with ciphertext to decrypt the message
def decrypt(string, key):
	return "decrypt " + string + " " + key



#confirm proper usage of program
if(len(sys.argv) < 3):
	print("Usage: python vigener-cipher.py -[d or e] KEY")
	exit()

#determine mode
if(sys.argv[1] == "-d"):
	#process all inputs from stdin as ciphertext
	####need to add ability to loop until interrupt
	text = sys.stdin.readline().split('\n')
	print(decrypt(text[0], sys.argv[2]))

elif(sys.argv[1] == "-e"):
	#process all inputs from stdin as plaintext
	####looping here too
	text = sys.stdin.readline().split('\n')
	print(encrypt(text[0], sys.argv[2]))

#report improper usage
else:
	print("Usage: python vigener-cipher.py -[d or e] KEY")
