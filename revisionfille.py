'''
inpnum,\t,\n,it will not show the type of int+str
data types,type casting
pop delete items
union ,add to add in set
literals in exception
read, readline, readlines
random.randint(1,9)
random.random() # generate values b/n 0 to 1
random.choice(name of the list from which you want random values)
instance variable and class variable
function, class, object, instance, variable
constructor, __init__, __dict__,decorator,alternate constructor,
single,multiple,multi-level inhertance,polymorphism,overriding concept
public protected private
Diamond Shape problem
overloading and dundermethod
abstract method
os
searching, setter_detter, regexpression
try,except,else,finally
'''

class Employee():
    def __int__(self, fname,lname):
        self.fname= fname
        self.lname=lname

    def kamal(self):
        return f"my name is{self.fname},hi {self.lname}@rocky.com"

    @property
    def change(self):
        return f"my name is{self.fname},hi {self.lname}@rocky.com"

