# fahrenheit_to_celsius.py

def main():
    print("This program converts Fahrenheit temperatures to Celsius.")

    fahrenheit = eval(input("Please enter the Fahrenheit temperature: "))

    celsius = (fahrenheit - 32) * (5/9)

    print(f"{fahrenheit} degrees Fahrenheit is {celsius} degrees Celsius.")


main()
