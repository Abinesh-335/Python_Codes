

name='sam' #or name="sam"
print(name[0]+name[2]) #sm

# Slicing
strg="world"
print(strg[:2]) # wo
print(strg[2:]) # rld
print(strg[:-1])#worl
print(strg[-3:])# rld
print(strg[-3:-1]) #rl
print(strg[2:-1]) #rl
print(strg[2:4]) #rl

mobile='1234567890'
masked=mobile[:2]+"******"+mobile[-2:]
print(masked)  #12*****90


# Formating String

book="the atomic habits"
author="van dros"
print(book.title()+'\n -by '+author.title())

location="chennai"
fixed_loc=location.replace("chennai","Trichy")
print(fixed_loc)

msg="This the id : uxwe123. please react"
print(msg.split(':')[1])                        # uxwe123. please react
print(msg.split(':')[1].split('.')[0])          # uxwe123
print(msg.split(':')[1].split('.')[0].strip())  #uxwe123

text="This is the offer only for Zn100 coupon"
if "Zn100" in text:
    print("Offer available")
    print(f"The position of Coupon:",text.find('Zn100'))

e_name="vinoth kumar Shanmugam"
samp_txt=(word[0].upper() for word in e_name.split(" "))
print(samp_txt)             # <generator object <genexpr> at 0x000001B93546FED0>
res_txt=" ".join(samp_txt)
print(res_txt)

strg="This is my practice section"
count=[len(word) for word in strg.split(' ')]
print(count)

