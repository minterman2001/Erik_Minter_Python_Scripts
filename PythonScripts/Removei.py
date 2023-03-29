def removei(e,lst):
    if type(lst)==str:
        for elem in lst:
            if elem==e:
                elem=""
                lst[e]=elem
                return lst
    if type(lst)==list:
        for elem in range:
            if elem==e:
                elem=[]
                lst[e]=elem
                return lst
        
def remove_at_index(e, lst):
    if type(lst) == str:
        newlst = ""
        for elem in range(len(lst)):
            if elem != e:
                newlst += lst[elem]
        return newlst
    elif type(lst) == list:
        newlst = []
        for elem in range(len(lst)):
            if elem != e:
                newlst+=[lst[elem]]
        return newlst
            
def member1(e,lst):
    if lst==[]:
        return False
    for element in lst:
        if element ==e:
            return True  
    else:
        return False     
