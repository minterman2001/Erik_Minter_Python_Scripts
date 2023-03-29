def recursivetranspose(lst):
    if lst==[] or len(lst)==1:
        return lst
    elif len(lst)>1:
        return [lst[1],lst[0]]+recursivetranspose(lst[2:])