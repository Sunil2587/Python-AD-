# Function to password validity

def validate-password(password):
    if len(password) >=8:
        if any(char.isalpha() for char in password):
            if any(char in "!@#$%^&*()_+=[]:;''<>,.")