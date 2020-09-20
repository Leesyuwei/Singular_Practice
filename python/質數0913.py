while 1:
    a=int(input())
    x=0
    if a == 2:
        print('質數')
        continue
    for i in range(3,a,2):
        if a%i==0:
            x=x+1
            break
    if x > 0:
        print('合數')
    else:
        print('質數')