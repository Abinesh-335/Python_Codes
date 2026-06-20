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


