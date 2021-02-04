#!/bin/python3
# -*- coding: utf-8 -*-
"""
Coded by parsa kazazi
@parsa_kazazi (Github, Twitter)

Quick and easy Hash Cracker python3 script
this script can crack md5, sha1, sha224, sha256, sha384, sha512, blake2b, blake2s, sha3_224, sha3_256, sha3_384 and sha3_512 hashes
Works on all operating systems
For legal activities only
Version: 1.0
"""

import os
import hashlib
import time

os_name = os.name

def clear():
    if (os_name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

clear()
if (os_name == "nt"):
    os.system("title Hash Cracker")
else:
    os.system("printf '\033]2;Hash Cracker\a'")

print("""

    ██   ██  █████  ███████ ██   ██        ██████ ██   ██
    ██   ██ ██   ██ ██      ██   ██       ██      ██  ██
    ███████ ███████ ███████ ███████ █████ ██      █████
    ██   ██ ██   ██      ██ ██   ██       ██      ██  ██
    ██   ██ ██   ██ ███████ ██   ██        ██████ ██   ██

    Quick and easy Hash Cracker
""")

question = str("\033[94m[?]\033[0m ")
info = str("\033[94m[i]\033[0m ")
good = str("\033[92m[+]\033[0m ")
error = str("\033[91m[-]\033[0m ")
hash_types = ["1", "2", "3", "3", "4", "5", "6", "7", "8", "9", "10", "10", "11", "12", "13", "14"]

print("""
1-md5   2-sha1   3-sha224   4-sha256   5-sha384   6-sha512   7-blake2b
8-blake2s   9-sha3_224   10-sha3_256   11-sha3_384   12-sha3_512
""")

hash_type_number = input(question + "Select hash type : ")

if (hash_type_number not in hash_types):
    print(error + "Invailed input\n")
    exit()

hash_string = input(question + "Enter Your hash : ")
wordlist_filename = input(question + "Wordlist file (Enter to default) : ")
time.sleep(2)
clear()
for i in range(20):
    print("\n " + "▌" * i + "\n\n" + info + "Please Wait...")
    time.sleep(0.3)
    clear()
time.sleep(2)
if (wordlist_filename == ""):
    wordlist_filename = "passwords.txt"

try:
    wordlist_file = open(wordlist_filename, "r").readlines()
except FileNotFoundError:
    print(error + "“" + wordlist_filename + "” : File not found\n")
    exit()
except UnicodeDecodeError:
    print(error + wordlist_filename + " : Unicode decode error\n")
    exit()
print("")
i = 0
for password in wordlist_file:

    password = password.strip()
    i += 1
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
    
    print(info + "Try test : " + password)

    if (hash_string == result):
        print(good + "Hash Cracked!")
        time.sleep(1)
        print(info + hash_string + " > " + password + "\n")
        exit()

print(error + "Wordlist “" + wordlist_filename + "” cannot crack hash : " + hash_string + "\n")
