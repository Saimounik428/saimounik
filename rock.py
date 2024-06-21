a=input("enter the value:").split()
b=[]
for i in a:
    if i not in b:
        b.append(i)
        print(b)
