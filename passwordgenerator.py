import string
import random

def generate_password():
    # Welcome message
    print("Welcome to the Password Generator!")

    try:
        # Prompt user for password length and number of characters to include
        length = int(input("How long do you want your password to be? (Enter a number): "))
        if length < 1:
            raise ValueError("Password length must be greater than zero.")
        
        include_letters = input("Do you want to include letters? (y/n): ")
        if include_letters == "y":
            num_letters = int(input("How many letters do you want to include? "))
            if num_letters < 0:
                raise ValueError("Number of letters must be non-negative.")
        else:
            num_letters = 0
            
        include_numbers = input("Do you want to include numbers? (y/n): ")
        if include_numbers == "y":
            num_numbers = int(input("How many numbers do you want to include? "))
            if num_numbers < 0:
                raise ValueError("Number of numbers must be non-negative.")
        else:
            num_numbers = 0
            
        include_symbols = input("Do you want to include symbols? (y/n): ")
        if include_symbols == "y":
            num_symbols = int(input("How many symbols do you want to include? "))
            if num_symbols < 0:
                raise ValueError("Number of symbols must be non-negative.")
        else:
            num_symbols = 0
        
        # Define character sets to choose from
        punc_chars = "!@#$%^&*()_-+={[}]|\\:;\"\'<,>.?/"
        num_chars = "1234567890"
        upper_chars = string.ascii_uppercase
        lower_chars = string.ascii_lowercase

        # Ensure enough characters are selected
        if num_letters + num_numbers + num_symbols > length:
            raise ValueError("You have requested more characters than your password length allows.")
            
        # Generate random password
        password = []
        for i in range(num_letters):
            password.append(random.choice(lower_chars + upper_chars))
        for i in range(num_numbers):
            password.append(random.choice(num_chars))
        for i in range(num_symbols):
            password.append(random.choice(punc_chars))
        for i in range(length - num_letters - num_numbers - num_symbols):
            char_set = random.choice([lower_chars, upper_chars, num_chars, punc_chars])
            password.append(random.choice(char_set))

        # Shuffle password and convert to string
        random.shuffle(password)
        password = "".join(password)

        print(f"Your random password is: {password}")
        
    except ValueError as ex:
        print(f"Error: {ex}")
    
generate_password()
