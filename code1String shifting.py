def lr(string):
    return string[1:len(string)]+string[0]
tc=int(input())
for i in range(tc):
    s=input()
    for j in range(len(s)):
        s=lr(s)
        print(s,end=" ")
    print("")