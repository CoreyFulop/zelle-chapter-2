# futval_defined_period.py
# Determines the future value of an investment,
# given a defined period and investment value.

def main():
    print("This program calculates the future value")
    print("of an n-year investment.")

    principal = eval(input("Enter the inital principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the duration of the investment, in years: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print(f"The value in {years} years is {principal}.")


main()
