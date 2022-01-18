##### Write a Python program to check if all dictionaries in a list are empty or not.

# my = [{},{},{}]
# my1 = [{123, 2345},{},{}]
# print(all(not d for d in my))
# print(all(not d for d in my1))

# o/p...True
#       False

### Write a python program to remove duplicates from a list of lists.

# import itertools
# num = [[110,120],[240],[330,456,425],[310,220],[133], [240]]
# print("Original list", num)
# num.sort()
# new_num = list(num for num,_ in itertools.groupby(num))
# print("New list", new_num)


### write a python program to extend a list without append.

# x = [103, 320, 430]
# y = [403, 503, 603]
#
# x[:0] = y
# print(x)

### Write a python program to find the list in a list of lists whose sum of elements is the highest

# num = [[1,2,3],[4,5,6],[10,11,12],[7,8,9]]
# print(max(num, key=sum))

### Write a Python program to access dictionary key's element by index.
# num = {'stats': 80, 'math': 90, 'algorithm': 86}
# print(list(num)[2])

###Creating Class and Object in Python
# class Parrot:
#
#     # class attribute
#     species = "bird"
#
#     # instance attribute
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# # instantiate the Parrot class
# blu = Parrot("Blu", 10)
# woo = Parrot("Woo", 15)
#
# # access the class attributes
# print("Blu is a {}".format(blu.__class__.species))
# print("Woo is also a {}".format(woo.__class__.species))
#
# # access the instance attributes
# print("{} is {} years old".format( blu.name, blu.age))
# print("{} is {} years old".format( woo.name, woo.age))
#
# # o/p
# # Blu is a bird
# # Woo is also a bird
# # Blu is 10 years old
# # Woo is 15 years old


####Creating Methods in Python
class Parrot:

    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)


# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())

# Output
# Blu sings 'Happy'
# Blu is now dancing