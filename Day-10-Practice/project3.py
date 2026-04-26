import random
import string

chars = string.ascii_letters + string.digits + string.punctuation

while True:
    num = int(input("Enter password length: "))

    password = ''.join(random.choice(chars) for _ in range(num))
    print("Generated Password:", password)

    # Strength checks
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    if num < 6:
        print("Weak password ❌ (Too short)")
    elif has_upper and has_lower and has_digit and has_symbol:
        print("Strong password ✅")
        break
    else:
        print("Medium password ⚠️ (Missing some criteria)")