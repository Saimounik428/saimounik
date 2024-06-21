l=input("enter the value:").split()
b=[]
for i in l:
    if l.count(i)%2!=0 and i not in b:
        b.append(i)
        print(b)
        
