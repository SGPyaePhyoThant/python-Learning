# p = False

# while p == False:
#     yourValue = input('Enter the number between 0 to 9: ')

#     try:
#         insertedValue = int(yourValue)

#         if insertedValue > 9:
#             print('Your number is over 9 !')
#         elif insertedValue < 0:
#             print('Your number is under 0 !')
#         else:
#             print('Your number is: ', insertedValue,'! .' '___Thanks You___')
#             p = True
#     except ValueError:
#         print('Please enter Number and Value must be between 0 to 9')


# print triangle
# for i in range(1,6):
#     for x in range(i):
#         print('*',end="")
#     print('/')

# Exercise 2.2
# total = 0
# for x in range(10):
#     total = total + x
# print(total)

# list = [1,5,2,7,8,9,200,155]

# p = 0
# for t in range(len(list)):
#     p = p + list[t]
#     print('now p is : ',p)
# print('total value: ',p)

# for t in list:
#     p = p + t
# print('total value is: ', p)

# enumerate function()

# for (p,item) in enumerate(list):
#     print(p,item)

# Immutable And Mutable
# Tuple cannot be changed
# List can be changed

# Finding Max Number
# list = [1,5,2,7,8,9,200,155]
# largestNumber = list[0]
# for p in list:
#     if largestNumber < p:
#         largestNumber = p
# print('Largest number in list is: ' , largestNumber)

# Finding Min Number
# smallestNumber = list[0]
# for p in list:
#     if smallestNumber > p:
#         smallestNumber = p
# print('Smallest Number is : ', smallestNumber)

# Array [3,4,1,2,9,7] ဆိုပြီး ရှိပါသည်။
# user ဆီက နံပတ်ကို လက်ခံပြီး 
# array အခန်းထဲတွေ တွေ့မတွေ့ user ကို print ထုတ်ပြပါမည်။
# တွေ့ခဲ့ပါက အခန်း ဘယ်လောက်မှာ တွေ့ခဲ့သည်ကို print ထုတ်ပြပါမည်။

# serverList = [3,4,1,1,9,7]
# old
# p = False
# doesNotExist = False
# while p == False:
#     userInput = input('Enter number between 0 to 9')

#     try:
#             insertedValue = int(userInput)
#             if insertedValue > 9:
#                 print('Your number is over 9 !')
#             elif insertedValue < 0:
#                 print('Your number is under 0 !')
#             else:
#                 print('Your number is: ', insertedValue,'! .' '___Thanks You___')
#                 print('Finding your number in server_____, Wait. . . .')
#                 for i,y in enumerate(serverList):
#                     if y ==  insertedValue:
#                         print('user inserted number exit, index is',i)
#                     else:
#                         doesNotExist = True
#                 if doesNotExist:
#                     print('Does not exist, please try again later')
#                     doesNotExist = False
#                 p = True
#     except ValueError:
#         print('Please enter Number and Value must be between 0 to 9')

# 
# Updated code ~~
# server_list = [3,4,1,1,9,7]

# p = False
# while p == False:
#     userInput = input('Enter number between 0 to 9')

#     try:
#             inserted_value = int(userInput)
#             if inserted_value > 9:
#                 print('Your number is over 9 !')
#             elif inserted_value < 0:
#                 print('Your number is under 0 !')
#             else:
#                 print('Your number is: ', inserted_value,'! .' '___Thanks You___')
#                 print('Finding your number in server_____, Wait. . . .')
#                 if inserted_value in server_list:
#                     index_of_number = server_list.index(inserted_value)
#                     print('user inserted number found, index is',index_of_number)
#                 else:
#                     print('user inserted number does not found')
#             p = True
#     except ValueError:
#         print('Please enter Number and Value must be between 0 to 9') 

# Finding Max Number and show index .
# server_list = [3,4,1,1,9,7]
# largest_number = server_list[0]
# for p in server_list:
#     if largest_number < p:
#         largest_number = p
# index_of_largest_number = server_list.index(largest_number)
# print('Largest number in list is: ' , largest_number)
# print('Index of Largest number in list is: ' , index_of_largest_number)

# FUNCTION

# def printHello(value):
#     print('Hello',value)

# printHello("Pyae")
# printHello("Phyo")

# def sum(value1,value2):
#         try:
#             insertedVal1 = int(value1)
#             insertedVal2 = int(value2)
#             return value1+value2
#         except ValueError:
#             print('Please number only to sum')
#             return None

# print('Sum :', sum(25,20))

# Finding Max Number for two Array with function 
# list_one = [1,5,2,7,8,9,200,155]
# list_two = [1,2,5,6,9,3,2]
# def findMax(checkArray):
#     largest_number = checkArray[0]
#     for p in checkArray:
#         if largest_number < p:
#             largest_number = p
#     print('Largest number in ${checkArray} is: ' , largest_number)

# findMax(list_one)
# findMax(list_two)


# Exercise 2-4
# def minus(number1,number2):
#     return print(number1,number2)
# minus(1,2)

# triangle_star 
p = False
while p == False:
    userInput = int(input('Enter number value between 0 and 9'))

    try:
        inserted_value = int(userInput)

        if inserted_value > 9:
            print('Your number is over 9 !')
        elif inserted_value < 0:
            print('Your number is under 0 !')
        else:
            print('Your number is: ', inserted_value,'! .' '___Thanks You___')
            print('Now.... Our Program is running to make triangle ... Wait...')
            for i in range(1,inserted_value+1):
                for j in range(i):
                    print('*',end=" ")
                print("")

            p = True
    except ValueError:
        print('Please enter Number and Value must be between 0 to 9')














