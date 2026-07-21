
'''
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

String Functions
"A".isalpha()       #True
"9".isalpha()       #False
" ".isalpha()       #False
"Abinesh".isalpha() #True
"Abi123".isalpha()  #False
"Abinesh R".isalpha() #False (space make this false)


print("sams".count("s"))  #2
islower()
isupper()
isdigit()
print("sama".startswith('s'))  # True
endswith()
replace()

"Abi  san vin".split(' ')  #['Abi','','san','vin']
"Abi   san   vin".split() #['Abi','san','vin']

'''
from idlelib.replace import replace

from django.utils.lorem_ipsum import sentence

'''
# user name validation
user_name=input("Enter the Username:")
if len(user_name)<8:
    print("Username is too short")
elif len(user_name)>10:
    print("Username is too long")
elif " " in user_name:
    print("Username cannot contain spaces")
elif not (user_name[0]).isalpha():
    print("Username must start with a letter")
else:
    print("Valid username")



#Password Strength Checker

password=input("Enter the password")
if len(password)>=8:
    check_upper=False
    check_lower=False
    check_digit=False
    check_space=False
    check_special=False

    for w in password:
        if w.isupper():
            check_upper = True
        if w.isdigit():
            check_digit=True
        if w.islower():
            check_lower=True
        if w.isspace():
            check_space=True
        if w in '@#!&$':
            check_special=True
    if not check_upper:
        print("Password must contain an uppercase letter")
    elif not check_digit:
        print("Password must contain a digit")
    elif not check_lower:
        print("Password must contain an lowercase letter")
    elif check_space:
        print("Password must not contain a Spaces")
    elif not check_special:
        print("Password must contain a special character")
    else:
        print("Strong Password")

else:
    print("Password is too short")


#Email Validation
ids=input("Enter the mail Id")
check_start = False
check_end = False
check_count=False
check_space = False
check_symbol = False

if ids.startswith("@"):
    check_start = True
if ids.endswith(".com"):
    check_end = True
if '@' in ids:
    check_symbol = True
    if ids.count('@')==1:
        check_count=True
if " " in ids:
        check_space=True
if  check_start:
    print("Email must start with alphabets")
elif not check_end:
    print("Email must end with .com")
elif not check_symbol:
    print("Email must have @")
elif not check_count:
    print("Must be one @")
elif check_space:
    print("Email doesn't contain space")
else:
    print("Valid Email")


name=input("Enter the name:")
ids=input("Enter the email ID:")
password=input('Enter the password:')
if  name.replace(' ','').isalpha():
    if ids.count('@')==1 and ids.endswith('.com') and not ' ' in ids:
        if len(password)>8 and not " " in password:
            check_upper=False
            check_lower=False
            check_digit=False

            for w in password:
                if w.isupper():
                    check_upper = True
                elif w.islower():
                    check_lower = True
                elif w.isdigit():
                    check_digit=True
            if check_digit and check_upper and check_lower:
                print("Registered Successfully")
        else:
            print("Enter a Valid Password")
    else:
        print("Enter a Valid EmailID")
else:
    print("Enter a valid Username")



# Word Counter
msg=input("Enter the sentence:")
char=0
vowel=0
const=0
digit=0
space=0
word=0

for i in range(len(msg)):
    w=msg[i]
    if i==0 or msg[i-1]==" " and msg[i]!=" ":
        word=word+1
    if w.isalpha():
        char=char+1
    if w.lower() in 'aeiou':
        vowel=vowel+1
    if w.lower() not in 'aeiou' and w.isalpha():
        const=const+1
    if w.isdigit():
        digit=digit+1
    if w.isspace():
        space=space+1

print(f"Words:{word}")
print(f"Letters:{char}")
print(f"Vowels:{vowel}")
print(f"Consonants:{const}")
print(f"Digit:{digit}")
print(f"Space:{space}")

'''


msg=input("Enter the sentence:")
letter=0
char=0
vowel=0
const=0
digit=0
space=0
word=0
upper=0
lwr=0
sent=0
for i in range(len(msg)):
    w=msg[i]
    char+=1
    if w in '!.?' and msg[i-1]!=" ":
        sent+=1
    if (i==0 or msg[i-1]==" ") and msg[i]!=" ":
        word+=1
    if w.isalpha():
        letter+=1
    if w.lower() in 'aeiou':
        vowel+=1
    if w.lower() not in 'aeiou' and w.isalpha():
        const+=1
    if w.isdigit():
        digit+=1
    if w.isspace():
        space+=1
    if w.isupper():
        upper+=1
    if w.islower():
        lwr+=1
print(f"Total characters:{char}")
print(f"Sentences:{sent}")
print(f"Words:{word}")
print(f"Letters:{letter}")
print(f"Vowels:{vowel}")
print(f"Consonants:{const}")
print(f"UpperCase Letters:{upper}")
print(f"lowerCase Letters:{lwr}")
print(f"Digit:{digit}")
print(f"Space:{space}")
