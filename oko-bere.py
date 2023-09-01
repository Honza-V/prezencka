from random import randrange

bodu = 0
print("Máš", bodu, "bodů.")
pokrac = input("\nChceš pokračovat?\n")
while (pokrac == "Ano" or pokrac == "ANO" or pokrac == "ano" or pokrac == "a") and bodu < 21:
    nova_karta = randrange(2, 11) 
    print("Na nové kartě je", nova_karta, "bodů.")
    bodu = bodu + nova_karta
    print("Máš", bodu, "bodů.")
    if bodu > 21:
        print("Prohrál jsi!")
    elif bodu == 21:
        print("Vyhrál jsi!")
    elif bodu < 21:
        pokrac = input("\nChceš pokračovat?\n")

print("Konec hry. Děkujeme za účast.")
