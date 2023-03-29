def rotate_word(i,num):
    if i==' ':
        return ' '
    shiftletter=chr(((ord(i)-97+num)%26)+97)
    return shiftletter
def scrambletext(s,n):
    l=len(s)-1
    if s=="" or s==[] or n==0:
        return s
    else:
        return rotate_word(s[0],n)+scrambletext(s[1:],n)