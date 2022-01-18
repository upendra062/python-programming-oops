# ###-----------self--------------
# #####decorator.
# def hero_my(powerss):
#     def heroine():
#         print("My power is growing very fast")
#         powerss()
#         print("Meri power world mai dhoom macha rhi hai")
#     return heroine
#
# @hero_my
# def upendra_power():
#     print("I am the boss of the universe.")
#
# upendra_power=hero_my(upendra_power)
#
# # upendra_power()
# print("I love you upendra you are my rockstar")
###-----------self--------------

#Decorators-Which modifies the functionality of a function
# def function1():
#     print("Subscribe Now")
# #
# func2=function1#Here function1 is assigned to func2  (address pass karte hai agar parenthesis nhi hai to )
# del function1 #Is func2 prints or not
# func2()
# function1()


# Code under is to return a function from a function
# def funcret(num):
#     if num==1:
#         return print
#
#     if num==0:
#         return sum
#
# a=funcret(0)
# # a("Hello World")
# b=[1,2,3]
# # # print(sum(b))
# print(a(b))
# a(int(2,3))
# sum(int(5))


#Below code is to pass function as an argument
def executor(func):
    func("This")

executor(print)

def dec2(gkj):
    pass
# Decorators
def dec1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Executed")
        return "Hello"

    return nowexec

@dec1
def who_are_you():
    print("We are Engineers")
    return "Hello"
# # #
who_are_you=dec1(who_are_you)
# who_are_you=dec1(who_are_you)
#
# print(who_are_you())



def upendra(func):
    def ritu():
        print("Yai print honai vala hai")
        print(func())
        print("Yai print ho gaya")
        return "Hello"
    return ritu

@upendra
def sweata():
    print("humari jeet hogi")
    # return "hello"

# sweata = upendra(sweata)
# print(sweata())
print(sweata())

# decorator new one
def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div = smart_div(div)
div(2,4)
