# Gæt ord
hemmelig_ord = 'kat'
gæt = ''
gæt_tæl = 0
gæt_limet = 5
ikke_flere_gæt = False

while gæt != hemmelig_ord and not(ikke_flere_gæt):
    if gæt_tæl < gæt_limet:
        gæt = input('Gæt på et ord: ')
        gæt_tæl += 1
    else:
        ikke_flere_gæt = True
        
if ikke_flere_gæt:
    print('Du har ikke flere gæt, DU TABTE !')
else:
    print(' Du vandt !')