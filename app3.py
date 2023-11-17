# Basic Calculator
# Define functions needed (add, sub, mul and div)
# print options to the user 
# ask for values
# call the functions
# while loop to continue the program until the user exits  
# print the result

def add(a,b):
    answer = a+b
    print(f"{a} + {b} = {answer} \n")

def sub(a,b):
    answer = a-b
    print(f"{a} - {b} = {answer} \n")

def mul(a,b):
    answer = a* b
    print(f"{a} * {b} = {answer} \n")

def div(a,b):
    answer = a/b
    print(f"{a} / {b} = {answer} \n")

while True:
    print("A, Addition")
    print("B, Subtraction")
    print("C, Multiplication")
    print("D, Division")
    print("E, Exit")


    choice = input("Input your choice: ").upper()
    if choice == "A":
        print("Addition")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        add(a,b)

    elif choice == "B":
        print("Subtraction")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        sub(a,b)    

    elif choice == "C":
        print("Multiplication")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        mul(a,b)

    elif choice == "D":
        print("Division")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        div(a,b)

    else:
        print("End of the Program")
        quit()