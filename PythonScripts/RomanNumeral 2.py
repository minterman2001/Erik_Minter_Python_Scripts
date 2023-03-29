################################################################################
#
#          filename: RomanNumeral.py
#
#      description: Changing natural number to Roman Numeral
#
#              author: Minter, Erik
# AMU e-mail id: erik.minter@my.avemaria.edu
#
#              course: CSCI 201: Introduction to Computer Programming
#         instructor: Dr. Perugini
#      assignment: Homework III
#
#          assigned: February 2, 2023
#                   due: February 7, 2023
#
################################################################################
number=int(input("Enter a Natural Number:"))

#The following steps take the number and divide it up among the elements.
#They then assign letters to each element and subtract off the element value.

if(number>=4000):
    print("Roman Numerals cannot go above 3999")
    Above=1
else: Above=0

if(number>=1000):
    t=(number/1000)
    M=("M"*int(t))
    number=number-int(1000*int(t))
else: M=""

if(number>=900):
    t=(number/900)
    CM=("CM"*int(t))
    number=number-(900*int(t))
else: CM=""

if(number>=500):
    t=(number/500)
    D=("D"*int(t))
    number=number-(500*int(t))
else: D=""

if(number>=400):
    t=(number/400)
    CD=("CD"*int(t))
    number=number-(400*int(t))
else: CD=""

if(number>=100):
    t=(number/100)
    C=("C"*int(t))
    number=number-(100*int(t))
else: C=""

if(number>=90):
    t=(number/90)
    XC=("XC"*int(t))
    number=number-(90*int(t))
else: XC=""

if(number>=50):
    t=(number/50)
    L=("L"*int(t))
    number=number-(50*int(t))
else: L=""

if(number>=40):
    t=(number/40)
    XL=("XL"*int(t))
    number=number-(40*int(t))
else: XL=""

if(number>=10):
    t=(number/10)
    X=("X"*int(t))
    number=number-(10*int(t))
else: X=""

if(number>=9):
    t=(number/9)
    IX=("IX"*int(t))
    number=number-(9*int(t))
else: IX=""

if(number>=5):
    t=(number/5)
    V=("V"*int(t))
    number=number-(5*int(t))
else: V=""

if(number>=4):
    t=(number/4)
    IV=("IV"*int(t))
    number=number-(4*int(t))
else: IV=""

if(number>=1):
    t=(number/1)
    I=("I"*int(t))
    number=number-(1*int(t))
else: I=""

#The following step adds the numerals together.
numeral=(M+CM+D+CD+C+XC+L+XL+X+IX+V+IV+I)

if (Above==0):
    print("That integer is the Roman Numeral:", numeral)
