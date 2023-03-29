#*******************************************************************************
#         purpose: To compute the approximate value of e.
# 
# input parameter: n, a natural number
#    return value: a natural number representing the approximate e of n
#******************************************************************************/

def approx_e(n):
    n+=1
    dummy=approx=new=0
    while n>0:
        dummy=approx+new
        approx=(1/factorial1(n))
        new=approx+dummy
        n-=1
    return new

def factorial1(n):
    if n==0:
        return 1
    while n>0:
        fact=n*factorial1(n-1)
        return fact
    
