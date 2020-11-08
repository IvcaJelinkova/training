# pwgenerator.py


import random

mala = 'abcdefghijklmnopqrstuvwxyz'
velka = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cisla = '0123456789'
spec_znaky = '!"#$%&\'()*+,-./:;<>=?@{}|~[]\\^_¨'



def vyber_znak(sada) -> str:
    """Vybírá konkrétní znak ze zadané sady (mala/velka/cisla/spec_znaky)
    dané globální proměnné. """
    return random.choice(sada)




def main(delka_hesla, pocet_hesel, slozeni) -> str:
    """Vygeneruje zadaný počet hesel dané délky a složení.
    Podmínkou je vybrat z každé sady min. 1 znak. """
    for pocet in range(pocet_hesel):
        heslo = []
        if slozeni == 1:
            heslo.append(vyber_znak(mala))
            heslo.append(vyber_znak(velka))

            for i in range(delka_hesla-2):
                sada = random.choice([mala, velka])
                heslo.append(vyber_znak(sada))

        elif slozeni == 2:
            heslo.append(vyber_znak(mala))
            heslo.append(vyber_znak(velka))
            heslo.append(vyber_znak(cisla))

            for i in range(delka_hesla-3):
                sada = random.choice([mala, velka, cisla])
                heslo.append(vyber_znak(sada))

        elif slozeni == 3:
            heslo.append(vyber_znak(mala))
            heslo.append(vyber_znak(velka))
            heslo.append(vyber_znak(cisla))
            heslo.append(vyber_znak(spec_znaky))

            for i in range(delka_hesla-4):
                sada = random.choice([mala, velka, cisla, spec_znaky])
                heslo.append(vyber_znak(sada))


        else:
            print('Zadej 1, 2 nebo 3. ')
            slozeni = int(input('''Zadej číslo 1–3 pro výběr složení: 
                                            1) pouze písmena,
                                            2) písmena a čísla, 
                                            3) písmena, čísla a spec. znaky. 
                Vybrané složení → '''))
        random.shuffle(heslo)
        print("".join(heslo))


if __name__ == "__main__":
    delka_hesla = int(input('Délka hesla: '))
    pocet_hesel = int(input('Počet hesel: '))
    slozeni = int(input('''Zadej číslo 1–3 pro výběr složení: 
                                1) pouze písmena,
                                2) písmena a čísla, 
                                3) písmena, čísla a spec. znaky. 
        Vybrané složení → '''))

    main(delka_hesla, pocet_hesel, slozeni)






