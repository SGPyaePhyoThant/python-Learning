# parChecker.py
from stack import Stack

def parChecker(symbolString):
    s = Stack()
    index = 0
    balanced = True
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "({[":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                pop =s.pop()
                if not matches(pop,symbol):
                    balanced = False

        index = index + 1
    if balanced and s.is_empty():
        return True
    else:
        return False

def matches(open,close):
    openers = "({["
    closers = ")}]"
    return openers.index(open) == closers.index(close)

print(parChecker("([])"))
            

    

