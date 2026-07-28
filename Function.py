'''
def hello(name):
    print("Welcome",name)
hello("vinoth")              # Welcome vinoth


def add(a,b):
    return a+b
result=add(5,5)
print(result)               #10

# *args

def add(*sums):
    tot=0
    for num in sums:
        tot+=num
    return tot
print(add(1,2,4,32,2))          #41


# **Kargs

def create_profile(**kargs):
    print(kargs.items())                #dict_items([('name', 'Abinesh'), ('age', 23), ('gender', 'male')])
    for key,val in kargs.items():
        print(f"{key}:{val}")           #name:Abinesh age:23 gender:male

create_profile(name="Abinesh",age=23,gender='male')


def show(n):
    if n==0:
        return
    else:
        print("*******************\nWelcome to Python\n*******************")
        return show(n-1)
show(3)



def welcome(obj="to python"):
    if obj:
        print(f"Welcome {obj}")
welcome()
welcome("vinoth")
welcome("sam")

def is_even(n):
    return n%2==0

print(is_even(6)) #True
print(is_even(9)) #False



def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
while True:
    a = int(input("Enter the value1:"))
    b = int(input("Enter the value2:"))
    print("1. Add\n2. Subtract]\n3. Multiply\n4. Divide\n5. Exit")
    opt=int(input("Enter the Option:"))
    if opt==1:
        res=add(a,b)
    elif opt==2:
        res=sub(a,b)
    elif opt==3:
        res=mul(a,b)
    elif opt==4:
        res=div(a,b)
    elif opt==5:
        print("Thank you")
        break
    else:
        print("Enter a valid option")
        break
    print(f"Result:{res}")

#Student Mark Manager

def add_mark(marks,mark):
    marks.append(mark)
    print("Add successfully")

def view_mark(marks):
    if len(marks)<1:
        print("No data")
    else:
        print(marks)

def highest_mark(marks):
    if len(marks)>0:
        hg=marks[0]
        for i in range(len(marks)):
            if hg<marks[i]:
                hg=marks[i]
        print("Highest Mark:",hg)
    else:
        print("marks is empty")


def avg_mark(marks):
    if len(marks)>0:
        tot=0
        for i in range(len(marks)):
            tot=tot+marks[i]
        print("The Average mark is:",tot/len(marks))
    else:
        print("marks is empty")

marks=[]
while True:
    print("1.ADD\n2.view\n3.Highest Mark\n4.Average Mark\n5.Exit")
    opt = int(input("Choose the Option"))
    if opt == 1:
        data = int(input("Enter the mark:"))
        add_mark(marks,data)
    elif opt == 2:
        view_mark(marks)
    elif opt==3:
        highest_mark(marks)
    elif opt==4:
        avg_mark(marks)
    elif opt==5:
        print("Thank you")
        break
    else:
        print("Enter the Valid option")

'''
from django.contrib.admin.actions import delete_selected


#Student Record Manager.

def add_std(students,name,mark):
    students.update({name:mark})
    print("Add successfully")

def view_std(students):
    if len(students)<1:
        print("No data")
    else:
        print(students)

def highest_mark(students):
    if len(students)>0:
        val=list(students.values())
        hg=val[0]
        for i in range(len(students)):
            if hg<val[i]:
                hg=val[i]
        print("Highest Mark:",hg)
    else:
        print("marks is empty")


def search_student(students,name):
    if name not in students.keys():
        return "Data is not available"
    else:
        return students.get(name)

def del_student(students,name):
    if name in students.keys():
        students.pop(name)
    else:
        print("No data in that name")
students={}
while True:
    print("1.ADD\n2.view\n3.Highest Mark\n4.search student\n5.Delete student\n6.Exit")
    opt = int(input("Choose the Option"))
    if opt == 1:
        name=input("Enter the name:")
        mark = int(input("Enter the mark:"))
        add_std(students,name,mark)
    elif opt == 2:
        view_std(students)
    elif opt==3:
        highest_mark(students)
    elif opt==4:
        name=input("Enter the name:")
        print("The mark is:",search_student(students,name))
    elif opt == 5:
        name = input("Enter the name:")
        del_student(students,name)
    elif opt==6:
        print("Thank you")
        break
    else:
        print("Enter the Valid option")
