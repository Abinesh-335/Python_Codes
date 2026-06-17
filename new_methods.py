class emp:
    comp="open ai"
    def insta(self):
        self.comp="new one"
        
    @classmethod
    def class_m(self,new):
        self.comp=new

    @staticmethod
    def statc(new): #just utility helper not depends on class or object run itself
        comp=new    #its only used with in this function 

print(emp.comp)

s= emp()
s.insta()
print(s.comp) # new one

emp.class_m("google")
print("After:",emp.comp)  #google

emp.statc("meta")       #google(it still not changed coz static works within itself)
print("After",emp.comp) #java static != python static


        
        
