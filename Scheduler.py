# NOTE: Run this program via terminal run/f5 not work (python3 file_name.py argv1 argv2 argv3...)

import sys
#check number of arguments
if len(sys.argv)==2:
    print("The Argument is not enough")
    sys.exit()

# for sure number of arguments
f_name=sys.argv[1]
l_name=sys.argv[2]
name=f_name+l_name

#Formate the name to email
email=name.lower().replace(' ','.')+"@company.com"

#print the details
print("\n__Your Detail__")
print(f'Full name:{name}')
print(f'Email id:{email}')



#python file.py Sam 4 Chennai

#for not sure arguments
list_name=sys.argv[1:]
print(list_name)     #['sam','4','chennai']

#using join
str_name=''.join(list_name)
print(str_name)      #sam4chennai