Eingabe = 1
Lösung1 = 2
Lösung2 = 3
Lösung3 = 1
Lösung4 = 4
Passwort = 2903
print("Wie alt bist du?")
print("1. 48")
print("2. 59")
print("3. 58")
print("4. 60")
print("Gib die Numer der Richtigen Antwort ein")
Eingabe = int(input())
if Eingabe == Lösung1:
    print("Richtig. Du bekommst die Zahl 2")
if Eingabe != Lösung1:
    print("Falsch. Die Richtige Antwort war 2. Du bekommst die Zahl 2.")
print("")
print("Wo schläfst du am meisten ein?")
print("1. Im Bett")
print("2. In einem Zelt")
print("3. Vor dem Fernseher")
print("4. Auf dem Boden")
print("Gib die Numer der Richtigen Antwort ein")
Eingabe = int(input())
if Eingabe == Lösung2:
    print("Richtig. Du bekommst die Zahl 9")
if Eingabe != Lösung2:
    print("Falsch. Die Richtige Antwort war 3. Du bekommst die Zahl 9.")
print("")
print("Wann wurdest du geboren?")
print("1. 1965")
print("2. 1912")
print("3. 1976")
print("4. 1989")
print("Gib die Numer der Richtigen Antwort ein")
Eingabe = int(input())
if Eingabe == Lösung3:
    print("Richtig. Du bekommst die Zahl 0")
if Eingabe != Lösung3:
    print("Falsch. Die Richtige Antwort war 1. Du bekommst die Zahl 0.")
print("")
print("Wo arbeitest du?")
print("1. Google")
print("2. Galaxus")
print("3. Hornbach")
print("4. ZKB")
print("Gib die Numer der Richtigen Antwort ein")
Eingabe = int(input())
if Eingabe == Lösung4:
    print("Richtig. Du bekommst die Zahl 3")
if Eingabe != Lösung4:
    print("Falsch. Die Richtige Antwort war 4. Du bekommst die Zahl 3.")
print("")
print("Gib das Passwort ein")
Eingabe = int(input())
if Eingabe == Passwort:
    print("Richtig. Du darfst die Geschenke von den anderen jetzt auspacken.")
if Eingabe != Passwort:
    print("Zugang zu den Geschenken verweigert. Mache 5 Liegestützen um die Geschenke auspacken zu können.")
