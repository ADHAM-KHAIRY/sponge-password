import re
import math
import getpass
import time
import random
import string
from datetime import datetime
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
nums = "0123456789"
schars = "!@#$%^&*()-_=+[{]}|;:" 


print("""                                                                             
 ____                                 ____               
/ ___| _ __   ___  _ __   __ _  ___  |  _ \ __ _ ___ ___ 
\___ \| '_ \ / _ \| '_ \ / _` |/ _ \ | |_) / _` / __/ __|
 ___) | |_) | (_) | | | | (_| |  __/ |  __/ (_| \__ \__ \
|____/| .__/ \___/|_| |_|\__, |\___| |_|   \__,_|___/___/
      |_|                |___/                           

""")
print("Sponge pass is a decent Password Strength Checker")
print("Enter a password you want to check [Press Enter to stop].")

def check_score(password):
    score = 0
    for i in uppercase:
        if i in password:
            score += 1
            break
    for i in lowercase:
        if i in password:
            score += 1
            break
    for i in nums:
        if i in password:
            score += 1
            break
    for i in schars:
        if i in password:
            score += 1
            break
    if len(password)>8:
        score += 1
    return score
        





while True:
    password = input("> ")
    if password: 
        print(check_score(password))
    else:
        break
    