import random
Regel = "Ich denke mir eine Zahl zwischen 1 und 10 aus"
print(Regel)
Zufall =random.randint(1,10)
print("Gib eine Zahl ein: ", end="")
Eingabe = int(input())
if Eingabe == Zufall :
    print("Richtig")
if Eingabe != Zufall :
    print("Falsch")
print("die Richtige Zahl ist " + str(Zufall))
