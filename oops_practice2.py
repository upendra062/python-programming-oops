# class Hoja:
#     up_is_best = 44
#
#     def __int__(self, la, lb, lc):
#         self.a = la
#         self.b = lb
#         self.c = lc
#     def printprog(self):
#         return f"a is{self.a}. b is{self.b}. c is {self.c}."
#
# ram = Hoja(11,33, 1)
#
#
# print(ram.printprog())
# print(ram.up_is_best)


# class U():
#
#     def __init__(self, au, asalary, arole):
#         self.u = au
#         self.salary = asalary
#         self.role = arole
#
#     def r(self):
#         return (f"Name is {self.u}. Salary is {self.salary}. Role is {self.role}")
#
#
# nitesh = U("Upendra", 22 ,"model")
# rs = U(334, 242 ,411)
#
# print(nitesh.r())


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
#
# aa = Employee(11,22,33)
#
# print(aa.printdetails())

class Employee:


        def __init__(self, aname, asalary, arole, alanguage=0):
            self.name = aname
            self.salary = asalary
            self.role = arole
            self.language = alanguage

        def printprog(self):
            return (f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}. Language is {self.language}")


sorry = Employee("Shubam", 676, "Programmaer")


print(sorry.printprog())



class Colledge(Employee):
    teacher_of_colledge= 2

    def __init__(self, aname, asalary, arole):
        super.__init__()
        self.name = aname
        self.salary = asalary
        self.role = arole
    def teacher(self):
        return f"Teacher name is {self.name}. His salary is {self.salary}. Her role is {self.role}."


rocky = Colledge("Pk", 33000, "teaching")

print(rocky.teacher())