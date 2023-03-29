#*******************************************************************************
#         purpose: To remove all instances of a given element
# 
# input parameter: number or letter, list
#    return value: a new list without the elements of the number or letter in it
#******************************************************************************/
def removeall(e,L):
    if type(L)==list:
        newlist=[]
        for item in L:
            if item != e:
                newlist+=[item]
    elif type(L)==str:
        newlist=''
        for item in L:
            if item != e:
                newlist+=item
    return newlist    