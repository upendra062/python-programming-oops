# #oops 4
#
# class Employee:
#     no_of_leaves=454
#
#
#     def __init__(self, aname, asalary, arole, aage):
#         self.name=aname
#         self.salary=asalary
#         self.role=arole
#         self.age=aage
#
#     def printdetails(self):
#         return f" Name is {self.name}. Salary is {self.salary}. Role is {self.role}. his age is {self.age}."
#
# sonu= Employee("sonu",3616,"singer","22")
# monu= Employee("monu",6464,"dancer","33")
#
#
#
# class Employee:
#     no_of_leaves=3
#
#     def __init__(self, ajadogar, awitch, ahipnotyger, aname, awork):
#         self.jadogar=ajadogar
#         self.witch=awitch
#         self.hipnotyger= ahipnotyger
#         self.name=aname
#         self.work=awork
#
#     def printdetails(self):
#         return f"Jadogar is {self.jadogar}. Witch is {self.witch}. Hipnotyger is {self.hipnotyger}. Name is {self.name}. Work is {self.work}"
#
# upendra = Employee("master",22,"alltypehipnotyger","upendra","programming")
# sunita = Employee("learner",33,"learningsfromupen","sunit","Teacher")
# mohan = Employee("dump",44,"no","mohan","lowerprogram")
# momramjanki = Employee("teacher",50,"never wants","ramjanki devi","house management")
# papabrijendra = Employee("teaching",55, "somemasti","brijendra singh", "master teacher")
#
#
# print(upendra.printdetails())
# print(sunita.printdetails())
# print(mohan.printdetails())
# print(momramjanki.printdetails())
# print(papabrijendra.printdetails())
# #
# print(upendra.__dict__)
# print(sunita.__dict__)
# print(mohan.__dict__)
# print(momramjanki.__dict__)
# print(papabrijendra.__dict__)
#
# print(Employee.__dict__)
# print(upendra.witch)


# list1 = [ ["Harry", 1], ["Larry", 2],
#           ["Carry", 6], ["Marie", 250]]
# dict1 = dict(list1)
# #
# # for item in dict1:
# #     print(item)
# for item, lollypop in dict1.items():
#     print(item, "and lolly is ", lollypop)


### To print the values integer float and string through for loop.
# items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]
#
# for item in items:
#     if str(item).isnumeric() and item>=6:
#         print(item)
# ,,,

#
# i = 0
#
# while(True):
#     if i+1<5:
#         i = i + 1
#         continue
#
#     print(i+1, end=" ")
#     if (i==44):
#
#         break # stop the loop
#     i=i+1
# # yaha par
#


# while(True):
#     num = int(input("Enter your favorite number\n"))
#     if num > 100:
#         print("you enter a correct number")
#     if (num > 150) and (num < 200):
#         print("Project pai dhhyan de bahut sahi ja rahia ho rocky the star")
#     elif num == 3000:
#         print("Your are the master of the universe you can do every thing rocky")
#     else:
#         print("Try again!\n")



### To multiply the 2 values times multipal time.
# while(True):
#     upn = int(input("Enter the god number: \n"))
#     upe = int(input("Enter the demon number: \n"))
#     print("multiplication of the both the number is:\n",upn*upe)
# #

## To extract the values of the ram and convert a list into a dictionary format.
# ram = [["Upendra", 100], ["Brijmohan", 1000], ["Sunita", 200], ["Brijendra", 5000],["Ramjanki", 30000], ["Divya", 1000]]
# #
# # print[ram]="Brijendra"
# # print(ram[2:4])
# dict1 = dict(ram)
# # # #
# # print(dict1)
# # print(ram)
# # print(dict1["Ramjanki"])
# # dict1["god"]="bhagwan"
# # print(dict1["god"])
# print(dict1["Upendra"])
# print(dict1["Brijmohan"])
# print(dict1["Sunita"])
# print(dict1["Ramjanki"])
# print(dict1["Brijendra"])
# print(dict1["Divya"])




### make a dictionary and access the values and change them and make dictionary into a dictionary.
# d2 = {'college': 'student','teacher':'master','Branch':{'CE':'center'},'library':'linda'}
# # print(d2["College"])
# print(d2["Branch"])
# d2["Branch"]["CE"]="CIVIL"
# d2["Library"]="Central"
# print(d2)
# #
# #
# for key, value in d2.items():
#     print(value, "and the sorro is", key)
#
#
#
#
# for key, value in dict1.items():
#     print(value, "and the happiness is", key)







#### program to run a multiple function of addition, subtraction, and multiplication.
# a = 3
# b = 2
# c = sum((a, b)) # built in function
#
# def function1(a, b):
#     print("Addition of a and b : ", a+b)
#     print("Multiplication of a and b : ", a*b)
#     print("Subtraction of a and b: ", a-b)
#     print("Dividation of the a and b: ", a/b)
#     print("Remainder of a and b:", a%b )
#     print("\n \n \n")
#
# function1(9,8)
# function1(9,5)
# function1(6,8)
# function1(9,7)
# function1(5,8)
# function1(9,9)
# function1(3,8)


#
a = 3
b = 2
c = sum((a, b)) # built in function



### Write a programm to take avaerage
# def upendrasystem1(a, b, c, d, e, f ):
#     """
#
#     :param a: i am the smarter bacha of the universe
#     :param b: i am the boss of the universe
#     :param c: i am gift of god god loves me very much
#     :param d: i worship god for healthy mind healthy body so that i can learn work hard and get the things right done.and earn lot of money earn respect in the society every body watch me like a motivational person or a idle person of her life.
#     :param e: My papa and mama loves me a lot
#     :param f: My brother don't loves me and if i will remains alone he will left me. He will never take care of me
#     :return:I have take care of my sister and my family and my loving ones. Be kind for working hard people
#     """
#     sum=(a+b+c+d+e+f)
#     # print(average)
#     return sum
#
# v= upendrasystem1(3, 2, 5, 6, 7, 8)
#
# print(v)
#
#
#
# def upendrasystem2(a, b):
#     average = (a+b)/2
#     print(average)
#     return average
#
# u=upendrasystem2(15, 6)
# print(u)
#
# print(upendrasystem1.__doc__)


# make a program to add repetedly the integer numbers/
# while(True):
#     upe = input("Enter upe numbr:\n:")
#     sun = input("Enter sun numbr:\n:")
#
#     try:
#         print("The sum of the number is :\n:", int(upe)+int(sun))
#     except Exception as e:
#         print(e)
#
#     print("This line is very important line to execute")


# #Operator overloading and Dunder method(those method which have trailing and heading of two underscore like __init__)
# #
# class Employee:
#     no_of_leaves=8
#     #self is the instance in which this function is applied if it i
#
#     def __init__(self, aname, asalary, arole):
#         self.name=aname
#         self.salary=asalary
#         self.role=arole
#     def printdetails(self):
#         return (f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}")
#
#     # Class method decorator used for changing the class variables
#     @classmethod
#     def change_no_of_leaves(cls, newleaves):
#         cls.no_of_leaves=newleaves
# #
# # #
# # # # __add__ is a dunder methd & it helps in operator overloading
# # # # # And for remaining see it in google Mapping operators to functions
#     def __add__(self, other):
#         return  self.salary + other.salary
# # # # #
#     def __truediv__(self, other):
#         return self.salary / other.salary
# #
#     def __sub__(self, other):
#         return self.salary - other.salary
# #
#     def __mul__(self, other):
#         return self.salary * other.salary
# # # # #
# # # # # #To represent your object in proper way we use __repr__ and __int__  dunder method
# # # # # #But __str__ has more priority than __repr__
# # # # #
#     def __repr__(self):
#         return (f"Employee ( '{self.name}')  {self.salary} ('{self.role}')")
#
#     def __str__(self):
#         return (f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}")
# #
# # #
# emp1=Employee("Nitesh", 250, "Teacher")
# emp2=Employee("Rohan", 125, "Cleaner")
# #
# #
# #
# #
# #
# print(emp1 + emp2)
# print(emp1 / emp2)
# print(emp1 - emp2)
# print(emp1 * emp2)
# #
# print(repr(emp1))
# print((emp1))
# print(emp2)
# print(emp1)
# #
# #
# print(emp1.salary+emp2.salary)
# print(emp1.printdetails())
# print(emp2.printdetails())


#
# i = 0
# while i<10:
#     print(i)
#     i = i + 1
#     if i==5:continue
#     print(i)

#
# i = 0
# while True:
#     i = i+1
#     if i%3==0:break
#     print(i, end="  ")

# floor division
# fibre, apook, paypal-vo youtube mai employee the , forcemoney,Upork
# How to bidding in AI project.


# 2, 5, 1
# 2, 2, 0
# 1, 1, 1  binary conversion of 5 is 101.



# nam nath ji soyabeen sabsai jada sail hoti hai.
# Upendra.hum_hai_to_kya_gam_hai() method is used to excess all element of upendra.
# class, object class variable and instance variable.templates.
# class Rocky:
#     no_of_juta=5
#
#     def __init__(self, apaisa, aroti , amakan , acar):
#         self.paisa = apaisa
#         self.car = acar
#         self.roti = aroti
#         self.makan = amakan
#
#     def hum_hai_to_kya_gum_hai(self):
#         return f"{self.paisa} to mal hai{self.roti}hai to shanti{self.makan} hai to masti hai{self.car}hai to party full on"
#
# Upendra = Rocky("Bahut hai", "bhook nhi hai", "ki jarrurt nhi hai", "car shok hai")
# anshul = Rocky("Paisa hai pr batayega nhi", " ghar pai rehta hai maje mai", " 5 6 hai", "car roj daily chalta hai")
#
#
# print(anshul.hum_hai_to_kya_gum_hai())
# print(Upendra.hum_hai_to_kya_gum_hai())



# Gui in python 1
# from tkinter import *
# Myroot = Tk()
# myLbl = Label(Myroot, text="Rocky", relief="groove", bd=300)
# myLbl.pack()
# Myroot.title("Tkinter Label in Python by Rocky Bhai")
# Myroot.mainloop()

### 2
# from tkinter import *
#
# Myroot = Tk()
# myvar = StringVar()
# myLbl = Label(Myroot, textvariable=myvar, relief="groove", font=("Courier", 14, "bold"), bd=1, fg="red", bg="#DDEEF0")
# myvar.set("Rocky Bhai\n Upendra singh\n brij singh \n mohan singh")
# myLbl.pack()
# Myroot.title("Tkinter Label in Python by Rocky Bhai")
# Myroot.mainloop()


### 3  how to print text from user and show it on screen.
# from tkinter import *
#
# MyRootDialog=Tk()
# #Set Tkinter Size And Location
# MyRootDialog.geometry("200x150+100+100")
#
# #Set Tkinter Title
# MyRootDialog.title("Get Input Value in Label")
#
# # Define Function for get Value
# def Get_MyInputValue():
#      getresult = MyEntryBox.get()
#      myTKlabel['text'] = getresult
#
# # Create Tkinter Entry Widget
# MyEntryBox = Entry(MyRootDialog, width=20)
# MyEntryBox.place(x=5, y=6)
#
# myTKlabel = Label(MyRootDialog, borderwidth=1, relief="ridge", height=3, width=25)
# myTKlabel.place(x=4, y=42)
#
# #command will call the defined function
# MyTkButton = Button(MyRootDialog, height=1, width=10, text="Get text", command= Get_MyInputValue)
# MyTkButton.place(x=4, y=112)
#
# mainloop()
#

### 4