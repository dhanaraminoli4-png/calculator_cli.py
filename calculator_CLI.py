oper = ['+', '-', '/', '*', '%']

while True:
    num1 = int(input("what is the number?"))
    operator = input("what opertor?")
    num2 = int(input("what is the number?"))

    if operator in oper:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        elif operator == '%':
            result = num1 % num2
        else:
            print("this calculator is not advanced enough to solve equations like that?")
    
    print("your result is: ")
    print(result)




