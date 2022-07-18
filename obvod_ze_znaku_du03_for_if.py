# Pomocí cyklů for a příkazu if napiš program, který z jednotlivých 'X' a mezer vypíše:
#
# X X X X X X
# X         X
# X         X
# X         X
# X         X
# X X X X X X
# znak a počet řádků uživatel zadá

znak = input('Zadej znak k vypisování: ')
pocet_radku = int(input('Zadej počet řádků: '))
pocet_sloupcu = int(input('Zadej počet sloupců: '))

for i in range(pocet_radku): 
    for i in range(pocet_sloupcu): 
        print(znak, end=' ')
    print()
