cycle1=int(input("give first cyclist speed:"))
cycle2=int(input("give second cyclist speed:"))
cycle3=int(input("give third cyclist speed:"))
averagespeed=(cycle1+cycle2+cycle3)/3
print("averege speed",averagespeed)
if cycle1<averagespeed:
    print("cycle1 slower then average,diffrence is:",averagespeed-cycle1)
elif cycle2<averagespeed:
    print("cycle2 slower then average,diffrence is:",averagespeed-cycle2)
else:
    print("cycle3 slower then average,diffrence is:",averagespeed-cycle3)