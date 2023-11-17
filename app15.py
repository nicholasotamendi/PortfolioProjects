#leap year checker
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("This year is a leap year")
            else:
                print("This year is not a leap year")
        else:
            print("This year is a leap year")
    else:
        print("This year is not a leap year")

user_year = eval(input("Enter your year: "))
is_leap_year(user_year) 
