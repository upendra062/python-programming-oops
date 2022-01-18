# # #Code for ClassMethod decorator if i does want to
# # # use self for purpose of latency or if
# # # I want to change the value of class variable for object
# # # instance Class method is able to access class variables
# # #It can be also used as alternative constructor in next program
# #
#
# class Employee:
#     # no_of_leaves=8
#     upendra_of_r=55
#     #self is the instance in which this function is applied if it i
#     def printdetails(self):
#         return (f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}")
#
# #
#     @classmethod
#     def change_no_of_leaves(cls, newleaves):
#     # def change_no_of_leaves(cls, newleaves):
#         cls.no_of_leaves=newleaves
#
#
#
# harry=Employee()
# rohan=Employee()
#
# harry.name="Harry"
# harry.salary=455
# harry.role="Instructor"
#
#
# rohan.name="Rohan"
# rohan.salary=777
# rohan.role="Student"
# #
# # #It can be accesable by object also
# harry.change_no_of_leaves(34)
# print(harry.no_of_leaves)
# # #
# # # #It can be accesable by class also
# Employee.change_no_of_leaves(34)
# print(Employee.no_of_leaves)
# #
# # #It also change for rohan as class method change the class variables
# # print(rohan.no_of_leaves)
# #
# # #
# print(harry.printdetails())
# print(rohan.printdetails())



class Ansul():
    boss_Rocky = 1001001

    def __init__(self, your_loan_amount, your_loan_date, your_charges):
        self.loan_amount = your_loan_amount
        self.loan_date = your_loan_date
        self.charges = your_charges

    def raghav(self):
        return (f"Your loan{self.loan_amount} date is{self.loan_date} charges are {self.charges}")


    @classmethod
    def pyush_remover(cls, master_rocky):
            cls.boss_Rocky = master_rocky

    @classmethod
    def change_by_underscore(cls, str):
        x=str.split("-")
        return cls(x[0],x[1],x[2])
        # return cls(*str.split("-") )

    @staticmethod
    def Yai_string_add_karega(Upe):
        return ("I am the boss" + Upe)

    @staticmethod
    def Plus(ilu):
        return ("checking of additional"+ilu+ilu*10,("_ka_matlab_iloveyou"))

kirti = Ansul(45618164, '26-jan-2021', '24%')
mistri = Ansul(2584616, '27-jan-2021', '29%')
Nagarzun = Ansul(2222222222, '26-jan-2021', '24%')


class Master_Rocky():
    Power_of_master_rocky="Unlimited"

    def __init__(self, your_loan_amount, your_loan_date, your_charges):
        self.loan_amount = your_loan_amount
        self.loan_date = your_loan_date
        self.charges = your_charges

    def Rco_son(self):
        return (f"it is your final amount{self.loan_amount} paying date {self.loan_date} final charges{self.charges} ")

hero = Master_Rocky(888845618164, '1-jan-2021', '91%')
villan = Master_Rocky(77745618164, '2-jan-2021', '80%')
producer = Master_Rocky(666645618164, '3-jan-2021', '55%')
director = Master_Rocky(3333345618164, '4-jan-2021', '45%')
underscoreer = Master_Rocky(3333345618164,'4-jan-2021',"45%")


print(villan.Rco_son())
