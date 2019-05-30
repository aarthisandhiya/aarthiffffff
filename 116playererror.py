a=int(input())
dict={}
b=[int(a) for a in input().split()]
s={b[i]:b.count(b[i]) for i in range(len(b))}
print(s)
m=0
lis=[]
for k,j in s.items():
    if j>m:
        m=j
        g=k 
        lis.append(g)
       # break
    elif j==m:
        if k>k-1:
            m=j 
            temp=k 
            k=k-1
            k-1=temp
            lis.append(k-1)
            lis.append(k)
            #break
else:
    g=k
    lis.append(g)
print(*lis)
    
        
        
    
