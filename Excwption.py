try:
    num=int(input("Enter the number"))
    price=2000/num
    print("Avereage:",price)

except FileNotFoundError:
    print("Enter valid values")

except Exception:
    print(Exception)

finally:   #consider if login and worked code crached put logout comment in finally
    print("logged out{following code maynot execute when exception but i do}")

print("This trasaction success")
