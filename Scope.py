#L -> E -> G ->B


# #L-Local variable
"""
def a():
    a=10
    print(a)
print(a)# not possible

from statistics import quantiles

#E-Enclosing (nested function)

def car():
    dis=10

    def check():
        small=10
        print("the off amt:",dis)
    check()
car()


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




#Bultin variable

print(__file__)
"""


delivery_partner="Zomato"
def hotel():
    food="Pizza"
    def order():
        quantity=2
        print(f"{quantity} {food} is delivered by {delivery_partner} ")
    #print(f'the quantity is {quantity}')❌
    order()
hotel()

# print(delivery_partner)✅
# print(food)❌


