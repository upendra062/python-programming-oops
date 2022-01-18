# f=open("piemr1","rt")
f=open("bhadauria 12","rt")

print(f.tell()) #It tells where is the position of file pointer in our case f
print(f.readline()) # to read the first line
print(f.tell())
print(f.readline())
print(f.tell())
#
# #
# # #Seek moves your file pointer to the position
# #
f.seek(0) # to set the file handle position. example f.seek(0) means position will be zero.
# print(f.tell())
print(f.readline())
#

