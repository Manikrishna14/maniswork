def isprime(n):
    if(n==1):
        return False
    elif(n==2):
        return True
    else:
        f=0
        for i in range(2,n//2+1):
            if(n%i==0):
                f+=1
        if(f==0):
            return True
        else:
            return False
for i in range(int(input())):
    a,b=map(int,input().split())
    s=0
    for j in range(a,b+1):
        if(isprime(j)):
            s+=1
    print(s)