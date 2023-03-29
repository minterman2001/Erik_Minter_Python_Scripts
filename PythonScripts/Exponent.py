#*******************************************************************************
# purpose: To compute the exponent of a list.
# 
# input parameter: list of (x,y)
# return value: a natural number representing the exponent of the x, y number of times
#******************************************************************************/
def exp1(x,y):
    return expB(1,x,y)

def expB(a,b,n):
  if n == 0:
     return a 
  else:
     return expB(a*b,b,n-1)
    