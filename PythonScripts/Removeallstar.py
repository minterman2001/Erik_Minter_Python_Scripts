def removeallstar(num, lst):
    if lst==[]:
        return []
    elif type(lst[0])!=list:
        if num==lst[0]:
            return removeallstar(num,lst[1:])
        else:
            return [lst[0]]+removeallstar(num,lst[1:])
    else:
        return [removeallstar(num,lst[0])]+removeallstar(num,lst[1:])

def removeallstariterate(num,lst):
    newlst=[]
    stack=[lst]
    for element in stack:
        if type(element)==list:
            stack+=element
        elif element!=num:
            newlst+=[element]
        stack=stack[1:]
    return newlst
