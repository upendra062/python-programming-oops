## ----------------self-----------------
### by normal function
# numbers = ["3", "34", "64"]
# i = 0
# for i in range(len(numbers)): # here len is used to  convert string to an integer
#     numbers[i] = int(numbers[i])
# numbers[2] = numbers[2] + 1
# print(numbers[2])

### by map function
# numbers = ["3", "34", "64"]
# print(map(int, numbers)) # To check map location at this memory location.
# numbers =list(map(int, numbers)) #first write map fir vo function likho jo tum chahatai ho subhi pai apply ho jaye i.e=int. then write name of the list. which is numbers
# # firstly number ko maine list mai type cast kiya. map nam k function nai int name k function ko subhi numbers pai chala diya. aur one by one subhi string ko isnai integer mai convert kr diya
# numbers[2] = numbers[2] + 1
# print(numbers[2])

### other by map function.
# def sq(a):
#     return a*a
# num = [2,3,4,5,6]
# square = list(map(sq, num))
# print(square)

####  by map and lambda function.
# num = [2,3,4,5,6]
# square = list(map(lambda x:x*x, num))
# print(square)

#### find cube, square, multiply by map,lambda function
# def sum(a):
#     return "sum of the number is", a+a
# def value(a):
#     return "the number is", a
# def plusfive(a):
#     return "plus five", a+5
# def minusone(a):
#     return "minusone", a-1
# def dividetwo(a):
#     return "divideby2", a/2
# def square(a):
#     return "square", a*a
# def cube(a):
#     return "cube", a*a*a

# func = [value, square, cube, sum, plusfive, minusone, dividetwo]
# num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13 ,14 ,15]
# for i in num:
# for i in range(0, 101):
#     val = list(map(lambda x:x(i), func))
#     print(val)

######--- filter method---
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# def is_greater_5(num):
#     return num>5
#
# gr_than_5 = list(filter(is_greater_5, list_1))# filter ke ander first function phir ata hai iterable(list)
# # first type cast in list. Then we use filter method. In filter first we place the function and after comma we place iterable(list,dictionary,etc).
# print(gr_than_5)
# #
#####filter you can explore your self.
#####----reduce method---

##by normal method.
# list1 = [1, 2, 3, 4]
# num = 0
# for i in list1:
#     num = num + i
# print(num)
## by reduce method.
# from functools import reduce
# list1 = [1, 2, 3, 4]
# num = reduce(lambda x,y:x+y, list1)
# num = reduce(lambda x,y:x*y, list1)
# num = reduce(lambda x,y:x-y, list1)
# num = reduce(lambda x,y:x/y, list1)
# print(num)
####


## ----------------self---------------




#Map Function: Apply Any Function to a List
#
# lis=["3","34","64"]
# lis=list(map(int, lis)) # map nai lis k sare element mai int ko chala diya aur yai function for loop ki jagh use ho jayega
# #
# for i in range(len(lis)):
#     lis[i]=int(lis[i])

# lis[2] = lis[2] + 1
# print(lis[2])


# num=[1,2,3,4,5,6]
# lst=[]
# def sq(a):
#     for item in a:
#         # b=0
#         b=item*item
#         lst.append(b)
# # #
# sq(num)
# print(lst)
#     return a * a

    # print(sq(num))

# num=list(map(sq, num))
# print(num)

# num=[1,2,3,4,5,6]
# print(num)
# num=list(map(lambda x : x * x, num))
# print(num)

# def sqr(a):
#         return a * a
# def cube(a):
#         return a*a*a
#
# func=[cube, sqr]
#
# for i in range(5):
#     val =(list(map(lambda x:x(i), func)))
#     print(val)


#Filter Function

# list_1=[1,2,3,4,5,6,7,8,9]
# print(list_1)

# def is_greater_5(num):
#     lis = []
#     for item in num:
#         if item > 5:
#             lis.append(item)
#             # print(lis)
#     return (lis)
#
#
# print(is_greater_5(list_1))
# #
# gr_thn_5=list(filter(is_greater_5, list_1))
# gr_thn_5=list(filter(lambda x : x>5, list_1))
# print(gr_thn_5  )



# REDUCE
# from functools import reduce
# # #
# list1=[1,2,3,4,5]
# num=reduce(lambda x,y: x*y, list1)
# print(num)

# list=[1,2,3,4,5,6,7,8,9]
# def add_no(num):
#         lis = []
#         for item in range(num):
#                 if item > 10:
#                         lis.add(item)
#                         print(lis)
#                 return(lis)
#
# print(lis)