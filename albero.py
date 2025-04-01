lettera = input("Immetti lettera: \n")
dimbase = int(input("Immetti dim base: \n"))
countPari = 0
countDispari = 0
"""
for i in range(1, dimbase + 1):
    if i % 2 == 0:
        countPari += 1
        print("Numeri pari ", i, countPari)
    else:
        countDispari += 1
        print("Numeri dispari", i, countDispari)
if dimbase % 2 == 0:
    for i in range(1, countPari + 1):
        print(" " * i, dimbase*i, " "*i)
else:
    for i in range(1, countDispari + 1):
        print(" " * i, dimbase*i, " "*i)
"""

i=1
while i <= dimbase:
    print(" " * ((dimbase-i) // 2)+ lettera*(i+1 - (dimbase%2)))
    i += 2