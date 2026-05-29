# Einfaches Python-Programm

print("Willkommen zum Mini-Rechner!")

# Eingabe vom Benutzer
zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))

# Operation auswählen
print("Wähle eine Operation:")
print("1 = Addition")
print("2 = Subtraktion")
print("3 = Multiplikation")
print("4 = Division")

wahl = input("Deine Auswahl (1-4): ")

# Berechnung
if wahl == "1":
    ergebnis = zahl1 + zahl2
    print("Ergebnis:", ergebnis)

elif wahl == "2":
    ergebnis = zahl1 - zahl2
    print("Ergebnis:", ergebnis)

elif wahl == "3":
    ergebnis = zahl1 * zahl2
    print("Ergebnis:", ergebnis)

elif wahl == "4":
    if zahl2 != 0:
        ergebnis = zahl1 / zahl2
        print("Ergebnis:", ergebnis)
    else:
        print("Fehler: Division durch 0!")

else:
    print("Ungültige Auswahl!")

print("Programm beendet.")
