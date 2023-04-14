import random
import string

# Function to generate a password
def generate_password(length, complexity):
    # Define the character sets based on the complexity level
    if complexity == 'low':
        chars = string.ascii_lowercase
    elif complexity == 'medium':
        chars = string.ascii_letters + string.digits
    elif complexity == 'high':
        chars = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''
    for i in range(length):
        password += random.choice(chars)
    
    return password

# Get the length and complexity of the password from the user
length = int(input("Enter the length of the password: "))
complexity = input("Enter the complexity of the password (low, medium, or high): ")

# Generate the password and print it to the console
password = generate_password(length, complexity)
print("Your password is:", password)
