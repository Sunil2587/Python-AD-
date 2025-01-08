# Function to password validity

def validate_password(password):
    if len(password) >=8:
        if any(char.isdigit() for char in password):
            if any(char.isupper() for char in password):
                if any(char.islower() for char in password):
                    if any(char in'!@#$%^&*()' for char in password):
                        if any(char.isalpha() for char in password):
                            if any(char.isalnum() for char in password):
                                return True
    return False
password=input("Enter a password: ")

if validate_password(password):
    print("Enter password is valid")
else:
    print("Password is Invalid")