# #File IO Basics
#
# """
# "r" - Open File in Read Mode
# "w" - Open File in Write Mode
# "x" - Creates File if not exist
# "a" - Add more content of file/append
# "t" - Text mode
# "b" - Binary Mode
# "+" - Read and Write both
# """
#
#By default it (rt) mode read and text mode.
#Here open function returns a file pointer and
# in our case it gets stores in f
# f=open("bhadauria 12",'rt')
# content=f.read()   ### To read the file f.read() method is used.
# list_1=content.split()
# print(list_1)
# print(len(list_1))  # calculate number words not the letter.
# print(type(content))
# print(content)
# # #
# f.close()

# #r is default mode and t(text file) is default type
# f=open("piemr", "rt")
# f=open("bhadauria 12", "rt")
# content=f.read()
# print(content)
# # #
# f.close()
# #
# f=open("piemr1", "rt")
# f=open("bhadauria 12", "rt")
# content=f.read(3)
# print(content)
#
# content=f.read(3)
# print(content)
# #
# f.close()
#
#
# #
# # #If you want to read line line by line than you may itrerate the lines
# f=open("piemr1", "rt")
# content=f.read()
# # #
# for char in content:
#     print(char, end=" ")
# #
# f.close()
# #
# #
# # # f=open("piemr", "rt")
# # # # content=f.read()
# # #
# # # for line in content:
# # #     print(line, end="")
# # #
# # # f.close
# #
# #
# # #Read line function
# f=open("piemr1", "rt")
# f=open("bhadauria 12", "rt")
# for _ in range(2): #check your self 2 means for two times iteration.
#     print(f.readline())
# print(f.readline())
# # print(f.readline())
#
#
# # #
# # # # #readlines for print in form of list
# f=open("bhadauria 12", "rt")
# print(f.readlines())
# f.close()

#
# #Writing and Appending to file
# f=open("piemr1", "w")
# f.write("Python Scripting")
# f.close()
# #
# f=open("piemr", "w")
# # f.write("Hello World")
# (f.write("I hope you are Enjoying"))
#
# f.close()
# # #
# f=open("bhadauria 12", "a")
# ### f.write("\nI hope you are Enjoying and doing fun")
# f.write("\nHe is a supermine")
# f.close()

#
#
# # #Handle read and write both
# f=open("bhadauria 12","w")
# print(f.readline())
# f.write("Thank You")
# f.close()

# print(f.read())

#
# f=open("piemr1")
# #Access file by  with Block
# with open("piemr1") as f:#it replaces both functions like open and close
#     a=f.read()
#     print(a)
#
#
#

# p=int(input("Enter number to which you want to check prime or not"))
#
#
# def prime(a):
#     for number in range(2,a):
#         if a%number==0:
#             break
#     else :
#         return (f"Number {a} is prime number")
#
# print(prime(p))



## append to add the things write to add nhi hota complete change hoga
# with open is also known as context manager.
# for path we have to give the enviroment + \ + "rt".