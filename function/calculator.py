def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("pl select the opration ")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
choice=input("enter your choice:")
if choice=="1":
    print(add(1,2))
elif choice=="2":
    print(subtract(1,2))
elif choice=="3":
    print(multiply(1,2))
elif choice=="4":
    print(divide(1,2))

