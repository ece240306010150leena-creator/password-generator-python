import secrets
import string
from datetime import datetime

print("=" * 50)
print("🔐 Secure Password Generator")
print("=" * 50)

# -----------------------------
# User Input
# -----------------------------
length = int(input("Enter password length: "))

if length <= 0:
    print("Invalid length.")
    exit()

uppercase = input("Include Uppercase letters? (Y/N): ").upper()
lowercase = input("Include Lowercase letters? (Y/N): ").upper()
numbers = input("Include Numbers? (Y/N): ").upper()
symbols = input("Include Symbols? (Y/N): ").upper()

characters = ""

if uppercase == "Y":
    characters += string.ascii_uppercase

if lowercase == "Y":
    characters += string.ascii_lowercase

if numbers == "Y":
    characters += string.digits

if symbols == "Y":
    characters += "!@#$%^&*()-_=+[]{}?/"

if characters == "":
    print("Please select at least one character type.")
    exit()

# -----------------------------
# Generate Password
# -----------------------------
password = ""

for i in range(length):
    password += secrets.choice(characters)

# -----------------------------
# Password Strength Checker
# -----------------------------
score = 0

if length >= 8:
    score += 1

if length >= 12:
    score += 1

if any(c.isupper() for c in password):
    score += 1

if any(c.islower() for c in password):
    score += 1

if any(c.isdigit() for c in password):
    score += 1

if any(c in "!@#$%^&*()-_=+[]{}?/" for c in password):
    score += 1

if score <= 2:
    strength = "Weak 🔴"
elif score <= 4:
    strength = "Medium 🟡"
else:
    strength = "Strong 🟢"

# -----------------------------
# Display Password
# -----------------------------
print("\nGenerated Password:")
print(password)

print("\nPassword Strength:", strength)

# -----------------------------
# Save Password
# -----------------------------
save = input("\nSave password to file? (Y/N): ").upper()

if save == "Y":
    with open("password_history.txt", "a") as file:
        file.write(
            f"{datetime.now()} | {password} | {strength}\n"
        )

    print("Password saved successfully.")

print("\nThank you for using Secure Password Generator!")
