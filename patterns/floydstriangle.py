rows=int(input("enter the number of rows:"))
no=1
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(no,end=" ")
        no=no+1
    print()