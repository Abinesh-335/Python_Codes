#Check password

'''
password="123@"
check=""
while True:
    if check=="123@":
        print("Access Granted")
        break
    check=input("Enter the password:")


nums=[5,-2,6,1,-2,0]
for i in nums:
    if i<0:
        continue
    print(i)        # 5 6 1 0
for i in nums:
    pass            # Future logic implementation


mul_no=int(input("Enter the Multiplier No:"))
no_range=int(input("Enter the range:"))
for i in range(10):
    print(f"{i}x{no_range}={i*mul_no}")
'''
from django.utils.http import escape_leading_slashes

"""
# Password Checker
password="123@god"
failed_attempts=1
for i in range(3):
    user_password = input("Enter the password:")
    failed_attempts=i+1
    if password==user_password:
        print("Login Successfully")
        break
    else:
        print("Password Wrong")
        if failed_attempts==3:
            print("Account Locked")
            break
"""

# ATM menu System
balance=1000
while True:
    print("1.Check Balance\n2.Deposit\n3.Withdrawal\n4.Exit")
    option = int(input("Choose the option:"))
    if option==1:
        print(f"Balance:{balance}")
    elif option==2:
        dep=int(input("Enter the amount want to Deposit:"))
        if dep>0:
            balance=balance+dep
            print(f"Balance:{balance}")
            print("Successfully Deposited")
        else:
            print("invalid amount")
    elif option==3:
        withdraw=int(input("Enter the Withdrawal Amount:"))
        if withdraw>0:
            cond_amt=balance-withdraw
            if balance<withdraw:
                print("Insufficient amount")
            else:
                if cond_amt>=500:
                    balance=cond_amt
                    print("Withdraw successful")
                else:
                    print("Minimum balance violation")
        else:
            print("Invalid amount")

    elif option==4:
        print("Thank you")
        break
    else:
        print("Choose the valid Option")
