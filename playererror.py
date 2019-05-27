a=input()
dict={}
for i in range(0,len(a)):
    s=a.count(a[i])
    dict.update({a[i]:s})
    
    
#print(dict)
minn=0
for j,k in dict.items():
    if k>minn:
        minn=k
for i in a:
        if minn==:
            ele=j 
print(j+' '+str(minn))
        
    
