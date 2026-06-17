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
class sample:
    def __init__(abi,name,reg):
        abi.n=name
        abi.r=reg

    def prints(guna):
        print(f"{guna.n} is {guna.r}")

s=sample('Abinesh',2021)
s.prints()

'''


'''
class diff():
    def sum(s,a,b):
        return a-b

s=diff()
print(s.sum(20,10))
'''

'''“Abstraction is the process of hiding implementation details and showing only
the essential features of an object.”
'''
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
