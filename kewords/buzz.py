word=int(input("enter your no.:"))
for i in range(word):
    if i%20==0:
        print("twist")
    elif i%15==0:
        pass
    elif i%5==0:
        print("fizz")
    elif i%3==0:
        print("buzz")
    else:
        print(word)