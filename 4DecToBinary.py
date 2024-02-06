# Decimal to Binary

from stack import Stack

def divideBy2(dec_number):
    remstack = Stack()

    while dec_number > 0:
        rem = dec_number % 2
        dec_number = dec_number //2
        remstack.push(rem)
    print(remstack.items)
    binary_string = ""
    while not remstack.is_empty():
        binary_string = binary_string + str(remstack.pop())
    print(binary_string)
    return binary_string

divideBy2(668)
