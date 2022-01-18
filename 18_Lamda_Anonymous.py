# #---------------------------self---------------------------------#
# Lambda functions or anonymous functions
# def add(a, b,):
# #     return a+b
#       return lambda x, y, z , a, b, c: x*y*z*a*b*c
# # #
# minus = lambda x, y: x-y
# rockythesuperstar = lambda x, y, z , a, b, c: x*y*z*a*b*c
#
# print("By adding and multiplying the number")


# def minus(x, y):
#     return x-y
# print(minus(8, 2))
# print(rockythesuperstar(2,2,2,2,2,2))

# # making function to represent first element by normal function
# def a_first(a):
#     return a[1]
#
# a = [[1, 14],[5, 6], [8, 23]]
# a.sort(key=a_first)
# print(a)
# # by lambda function to represent the first element.means koi bhi list list usko di jaye uska first element i.e x:x[1]
# a = [[1, 14], [5, 6], [8, 23]]
# a.sort(key=lambda x:x[1])
# print(a)
# ## sort function ki property hoti hai ki key = as a function leta hai. means key = function ka nam leta hai
# #---------------------------------self-------------------------------------
#


# Lambda or Anonymous Function
# def add(a, b, c):
#     return a+b+c
#
# print(add(5,4,3))
#
addition = lambda x, y, z : x + y + z
print(addition(5, 4, 3))