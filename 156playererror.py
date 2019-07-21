a,k=map(int,input().split())
s=[int(a) for a in input().split()]
s=" "
for i in range(0,k):
    for j in range(0,k-1):
        for l in range(0,k):
            if s[j]>s[l]:
                temp=s[j]
                s[j]=s[l]
                s[l]=temp
        s=s+int(s[j])+" "
for i in range(k,len(s)):
    for j in range(0,len(s)-1):
        for l in range(j+1,len(s)):
            if s[j]<s[l]:
                temp=s[j]
                s[j]=s[l]
                s[l]=temp
        s=s+int(s[j])+" "
print(s)
                
            
