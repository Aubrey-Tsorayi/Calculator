run = True

while run == True:

    num1 = float(input("Enter first number: ")) 
    num2 = float(input("Enter second number: "))
    op = input("Enter an operator: ")

    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '/':
        print(num1 / num2)
    elif op == '*':
        print(num1 * num2)
    else:
        print("operator not register, Try again")