#Difference Between Instance Variables and Class Variables
# & it also give the concept that class variables would not change
# by instance variables it only accessed by it
#
class Employee:
#Class Variables which is for both ie for harry and Rohan
    no_of_leaves=8
#     # pass
#
harry=Employee()
rohan=Employee()


#Below is the property of Harry and Rohan itself it does not occupied it from class and this are instance variable
harry.name="Harry"
harry.salary=455
harry.role="Instructor"
#
#
rohan.name="Rohan"
rohan.salary=777
rohan.role="Student"
harry.no_of_leaves=23

print(harry.no_of_leaves)
print(rohan.no_of_leaves)


#If we change rohan number of leaves it would not change the employee number of list

# rohan.no_of_leaves=9
# print(rohan.no_of_leaves)
# # #
# print(harry.no_of_leaves)
# # #
# #
# print(Employee.no_of_leaves)
# # #
# #If i use dict attribute for rohan then it gives it returns ditionary which shows what instance variables have this object
# print(rohan.__dict__)# to show the rohan's total variables in form of dictionary.
# print(Employee.__dict__)# to show the Employees total variables in form of dictionary.
# #
# # #but for emplyee it would remains same as it is in class variablesS returns ditionary which shows what  variables are for class
# # prin

# if same variable is available in both class and instance then it will first execute instance variable
#Class Method and concept of init

# class Employee:
#     no_of_leaves=8
    #self is the instance in which this function is applied if it is
    # def printdetails(self):

    # def printdetails(self):
    #     return (f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}")
#
# monu=Employee()
# sonu=Employee()
#
# monu.name="monu"
# monu.salary=455
# monu.role="Instructor"
#
#
# sonu.name="sonu"
# sonu.salary=777
# sonu.role="Student"
#
# print(monu.printdetails())
# print(sonu.printdetails())



