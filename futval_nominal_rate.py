# futval_nominal_rate.py
# Determines the future value of an investment.

def main():
    print("This program determines the future value of an investment.")

    principal = eval(input("What is the pricipal investment: "))
    rate = eval(input("What is the yearly interest rate: "))
    years = eval(input("What is the duration of the investment, in years: "))
    periods = eval(input("How many times is the interest compounded each year?"))

    for i in range(years * periods):
        principal = principal * (1 + rate/periods)

    print(f"The value of the investment after {years} years is {principal}.")


main()
