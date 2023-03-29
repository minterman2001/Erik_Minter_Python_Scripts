#*******************************************************************************
#
#      filename:  Encryption1.py
#
#   description:  Implements an encryption of lowercase characters
#
#        author:  Minter, Erik
# AMU e-mail id:  erik.minter@my.avemaria.edu
#
#        course:  CSCI 201: Introduction to Computer Programming
#    instructor:  Dr. Perugini
#    assignment:  Homework VII
#
#      assigned:  March 7, 2023
#           due:  March 16, 2023
#
#*******************************************************************************
#*******************************************************************************
#         purpose: Algorithm to shift characters, only lowercase characters.
# 
# input parameter: ('any lowercase letter',any number)
#    return value: 'lowercase letter representing the shifted letter'
#******************************************************************************/
def shift(c,n):
    if c==' ':
        return ' '
    shiftletter=chr(((ord(c)-97+n)%26)+97)
    return shiftletter
#*******************************************************************************
#         purpose: encryption algorithm to scramble letters n number of times
# 
# input parameter: ('any lowercase words or letters with spaces',any number)
#    return value: 'lowercase word or letter scrambled n number of times'
#******************************************************************************/
def scrambletext(s,n):
    l=len(s)-1
    if s=="" or s==[] or n==0:
        return s
    else:
        return shift(s[0],n)+scrambletext(s[1:],n)
    
## shift test cases
print(shift)

print(shift('a',6)) # 'g'

print(shift('y',7)) # 'f'

print(shift('h',77)) # 'g'

print(shift('a',-6)) # 'u'

print(shift('y',-7)) # 'r'

print(shift('h',-77)) # 'i'

## scrambletext test cases
print(scrambletext)

print(scrambletext("",3))

print(scrambletext("functional",0))

#ans: "ixqfwlrqdo" 
print(scrambletext("functional", 3))

# ans: "functional"
print(scrambletext(scrambletext("functional",3), -3))

# ans: "crkzqflkxi"
print(scrambletext("functional",-3))

# ans: "functional"
print(scrambletext(scrambletext("functional",-3),3))

# ans: "yixgshrk"
print(scrambletext("scrambletext",6))

# ans: "lzw imauc xgp"
print(scrambletext("the quick fox",70))

# ans: "the quick fox"
print(scrambletext(scrambletext("the quick fox",81),-81))

#; an English pangram (contains all the letters in the English alphabet)
# ans: "the quick brown fox jumped over the lazy dog"
print(scrambletext(scrambletext("the quick brown fox jumped over the lazy dog", 360), -360))
