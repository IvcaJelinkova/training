#sibenice.py

# rozděl projekt do funkci a modulu s hezkymi jmény, piš testy a dokumentační řetězce,
# funkční kousky dávej postupně do Gitu.

# OK - Počítač náhodně zvolí slovo (trávník, stromek, stavení). malá písmena a bez opakujících se písmen (čokoláda).

#  - Výchozí stav je řetězec s tolika podtržítky, kolik je ve vybraném slově písmen.
#  - Výchozí počet neúspěšných pokusů je nula.
# Stále dokola:
    #  - Zeptej se hráče na písmeno.
    #  - Pokud je to písmeno ve vybraném slově, zaměň ve stavu příslušná podtržítka
            # za ono písmeno. (Bude se hodit řetězcová metoda index. a funkce zamen.)
    #  - Pokud dané písmeno není ve vybraném slově, započítej neúspěšný pokus.
    #  - Vypiš stav (slovo s případnými podtržítky).
    #  - Pokud už ve slově nejsou podtržítka, pogratuluj hráči a ukonči hru.
    #  - Vypiš počet neúspěšných pokusů a odpovídající obrázek. Funkci, která ti vrátí
    #       obrázek podle počtu pokusů, si můžeš stáhnout z Gitu
    #  - Pokud je počet neúspěšných pokusů 9 (nebo víc), hráč prohrál. Dej mu to najevo a ukonči program.


from random import choice

def vyber_slovo():
        mozna_slova = ["trávník", "stromek", "stavení"]
        slovo = choice(mozna_slova)
        return slovo
print(vyber_slovo())


#obrazek.py download from https://gist.github.com/encukou/77376e445356a9843e278ba387b168f0.js
def obrazek(level):
    if level == 0:
        return """
        ~~~~~~~
        """
    elif level == 1:
        return """
        +
        |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif level == 2:
        return """
        +---.
        |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif level == 3:
        return """
        +---.
        |   |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif level == 4:
        return """
        +---.
        |   |
        |   O
        |
        |
        |
        ~~~~~~~
        """
    elif level == 5:
        return """
        +---.
        |   |
        |   O
        |   |
        |
        |
        ~~~~~~~
        """
    elif level == 6:
        return """
        +---.
        |   |
        |   O
        | --|
        |
        |
        ~~~~~~~
        """
    elif level == 7:
        return """
        +---.
        |   |
        |   O
        | --|--
        |
        |
        ~~~~~~~
        """
    elif level == 8:
        return """
        +---.
        |   |
        |   O
        | --|--
        |  /
        |
        ~~~~~~~
        """
    else:
        return """
        +---.
        |   |
        |   O
        | --|--
        |  / \\
        |
        ~~~~~~~
        """


