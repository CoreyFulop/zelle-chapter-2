# futval_investment_plan.py
# Determines the future value of an investment,
# given a yearly investment, interest rate, and duration.

def main():
    print("This program determines the future value of an investment.")

    yearly_amount = eval(input("How much to invest each year: "))
    apr  = eval(input("Enter the annual interest rate: "))
    years = eval(input("How many years will the investment plan last: "))

    investment = yearly_amount * (1 + apr)

    for i in range(years - 1):
        investment = (investment + yearly_amount ) * (1 + apr) 

    print(f"The value of the investment plan after {years} is {investment}.")


main()
