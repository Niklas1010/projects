import random
def initGame() :
    Regel = "Ich denke mir eine Zahl zwischen 1 und 1000"
    print(Regel)
def playGame(Versuche, Eingabe) :
    Zufall =random.randint(1,1000)
    while Eingabe != Zufall :
        print("Rate mal: ", end="")
        Eingabe = int(input())
        Versuche += 1
        if Eingabe < Zufall :
            print("Zu klein!")
        if Eingabe > Zufall :
            print("ZU gross!")
        if Eingabe == Zufall :
            print("Richtig")
    return Versuche 
def endGame(Versuche) :
    print("DU hast " + str(Versuche) + " Mal geraten.")
initGame()
Spiel = playGame(0,0)
endGame(Spiel)
