# #
#
# l=10 #Global Variables
# def function1(n):
#     print(n, "I have already Printed")
# # # #     # local variable only defined under this function
# # # #
#     global m
#     m=8
#     # global l #Global keyword is used to change the global variable from local scope
#     l = 5
#     l = l + 45
#     print(l , m)
# # # # # # You can change the local variable but YOu can not change the global variable by increasing and decreasing the value. But if you use a (global) keyword in function you can change the value by increasing or decreasing the value of that variable.
# #
# function1("This is me")
# print(l)
# print(m)

#
x=0
def func():
    x=20
    def rohan():
        global x
        x=98
        print(x)

#
#
    print("before calling rohan", x)
    rohan()
    print("After calling rohan", x)# It would not change the value of X because it searches in the main function while not in any function
print(x) # if you change global varible. Then before calling func() you print the value of x you will get the unchanged value 0. but after calling the func() you print the value of x you will get the changed value 98.

func()
print(x)


# do not try to print the value of x in between the func() you will get the error.
# By using global keyword we can change the value of global varible. But we can not change the value of variable of the function ex.- func() , means by rohan() function we can not change the value of the func() function by using global keyword. we can only change the value of the global variable i.e x=0