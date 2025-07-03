
import random
import string

# Line divider for neatness
line = "-" * 45
print(line)
print("🔐 Welcome To The Secure Password Generator 🔐")
print(line)

# Ask user for password length
length = int(input("Enter the desired password length: "))

# Ask user for character types
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
include_digits = input("Include digits? (y/n): ").lower() == "y"
include_special = input("Include special characters? (y/n): ").lower() == "y"

# Build the character pool
characters = ""
if include_uppercase:
    characters += string.ascii_uppercase  # A-Z
if include_lowercase:
    characters += string.ascii_lowercase  # a-z
if include_digits:
    characters += string.digits           # 0-9
if include_special:
    characters += string.punctuation      # Special characters like !@#$%^&*()

# Check if character pool is empty
if not characters:
    print("Error: No character types selected!")
else:
    # Generate password
    password = "".join(random.choice(characters) for _ in range(length))
    print(line)
    print(f"Your secure password is: {password}")
    print(line)

    # Check password strength
    strength = ""
    if (
        length >= 12 and
        include_uppercase and include_lowercase and include_digits and include_special
    ):
        strength = "🔐 Strong password!"
    elif (
        length >= 8 and
        (include_uppercase or include_lowercase) and (include_digits or include_special)
    ):
        strength = "🟡 Medium Strength Password."
    else:
        strength = "🔴 Weak password! Try making it longer with more special characters."

    print(f"Password Strength: {strength}")
    print(line)

print("\nThank You For Using This Secure Password Generator 😊")
