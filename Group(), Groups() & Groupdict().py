import re
s=input()
if len(s)<=0 or len(s)>=100:
    print(None)
else:
    for i in range(1, len(s)):
        if s[i]==s[i-1] and s[i].isalnum():
            print(s[i])
            break
    else:
        print(-1)