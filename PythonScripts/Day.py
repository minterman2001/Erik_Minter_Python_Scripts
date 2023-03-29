################################################################################
#
#          filename: day.py
#
#      description: Implements of ordinal day of the year program.
#
#              author: Minter, Erik
# AMU e-mail id: erik.minter@my.avemaria.edu
#
#              course: CSCI 201: Introduction to Computer Programming
#         instructor: Dr. Perugini
#      assignment: Homework III
#
#          assigned: January 26, 2023
#                   due: February 2, 2023
#
################################################################################
month=int(input("Enter a month as an integer: ")) 
day=int(input("Enter a day of the month as an integer: "))
year=int(input("Enter a year as an integer: ")) #Steps 1-3 serve to define month, day, and year as integers
answer=0 #Initial day of year is 0. Final day of year is 364
if(month>=1):
   answer=day-1 #Subtract first day by 1
if(month>=2):
    answer=day+30 #Add 30 if month is greater or equal to 2
if(month>=3):
    answer=answer+28 #Add 28 if month is greater or equal to 3
if(month>=4):
    answer=answer+31 #Add 31 if month is greater or equal to 4
if(month>=5):
    answer=answer+30 #Add 30 if month is greater or equal to 5
if(month>=6):
    answer=answer+31 #Add 31 if month is greater or equal to 6
if(month>=7):
    answer=answer+30 #Add 30 if month is greater or equal to 7
if(month>=8):
    answer=answer+31 #Add 31 if month is greater or equal to 8
if(month>=9):
    answer=answer+31 #Add 31 if month is greater or equal to 9
if(month>=10):
    answer=answer+30 #Add 30 if month is greater or equal to 10
if(month>=11):
    answer=answer+31 #Add 31 if month is greater or equal to 11
if(month>=12):
    answer=answer+30 #Add 30 if month is greater or equal to 12
print("\nThe date ", month, "/", day, "/", year, " is day ", answer, " of year ", year, ".", sep="")