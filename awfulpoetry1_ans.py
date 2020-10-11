#!/usr/bin/env python3

import random, sys


def main():
    try:  
        row = 0 
        digit = 0
        argumentos = sys.argv
        artigos = ["a", "o", "um", "uma", "e"]
        sujeitos = ["irmao", "peixe", "lua", "pai", "mae"]
        verbos = ["corre", "pula", "nada", "foge"]
        adverbios = ["vagarosamente", "silenciosamente", "bem", "mal"]
        
        txt = ""

        if len(argumentos) > 1:
            digit = int(argumentos[1])
        else:
            digit = 5

        limit = digit if digit <= 10 else 10

        while row < limit:
            line = ""

            artigo = random.choice(artigos)

            sujeito = random.choice(sujeitos)

            verbo = random.choice(verbos)

            adverbio = random.choice(adverbios)

            line = '{0} {1} {2} {3}'.format(artigo, sujeito, verbo, adverbio)

            txt += line + "\n"

            row += 1
    except ValueError as err:
        print(err, "in", digit)

    print(txt)


main()
        