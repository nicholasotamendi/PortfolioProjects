#random password generator 
#ask the user if they want to generate a password or not
#if yes, ask for password length then proceed to generate the password and print it 
#if no, quit the program


import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()+_")

def generate_password():
    password_length = int(input("How long do you want your password to be: "))
    random.shuffle(characters)

    password = []
    for i in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)

    password = "".join(password)

    print(f"Your password is {password}")


option = input("Do you want to generate a password: (Yes/No): ").lower()

#while True:

if option == "yes":
    generate_password()
elif option == "no":
    print("goodbye, program ended")
    quit()
else:
    print("Invalid Input, Enter Yes or No")

  
