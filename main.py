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

    def calculate_entropy(self, password):
        """Calculate password entropy (measure of randomness)"""
        char_set_size = 0
        if re.search(r'[a-z]', password):
            char_set_size += 26
        if re.search(r'[A-Z]', password):
            char_set_size += 26
        if re.search(r'[0-9]', password):
            char_set_size += 10
        if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]', password):
            char_set_size += 33  # Common special characters count
        
        if char_set_size == 0:  # Fallback if nothing matched
            char_set_size = 26
            
        entropy = math.log2(char_set_size) * len(password)
        return entropy

    def check_repetitive_patterns(self, password):
        """Check for repetitive patterns like 'aaa', '111', etc."""
        issues = []
        pattern = re.compile(r'(.)\1{2,}')  # Same character repeated 3+ times
        if pattern.search(password):
            issues.append("Contains repetitive characters (e.g., 'aaa', '111')")
        
        # Check for repeated sequences (e.g., abcabc)
        for i in range(2, len(password)//2 + 1):
            for j in range(len(password) - i*2 + 1):
                if password[j:j+i] == password[j+i:j+i*2]:
                    issues.append(f"Contains repeated sequence: '{password[j:j+i]}'")
                    break
            
        return issues
    
    def check_keyboard_patterns(self, password):
        """Check for keyboard patterns"""
        password_lower = password.lower()
        for pattern in self.keyboard_patterns:
            if pattern in password_lower:
                return True
        
        # Check for diagonal patterns
        diagonals = ["qaz", "wsx", "edc", "rfv", "tgb", "yhn", "ujm"]
        for diag in diagonals:
            if diag in password_lower:
                return True
                
        return False

    def check_date_patterns(self, password):
        """Check for date patterns in the password"""
        # Common date formats: MMDDYYYY, DDMMYYYY, MMDDYY, DDMMYY, YYYY
        date_patterns = [
            r'\d{2}[/\-_.]\d{2}[/\-_.]\d{2,4}',  # MM/DD/YYYY or similar
            r'\d{8}',  # MMDDYYYY or DDMMYYYY
            r'\d{6}',  # MMDDYY or DDMMYY
            r'\d{4}',  # Year like 1990, 2021
        ]
        
        current_year = datetime.now().year
        years = [str(year) for year in range(current_year-100, current_year+1)]
        
        for pattern in date_patterns:
            if re.search(pattern, password):
                return True
                
        for year in years:
            if year in password:
                return True
                
        return False
    
    def generate_password_suggestion(self, length=16):
        """Generate a strong password suggestion"""
        char_sets = [
            string.ascii_lowercase,
            string.ascii_uppercase,
            string.digits,
            string.punctuation
        ]
        
        # Ensure at least one character from each set
        password = [random.choice(char_set) for char_set in char_sets]
        
        # Fill the rest with random characters from all sets
        all_chars = ''.join(char_sets)
        password.extend(random.choice(all_chars) for _ in range(length - len(password)))
        
        # Shuffle to avoid predictable positioning
        random.shuffle(password)
        return ''.join(password)

    def estimate_crack_time(self, entropy):
        """Estimate password cracking time based on entropy"""
        # Assume 10 billion guesses per second (modern hardware)
        guesses_per_second = 10000000000
        
        # 2^entropy is the average number of guesses needed
        seconds = (2**entropy) / guesses_per_second
        
        if seconds < 60:
            return f"Instant to {seconds:.1f} seconds"
        elif seconds < 3600:
            return f"About {seconds/60:.1f} minutes"
        elif seconds < 86400:
            return f"About {seconds/3600:.1f} hours"
        elif seconds < 2592000:
            return f"About {seconds/86400:.1f} days"
        elif seconds < 31536000:
            return f"About {seconds/2592000:.1f} months"
        elif seconds < 315360000:  # 10 years
            return f"About {seconds/31536000:.1f} years"
        else:
            return f"Over {seconds/31536000:.0f} years"
