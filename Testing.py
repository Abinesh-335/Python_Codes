'''
i=10.87 
print(type(i))
j=int(i)
print(type(j),i)


import sys

if len(sys.argv)==2:
    print("You might be give two argumernts")
    sys.exit()
fullname=sys.argv[1:]
print ("Length is: ",len(fullname))

strg=" ".join(fullname)
print(strg)

email=strg.lower().replace(" ",".")+"@gmail.com"

print("fullname:",fullname)
print("email:",email)



strg="world"
print(strg[:2]) # wo
print(strg[2:]) # ld
print(strg[:-1])#worl
print(strg[-3:])# rld
print(strg[-3:-1]) #rl
print(strg[2:-1]) #rl
print(strg[2:4]) #rl
'''
'''
strg="This the id : uxwe123. please react"
res=strg.split(':')[1].split('.')[0].strip()
print(res)


off="This is your kind msg Np100 cupon"
if 'Np100' in off:
    print("offer valis")

print(off.find("Np100"))


name="Abinesh Rajendran"
lis= ''.join([word[0].upper() for word in name.split()])
print(lis)

r=0
count=sum([len(word) for word in name.split()])
print(count)
'''
data=[1,2,3,4,5]
sam=(data for i in data if i==3)
print(sam)




