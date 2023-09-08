
def isPalindrome(s):
       
    #to change it the string is similar case
    s = s.lower()
    # length of s
    l = len(s)
     
    # if length is less than 2
    if l < 2:
        return True
 
    # If s[0] and s[l-1] are equal
    elif s[0] == s[l - 1]:
        
        # Call is pallindrome form substring(1,l-1)
        return isPalindrome(s[1: l - 1])
 
    else:
        return False

def MakePalindrome(s):
    if isPalindrome(s):
        return None
    else:
        p = s
        t = ""
        i = -1
        while not isPalindrome(p):
            p = s
            t += p[i]
            p = t + p
            i -= 1
        return t


s = input()
print(MakePalindrome(s))