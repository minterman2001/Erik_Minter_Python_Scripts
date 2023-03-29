def restart():
    Q=0
    D=0
    N=0
    P=0

    M=(int(input("Enter a number between 0 and 99: ")))

    if (M>=99):
        print("You can't type a number above 99")
        restart()
        Above=1
    else: Above=0
    while (M>=25):
        Q+=1
        M-=25
    while (M>=10):
        D+=1
        M-=10
    while (M>=5):
        N+=1
        M-=5
    while (M>=1):
        P+=1
        M-=1
    if (Above==0):
        print("Quarters:",Q, "Dimes:",D,"Nickels:",N,"Pennies:",P)

restart()
