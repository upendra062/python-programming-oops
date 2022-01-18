### ------------self-------------
# def function_name(a, b, c, d, e):
#     print(a, b, c, d, e)
#
# function_name("Rocky", "mohan", "sita", "gita", "reshma")



# def funargs(normal, *args, **kwargs): # sequence is important ex- normal,*args,**kwargs other wise it will show you error
#     print(normal) # uper normal hai to nichai print(normal) karna jarrori hai
#     for item in args:
#         print(item)
#     print("\nNow I would Like to introduce some of our heroes:")
#     for key, value in kwargs.items():
#         print(f"{key} is a {value}")
#
# rocky = ["Rocky", "mohan", "sita", "gita", "reshma"]
# normal = "I am a normal Argument and the student are:"
# kw = {"Mohan": "Monitor", "Rocky":"programer", "Instructor":"Cordinator"}
#
# funargs(normal, *rocky, **kw)


### ------------self-------------

# def func1(a,b,c,d):
#     print(a,b,c,d)

# func1(2, 3, 4, 5)
# # # If i has one more value than it is not going to
# # accept as it exceeds the length of variables
# func1(1,2,3,4,5)
#
# # # To handle this we use *args & **kwargs and type of args is
# # always tuple
# # #
# def funargs( *args):
#      print(type(args))
#      for item in args:
#          print(item, end=" ")
#
# a=[1,2,3,4,5,6,7,8]
# # # #
# funargs(*a)
# # # # #
# def funargs(  *args,  **kargs):
#     # print(normal)
#     print(type(args)) # Its type is tuple
#     for item in args:
#         print(item, end=" ")
#         # print()
#     for key, value in kargs.items():
#         # print(type(kargs))
#         print(f"\n {key} is  {value}")
# #
# normal="Python scripting is fun"
# arg = [1, 2, 3, 4, 5, 6, 7]
# karg={"Clg":"Piemr", "Subject":"Python", "Workshop": "IOT"}
# # # #
# funargs( normal, *arg,  **karg)
# # # #
# #
