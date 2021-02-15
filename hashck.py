#!/bin/python3
# -*- coding: utf-8 -*-
"""
Coded by parsa kazazi
GitHub: https://github.com/parsa-kazazi
Twitter: https://twitter.com/parsa_kazazi

Quick and easy Hash Cracker python3 script
Works on all operating systems
For legal activities only
Version: 1.0
"""

import os
import hashlib
import time

os_name = os.name

if (os_name == "nt"):
    os.system("title HASH-CK")
else:
    os.system("printf '\033]2;HASH-CK\a'")

print("""
HASH-CK
Quick and easy Hash Cracker. version 1.0
""")

put = str("\033[94m[*]\033[0m ")
info = str("\033[94m[i]\033[0m ")
good = str("\033[92m[+]\033[0m ")
error = str("\033[91m[!]\033[0m ")

hash_types = ["1", "2", "3", "3", "4", "5", "6", "7", "8", "9", "10", "10", "11", "12", "13", "14"]

print("""
1-md5   2-sha1   3-sha224   4-sha256   5-sha384   6-sha512   7-blake2b
8-blake2s   9-sha3_224   10-sha3_256   11-sha3_384   12-sha3_512
""")

hash_type_number = input(put + "Select hash type: ")

if (hash_type_number not in hash_types):
    print(error + "Invailed input\n")
    exit()

hash_string = input(put + "Enter Your hash: ")
wordlist_filename = input(put + "Wordlist file (Enter to default): ")
if (wordlist_filename == ""):
    wordlist_filename = "passwords.txt"

try:
    wordlist_file = open(wordlist_filename, "r", encoding="latin-1").readlines()
except FileNotFoundError:
    print(error + '"' + wordlist_filename + '" : File not found\n')
    exit()
except UnicodeDecodeError:
    print(error + '"' + wordlist_filename + '" : Unicode decode error\n')
    exit()
print("")
time.sleep(2)
print(info + "Please Wait...\n")
time.sleep(3)
for password in wordlist_file:

    password = password.strip()
    
    if (hash_type_number == "1"):
        result = hashlib.md5(password.encode("utf-8")).hexdigest()
    elif (hash_type_number == "2"):
        result = hashlib.sha1(password.encode("utf-8")).hexdigest()
    elif (hash_type_number == "3"):
        result = hashlib.sha224(password.encode("utf-8")).hexdigest()
    elif (hash_type_number == "4"):
        result = hashlib.sha256(password.encode("utf-8")).hexdigest()
    elif (hash_type_number == "5"):
        result = hashlib.sha384(password.encode("utf-8")).hexdigest()
    elif (hash_type_number == "6"):
        result = hashlib.sha512(password.encode("utf-8")).hexdigest()
    elif (hash_type_number == "7"):
        result = hashlib.blake2b(password.encode("utf-8")).hexdigest()
    elif (hash_type_number == "8"):
        result = hashlib.blake2s(password.encode("utf-8")).hexdigest()
    elif (hash_type_number == "9"):
        result = hashlib.sha3_224(password.encode("utf-8")).hexdigest()
    elif (hash_type_number == "10"):
        result = hashlib.sha3_256(password.encode("utf-8")).hexdigest()
    elif (hash_type_number == "11"):
        result = hashlib.sha3_384(password.encode("utf-8")).hexdigest()
    elif (hash_type_number == "12"):
        result = hashlib.sha3_512(password.encode("utf-8")).hexdigest()
    
    print(info + "Try test: " + password)

    if (hash_string == result):
        print(good + "Hash Cracked!")
        time.sleep(1)
        print(info + hash_string + " > " + password + "\n")
        exit()

print('\n' + error + 'Wordlist "' + wordlist_filename + '" cannot crack hash: ' + hash_string + '\n')
