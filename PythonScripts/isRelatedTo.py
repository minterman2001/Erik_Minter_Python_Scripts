# a set of cities
cities = ["Vancouver", "Los Angeles", "Mexico", "Minneapolis",
          "Omaha", "Kansas City", "Denver", "St. Louis",
          "Memphis", "Chicago", "New Orleans", "Cinncinati",
          "Pittsburgh", "Montreal", "New York"]

# a set of rivers
rivers = ["Missouri", "Platte", "North Platte", "South Platte",
          "Arkansas", "Canadian", "Kansas", "Mississippi",
          "Tennessee", "Ohio", "Allegheny", "Monongahela"]

# a relation: a subset of cities x rivers
isOnRiver = [("Denver", "Platte"), ("Omaha", "Missouri"),
             ("Omaha", "Platte"), ("Kansas City", "Missouri"),
             ("Kansas City", "Kansas"),
             ("Minneapolis", "Mississippi"),
             ("St. Louis", "Mississippi"),  
             ("St. Louis", "Missouri"),
             ("Memphis", "Mississippi"),
             ("New Orleans", "Mississippi"),
             ("Cinncinati", "Ohio"),
             ("Pittsburgh", "Ohio"),
             ("Pittsburgh", "Allegheny"),
             ("Pittsburgh", "Monongahela")]

# a relation: a subset of rivers x rivers
flowsInto = [("Platte", "Missouri"), ("Kansas", "Missouri"),
             ("Missouri", "Mississippi"), 
             ("Allegheny", "Ohio"), ("Monongahela", "Ohio"),
             ("Tennessee", "Ohio"), ("North Platte", "Platte"),
             ("South Platte", "Platte"),
             ("Ohio", "Mississippi")]




"""def isRelatedTo(a,b,r):
    if r==[]:
        return False
    else:
        return r[1:]+isRelatedTo(a,b,r[1:]) or r[0]+isRelatedTo(a,b,r[0])"""
def isRelatedTo(a, b, r):
    if not r:
        return False
    else:
        head = r[0]
        tail = r[1:]
        if a == head[0] and b == head[1]:
            return True
        elif a == head[1] and b == head[0]:
            return True
        else:
            return isRelatedTo(a, b, tail)
