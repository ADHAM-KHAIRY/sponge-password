# Sponge Password Checker

A comprehensive password strength evaluation tool that analyzes passwords using multiple security criteria to help users create and maintain strong, secure passwords.


## Features

- **Comprehensive Password Analysis**: Evaluates passwords based on multiple criteria:
  - Length assessment
  - Character variety (lowercase, uppercase, numbers, special characters)
  - Entropy calculation
  - Common password detection
  - Keyboard pattern recognition
  - Date pattern detection
  - Repetitive sequence identification

- **Detailed Feedback**: Provides specific feedback on password strengths and weaknesses

- **Crack Time Estimation**: Calculates approximate time needed to crack the password

- **Password Suggestions**: Offers personalized improvement recommendations

- **Password Generator**: Creates strong, random passwords on demand

- **Password Statistics**: Tracks and displays statistics of previously checked passwords

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/ADHAM-KHAIRY/sponge-password.git
   cd sponge-password
   ```

2. Install required dependencies:
   ```
   pip install pyfiglet
   ```

## Usage

Run the program:
```
python password_checker.py
```

### Available Commands

- **Check Password**: Simply enter any password to analyze its strength
- **Generate**: Type `generate` to create a strong random password
- **Statistics**: Type `stats` to view statistics about previously checked passwords
- **Help**: Type `help` to display available commands
- **Exit**: Type `exit`, `quit`, or `q` to close the program

## Example Output

```
============================================================
PASSWORD STRENGTH: STRONG
Score: 8/10
============================================================

ANALYSIS:
  • Good password length
  • Excellent character variety
  • Good entropy (65.33 bits)

ENTROPY: 65.33 bits
ESTIMATED CRACK TIME: About 2.3 years

SUGGESTIONS:
  • Your password is already quite strong

PASSWORD SUGGESTION:
  7dE$xP!9aF#2jKm@

Note: Generated passwords are not stored and are shown only once.
============================================================
```

## Security Note

This tool is for educational purposes only. For optimal security:

- Use a dedicated password manager
- Enable two-factor authentication where available
- Use unique passwords for each service
- Regularly update critical passwords

## Technical Details

The password strength evaluation uses several techniques:

- **Entropy Calculation**: Measures randomness based on character set size and password length
- **Pattern Detection**: Identifies common patterns that weaken passwords
- **Dictionary Checking**: Compares against known common passwords
- **Keyboard Layout Analysis**: Detects sequential characters from keyboard rows

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
