################################################################################
#
#      filename:  roman.py
#
#   description:  Implements of Roman numeral converter.
#
#        author:  Minter, Erik
# AMU e-mail id:  erik.minter@my.avemaria.edu
#
#        course:  CSCI 201: Introduction to Computer Programming
#    instructor:  Dr. Perugini
#    assignment:  Homework IV
#
#      assigned:  February 7, 2023
#           due:  February 14, 2023
#
################################################################################
def restart():    
    number=int(input("\nEnter a Natural Number: "))
    #The following steps take the number and divide it up among the elements.
    #They then assign letters to each element and subtract off the element value.

    pristine=number
    numeral=""
    if(number>=4000):
        print("Roman Numerals cannot go above 3999")
        Above=1
        restart()
    else: Above=0

    while(number>=1000):
        numeral+="M"
        number-=1000

    while(number>=900):
        numeral+="CM"
        number-=900

    while(number>=500):
        numeral+="D"
        number-=500

    while(number>=400):
        numeral+="CD"
        number-=400

    while(number>=100):
        numeral+="C"
        number-=100

    while(number>=90):
        numeral+="XC"
        number-=90

    while(number>=50):
        numeral+="L"
        number-=50

    while(number>=40):
        numeral+="XL"
        number-=40

    while(number>=10):
        numeral+="X"
        number-=10

    while(number>=9):
        numeral+="IX"
        number-=9

    while(number>=5):
        numeral+="V"
        number-=5

    while(number>=4):
        numeral+="IV"
        number-=4

    while(number>=1):
        numeral+="I"
        number-=1

    if (Above==0):
        print("\nThe integer", pristine, "is the Roman Numeral:", numeral)
        question = input("\nWould you like to try another number? (Y/N): ")
        if question=="y" or question=="Y" or question=="Yes" or question=="YES" or question=="yes":
            restart()
        if question=="n" or question=="N" or question=="No" or question=="NO" or question=="no":
            print("\nAight bye!")
restart()  