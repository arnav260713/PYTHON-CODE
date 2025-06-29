hindi_marks=int(input("give your hindi marks:"))
science_marks=int(input("give your science marks:"))
english_marks=int(input("give your english marks:"))
maths_marks=int(input("give your maths marks:"))
sst_marks=int(input("give your sst marks:"))
percentage=(science_marks+hindi_marks+sst_marks+english_marks+maths_marks)/5
print("Your percentage is",percentage)
if percentage>90 and percentage<100:
    print("A+")
elif percentage>80 and percentage<90:
    print("B+")
elif percentage>70 and percentage<80:
    print("C+")
elif percentage>60 and percentage<70:
    print("D+")
elif percentage>50 and percentage<60:
    print("E")
elif percentage>40 and percentage<50:
    print("F")
else:
    print("you are failed")