import random

antal_gissningar = 0
n = random.randint(1, 100)
print("Jag tänker på en siffra mellan 1 och 100. Gissa vilken?")







def mainloop(antal_gissningar, n):
    while True:
        text = input("Din gissning: ")
        as_number = int(text)
        antal_gissningar = antal_gissningar + 1
        if as_number == n:
            print(f"Korrekt! {antal_gissningar}  gissningar använda")
            break

        if as_number < n:
            print("Fel, mitt nummer är högre... Försök igen!")
            print("du har gjort " + str(max_guesses) + " gissningar använda")

        if as_number > n:
            print("Fel, mitt nummer är lägre... Försök igen!")
            print("du har gjort " + str(max_guesses) + " gissningar använda")


mainloop(antal_gissningar, n)

