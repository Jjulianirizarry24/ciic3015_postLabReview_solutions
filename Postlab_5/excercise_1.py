def validatePassword():
    attempts = 3
    correct_password = "YourStrongPassword"
    
    while attempts > 0:
        # Ask the user for the password
        user_password = input("Enter your password: ")
        
        # Check if the password matches
        if user_password == correct_password:
            return True  # Password matched
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect password. You have {attempts} attempt(s) remaining.")
    
    return False  # All attempts failed
    
def processLogin():
    if validatePassword():
        print("User logged in!")
    else:
        print("All attempts used. Failed to match the password.")


processLogin()