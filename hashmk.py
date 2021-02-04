#!/bin/python3
# -*- coding: utf-8 -*-
"""
Hash maker
Convert a string to hash
"""

import hashlib

string = input("\nEnter string : ")
print("\nSelect Hash type")
print("""
1-md5   2-sha1   3-sha224   4-sha256   5-sha384   6-sha512   7-blake2b   8-blake2s
9-sha3_224   10-sha3_256   11-sha3_384   12-sha3_512
""")
hash_type_number = input(": ")
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
if (hash_type_number not in numbers):
    print("\nInvailed input")
    exit()
elif (hash_type_number == "1"):
    hash_type = "md5"
elif (hash_type_number == "2"):
    hash_type = "sha1"
elif (hash_type_number == "3"):
    hash_type = "sha224"
elif (hash_type_number == "4"):
    hash_type = "sha256"
elif (hash_type_number == "5"):
    hash_type = "sha384"
elif (hash_type_number == "6"):
    hash_type = "sha512"
elif (hash_type_number == "7"):
    hash_type = "blake2b"
elif (hash_type_number == "8"):
    hash_type = "blake2s"
elif (hash_type_number == "9"):
    hash_type = "sha3_224"
elif (hash_type_number == "10"):
    hash_type = "sha3_256"
elif (hash_type_number == "11"):
    hash_type = "sha3_384"
elif (hash_type_number == "12"):
    hash_type = "sha3_512"

def hashing(hash_type, string):
    hash = hashlib.new(hash_type, bytes(string,"utf-8")).hexdigest()
    return hash
    
hash = hashing(hash_type, string)
print("\n" + string + " : " + hash + "\n")