number=int(input("enter your number:"))
no2=int(input("enter the number from which to check divisibilty:"))
if number==0:
     print("change the no.")
elif number%no2==0:
    print(f"{number} is divisible by {no2}")
else:
     print(f"{number} is not divisible by {no2}")
