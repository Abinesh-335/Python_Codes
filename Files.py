'''Core modes (what you already wrote, explained properly)
r – Read
->File must exist
->Cursor at beginning
❌ No writing allowed

w – Write
->Overwrites everything
->Creates file if not exists
->Cursor at beginning

👉 This is dangerous if you don’t intend to erase data

a – Append
->Adds data at the end
->Doesn’t delete existing content
->Creates file if not exists
---------------------------------------------------------
Combined modes (read + write)
r+
Read + write
File must exist
Cursor at beginning
Doesn’t erase content automatically

w+
read + write
Deletes all existing content
Creates file if not exists

a+
Read + append
Cursor at end for writing
Can read, but you may need seek(0)
Binary modes (for images, videos, etc.)

--------------------------------------------------
rb
Read binary

wb
Write binary (overwrites)

ab
Append binary

===========================================
The part most people miss
You can combine modes:

rb+ → read + write binary

wb+ → overwrite + read binary

ab+ → append + read binary

Interview-level summary (say this cleanly)

“File modes like r, w, and a control how a file is opened—whether for reading,
writing, or appending. Modes with + allow both reading and writing, while b is
used for binary files.
Each mode also defines whether the file must exist or if it will be created or
overwritten.”'''

##################################################################################


'''
file=open("sample.txt",'w')
file.write("Hello welcome to python\n")
file.write("pathunadthukoda\n")
file.close()


d=open("sample.txt",'r')
print(d.read())
d.close()
'''
######
'''
#append
file=open("sample.txt",'a')       # if we give 'w' it overwrites
file.write("Error code conflict")
file.close()
'''
######
'''

with open("sample.txt","r") as file:  #no need to close the file while use with
    for i in file:
        print(i)
'''


#######
'''
cont=input("Enter your feedback:\n")
with open("writers.txt","a") as file:
    file.write(cont+'\n')  
print("Success")


    
with open("writers.txt","r") as file:
    print("The contents in file")
    for i in file:
        print(i)

'''
####
'''
#read()
with open ("sample.txt",'r') as file:
     content=file.read() #its read the entier contents in file
     for line in content: #it returns letter by letter
            print(line)

#readline()
with open ("sample.txt",'r') as file:
   while True:
       c=file.readline()      # its returns each line in the file
       if not c:
           break
       if 'Error' in c:
            print(c.strip())
 '''

####

with open ("sample.txt",'r') as file:
    for _ in range(10):
        print(file.readline())

print("*************************88")
        
with open ("sample.txt",'r') as file:
    for _ in range(10):
        c=file.readline()
        if not c:
            print("empty")
            continue
        print(c)
            


