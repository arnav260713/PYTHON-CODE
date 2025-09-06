try:
    no=int(input("Enter your number:"))
    print(no)
except ValueError as e:
    print("exception",e)