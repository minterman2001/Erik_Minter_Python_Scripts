def count1(letter, word):
    count=0
    for element in word:
        if element==letter:
            count+=1
    return count

def count2(letter, word):
    if len(word)==0:
        return 0
    elif len(word)>0:
        return count2(letter, word[1:]) + (1 if word[0]==letter else 0)