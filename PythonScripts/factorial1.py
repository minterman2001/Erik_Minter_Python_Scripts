#*******************************************************************************
#         purpose: To compute the factorial of a non-negative integer n.
# 
# input parameter: n, a natural number
#    return value: a natural number representing the factorial of n
#******************************************************************************/

def factorial1(n):
    if n==0 or n==1:
        return 1
    while n>0:
        fact=n*factorial1(n-1)
        return fact
        
        
        
       
