import random
Kugel = []
for Nr in range (1,50) :
    Kugel.append(False)
Zufall = random.randint(1,49)
for Nr in range(6) :
    while Kugel[Zufall] == 1 :
     Zufall = random.randint(1,49)
    Kugel[Zufall] = True
    print("Nr. " + str(Nr+1) + " => " + str(Zufall))
