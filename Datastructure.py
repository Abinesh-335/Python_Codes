'''
#List

lis=["abi","arul","gotham","sam"]

lis.append("vinoth")
print("Append-->",lis)              #Append--> ['abi', 'arul', 'gotham', 'sam', 'vinoth']

lis.insert(2,"arul")
print("Insert-->",lis)              #Insert--> ['abi', 'arul', 'arul', 'gotham', 'sam', 'vinoth']

lis.remove("vinoth")
print('Remove-->',lis)              #Remove--> ['abi', 'arul', 'arul', 'gotham', 'sam']


lis.reverse()
print("Reverse-->",lis)             #Reverse--> ['sam', 'gotham', 'arul', 'arul', 'abi']

lis.pop()
print("Pop-->",lis)                 #Pop--> ['sam', 'gotham', 'arul', 'arul']

print("count",lis.count("arul"))    #count 2

#list slicing

print(lis[:2])                      #['sam', 'gotham']
print(lis[-2:])                     #['arul', 'arul']

#List iteration

for i in lis:
    print("--",i)

#check if
if 'sam' in lis:
    print ("yes")                   # yes


#update list(change)

lis[3]="samuvel"
print("changed-->",lis)             #changed--> ['sam', 'gotham', 'arul', 'samuvel'] (mutable)


for index,values in enumerate(lis):
    print(f"{index}:{values}")
# 0:sam
# 1:gotham
# 2:arul
# 3:samuvel


length=len(lis)
print(f"Length={length}")           # Length=4
'''
#------------------------------------------------------------------------------------
'''
#Tuple


tup=(1,2,4,3,2)
print(tup)              #(1, 2, 4, 3, 2)

print(tup[2])

# tup[2]=8            ❌ Not changed (immutable)

print(tup[2])

print("count-->",tup.count(3))  # count--> 1
print("Index-->",tup.index(2))  # Index--> 1


for index,k in enumerate(tup):
    print(f"{index}:{k}")


'''
#--------------------------------------------

'''
#Set

sets={"abi","arul","gotham","sam"}
  #(or)
lis=["abi","arul","gotham","sam"]
change_dt=set(lis)
print(change_dt)            #{'sam', 'abi', 'gotham', 'arul'}

for i,k in enumerate(sets):
    print(f"{i}:{k}")

city1={"Kum","chennai","bangalore"}
city2={"chennai","vellore","madurai"}

print("Union-->",city1.union(city2))                #Union--> {'chennai', 'vellore', 'bangalore', 'Kum', 'madurai'}
print("Instesection-->",city1.intersection(city2))  #Instesection--> {'chennai'}
print("difference-->",city1.difference(city2))      #difference--> {'bangalore', 'Kum'}


city1.add("thanjavur")
print(city1)                            # {'bangalore', 'Kum', 'thanjavur', 'chennai'}


city1.remove("chennai")
print(city1)                            #{'bangalore', 'Kum', 'thanjavur'}


#safe remove
city1.discard("trichy") # ✅Safe remove Even no value in tuple its not show any Error

#normal remove
#city1.remove("trichy")  # ❌Show Error
'''
#--------------------------------------------
'''

#Dictionary

dic={"loc":"airport",
     "ids":"ux123",
     "pickup":"station",
     "drop":"home",
     "driver":"ravi"}
print(dic["ids"])

print(dic.get('airport')) #safe use of search if not in dic return none

print(dic.keys())

print(dic.values())
      
#Iteration

for k,v in dic.items():
    print(f"{k}:{v}")

#absend
dic.update({"time":"morning"}) #its adds the time
print(dic)

dic.update({'time':'evening'}) #its modify the time
print(dic)

dic.pop("driver")
print(dic)

'''
#multiple values for key
'''
dic1={"loc":"airport",
     "ids":"ux123",
     "pickup":"station",
     "drop":['home','office','park'],
     "driver":"ravi"}

print(dic1['drop'])

print(dic1['drop'][2])

for loc in dic1['drop']:
    print(loc)


trips={
   "ux001": {"loc":"airport",
     "ids":"ux001",
     "pickup":"home",
     "drop":['home','office','park'],
     "driver":"ravi"},
    
    "ux002":{"loc":"airport",
     "ids":"ux002",
     "pickup":"station",
     "drop":['home','office','central'],
     "driver":"ravi"},
    
    "ux003":{"loc":"airport",
     "ids":"ux003",
     "pickup":"court",
     "drop":['home','office','park'],
     "driver":"ravimohan"}
    }
#if we give within list
#print(trips[1]['drop'])

print(trips["ux003"]['driver'])

for i,d in trips.items():
    print(i)
    print(f"location:{d['pickup']}-->{d['drop'][2]}")
'''


# Student using list
details=[]
while True:
    print("1.ADD\n2.view\n3.Highest Mark\n4.Lowest Mark\n5.Exit")
    opt=int(input("Choose the Option"))
    if opt==1:
        data=int(input("Enter the mark:"))
        details.append(data)
    elif opt==2:
        print(details)
    elif opt==3:
        if len(details)>0:
            max_val=details[0]
            for i in range(len(details)):
                if details[i]>max_val:
                    max_val=details[i]
            print(f'Maximum : {max_val}')
        else:
            print("No marks Available")
    elif opt==4:
        if len(details) > 0:
            min_val = details[0]
            for i in range(len(details)):
                if details[i] < min_val:
                    min_val = details[i]
            print(f'Minimum : {min_val}')
        else:
            print("No marks Available")
    elif opt==5:
        print("Thank you")
        break
    else:
        print("Invalid option")
