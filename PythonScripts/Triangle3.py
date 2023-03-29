def triangle(n):
    i=0
    while i<=n:
        j=n
        while i<j:
            print("*",end='')
            j-=1
        print ("")
        i+=1
