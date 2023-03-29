def sqrt2():
    n=float(input("Enter a number: "))
    InitialGuess=float(input("Enter an initial Guess: "))
    print ("Computing the Square Root of: ",n)
    delta=.001
    NewGuess=1.0
    tally=0
    difference=1
    while (delta<=difference) or (difference<0):
        InitialGuess=NewGuess
        Quo=n/NewGuess
        Avg=(Quo+NewGuess)/2
        NewGuess=Avg
        difference=InitialGuess-NewGuess
        print ("Iteration",tally, ":", NewGuess)
        tally+=1
    print ("The Square Root of", n, "is", NewGuess)
    return NewGuess