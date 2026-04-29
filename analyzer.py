# analyzer.py
import re
import math

def calculate_entropy(password):
    pool = 0
    if re.search(r"[a-z]", password): pool += 26
    if re.search(r"[A-Z]", password): pool += 26
    if re.search(r"[0-9]", password): pool += 10
    if re.search(r"[!@#$%^&*]", password): pool += 14
    return round(len(password) * math.log2(pool), 2) if pool else 0

def analyze(password):
    feedback = []
    score = 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    if re.search(r"[A-Z]", password): score += 1
    else: feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password): score += 1
    else: feedback.append("Add lowercase letters.")

    if re.search(r"[0-9]", password): score += 1
    else: feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*]", password): score += 1
    else: feedback.append("Add special characters.")

    entropy = calculate_entropy(password)

    strength = "Weak"
    if score >= 5 and entropy > 60:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"

    return strength, entropy, feedback