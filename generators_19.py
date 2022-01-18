
# """
# Iterable- __iter__ or __getitem__  this method provides Iterator to that object in which it runs
# Iterator - __next__
# Iteration- Process of Iterate is  known as Iteration
#
# Generator- Are the Iterators which get traverse only once
# """
#
# #
# # for i in range(100000000):
# #     print(i)
# # print("Hello")
# # def gen(n):
# #     for i in range (n):
# #         yield i # Yield is a generator ie it generates values on the fly so that we save our ram
# # # #
# # g=gen(3)
# # # print(g)
# # # # for i in range(4):
# # print(g.__next__())
# # print(g.__next__())
# # print(g.__next__())
# # # print(g.__next__())
#
#
# name="Nitesh"
# ier=iter(name)
# print(ier)
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
#
#
#
#
#
# # # factorial using generator
# # def factorial_using_generator(n):
# #  mul = 1
# #  for i in range(1, n+1):
# #   mul = mul * i
# #   yield mul
# #
# # x = factorial_using_generator(5)
# # print(x.__next__())
# # print(x.__next__())
# # print(x.__next__())
# def foo(x):
#     x = ['def', 'abc']
#     return id(x)
# q = ['abc', 'def']
# print(id(q) == foo(q))
# =d['freq']+1
# fo = open("temp.txt", "rw+")
# print("FileName: ", fo.name)

# Assuming file has following 3 lines
# First line
# Second line
# Third line

# for index in range(3):
#     line = fo.next()
#     print("iterator %d - %s" % (index, line))
#
# # Close opend file
# fo.close()

