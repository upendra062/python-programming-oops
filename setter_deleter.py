#Setter and Deleter

class Employee:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
        self.email=f"{self.fname}.{self.lname}@gmail.com"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            print ("Email is not set Yet.....")
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        print("Setting now..........")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname = names.split(".")[1]
    #
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

ibm_ice=Employee("ibm", "ice")
#
# ibm_ice.fname="IBM"
# #
ibm_ice.email="aptech.ice@gmail.com"
#
print(ibm_ice.email)
#
del ibm_ice.email
print(ibm_ice.email)

