upperrange=int(input("enter starting no:"))
lowerrange=int(input("enter ending no:"))
for i in range(upperrange,lowerrange+1):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
                print(i)