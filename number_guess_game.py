#generaza un int random intre 0 si 10, folosind libraria random
import random
numar = random.randint(0,10)
#te intreaba care este numele tau, asteapta input
print ("-Care este numele tau?")
nume = input()
print (f"-Buna, {nume}!")
print ("-Ma gandesc la un numar intre 0 si 10")
"""
asteapta numarul ca si input si adauga fiecare incercare unei liste goale folosind functia append.
odata ce numarul a fost ghicit, loop-ul se termina si se printeaza mesajul numar corect, plus numarul de incercari
"""
guesses = [0]
while True:
    guess = int(input ("La ce numar ma gandesc?\n"))
    if guess < 0:
        print ("-Numarul nu poate fi negativ!")
        continue
    if guess > 10:
        print ("-Numarul este mai mare decat 10\nMai incearca!")
        continue
    guesses.append(guess)
    if guess != numar:
        print ("-Numar gresit! Mai incearca!")
        continue
    if guess == numar:
        print ("Numar Corect!\n")
        break
print (f"-Felicitari! Ai ghicit numarul in {len(guesses) - 1} incercari!")
