''''Suatu proyek pembangunan membutuhkan besi beton dengan diameter 16 mm sebagai berikut:
5.4 m, 4.5 m, 4.2 m, 4.1 m, dan 2.15 m, masing-masing sebanyak 160, 204,152, 480, dan 160 unit

Sementara itu, panjang besi beton yang tersedia adalah 12 m dan 15 m.
Oleh karena kebutuhan yang beragam, besi beton tersebut harus dipotong-potong sesuai kebutuhan.
Pemotongan tersebut direncanakan dengan menyusun beberapa pola dengan memperhatikan kriteria-kriteria berikut:
1.	panjang total hasil pemotongan harus sama atau lebih pendek dari 12 m atau 15 m,
2.	panjang sisa pemotongan kurang dari 2.15 m, dan
3.	tidak ada duplikasi pola.
'''

LStandard=[12,15]
LDemand = [5.4, 4.5, 4.2, 4.1, 2.15]

for i in LStandard:
    print("S=", i)
    bilmaks=[]
    for k in LDemand:
        n = int(i/k)
        bilmaks.append(n)
        if k == LDemand[-1]:
            break

    listmaks=[]
    HKali=[0,0,0,0,0]
    for j in range(len(LDemand)):
        listmaks.append(list(range(bilmaks[j]+1)))

    import itertools
    for q in itertools.product(listmaks[0],listmaks[1],listmaks[2],listmaks[3],listmaks[4]):
        p=list(q)
        for k in range(len(p)):
            HKali[k]=p[k]*LDemand[k]
        total=sum(HKali)
        if total<=i:
            if i-total<=2.15:
                print(p)
                total=0
            else:
                total=0