#*******************************************************************************
#
#      filename:  Clique.py
#
#   description:  Implements a set of commands for uniformity in a list
#
#        author:  Minter, Erik
# AMU e-mail id:  erik.minter@my.avemaria.edu
#
#        course:  CSCI 201: Introduction to Computer Programming
#    instructor:  Dr. Perugini
#    assignment:  Homework VIII
#
#      assigned:  March 16, 2023
#           due:  March 23, 2023
#
#  FYI this script took me well over seven hours to complete... Have mercy please!
#*******************************************************************************
#*******************************************************************************
clique1 = [1,1,0,0,0,1,0,0,0,1,1,0,1]
clique2 = [1,1,0,0,0,1,0,0,0,1,1,1,1]
clique3 = [1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0]
clique4 = [1,0,1,0,1,0,1,0,1,0]
clique5 = [1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,1,1,0]
clique6 = [1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
clique7 = [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

cliques = [clique1,clique2,clique3,clique4,clique5,clique6,clique7]

def generateCommands(clique):
#calculates if there are more groups of 1s or 0s
    if not clique:
        return 0
    count0, count1 = 0, 0
    in_group0=False
    in_group1 =False 
    for element in clique:
        if element == 0:
            in_group1=False
            if not in_group0:
                in_group0 = True
                count0 += 1          
        else:
            in_group0=False   
            if not in_group1:
                in_group1 = True
                count1+=1
#Counts the number of 1s and 0s in the list
    number0=0
    number1=0
    for element in clique:
        if element ==0:
            number0+=1
        else:
            number1+=1
#Iterates over the groups from start to end
    groups = []
    start=None
    end = None
    if clique[0]==1:
        if count0 > count1:
            for i in range(len(clique)):
                if clique[i] == 0:
                    if start != None and end != None:
                        groups+=[[start,end]]
                        start, end = None, None
                else:
                    if start == None:
                        start = i + 1
                    end = i + 1
            if start != None and end != None:
                groups+=[[start,end]]
        
        elif count1 > count0 or number1>=number0:
            for i in range(len(clique)):
                if clique[i] == 1:
                    if start != None and end != None:
                        groups+=[[start,end]]
                        start, end = None, None
                else:
                    if start == None:
                        start = i + 1
                    end = i + 1
            if start != None and end != None:
                groups+=[[start,end]]
                
        elif number0>number1:
            for i in range(len(clique)):
                if clique[i] == 0:
                    if start != None and end != None:
                        groups+=[[start,end]]
                        start, end = None, None
                else:
                    if start == None:
                        start = i + 1
                    end = i + 1
            if start != None and end != None:
                groups+=[[start,end]]
                       
    else:
        for i in range(len(clique)):
            if clique[i] == 0:
                if start != None and end != None:
                    groups+=[[start,end]]
                    start, end = None, None
            else:
                if start == None:
                    start = i + 1
                end = i + 1
        if start != None and end != None:
            groups+=[[start,end]]

    for group in groups:
        output=print("Guests in positions", group[0]-1, "to", group[1]-1, "conform.")
    return output
# main program
i = 1
for clique in cliques:
    print("Clique", str(i)+":")
    generateCommands(clique)
    print()
    i += 1
    