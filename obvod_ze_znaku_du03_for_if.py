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

for cislo_radku in range(pocet_radku): 
    #print('i:', cislo_radku, end='')
    if cislo_radku in (0, pocet_sloupcu-1):     # prvni a posledni radek ma vzdy (znak+mezera)
        print((znak + ' ') * pocet_sloupcu) 
    else: 
        print(znak + ' ' + (' ' * 2) * (pocet_sloupcu - 2) + znak)      # ostatni radky maji (znak+mezera) pouze jako prvni a posledni clen
    

#another tasks: 
for i in 'Ahoj světe!': 
    print(i)        #print each character, don't work for numbers of course


