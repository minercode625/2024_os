# Calculator

def main():
    print("Welcome to the calculator!")
    print("Please enter the first number:")
    num1 = float(input())
    print("Please enter the second number:")
    num2 = float(input())
    print("Please enter the operation:")
    operation = input()

    result = 0
    if operation == "+":
        print("Not implemented yet")
    elif operation == "-":
        print("Not implemented yet")
    elif operation == "*":
        print("Not implemented yet")
    elif operation == "/":
        print("Not implemented yet")
    else:
        print("Invalid operation")

    print("The result is: " + str(result))


if __name__ == "__main__":
    main()
