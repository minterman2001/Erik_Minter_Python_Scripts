def nested_sum(lst):
    total=0
    stack=[lst]
    while len(stack)>0:  
        current=stack[0]
        stack=stack[1:]
        for element in current:
            if type(element)==list:
                stack=[element]+stack
            else:
                total+=element    
    return total
