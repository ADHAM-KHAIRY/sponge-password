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
        
    def check_password(self, password):
        """
        Comprehensive password strength analysis.
        Returns a dictionary with all assessment results.
        """
        results = {
            "score": 0,
            "max_score": 10,
            "strength": "",
            "feedback": [],
            "details": {},
            "entropy": 0,
            "crack_time_estimate": "",
            "suggestions": [],
        }
        
        # Record this check in history
        self.password_history.append({
            "timestamp": datetime.now(),
            "length": len(password),
            "score": 0  # Will update this later
        })
        
        # 1. Check length
        length = len(password)
        results["details"]["length"] = length
        
        if length < 8:
            results["feedback"].append("Password is too short (minimum 8 characters recommended)")
        elif length < 12:
            results["score"] += 1
            results["feedback"].append("Password length is acceptable but could be improved (12+ recommended)")
        elif length < 16:
            results["score"] += 2
            results["feedback"].append("Good password length")
        else:
            results["score"] += 3
            results["feedback"].append("Excellent password length")
        
        # 2. Check character composition
        has_lowercase = bool(re.search(r'[a-z]', password))
        has_uppercase = bool(re.search(r'[A-Z]', password))
        has_numbers = bool(re.search(r'[0-9]', password))
        has_special = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]', password))
        
        results["details"].update({
            "has_lowercase": has_lowercase,
            "has_uppercase": has_uppercase,
            "has_numbers": has_numbers,
            "has_special": has_special
        })
        
        char_categories = sum([has_lowercase, has_uppercase, has_numbers, has_special])
        
        if char_categories == 4:
            results["score"] += 3
            results["feedback"].append("Excellent character variety")
        elif char_categories == 3:
            results["score"] += 2
            results["feedback"].append("Good character variety")
        elif char_categories == 2:
            results["score"] += 1
            results["feedback"].append("Limited character variety")
        else:
            results["feedback"].append("Poor character variety - use a mix of character types")
        
        # 3. Check common passwords
        password_lower = password.lower()
        if password_lower in self.common_passwords:
            results["score"] = 0  # Automatically set to zero
            results["feedback"].append("❌ CRITICAL: This is a commonly used password!")
            results["suggestions"].append("Choose a completely different password")
        
        # 4. Check for keyboard patterns
        if self.check_keyboard_patterns(password):
            results["score"] = max(results["score"] - 2, 0)
            results["feedback"].append("Contains keyboard patterns (e.g., 'qwerty', 'asdf')")
            results["suggestions"].append("Avoid sequential keyboard patterns")
        
        # 5. Check for date patterns
        if self.check_date_patterns(password):
            results["score"] = max(results["score"] - 1, 0)
            results["feedback"].append("Contains what appears to be a date")
            results["suggestions"].append("Avoid using dates, especially personal ones")
        
        # 6. Check for repetitive patterns
        repetitive_issues = self.check_repetitive_patterns(password)
        if repetitive_issues:
            results["score"] = max(results["score"] - 1, 0)
            results["feedback"].extend(repetitive_issues)
            results["suggestions"].append("Avoid repeating characters or sequences")
        
        # 7. Check for sequential characters
        if any(seq in password_lower for seq in self.common_sequences):
            results["score"] = max(results["score"] - 1, 0)
            results["feedback"].append("Contains sequential characters")
            results["suggestions"].append("Avoid sequential characters like '1234' or 'abcd'")
        
        # 8. Calculate entropy and crack time
        entropy = self.calculate_entropy(password)
        results["entropy"] = round(entropy, 2)
        results["crack_time_estimate"] = self.estimate_crack_time(entropy)
        
        if entropy < 40:
            results["feedback"].append(f"Low entropy ({entropy:.2f} bits) - easily crackable")
        elif entropy < 60:
            results["feedback"].append(f"Moderate entropy ({entropy:.2f} bits)")
        elif entropy < 80:
            results["feedback"].append(f"Good entropy ({entropy:.2f} bits)")
            results["score"] += 1
        else:
            results["feedback"].append(f"Excellent entropy ({entropy:.2f} bits)")
            results["score"] += 2
        
        # 9. Generate custom suggestions
        if not has_lowercase:
            results["suggestions"].append("Add lowercase letters (a-z)")
        if not has_uppercase:
            results["suggestions"].append("Add uppercase letters (A-Z)")
        if not has_numbers:
            results["suggestions"].append("Add numbers (0-9)")
        if not has_special:
            results["suggestions"].append("Add special characters (!@#$%^&*())")
        if length < 12:
            results["suggestions"].append(f"Increase length to at least 12 characters (currently {length})")
            
        # If no specific suggestions were added, provide a general one
        if not results["suggestions"]:
            results["suggestions"].append("Your password is already quite strong")
        
        # Add a password generator suggestion
        results["generated_password"] = self.generate_password_suggestion()
        
        # Determine final strength category
        if results["score"] <= 3:
            results["strength"] = "Weak"
        elif results["score"] <= 6:
            results["strength"] = "Moderate"
        elif results["score"] <= 8:
            results["strength"] = "Strong"
        else:
            results["strength"] = "Very Strong"
            
        # Update history with final score
        self.password_history[-1]["score"] = results["score"]
            
        return results
