#variables - Container
var1="Hello World"
var2=4
var3=25.7
var4="How are you"
#
# print(type(var1))
# var5=5*var1
# print(var5)

# a=int(input("Enter the value of a: "))
# b=int(input())
# print(f"value of {a} and {b} is a + b")
# print(a+b)

# a=int(input("Enter value of a: "))
# b=int(input("Enter value of b: "))
# print(a+b)
# a=5
# print("a")
# print(a)
#
# print(var1)
# #
#
# print(type(var2))
# print(type(var1))
# print(type(var2))
# print(type(var3))
# # # #
# print(type(var2+var3), var2+var3)
# print(var1+var4)
# #
# #
# #
# var5="6"
# var6="8"
# var7="python"
# print(type(var5))
# print(var5 + var6)
# print(int(var5) + int(var6))
# print(int(var7))  # only integer valuees ko hi print karega jo string mai hai

# # #
#
# print(5*6)
# print(10*var1)
# print(10.5*var2)

# a=input("Enter value of a: ")
# b=input("Enter value of b: ")
# print(a+b)
# print(type(a))
# a=int(input("Enter the value of a: "))
# b=int(input("Enter the value of b: "))
# c=a+b
# print(f"Sum of {a} & {b} is {c}")
# #
# #
# print("Enter a number")
# inpnum=input()#Here inpnum is String and not the string
# print(type(inpnum))
#
# # print("You entered", inpnum + "10")
#

# a="Hello"
# print(a)
# print("a")
# print("a" * 5)
# print(a * 5)
# print(5 * 2)
# # #Task make a sum of two numbers where input is
# # provided by the user
#
# a="five"
# print(int(a))

"""
(Type Conversion)
-------------------
The process of converting the value of one data type (interger, string, float, etc.) to another data type is called type conversion. Python has two types of type conversion.
1. Implicit Type Conversion
2. Explicit Type Conversion
Implicit Type Conversion
------------------------
in implicit type conversion, Python automatically converts one data type to another data type. This process doesn't need any user involvement.
Lets see an example where Python promotes the conversion of the lower data type (integer) to the higher data type(float) to avoid data loss.
it will not add interger and string like 122+ "131" output comes an error in this situation we use explicit Type conversion.
Explicit Type Conversion
-------------------------
In Explicit Type Conversion, users convert the data type of an object to required data type. We use the predefined functions like int(), float(), str(), etc to perform explicit type conversion.
This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.
Syntax :

<required_datatype>(expression)
Typecasting can be done by assigning the required data type function to the expression.


Example 3: Addition of string and integer using explicit conversion
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))
"""


# num_int = 123
# num_str = "456"
#
# num_str = int(num_str)
#
# num_sum = num_int + num_str
#
# print("Sum of num_int and num_str:", num_sum)
# print("Data type of the sum:",type(num_sum))

num_int = 123
num_str = "456"

print("Sum of num_int + num_str")

