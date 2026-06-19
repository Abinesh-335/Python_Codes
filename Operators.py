"""
#Arithmetic Operators
a=7
b=5

print(a+b)  # 12
print(a-b)  # 2
print(a*b)  # 35
print(a/b)  # 1.4
print(a%b)  # 2 (remainder)
print(a**b) # 16807 (a^b= 7*7*7*7*7)
print(a//b) # 1 (floor division)

# Comparison Operator

print(a==b) # False
print(a>b)  # True
print(a<b)  # False
print(a>=b) # True
print(a<=b) # False
print(a!=b) # True

# Logical Operator

t=True
f=False

print(t and f) # False
print(t or f)  #True
print(not t)   #False

"""


"""
# Movie Ticket Eligibility🎞️🎬

Id=input("Do you have Id card?(y/n):")
Age=int(input("Enter the age:"))
if Age>0:
    if Age<13:
        print("Child Ticket")
    elif Age<60 and Id=='y':
        print("Ticket is Approved")
    elif Age<60 and Id=='n':
        print("Ticket is Denied - Id required")
    else:
        print("Senior Citizen Ticket")
else:
    print("Invalid Age")




# Electricity Bill
units=int(input("Enter the Units:"))
if units>0:
    if units <101:
        bill=units*2
    elif units<301:
        bill=units*5
    else:
        bill=units*8
    print(f"Bill Amount:{bill}")
    if bill>2000:
        print("High Electricity Usage")
    else:
        print("Normal Electricity Usage")
else:
    print("Invalid Units")
    


# Bank Loan Approval

age=int(input("Enter the Age:"))
if age<0:
    print("Invalid Input")
elif age > 18:
    salary = int(input("Enter the salary:"))
    credit = int(input("Enter the credits:"))
    if salary<0 or credit<0:
        print("invalid Inputs")
    else:
        if salary>=25000:
            if credit>=700:
                print("Loan Approved")
            else:
                print("Loan Rejected: Low Credit score")
        else:
            if credit < 700:
                print("Loan Rejected: Insufficient Salary and Low Credit score")
            else:
                print("Loan Rejected: Insufficient Salary")
else:
    print("Not Eligible:Underage")
"""


# ATM Withdrawal System
balance=int(input("Enter the Account Balance:"))
withdrawal=int(input("Enter the withdrawal Amount:"))
after_withdrawal_bal=balance-withdrawal
if balance<0 or withdrawal<0:
    print("Invalid input")
else:
    if withdrawal==0:
        if balance<500:
            print("FINE ALERT!! Account haven't minimum balance")
        else:
            print("You have Minimum balance only")

    elif after_withdrawal_bal<0:
        print("Insufficient Amount")
    elif after_withdrawal_bal<500:
        print("Minimum balance violation")
    else:
        print("Withdrawal Successful")
        print(f"Remaining Balance:{after_withdrawal_bal}")
