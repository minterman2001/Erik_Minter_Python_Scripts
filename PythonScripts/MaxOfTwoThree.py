def MaxOfTwo(x,y):
        if x > y:
           return x
        else:
           return y
        
def MaxOfThree(x,y,z):
    if (MaxOfTwo(x,y) is x) and (x>=z):
       return x
    if (MaxOfTwo(x,y) is y) and (y>=z):
        return y
    if (z>=y) and (z>=x):
       return z
    
