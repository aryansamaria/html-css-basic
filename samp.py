l=[1,2,3,4,5]
for i in range(len(l)-1):
    c=i
    for j in range(1,len(l)):
        l[c],l[j]=l[j],l[c] 
        c+=1
print(l)        
