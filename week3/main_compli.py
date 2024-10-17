# Calculator

from operation import add, subtract, multiply, divide


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
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        print("Invalid operation")

    print("The result is: " + str(result))


if __name__ == "__main__":
    main()
