#*******************************************************************************
#         purpose: To remove all instances of a given element
# 
# input parameter: number, list
#    return value: a new list without the elements with number in it
#******************************************************************************/
def removeall(num,lst):
    newlst=[]
    for element in lst:
        if element!=num:
            newlst+=[element]
    return newlst
