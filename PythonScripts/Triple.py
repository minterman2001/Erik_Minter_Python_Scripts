#*******************************************************************************
#         purpose: To compute the triple of a list.
# 
# input parameter: list of n
#    return value: a natural number representing the triple of that list 
#******************************************************************************/
def triple1(L):
    if L == [] or L == "":
        return []
    else:
        return [L[0]]*3+triple1(L[1:])

   