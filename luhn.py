# luhn.py

import sys

print()

def luhn(cardnum) -> bool:
    """Bere cislo karty a vrati True/False podle toho jestli Luhnuv algoritmus overi
    platnost karty.
    1. Cifry v cisle karty se revertuji
    2. Cifry na sudych pozicich se zesumuji
    3. Cifry na lichych pozicich se vynasobi cislem 2 + ciferne se sectou
    4. Udela se vysledna suma
    5. Vysledek musi byt delitelny 10
    """

    cardnum_revert = cardnum[::-1]  # revertuju

    # cardnum_sude = cardnum_revert[1::2] nebo
    suma = 0
    for i, cislice in enumerate(cardnum_revert):
        if i % 2 == 0:
            suma += int(cislice)
        else:
            dvojnasobek = int(cislice) * 2
            if dvojnasobek < 9:
                suma += dvojnasobek
            else:
                while dvojnasobek > 0:
                    dvojnasobek, zbytek = divmod(dvojnasobek, 10)
                    suma += zbytek

    # zbytek po dělení 10 je 0 --> číslo je platné
    return suma % 10 == 0


def main(cardnum: str) -> None:
    """ Vypisuje, zda se jedná o validní či nevalidní číslo karty.
    V případě validní vypíše i značku (Mastercard/VISA/Maestro/jiná).

    Mastercard:
      prefix (rozsah): 51-55
      dlzka: 16

    Visa:
      prefix: 4
      dlzka: 16

    Maestro:
      prefix (rozsah): 50, 56-69
      dlzka: 12-19
    """
    if not luhn(cardnum):
        print('Nevalidní číslo karty. ')
        return

    prefix = int(cardnum[0:2])
    prefix_v = int(cardnum[0])
    delka = len(cardnum)
    if prefix in range(51, 56) and delka == 16:
        print('Validní číslo karty: Mastercard')
        return
    elif prefix_v == 4 and delka == 16:
        print('Validní číslo karty: VISA')
        return
    elif (delka in range(12, 20)) and (prefix == 50 or prefix in range(56, 70)):
        print('Validní číslo karty: Maestro')
        return
    else:
        print('Validní číslo karty: jiná značka. ')
        return


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("{}: Program bere prave 1 argument "
                 "pro cislo karty".format(sys.argv[0]))
    main(sys.argv[1])



# Priklady vystupu:
# ./python3 luhn.py 4532793439971390
#       Validni cislo karty: VISA
#
# ./python3 luhn.py 5519664409261324
#       Validni cislo karty: Mastercard
#
# ./python3 luhn.py 376932432175784
#       Validni cislo karty: Neznamy vyrobce
#
# ./python3 luhn.py 372232432175784
#       Nevalidni cislo karty
#


