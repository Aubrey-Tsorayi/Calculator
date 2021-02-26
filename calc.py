from math import *

run = True

option = input("Do you want a simple calculator (Y/n): ")

while run == True:

    if option.lower() == "y":
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            op = input("Enter an operator: ")

            if op == "+":
                print(num1 + num2)
            elif op == "-":
                print(num1 - num2)
            elif op == "/":
                try:
                    print(num1 / num2)
                except ZeroDivisionError:
                    print("You cant divide by zero")
            elif op == "*":
                print(num1 * num2)
            else:
                print("operator not registered, Try again")
        except ValueError:
            print("Enter a valid number")

    elif option.lower() == "n":
        print("Please select an option")
        print(
            """
            pi: to get the value of pi
            pow: calculate power
            sq: to get the sqaure root
            si: sin of an angle
            co: cos of an angle
            ta: tan of an angle
            quit: quits calculator

        """
        )

        command = input(">>: ")

        if command == "pi":
            print("The value of pi is " + str(pi))

        elif command == "pow":
            try:
                base = eval(input("Enter base number: "))
                power = eval(input("Enter power number "))
                print(pow(base, power))
            except NameError as err:
                print("Enter an valid number")

        elif command == "sq":
            try:
                sqa = eval(input("Enter number to be squared: "))
                print(sqrt(sqa))
            except NameError as err:
                print("Enter an valid number")

        elif command == "si":
            try:
                si = eval(input("Enter an angle: "))
                print(round(sin(si)))
            except NameError as err:
                print("Enter an valid number")

        elif command == "co":
            try:
                si = eval(input("Enter an angle: "))
                print(round(cos(si)))
            except NameError as err:
                print("Enter an valid number")

        elif command == "ta":
            try:
                si = eval(input("Enter an angle: "))
                print(round(tan(si)))
            except NameError as err:
                print("Enter an valid number")

        elif command == "quit":
            print("THANK YOU")
            break

        else:
            print("Invalid option, please select a valid option")
