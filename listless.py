a=[1,1,3,5,64,14,15,78,25,50]
n=int(input("enter a number: "))
new_a=[]
for i in a:
    if i<n:
        new_a.append(i)
print(new_a)