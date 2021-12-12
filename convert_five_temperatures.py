# convert_five_temperatures.py
# Converts five Celsius temperatures to Fahrenheit,
# demonstrates the use of loops.

def main():
    print("This program converts Celsius temperatures into Fahrenheit.")
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = (9/5) * celsius + 32
        print(f"The temperature is {fahrenheit} degrees Fahrenheit.")


main()