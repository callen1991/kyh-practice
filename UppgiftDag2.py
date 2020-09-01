import random

n = random.randint(1, 100)
print("Jag tänker på en siffra mellan 1 och 100. Gissa vilken?")

while True:
    text = input("Din gissning: ")
    as_number = int(text)

    if as_number == n:
        print("Korrekt!")
        break

    if as_number < n:
     print("Fel, mitt nummer är högre... Försök igen!")

    if as_number > n:
     print("Fel, mitt nummer är lägre... Försök igen!")






