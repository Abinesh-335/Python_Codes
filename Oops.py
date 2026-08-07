'''Self:
We use abi and guna instead of using self.“In Python, self refers to the current
instance of a class.It is used to access instance variables and methods inside the
class. When a method is called on an object,Python automatically passes that object
as the first argument to the method, which we conventionally name self.”

self is not a keyword, it’s just a naming convention. It helps differentiate
instance variables from local variables and ensures that each object maintains
its own state.”

Instance:
An instance is an object created from a class. It represents a specific realization
of that class with its own data.

A class is like a blueprint, and an instance is the actual object built from that
blueprint.Each instance can have its own values for the attributes defined in the
class.'''

'''
class Sample:
    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark

    def show(self):
        print(f"Name:{self.name}\nAge:{self.age}\nMark:{self.mark}")

    def result(self):
        if self.mark>=35:
            print("Result:Pass")
        else:
            print("Result:Fail")

s1=Sample('Vinoth',20,60)
s2=Sample('Sam',21,63)
s1.show()
s1.result()
s2.result()
s2.show()
'''





'''

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def is_square(self):
        return self.length==self.width

obj1=Rectangle(40,40)
print(obj1.area())
print(f"Is it Square:{obj1.is_square()}")

'''
'''
#Bank Account Details
class BankAccount:
    def __init__(self,acc_holder,avl_bal):
        self.acc_holder=acc_holder
        self.avl_bal=avl_bal

    def deposit(self,amt):
        if (amt>0):
            self.avl_bal+=amt
            return "Deposit Successful"
        else:
            return "invalid Amount"

    def withdraw(self,amt):
        if amt>0:
            if amt<self.avl_bal:
                check_min=self.avl_bal-amt
                if check_min>500:
                    self.avl_bal = check_min
                    return "Withdraw Successful"
                else:
                    return "Insufficient Minimum Balance"
            else:
                return "Insufficient amount"
        else:
            return "Invalid Amount"

    def avl_balance(self):
        return self.avl_bal

obj1=BankAccount("Aravinth",7000)
while True:
    print("1.Deposit\n2.Withdraw\n3.Available Balance\n4.Exit")
    try:
        opt=int(input("Enter the option:"))
        if opt==1:
            amt=int(input("Enter the Deposit Amount:"))
            print(obj1.deposit(amt))

        elif opt==2:
            amt = int(input("Enter the Withdraw amount:"))
            print(obj1.withdraw(amt))
        elif opt==3:
            print(obj1.avl_balance())
        elif opt==4:
            print("Thank You")
            break
        else:
            print("No Options")
    except ValueError:
        print("Enter the valid input")
'''


#“Abstraction is the process of hiding implementation details and showing only the essential features of an object.”
'''
#Abstraction
from abc import ABC,abstractmethod
class checking(ABC):
    @abstractmethod
    def enter(self):
        print("hello")

    @abstractmethod
    def exit(self):
        pass

    def thaks(self):
        print("see you")

class junior(checking):
    def exit(self):
        print("come again")
    def enter(self):
        print("welcome")

s=junior()
s.enter()
s.exit()
s.thaks()
'''
'''
#Access Specifier

class first:
    def __init__(self):
        self.p="public"
        self._pr='protected'
        self.__pv="private"

    def access_from_class(self):
        print("Inside the same class")
        print(self.p)
        print(self._pr)
        print(self.__pv)

class second(first):
    def access_from_class(self):
        print("From sub-class")
        print(self.p)
        print(self._pr)
        try:
            print(self.__p)

        except:
            print("Can't access")

class third:
    def access_from_class(self,obj):
        print("From other-class")
        print(obj.p)
        try:
            print(obj._pr)

        except:
            print("Can't access")
        
        try:
            print(obj.__p)

        except:
            print("Can't access")
f=first()
t=third()
t.access_from_class(f)
       

'''

'''We can access the private variable of one class from any other unrelated classes
as well by "Name mangling"
“Name mangling in Python is a mechanism where variables with double underscores (__)
are internally renamed to avoid name conflicts, especially in inheritance.”

class Test:
    def __init__(self):
        self.__x = 5

t = Test()

print(t.__x)        # ❌ Error
print(t._Test__x)   # ✅ 5

'''

'''
# Using access specifier in methods

class first:
    def public(self):
        print("Its from public")
    def _protect(self):
        print("Its from public")
    def __private(self):
        print("Its from public")
    def calling(self):
        print("From same class")
        self.public()
        self._protect()         #We can call the funtion within another function
        self.__private()
class second(first):
    def calling(self):
        print("From sub_class class")
        self.public()
        self._protect()
        try:
            self.__private()
        except:
            print("can't access")

class third:
    def calling(self,obj):
        print("From other_class class")
        obj.public()
        obj._protect()
        try:
            obj.__private()
        except:
            print("can't access")

f=first()
t=third()
t.calling(f)
'''
