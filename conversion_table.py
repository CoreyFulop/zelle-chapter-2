# conversion_table.py
# Prints a table of Celsius temperatures and corresponding Fahrenheit temperatures
# every 10 deg from 0 C to 100 C.

def main():
    for celsius in range(0, 110, 10):
        fahrenheit = (9/5) * celsius + 32
        print(f"Celsius: {celsius}, Fahrenheit: {fahrenheit}")


main()