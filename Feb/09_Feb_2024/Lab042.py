
Scale = int(input("enter the score"))

if Scale <= 100 and Scale >= 90:
    print("Grade A")
elif Scale < 90 and Scale >= 80:
    print("Grade B")
elif Scale < 80 and Scale >= 70:
    print("Grade C")
else :
    print("fail")