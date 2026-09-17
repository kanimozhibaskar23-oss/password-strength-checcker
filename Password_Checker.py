import string
import math

print("================================")
print("     PASSWORD STRENGTH CHECKER")
print("================================")

password = input("Enter your password: ")

print("\nChecking password strength...")

# Password policy checks
length_ok = len(password) >= 8
uppercase_ok = any(char.isupper() for char in password)
lowercase_ok = any(char.islower() for char in password)
digit_ok = any(char.isdigit() for char in password)
special_ok = any(char in string.punctuation for char in password)

print("\n--- Password Policy Check ---")
print("Length (8+):", length_ok)
print("Uppercase:", uppercase_ok)
print("Lowercase:", lowercase_ok)
print("Digit:", digit_ok)
print("Special Character:", special_ok)

# Entropy calculation
charset = 0

if uppercase_ok:
    charset += 26

if lowercase_ok:
    charset += 26

if digit_ok:
    charset += 10

if special_ok:
    charset += len(string.punctuation)

if charset > 0:
    entropy = len(password) * math.log2(charset)
else:
    entropy = 0

print("\n--- Entropy Calculation ---")
print("Character Set Size:", charset)
print("Entropy:", round(entropy, 2), "bits")

# Common password check
common_passwords = {
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "letmein",
    "welcome",
    "password123"
}

if password.lower() in common_passwords:
    dictionary_found = True
else:
    dictionary_found = False

print("\n--- Dictionary Check ---")

if dictionary_found:
    print("Common Password: YES")
else:
    print("Common Password: NO")

# Strength classification
score = 0

if length_ok:
    score += 1

if uppercase_ok:
    score += 1

if lowercase_ok:
    score += 1

if digit_ok:
    score += 1

if special_ok:
    score += 1

if entropy >= 80 and score == 5:
    strength = "Exceptional"
elif entropy >= 60 and score >= 4:
    strength = "Strong"
elif entropy >= 40 and score >= 3:
    strength = "Moderate"
else:
    strength = "Weak"

if dictionary_found:
    strength = "Weak"

print("\n--- Password Strength ---")
print("Score:", score, "/ 5")
print("Strength:", strength)

# Actionable feedback
print("\n--- Suggestions ---")

if not length_ok:
    print("- Use at least 8 characters.")

if not uppercase_ok:
    print("- Add at least one uppercase letter.")

if not lowercase_ok:
    print("- Add at least one lowercase letter.")

if not digit_ok:
    print("- Add at least one digit.")

if not special_ok:
    print("- Add at least one special character.")

if dictionary_found:
    print("- Avoid common or easily guessed passwords.")

if length_ok and uppercase_ok and lowercase_ok and digit_ok and special_ok and not dictionary_found:
    print("- Good job! Your password meets the basic security policy.")
    print("- For better security, use a longer unique passphrase.")