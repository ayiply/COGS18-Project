# Andy Y. Ly
# A10710024
# COGS 18 Project

import hashlib

#Helper function to open file
def openfile(filename):
    data = open(filename, "r")
    input = data.readline()
    input = input.strip()
    return input

#Generate Hash Byte and Hexideciaml equivalents
def MD5HashHex(filename):
    input = openfile(filename)
    output = ""
    output = hashlib.md5(input.encode())
    output_filename = "MD5Hash_Output_" + str(filename)
    ex = open(output_filename, "w")
    ex.write("Original String: " + input + "\n" + "Byte Equivalent: " + str(output.digest())+ "\n" + "Hexideciaml Equivalent: " + output.hexdigest())
    ex.close
    print("Output file: " + output_filename)

#Vernam Cipher
def Vernam(filename, key, encode = False):
    input = openfile(filename)
    output = ""
    ptr = 0
    for char in input:
        output = output + chr(ord(char) ^ ord(key[ptr]))
        ptr = ptr + 1
        if ptr == len(key):
            ptr = 0
    if encode:
        output_filename = "VernamCrypt_Output_" + str(filename)
    else:
        output_filename = "VernamDecrypt_Output_" + str(filename)
    ex = open(output_filename, "w")
    ex.write(output)
    ex.close()
    print("Output file: " + output_filename)

#Caeser Cipher
def Caeser(filename, key, encode = False):
    input = openfile(filename)
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low_alpha = alpha.lower()
    output = ""
    if encode:
        for letter in input:
            if letter in alpha:
                letter_index = (alpha.find(letter) + key) % len(alpha)
                output = output + alpha[letter_index]
            elif letter in low_alpha:
                letter_index = (low_alpha.find(letter) + key) % len(low_alpha)
                output = output + low_alpha[letter_index]
            else:
                output = output + letter
            output_filename = "CaeserEncrypt_Output_" + str(filename)
    else:
        for letter in input:
            if letter in alpha:
                letter_index = (alpha.find(letter) - key) % len(alpha)
                output = output + alpha[letter_index]
            elif letter in low_alpha:
                letter_index = (low_alpha.find(letter) - key) % len(low_alpha)
                output = output + low_alpha[letter_index]
            else:
                output = output + letter
        output_filename = "CaeserDecrypt_Output_" + str(filename)

    ex = open(output_filename, "w")
    ex.write(output)
    ex.close
    print("Output file: " + output_filename)
    print("Key: " + str(key))
