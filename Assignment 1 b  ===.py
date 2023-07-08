print("Twinke twinkle little star",
      "\n \t How I wonder  what you are",
                  "\n\t Up abpve the world so high",
                  "\n\t Like a diamond in the sky",
       "\n Twinkle twinkle little star",
       "\n\thow i wonder what you are")

# verssiom
import sys
print("system version")
print(sys.version)
print("Version info")
print(sys.version_info)

#date and time 
import datetime

now= datetime.datetime.now()
print("date and time: ")
print(now.strftime("%y-%m-%d  %H:%M:%S"))

#Area of a circle


import math
radius = float(input("enter the radius of a circle"))
area = math.pi * radius * radius
print("area of a circle is: {0}" .format(area))





# reverse order with space



firstname = input("enter the name")
lastname =  input("enter the name")
print(f"{lastname} {firstname}")


## program to take 2 input and gAVE ADDITION
 
A = int(input( "fisrt number"))
B = int(input("second number"))
C = A + B
print(C)


## how to check odd or even


number = int(input("enter a number: "))

if(number %2) == 0:
    print("it is a even number" .format(number))
else:
    print ("{0} is an odd number" .format(number))




#marksheet taking input of 5 subjects

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



