#Overriding Concept

class A:
    classvar1= "I am a class variable in class A"
    def __init__(self):
        self.var1="I am inside class A's constructor"
        self.classvar1="I am instance var of class A"
        self.special="Special"


class B(A):
    classvar1 = "I am class variable of B"
    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class b"
        # super().__init__() # agar super method instance variable k upper lagego to usi class ka constructor run hoga agar instance variable (e.x=means self.var1) k nichai super method hai to parent class ka constructor run hoga
        # print(super().classvar1)


a=A()
b=B()

print(b.classvar1)
print (b.special,b.var1,b.classvar1)
print(b.special)


