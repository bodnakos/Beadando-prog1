def alter(szamsor):
    summa=[]
    sor=[]
    a=str(szamsor)
    minden=[]
    for i in range(len(a)):
        summa.append(int(a[i]))
    cd=len(summa)
    for i in range(len(summa)):
        if i != cd-1 and summa[i]%2==0 and summa[i+1]%2!=0:
            sor.append(summa[i])
            sor.append(summa[i+1])
        elif i != cd-1 and  summa[i]%2!=0 and summa[i+1]%2==0:
            sor.append(summa[i])
            sor.append(summa[i+1])
        elif i != cd-1 and summa[i]%2!=0 and summa[i+1]%2!=0:
            minden.append(sor)
            sor=[]
        elif i != cd-1 and summa[i]%2==0 and summa[i+1]%2==0:
            minden.append(sor)
            sor=[]
        minden.append(sor)
    leghosszabb=[]
    hossz=0
    for i in minden:
        if hossz < len(i):
            leghosszabb=i
            hossz=len(i)
    kesz=[]
    kesz.append(leghosszabb[0])
    for i in range(1,len(leghosszabb)):
        if leghosszabb[i]!=leghosszabb[i-1]:
            kesz.append(leghosszabb[i])
    joforma=""
    q=len(kesz)
    for i in kesz:
        joforma=joforma+str(i)
    joforma=joforma+" és ez "+str(q)+" karakter hosszú"
    return joforma

try:
    k=int(input("adja meg a számsort: "))
    x=75856312852
    y=12345678923456789
    z=234456693
    p=124896217962145697822
    print(alter(k))
except:
    print("hibás bemenet")