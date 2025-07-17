def Pow_fun(a, b, m):
    if a>10 or a<1:
        return False
    elif b>10 or b<1:
        return False
    elif m>1000 or m<2:
        return False
    else:
        print(pow(a, b))
        print(pow(a, b, m))
a=int(input())
b=int(input())
m=int(input())
Pow_fun(a, b, m) 
