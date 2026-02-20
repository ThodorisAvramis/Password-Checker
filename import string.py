import string

def check_common_password(password):
    try:
        with open('common-passwords.txt', 'r') as f:
            for line in f:
                if password == line.strip():
                    return True
        return False
    except FileNotFoundError:
        print("Warning: common-passwords.txt not found. Skipping common password check.")
        return False

def password_strength(password):
    score = 0
    length = len(password)

    upper_case = any(c.isupper() for c in password)
    lower_case = any(c.islower() for c in password)
    special_char = any(c in string.punctuation for c in password)
    digits = any(c.isdigit() for c in password)

    character_types = sum([upper_case, lower_case, special_char, digits])
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 17:
        score += 1
    if length >= 20:
        score += 1

    score += min(character_types - 1, 1)  # Cap to avoid score >5

    if score < 4:
        return "Weak", score
    elif score == 4:
        return "Moderate", score
    else:
        return "Strong", score

def feedback(password):
    if not password:
        return "Password cannot be empty."
    
    if check_common_password(password):
        return "Password was found in the common passwords list. Please choose a different password."
    
    strength, score = password_strength(password)

    feedback_message = f"Password strength: {strength} (score: {score}/5)."

    if strength == "Weak":
        feedback_message += " Consider using a longer password with a mix of uppercase letters, lowercase letters, digits, and special characters."

    if len(password) < 8:
        feedback_message += " Password is too short. Consider using at least 8 characters."
    if not any(c.isupper() for c in password):
        feedback_message += " Include at least one uppercase letter."
    if not any(c.islower() for c in password):
        feedback_message += " Include at least one lowercase letter."
    if not any(c in string.punctuation for c in password):
        feedback_message += " Include at least one special character."
    if not any(c.isdigit() for c in password):
        feedback_message += " Include at least one digit."
    
    return feedback_message

password = input("Enter a password to check: ")
print(feedback(password))