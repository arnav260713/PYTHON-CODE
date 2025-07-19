word=str(input("enter yuor word:"))
charactor=str(input("enter you alphabet:"))
i=0
count=0
while i<len(word):
    if word[i]==charactor:
        count=count+1
    i=i+1
print(count)