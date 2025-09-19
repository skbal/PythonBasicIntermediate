
#Write a program that asks a user for a number of years and the print it number of days, hours, minutes and seconds


years = int(input("Enter the number of years: "))
inSec= years*365*24*60*60
print(inSec)



#Obtain temperature of 7 days and print average temperature.

tempList = str(input("enter 7 days temp with comma seperated")).split(",")
print (tempList)
avegTemp = sum([int(temp) for temp in tempList])/len(tempList)
print(avegTemp)



#Odd or Even - Write a program that takes an integer as input and checks whether it’s odd or even.

getIntput = int(input("Enter u r number"))

if getIntput % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
	

#Positive, Negative, or Zero - Accept a number and print whether it’s positive, negative, or zero.

getIntput = int(input("Enter u r number"))

if getIntput  == 0:
    print("Number is ZERO")
elif getIntput > 0 :
    print("Number is +")
elif getIntput < 0 :
    print("Number is -")
else :
    print("Invalid input")
	
	

#Check Leap Year - Ask the user for a year and determine if it is a leap year or not.
#(Hint: A year is leap if divisible by 4, not divisible by 100 unless divisible by 400)

getYear = int(input("Enter Year to check"))

if getYear % 4 == 0 and getYear % 100 != 0 or getYear % 400 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
	

#Largest of Two Numbers  -Take two integers as input and print which one is greater (or if they are equal).0

getInt1 = int(input("Enter Number 1"))
getInt2 = int(input("Enter Number 2"))

if getInt1 > getInt2:
    print(getInt1)
elif  getInt1 == getInt2:
    print("Equal")
else:
    print(getInt2)
	



#Grade Calculator - Accept a student’s marks and print the grade:
#
#90+ : A
#
#80–89 : B
#
#70–79 : C
#
#60–69 : D
#
#< 60 : Fail
#
mark = int(input("ENTER the MARK"))
if mark >= 90:
	print("GRADE A")
elif mark >=80 and mark < 90:
	print("GRADE B")
elif mark >=70 and mark < 80:
	print("GRADE C")
elif mark >=60 and mark < 70:
	print("GRADE D")
elif mark < 60:
	print("GRADE Fail")
else
	print("not valid entry")

#Password Strength Checker - Ask for a password and check:
#
#Length ≥ 8
#
#Contains both letters and numbers
#
#Contains at least one special character (!, @, #, etc.)
#
#Triangle Type Checker - Accept the lengths of three sides and determine whether the triangle is:
#
#Equilateral (all sides equal)
#
#Isosceles (two sides equal)
#
#Scalene (all sides different)
#
#Or invalid (violates triangle inequality rule)
#
#ATM Withdrawal Simulation - Input balance and withdrawal amount:
#
#If amount ≤ balance and is a multiple of 100, approve withdrawal and print remaining balance.
#
#Otherwise, print an error message.
#
#Electricity Bill Calculator - Based on units consumed:
#
#First 100 units: ₹5/unit.;
#
#Next 100 units: ₹7/unit
#
#Above 200 units: ₹10/unit
#
#(Add a fixed meter charge of ₹100)
#
#Nested Discount System - Input purchase amount:
#
#If amount ≥ 5000 → discount 20%
#
#Else if amount ≥ 3000 → discount 15%
#
#Else if amount ≥ 1000 → discount 10%
#
#Else → no discount
#
#(Also, if customer is a "Premium Member", add an extra 5% discount on the final bill)
#
#Create a BMI calculator
