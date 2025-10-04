wheather=(1,0,0,0,1,1,0)
rainy=0
sunny=0
for i in wheather:
    if i==0:
        rainy+=1
    else:
        sunny+=1
if sunny>rainy:
    print("good wheather")
else:
    print("bad wheather")