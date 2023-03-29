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
