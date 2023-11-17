#Interest Rate monthy payment calculator 
#collect the necessary inputs: principal, interest rate, tenor
#calculate the monthly payment
#show that to the user

def main():
    print("This is a monthtly interest rate payment loan calculator \n")

    principal = float(input("Enter the loan amount: "))
    apr = float(input("Enter the annual interest rate: "))
    tenor = int(input("Enter the duration in years: "))

    monthly_interest_rate = apr/100
    amount_month = tenor * 12

    monthly_payments = round((principal * monthly_interest_rate)/(1-(1+monthly_interest_rate)**(-amount_month)), 2)
    print(f"The monthly payment for this loan is {monthly_payments}")

main()