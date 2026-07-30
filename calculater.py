import math

print("===== Python Calculator =====")

while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Power")
    print("7. Factorial")
    print("8. Sin")
    print("9. Cos")
    print("10. Tan")
    print("11. Log (base 10)")
    print("12. Exit")

    choice = int(input("Enter your choice: "))

    if choice == "12":
        print("Thank you for using the calculator!")
        break

    if choice in ["1", "2", "3", "4", "6"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result =", num1 + num2)

        elif choice == "2":
            print("Result =", num1 - num2)

        elif choice == "3":
            print("Result =", num1 * num2)

        elif choice == "4":
            if num2 != 0:
                print("Result =", num1 / num2)
            else:
                print("Error! Division by zero.")

        elif choice == "6":
            print("Result =", math.pow(num1, num2))

    elif choice == "5":
        num = float(input("Enter a number: "))
        if num >= 0:
            print("Square Root =", math.sqrt(num))
        else:
            print("Square root of a negative number is not allowed.")

    elif choice == "7":
        num = int(input("Enter a positive integer: "))
        if num >= 0:
            print("Factorial =", math.factorial(num))
        else:
            print("Factorial is not defined for negative numbers.")

    elif choice == "8":
        angle = float(input("Enter angle in degrees: "))
        print("Sin =", math.sin(math.radians(angle)))

    elif choice == "9":
        angle = float(input("Enter angle in degrees: "))
        print("Cos =", math.cos(math.radians(angle)))

    elif choice == "10":
        angle = float(input("Enter angle in degrees: "))
        print("Tan =", math.tan(math.radians(angle)))

    elif choice == "11":
        num = float(input("Enter a positive number: "))
        if num > 0:
            print("Log =", math.log10(num))
        else:
            print("Log is only defined for positive numbers.")

    else:
        print("Invalid choice! Please try again.")