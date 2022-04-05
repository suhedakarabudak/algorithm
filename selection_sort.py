#selection sort algorithm
dizi=[1,36,17,10,9,12]

for i in range(5): 
    min=i     
    for j in range(i,6): 
        if dizi[j]< dizi[min]: 
            min=j
            
    aracieleman=dizi[i]
    dizi[i]=dizi[min]
    dizi[min]=aracieleman
print(dizi)




