firstNumber = input(' Enter First Number')
secondNumber= input(' Enter Second Number')
try:
    first = int(firstNumber)
    second= int(secondNumber)
    if second <= 0:
        print('secondNumber must be greater than 0')
    else:
        print('first/second')
        print(first/second)
except ValueError:
    print('Enter Number only______')
