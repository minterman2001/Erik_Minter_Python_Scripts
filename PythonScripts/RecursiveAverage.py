def recursiveaverage(lst):
    if len(lst)==0:
        return None
    elif len(lst)==1:
        return lst[0]
    else:
        return (lst[0]+(len(lst)-1)*recursiveaverage(lst[1:]))/len(lst)