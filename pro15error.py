a=int(input())
lis=[]
cou=0
q=[]
dictt={}
c=[int(a) for a in input().split()]
for i in range(0,len(c)):
    d=bin(c[i])
    lis.append(d)
print(lis)
for j in range(0,len(lis)):
    s=lis[j]
    print(s)
    for k in range(len(s)):
        if s[k]=="1":
            cou=cou+1 
    dictt.update({s:cou})
    cou=0
