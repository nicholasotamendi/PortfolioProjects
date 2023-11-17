#dice roller simulator

#ask the user to roll a die 
#simulate the numbers 
#show users the value of the die rolled

#import random
#define function to roll die
#create dictionary that holds the images of the die
#implement dice roller function 


import random



def dice_roll():

    die_drawing = {
        1: """
            _______
           |       |
           |   ⚀   |
           |_______|
          """,
        2: """
            _______
           |       |
           | ⚁   ⚁ |
           |_______|
          """,
        3: """
            _______
           | ⚂     |
           |   ⚂   |
           |     ⚂ |
           |_______|
          """,
        4: """
            _______
           | ⚃   ⚃ |
           |       |
           | ⚃   ⚃ |
           |_______|
          """,
        5: """
            _______
           | ⚄   ⚄ |
           |   ⚄   |
           | ⚄   ⚄ |
           |_______|
          """,
        6: """
            _______
           | ⚅   ⚅ |
           | ⚅   ⚅ |
           | ⚅   ⚅ |
           |_______|
          """
    }
    roll = input("Do you want to roll a die (Yes/No): ").lower()

    while roll == 'yes':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"The dice rolled landed on {dice1} and {dice2} \n")
        print(f"{die_drawing[dice1]} {die_drawing[dice2]}")

        roll = input("Do you want to roll again? (Yes/No): ")

dice_roll()