#*******************************************************************************
#
#      filename:  sqrt1.py
#
#   description:  Implements a Square Root conversion.
#
#        author:  Minter, Erik
# AMU e-mail id:  erik.minter@my.avemaria.edu
#
#        course:  CSCI 201: Introduction to Computer Programming
#    instructor:  Dr. Perugini
#    assignment:  Homework IV
#
#      assigned:  February 14, 2023
#           due:  February 21, 2023
#
#*******************************************************************************
def sqrt2():
    n=float(input("Enter a number: "))
    InitialGuess=float(input("Enter an initial Guess: "))
    print ("Computing the Square Root of: ",n)
    delta=.001
    if n>0:
        squares=sqrt1(n,InitialGuess,delta)
    print ("The Square Root of", n, "is", squares)
    return squares
#*******************************************************************************
#         purpose: To compute the square root of a non-negative integer n.
# 
# input parameter: n, a natural number
#    return value: a natural number representing the factorial of n
#******************************************************************************/
def sqrt1(n,InitialGuess=1.0,delta=.001):
    NewGuess=1.0
    tally=0
    difference=1
    while (delta<=difference) or (difference<0):
        InitialGuess=NewGuess
        Quo=n/NewGuess
        Avg=(Quo+NewGuess)/2
        NewGuess=Avg
        difference=InitialGuess-NewGuess
        print ("Iteration",tally, ":", NewGuess)
        tally+=1
    return NewGuess

sqrt2()
