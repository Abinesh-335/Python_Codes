'''
#List

lis=["abi","arul","gotham","sam"]

lis.append("vinoth")
print("Append-->",lis)

lis.insert(2,"arul")
print("Insert-->",lis)

lis.remove("vinoth")
print('Remove-->',lis)

lis.reverse()
print("Reverse-->",lis)

lis.pop()
print("Pop-->",lis)

print("count",lis.count("arul"))

#list slicing

print(lis[:2])
print(lis[-2:])

#List iteration

for i in lis:
    print("--",i)

#check if
if 'abi' in lis:
    print ("yes")


#update list(change)

lis[3]="samuvel"
print("changed-->",lis)


for i,k in enumerate(lis):
    print(f"{i}:{k}")
'''
#--------------------------------------------
'''
#Tuple

tup=(1,2,4,3,2)
print(tup)

print(tup[2])

#tup[2]=8 not worked

print(tup[2])

print("count-->",tup.count(2))
print("Index-->",tup.index(2))


for i,k in enumerate(tup):
    print(f"{i}:{k}")

}")
'''
#--------------------------------------------
'''

#Set

#sets={"abi","arul","gotham","sam"}
  #(or)

lis=["abi","arul","gotham","sam"]
sets=set(lis)

for i,k in enumerate(sets):
    print(f"{i}:{k}")

city1={"Kum","chennai","bangalore"}
city2={"chennai","vellore","madurai"}

print("Union-->",city1.union(city2))
print("Instesection-->",city1.intersection(city2))
print("difference-->",city1.difference(city2))


city1.add("thanjavur")
print(city1)


city1.remove("chennai")
print(city1)

#safe remove
city1.discard("trichy")

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
