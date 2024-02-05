# Class
# class animal:
#     number_of_legs = 0

#     def __init__(self):
#         self.number_of_legs = 4

#     def sleep(slept):
#         print('Zzz')

# Instances
# dog = animal()
# dog.number_of_legs = 4
# dog.sleep()
# print("Dog has {} legs".format(dog.number_of_legs))

# bird = animal()
# bird.number_of_legs = 2
# bird.sleep()
# print("Bird has {} legs".format(bird.number_of_legs))

# class function
# class ထဲမှာ function ကို ဖန်တီးတဲ့ အခါမှာ (self) ဆိုပြီး ထည့်ထားတာကို တွေ့ရပါမယ်။ အဲဒီလို ထည့်ထားမှသာ class ထဲမှာ ရှိတဲ့ variable ကို လှမ်းခေါ်လို့ ရပါလိမ့်မယ်။

# Constructor
# class animal:
#     number_of_legs = 0

#     def __init__(self,legs=4):
#         self.number_of_legs = legs
    
# dog = animal(7)
# print('Dog has {} legs'.format(dog.number_of_legs))

# Inheritance

# class animal:
#     number_of_legs = 0

#     def sleep(slef):
#         print('Zzz')

#     def count_legs(self):
#         # self.number_of_legs = legs
#         print('I have {} legs'.format(self.number_of_legs))

# dog = animal()
# dog.sleep()
# dog.count_legs()

# class dog(animal):
#     def __init__(self):
#         self.number_of_legs = 4
#     def bark(self):
#         print('Woof Woof')
# mydog = dog()
# mydog.sleep()
# mydog.bark()
# mydog.count_legs()

# Exercise 3
class MyMath :
    def add(slef,x,y):
        return x+y
    def substract(slef,x,y):
        return x-y
    def multiple(slef,x,y):
        return x*y
    def divide(slef,x,y):
        return x/y
# math = MyMath ()
# print(math.add(4,3))
# print(math.substract(4,3))
# print(math.multiple(4,3))
# print(math.divide(4,3))

class MyMathExt(MyMath):
    def square(self,x):
        return x**2
    def third(self,y):
        return y**3

math = MyMathExt()
print(math.add(5,7))
print(math.substract(10,4))
print(math.multiple(5,2))
print(math.divide(3,2))
print(math.square(2))
print(math.third(6))

