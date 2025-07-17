if __name__ == '__main__':
    n = int(input())
    l = ''
    if n<1 or n>150:
        print('wrong value')
    else:
        for i in range(1,n+1):
            l += str(i)
        print(l)
