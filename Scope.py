#L -> E -> G -> B
'''
#L-Local variable

def a():
    a=10
    print(a)
print(a)# not possible

#E-Enclosing (nested function)

def car():
    dis=10

    def check():
        small=10
        print("the off amt:",dis)
    check()
❌✅car()✅


#G-Global
n=5
def car():
    dis=10+n
    print("the off1 amt:",dis,n)
def check():
    small=10+n
    print("the off2 amt:",small,n)
print("the offo amt:",n)
check()
car()

'''


#Bultin variable

print(__file__)
