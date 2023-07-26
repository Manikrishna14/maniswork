for i in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    a=1
    for j in li:
        a*=j
    lii=[]
    for j in range(1,a+1):
        if(a%j==0):
            lii.append(j)
    print(len(lii))