special_characters = "!@#$%^&*()_-=+\]|"

def pass_logic(password):
    if len(password) < 7:
        return "Password must be at least seven characters long."
    
    if not any(char in special_characters for char in password):
        return "Password must contain at least one special character."
    
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."
    
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return "Password must have at least one upper case and one lower case letter."
    
    if len(password) > 12 and any(char in special_characters for char in password) and any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(char.islower() for char in password):
        return "Password is very strong"
    
    return "Password is strong.  It meets basic criteria."


def main():

    attempts_left = 3

    while attempts_left > 0:

        print("Welcome to Password Checker!")
        input("Press any key to continue...\n")

        print("The password must meet the following criteria:\n1. It must include at least 1 special character\n2. It must be at least 7 characters long\n3. It must include at least 1 number\n")

        password = input("Please enter your password: ")

        feedback = pass_logic(password)
        print(feedback)

        if 'strong' in feedback:
            break
        else:
            attempts_left -= 1
            print(f"Attempts Left: {attempts_left}.")

        if attempts_left == 0:
            print(f"You have exceeded your attempts. Please try again later.")

if __name__ == "__main__":
    main()



