# Andy Y. Ly
# A10710024
# COGS 18 Project
from cipherlib import *
from pathlib import Path

#driver program
def ManyCrypt():
    #user input
    print("Enter Filename: ")
    file = input()
    if Path(file).is_file():
        print("File Selected: "  + str(file))
    else:
        print("File Not Found")
        exit()
    print("Select Encryption: C - CaeserCipher,  M - MD5, V- VernamCipher")
    encryption = input()

    #boolean operator to determine encode or decode
    bool_op = None
    if encryption == 'C' or encryption == 'c' :
        print("Select CaeserCipher Operation: E - Encode, D - Decode")
        operation = input()
        if operation == "E":
            bool_op = True
        elif operation == "D":
            bool_op = False
        print("Input Key Value(integer): ")
        key = int(input())
        Caeser(file, key, bool_op)

    elif encryption == "M" or encryption == 'm':
        print("Hashing is non-reversible!")
        MD5HashHex(file)

    elif encryption == 'V' or encryption == 'v' :
        print("Select VernamCipher Operation: E - Encode, D - Decode")
        operation = input()
        if operation == "E":
            bool_op = True
        elif operation == "D":
            bool_op = False
        print("Input Key Value(string): ")
        key = input()
        Vernam(file, key, bool_op)
    else:
        print("Invalid Selection.")

ManyCrypt()
