number=int(input("Enter a Natural Number:"))

#The following steps take the number and divide it up among the elements.
#They then assign letters to each element.
if(number>=4000):
    print("Roman Numerals cannot go above 3999")
    Above=1
else: Above=0
if(number>=1000):
    t=(number/1000)
    M=("M"*int(t))
    number=number-(1000*int(t))
else: M=""
if(number>=500):
    t=(number/500)
    D=("D"*int(t))
    number=number-(500*int(t))
else: D=""
if(number>=100):
    t=(number/100)
    C=("C"*int(t))
    number=number-(100*int(t))
else: C=""
if(number>=50):
    t=(number/50)
    L=("L"*int(t))
    number=number-(50*int(t))
else: L=""
if(number>=10):
    t=(number/10)
    X=("X"*int(t))
    number=number-(10*int(t))
else: X=""
if(number>=5):
    t=(number/5)
    V=("V"*int(t))
    number=number-(5*int(t))
else: V=""
if(number>=1):
    t=(number/1)
    I=("I"*int(t))
    number=number-(1*int(t))
else: I=""

#The following step adds the numerals together.
numeral=(M+D+C+L+X+V+I)

#The following steps are for exceptions.
num=numeral.replace("DCCCC", "CM")
numeral=num
num=numeral.replace("CCCC","CD")
numeral=num
num=numeral.replace("LXXXX", "XC")
numeral=num
num=numeral.replace("XXXX", "XL")
numeral=num
num=numeral.replace("VIIII", "IX")
numeral=num
num=numeral.replace("IIII", "IV")
numeral=num

if (Above==0):
    print("That integer is the Roman Numeral", numeral)
print("test")

