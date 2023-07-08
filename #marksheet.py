sub1=int(input("english: "))
sub2=int(input("maths: "))
sub3=int(input("islamiat: "))
sub4=int(input("urdu: "))
sub5=int(input("science: "))
perc=((sub1+sub2+sub3+sub4+sub5)/500)*100
if(perc>=90):
    print("Grade: A")
elif(perc>=80 and perc<90):
    print("Grade: B")
elif(perc >=70 and perc<80):
    print("Grade: C")
elif(perc>=60 and perc<70):
    print("Grade: D")
else:
    print("Grade: F")



    