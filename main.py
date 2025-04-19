import re
import math
import getpass
import time
import random
import string
from datetime import datetime
# uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# lowercase = "abcdefghijklmnopqrstuvwxyz"
# nums = "0123456789"
# schars = "!@#$%^&*()-_=+[{]}|;:" 


# print("""                                                                             
#  ____                                 ____               
# / ___| _ __   ___  _ __   __ _  ___  |  _ \ __ _ ___ ___ 
# \___ \| '_ \ / _ \| '_ \ / _` |/ _ \ | |_) / _` / __/ __|
#  ___) | |_) | (_) | | | | (_| |  __/ |  __/ (_| \__ \__ \
# |____/| .__/ \___/|_| |_|\__, |\___| |_|   \__,_|___/___/
#       |_|                |___/                           

# """)
# print("Sponge pass is a decent Password Strength Checker")
# print("Enter a password you want to check [Press Enter to stop].")

# def check_score(password):
#     score = 0
#     for i in uppercase:
#         if i in password:
#             score += 1
#             break
#     for i in lowercase:
#         if i in password:
#             score += 1
#             break
#     for i in nums:
#         if i in password:
#             score += 1
#             break
#     for i in schars:
#         if i in password:
#             score += 1
#             break
#     if len(password)>8:
#         score += 1
#     return score
        
class AdvancedPasswordChecker:
    def __init__(self):
        # Common passwords dictionary 
        self.common_passwords = {
            "password", "123456", "qwerty", "admin", "welcome", 
            "letmein", "monkey", "1234567890", "abc123", "password123"
        }
        
        # Common sequences to check for
        self.common_sequences = [
            "1234", "4321", "abcd", "qwerty", "asdf", "zxcv"
        ]
        
        # Common keyboard patterns
        self.keyboard_patterns = [
            "qwerty", "asdfgh", "zxcvbn", "qazwsx", "123456"
        ]
        
        # Common substitutions
        self.substitutions = {
            'a': ['4', '@'], 'e': ['3'], 'i': ['1', '!'], 'o': ['0'], 
            's': ['$', '5'], 'l': ['1'], 't': ['7', '+']
        }
        
        # Initialize history of checked passwords
        self.password_history = []

