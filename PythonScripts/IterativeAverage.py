def iterativeaverage(lst):
    if lst==[]:
        return lst
    count=len(lst)
    total=0
    for item in lst:
        total+=item
    return total/count
