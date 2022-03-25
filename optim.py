import random
dizi=[]
n=int(input("Eleman sayısını girin:"))
for i in range(n):
    dizi.append("x"+str(i))
print(dizi)
for i in range(n):
    def Rx(n):
        for i in range(n):
            dizi[i]=random.randint(0,1)
        return dizi
    print("Ragele çözüm = {}".format(Rx(n)))

#kısıtların uygunluğu kontrolü
def kisit(n):
    uygun=0
    for i in range()
    if dizi[i]*3+dizi[i+1]+3*dizi[i+2]+ 2*dizi[i+3]+4*dizi[i+4] < 10:
        uygun=1    
    if dizi[i+2]-dizi[i+3] > 0:
        uygun=1
    if dizi[i+2]-dizi[i+4] > 0:
        uygun=1
    if dizi[i]+dizi[i+1]+dizi[i+2]+dizi[i+3]+dizi[i+4] <4:
        uygun=1
        
    return uygun
print("Kısıtlar uygun çözümü sağlıyor ise  {} değilse {} = {}".format(0,1,kisit(n)))

#amaç fonksiyonu
def Amac(n):
    F_deger=dizi[0]+3*dizi[1]-2*dizi[2]+2*dizi[3]-dizi[4]
    return F_deger
#Rasgele aramayı kullanan ana fonksiyon
#iterasyon_sınırı=print("iterasyon sınırını girin:{}".format(int(input())))
def RA(iterasyon_sınırı):
    x_mevcut=Rx(n)
    while kisit(x_mevcut)==1:
        x_mevcut=Rx(n)
        break
    i=1
    for i in range(10):
        x_aday=Rx(n)
        while kisit(x_aday)==1:
            x_aday=Rx(n)
            break
    if Amac(x_aday)>Amac(x_mevcut):
        x_mevcut=x_aday
    return x_mevcut

print("Bulunan en iyi uygun çözüm={}".format(RA(10)))
print("Optimal çözüm = {}".format(Amac(n)))
