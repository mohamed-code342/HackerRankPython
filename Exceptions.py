n=input()
for i in range(int(n)):
    a,b=input().split()
    try:
        print(int(a) // int(b))
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero')    
    except ValueError :
        if a.isalnum():
            c=b
        else:
            c=a
        print(f"Error Code: invalid literal for int() with base 10: '{c}'")
