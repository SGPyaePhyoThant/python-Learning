p = False

while p == False:
    yourValue = input('Enter the number between 0 to 9: ')

    try:
        insertedValue = int(yourValue)

        if insertedValue > 9:
            print('Your number is over 9 !')
        elif insertedValue < 0:
            print('Your number is under 0 !')
        else:
            print('Your number is: ', insertedValue,'! .' '___Thanks You___')
            p = True
    except ValueError:
        print('Please enter Number and Value must be between 0 to 9')
