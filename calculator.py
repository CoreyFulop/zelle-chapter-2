# calculator.py
# A really basic calculator.

def main():
    print("This program is a really basic calculator - it will evaluate a given mathematical expression.")

    calculations = eval(input("How many calculations would you like to make: "))

    for i in range(calculations):
        result = eval(input("Enter a mathematical expression to calculate: "))
        print(f"The answer is {result}")


main()
