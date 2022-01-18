# list=[]
# for i in range(100):
#     if i % 3 == 0:
#         list.append(i)
#
# print(list)
# #
# # #Above code will be done by list comprehension
# #
# list=[i for i in range(100) if i % 3 == 0 ]
# print(list)
# # #
# # #Dictionary Comprehension
# dict1={i:f"Item {i}" for i in range(5)}
# dict2={a:b for b,a in dict1.items()}
# dict3={'A':1, 'B':2, 'A':3}
# print(dict3['A'])
# print(dict1)
# print(dict2)

# # #
# # #
# # #set Comprehension
# dresses={dress for dress in ["dress1", "dress2", "dress3", "dress2"]}
# print (dresses)
# #
# #
# #
# # # #Generators Comprehensions
# evens=(i for i in range(100) if i % 5 ==0)
# print(evens)
# for i in range(5):
#     print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())

# insequencial data types ... ismai entry indexing k hisab sai print karega.
