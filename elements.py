a=list(map(int,input("enter the value:").split()))
b=[]
a.sort()
for i in a:
    if i%2==0:
        b.insert(0,i)
    else:
            b.append(i)
            print(b)
