def is_strong_password(password):
    """
    Check if a password is strong based on basic criteria:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one digit
    - Contains at least one special character
    
    Returns True if strong, False otherwise
    """
    if len(password) < 8:
        return False
    
    has_uppercase = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
    
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    
    return has_uppercase and has_digit and has_special