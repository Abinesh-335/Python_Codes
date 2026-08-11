"""
Self:
We use abi and guna instead of using self.“In Python, self refers to the current
instance of a class.It is used to access instance variables and methods inside the
class. When a method is called on an object,Python automatically passes that object
as the first argument to the method, which we conventionally name self.”

self is not a keyword, it’s just a naming convention. It helps differentiate
instance variables from local variables and ensures that each object maintains
its own state.

Instance:
An instance is an object created from a class. It represents a specific realization
of that class with its own data.

A class is like a blueprint, and an instance is the actual object built from that
blueprint.Each instance can have its own values for the attributes defined in the
class.
"""
from traceback import print_tb

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
#########################/ CLASS /###############################
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

################/ INHERITANCE /#######################
#Student Mark
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_details(self):
        print(f"Name:{self.name}\nAge:{self.age}")

class Student(Person):
    def __init__(self,name,age,mark):
        super().__init__(name,age)
        self.mark=mark
    def show_mark(self):
        print(f"Mark:{self.mark}")

s1=Student("Arun",24,70)
s1.show_details()
s1.show_mark()
'''

################/ INHERITANCE(Method Overriding /#######################
'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_role(self):
        print("I'm the person")

class Student(Person):
    def __init__(self,name,age):
        super().__init__(name,age)

    def show_role(self):
        print("I'm the Student")

p1=Person("Vino",22)
s1=Student("Arun",24)
s1.show_role()
p1.show_role()
'''

###Example 2###
'''

class Animal:
    def sound(self):
        print("Animal makes Sound")
class Dog(Animal):
    def sound(self):
        print("Dog Barks")
class Cat(Animal):
    def sound(self):
        print("Cat meow")

animals=[Animal(),Dog(),Cat()]
for animal in animals:
    # print(animal)
    # < __main__.Animal object at 0x000002098D7AF990 >
    # < __main__.Dog object at 0x000002098D7BC3D0 >
    # < __main__.Cat object at 0x000002098D7BC410 >
    animal.sound()
print(f"Testing:{Animal().sound()}") #Testing:None
'''
#############/ Student Management /##############

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        #self.id=id
        self.__marks=[]

    def show_mark(self):
        print(f"Marks:{self.__marks}")

    def add_mark(self,mark):
        if 0<=mark<=100:
            self.__marks.append(mark)
            return "Mark Added Successfully"
        else:
            return "Invalid Mark"

    def average_mark(self):
        if len(self.__marks)>0:
            total=0
            for m in self.__marks:
                total=total+m
            avg=total/len(self.__marks)
            return avg
        else:
            return "No mark"

    def get_result(self):
        avg=self.average_mark()
        if avg=="No mark":
            return "No Marks"
        elif avg>=50:
            return "Pass"
        else:
            return "Fail"

    def show_details(self):
        super().show_details()
        print(f"Marks: {self.__marks}")
        print(f"Average: {self.average_mark()}")
        print(f"Result: {self.get_result()}")


def add_student(students):
    name=input("Enter the name:")
    age=int(input("Enter the age:"))
    student=Student(name,age)
    students.append(student)
    print("Student added Successfully")

def view_student(students):
    if len(students)<0:
        return "No records"

    for student in students:
        student.show_details()

def search_student(students,name):
    for student in students:
        if student.name==name:
            return student.show_details()
    return "Not Found"

def delete_student(students,name):
    for student in students:
        if student.name==name:
            students.remove(student)
            print("Successfully Deleted")
    return "Not Found"

def add_mark_to_student(students, name, mark):
    for student in students:
        if student.name == name:
            return student.add_mark(mark)


    return "Student not found"

students=[]
# add_student(students)
# add_student(students)
# view_student(students)
# res=search_student(students,"vinoth")
# if res:
#     res.show_details()
# else:
#     print("Student not found")
# delete_student(students,"vino")
# print("After deleting:\n\n")
# view_student(students)
# print("The result\n")
# print(add_mark_to_student(students,"vino",70))
# print(add_mark_to_student(students,"viky",120))
# print(add_mark_to_student(students,"somu",70))
# print(add_mark_to_student(students,"vino",55))
# view_student(students)


while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Add Mark")
    print("5. Delete Student")
    print("6. Exit")

    try:
        choice = int(input("Enter option: "))

        if choice == 1:
            add_student(students)

        elif choice == 2:
            view_student(students)

        elif choice == 3:
            name=input("Enter the name:")
            print(search_student(students,name))

        elif choice == 4:
            name = input("Enter the name:")
            mark = int(input("Enter the Mark:"))
            print(add_mark_to_student(students,name,mark))

        elif choice == 5:
            name = input("Enter the name:")
            delete_student(students,name)

        elif choice == 6:
            print("Thank you")
            break

        else:
            print("Invalid option")

    except ValueError:
        print("Enter a valid number")









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

    def thanks(self):
        print("see you")

class junior(checking):
    def exit(self):
        print("come again")
    def enter(self):
        print("welcome")

s=junior()
s.enter()
s.exit()
s.thanks()
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
        self._protect()         #We can call the function within another function
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
