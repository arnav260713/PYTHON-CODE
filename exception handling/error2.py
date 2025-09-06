try:
    no=int(input("Enter your no:"))
    nu=int(input("Enter your nu:"))
    result=no/nu
    print(result)
except ZeroDivisionError:
    print("you have divided the no with zero")
except:
    print("wrong input")
else:
    print("no exception")
finally:
    print("this block will execute always")