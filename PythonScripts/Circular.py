#*******************************************************************************
#         purpose: To cycle a list i number of times
# 
# input parameter: number, list
#    return value: a new list that has been cycled i number of times
#******************************************************************************/
def circular(i,L):
    if L==[] or L==[1] or i==0:
        return L
    else:  
        return circular(i-1,L[1:])+[L[0]]