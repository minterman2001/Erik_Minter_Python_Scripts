def isaleapyear(year):
    if (year % 100 == 0) and (year % 400 == 0):
        year=True
        return year
    elif (year % 100 !=0) and (year % 4 == 0):
        year=True
        return Year
    else:
        year=False
        return year
        