import re

def check_password_strength(password):
    # Define password strength criteria
    criteria = {
        'length': len(password) >= 8,
        'uppercase': re.search(r'[A-Z]', password) is not None,
        'lowercase': re.search(r'[a-z]', password) is not None,
        'digit': re.search(r'[0-9]', password) is not None,
        'special_char': re.search(r'[\W_]', password) is not None  # Non-word characters
    }

    # Calculate strength score
    score = sum(criteria.values())

    # Determine strength level and provide feedback
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Feedback message
    feedback = {
        'length': "Password is at least 8 characters long." if criteria['length'] else "Password should be at least 8 characters long.",
        'uppercase': "Password contains uppercase letters." if criteria['uppercase'] else "Password should include at least one uppercase letter.",
        'lowercase': "Password contains lowercase letters." if criteria['lowercase'] else "Password should include at least one lowercase letter.",
        'digit': "Password contains digits." if criteria['digit'] else "Password should include at least one digit.",
        'special_char': "Password contains special characters." if criteria['special_char'] else "Password should include at least one special character."
    }

    # Output feedback
    print(f"Password Strength: {strength}\n")
    for key in criteria:
        print(f"- {feedback[key]}")

# Example usage:
password = input("Enter a password to check its strength: ")
check_password_strength(password)
