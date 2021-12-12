# convert_welcome.py
# Converts Celsius temperatures to Fahrenheit,
# and prints a welcome message.

def main():
    print("This program converts Celsius temperatures into Fahrenheit.")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = (9/5) * celsius + 32
    print(f"The temperature is {fahrenheit} degrees Fahrenheit.")


main()
