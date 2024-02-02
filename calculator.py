firstNumber = input('First Number : ')
yourOperator = input('Enter operator : ')
secondNumber = input('Second Number : ')
try:
    first = int(firstNumber)
    second = int(secondNumber)
    output = True
    if yourOperator == '+':
        result = firstNumber + secondNumber
    elif yourOperator == '-':
        result = firstNumber - secondNumber
    elif yourOperator == '*':
        result = firstNumber * secondNumber
    elif yourOperator == '/':
        result = firstNumber / secondNumber
    else:
        print('Wrong Operator')
        output = False
    if output == True:
     print('result is',result) 
except ValueError:
    print('Numbers only accept to calculate! Please try again . . ')
