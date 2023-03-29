def oddevensum(l):
    if l==[]:
        return (0,0)
    else:
        return (l[0]+oddevensum(l[2:])[0],l[1]+oddevensum(l[2:])[1])
    
    
def oddevensumi(l):
    oddtotal=eventotal=0
    for position in range(len(l)):
        if position % 2==0:
            eventotal+=l[position]
        else:
            oddtotal+=l[position]
    return (eventotal,oddtotal)

def equaliterative(lst):
    total0=0
    total1=0
    for element in lst:
        if element==lst[0]:
            total0+=1
        else:
            total1+=1
    if total1==total0:
        return True
    else:
        return False
    
def reversei(lst):
    left=0
    right=len(lst)-1
    while left<right:
        temp = lst[left]
        lst[left] = lst[right]
        lst[right] = temp
        left+=1
        right-=1
    return lst

def sumr(lst):
    if lst==[]:
        return 0
    else:
        return (lst[0]+sumr(lst[1:]))
    
    
def multiplication(lst):
    if lst == []:
        return 1
    elif len(lst)==1:
        return lst[0]
    else:
        return lst[0] * multiplication(lst[1:])

def average(lst):
    if lst==[]:
        return 0
    elif len(lst)==1:
        return lst[0]
    else:
        return (lst[0]+average(lst[1:])*(len(lst)-1))/len(lst)
    