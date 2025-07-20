rows=int(input("enter the number of rows:"))
for i in range(rows+1):
    for j in range(i+1):
        print("*",end=" ")
    print()