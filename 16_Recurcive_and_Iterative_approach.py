#Recursion- To use Function inside Function

# def print2(str1):
#
#     print("This is " + str1)
#
# print2("Python")

#
# #n! = n*n-1*n-2*n-3.....1
# #n! = n*(n-1)!
# def factorial_itrative(n):
#     """
#     :param n: Integer
#     :return: n*n-1*n-2*n-3.....1
#     """
#     fac=1
#     for i in range(n):
#         fac=fac * (i+1)
#     return fac
# number = int(input("Enter the number for which you want to take the factorial:\n"))
# # print("Factorial of the number is ", factorial_itrative(int(input("factorial of the number is:\n"))) )
# print("Factorial using iterative method", factorial_itrative(number))
# # #
# #
# # # #
# # #
# # #
# # #
# #
# def factorial_recursive(n):
#     if n==1 or n==0:
#         return 1
#
#     else:        return n*factorial_recursive(n-1)
#     # print(a)
# number=int(input("Enter the number"))
# # print("Factorial using iterative method", factorial_recursive("Enter your favorite number"))
# print("Factorial using recursive method", factorial_recursive(number))
#
# # print(a)
#
#
#
# #Fibonacci sequence
# #0 1 1 2 3 5 8 13 ....
#
# def fibonacci(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# number=int(input("Enter number you want to calculate fibonacci series"))
# print("Fibonacci series of number is: ", fibonacci(number))







# def ru(n):
#     num=1
#     for i in range(n):
#         num=num*(i+1)
#     return num
# number= int(input('tljlksljflk'))
# print('them',ru(number))

# number = int(input("Theh number is"))
# def ru(n):
#     if n==1 or n==0:return 1
#     else:return n*ru(n-1)
# print('factorial of', ru(number))