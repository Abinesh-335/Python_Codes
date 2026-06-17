'''
# *args

def add(*sums):
    tot=0
    for num in sums:
        tot+=num
    return tot
print(add(1,2,4,32,2))


# **Kargs

def create_profile(**kargs):
    for key,val in kargs.items():
        print(f"{key}:{val}")

create_profile(name="Abinesh",age=23,gender='male')
'''

