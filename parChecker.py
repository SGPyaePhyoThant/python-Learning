# parChecker.py

from stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        print('symbol',symbol)
        if symbol == "(":
            s.push(symbol)
            print(s.items)
        else:
            print('this is else condition')
            print(s.is_empty())
            print(s.items)
            if s.is_empty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False

print(parChecker('((()))'))
