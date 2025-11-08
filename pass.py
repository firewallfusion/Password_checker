import re
import math
import hashlib

# Common weak passwords (dictionary)
common_passwords = ["password", "123456", "qwerty", "abc123", "admin", "letmein"]

def calculate_entropy(password):
    pool = 0
    if re.search(r"[a-z]", password): pool += 26
    if re.search(r"[A-Z]", password): pool += 26
    if re.search(r"[0-9]", password): pool += 10
    if re.search(r"[^a-zA-Z0-9]", password): pool += 32
    entropy = len(password) * math.log2(pool) if pool > 0 else 0
    return round(entropy, 2)

def check_password_strength(password):
    if password.lower() in common_passwords:
        return "❌ Weak (Dictionary word used!)"
    entropy = calculate_entropy(password)
    if len(password) < 8:
        return "❌ Weak (Too short)"
    elif entropy < 40:
        return "⚠️ Medium strength"
    else:
        return "✅ Strong password"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ---- Main Program ----
password = input("Enter your password: ")

print("\n🔒 Password Analysis:")
print(f"Password: {password}")
print(f"Strength: {check_password_strength(password)}")
print(f"Entropy: {calculate_entropy(password)} bits")
print(f"SHA-256 Hash: {hash_password(password)}")
