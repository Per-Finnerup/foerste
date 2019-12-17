# Gæt et tal
import random

def for_høj_eller_for_lav(gæt, hem):
    if gæt < hem:
        print('Dit gæt er for lavt')
        print()
    if gæt > hem:
        print('Dit gæt er for højt')
        print()

def prøv_igen():
    print('Prøv igen')
    print()
    tal = int(input('Vælg et tal imellem 1 og 100: '))
    print()
    return tal

def gæt_et_tal():
    hem_tal = random.randint(1, 100)
    gæt_tal = int(input('Vælg et tal imellem 1 og 100: '))
    print()
    tæl = 1
    while gæt_tal != hem_tal:
        for_høj_eller_for_lav(gæt_tal, hem_tal)

        tæl = tæl + 1
        gæt_tal = prøv_igen()
    print('Hurra du gættede det hemmelige tal på',tæl,'gæt ')

gæt_et_tal()

