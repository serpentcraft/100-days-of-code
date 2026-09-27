def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

import art

def calculator():
    print(art.logo)
    calculating = True
    n1 = float(input("Enter first number: "))

    while calculating:
        for symbol in operations:
            print(symbol)

        while True:
            operator = input("Enter a mathematical operator: ")
            if operator in operations:
                break
            print("Invalid operator. Try again.")

        n2 = float(input("Enter second number: "))
        answer = operations[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {answer}")

        choice = input(f"Do you want to continue with the previous result {answer}? (y/n): ")

        if choice == "y":
            n1 = answer
        else:
            calculating = False
            print("\n" * 20)
            calculator()

calculator()
