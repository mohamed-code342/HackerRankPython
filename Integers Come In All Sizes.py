def cul(a, b, c, d):
    if a<1 or a>1000:
        return False
    elif b<1 or b>1000:
        return False
    elif c<1 or c>1000:
        return False
    elif d<1 or d>1000:
        return False
    else:
        res = pow(a, b) + pow(c, d)
        print(res)
a=int(input())
b=int(input())
c=int(input())
d=int(input())
cul(a, b, c, d)
