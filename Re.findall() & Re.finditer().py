s=input()
vowels = "aeiouAEIOU"
con = "qwrtypsdfghjklzxcvbnmQWRYPSDFGHJKLZXCVBNM"
matches=[]
if len(s)<=0 or len(s)>=100:
    print(None)
else:
    i=0
    while i<len(s):
        if s[i] in vowels:
            start=i
            while i<len(s) and s[i] in vowels:
                i+=1
            substring=s[start:i]
            if len(substring)>1 and start>0 and i<len(s) and s[start-1] in con and s[i] in con:
                matches.append(substring)
        else:
            i+=1
    if matches:
        for match in matches:
            print(match)
    else:
        print(-1)
