amount=int(input("enter your amount-"))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("notes of 100 rupees-",note1)
print("notes of 50 rupees-",note2)
print("notes of 10 rupees-",note3)