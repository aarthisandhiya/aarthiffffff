a=input()
s=[]
k=[]
t=''
'''lst1=[]
hst1=[]
for i in range(0,len(a)):
    if a[i].isdigit():
        lst1.append(a[i])
    else:
        hst1.append(a[i])'''
        
for i in range(0,len(a)-1):
    x=len(a)-2
    if i==0:
        s.append(a[i])
    if a[i].isdigit():
        if a[i+1].isdigit():
            t=t+str(a[i])+''
            t=t+str(a[i+1])+''
            k.append(t)
        if i==x:
            if a[i].isdigit():
                if a[i-1].isdigit():
                    t=t+str(a[i])+''
                    t=t+str(a[i-1])+''
                    k.append(t)
                else:
                    k.append(a[i])
                
                
    else:
        if a[i] not in s:
            s.append(a[i])
    
    
print(s)
print(k)
'''print(lst1)
print(hst1)'''
