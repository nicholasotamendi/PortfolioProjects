#currency converter 

#def  function that converts a currency
#collect input from user 
#convert the currency 
# show the converted currency to user 

def main():
    print("This program converts US Dollars to Pounds Sterling \n")

    dollars = eval(input("Enter your dollar amount: "))
    naira = convert_to_naira(dollars)
    print(f"{dollars} dollars is the equivalent of {naira} naira")

convert_to_naira = lambda dollars: 1001 * dollars

main()
