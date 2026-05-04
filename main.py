/mvnw text eol=lf
*.cmd text eol=crlf
import random
import string

def generate_password(length=12):
    """Generates a random password of a given length."""
    # Combine uppercase, lowercase, numbers, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate and print a 16-character password
print("Your generated password is:", generate_password(16))
