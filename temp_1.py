'''
Temp. konverter
Konvertere temp fra Celius til Fahrenheit, Reaumur og Kelvin, med 1 decimal.
'''

# konverter fra Celsius til Fahrenheit
def c_til_f(c):
    fahrenheit = c * 1.8 + 32
    streng =  '{:0.1f}{} Fahrenheit, eller '.format( fahrenheit, u'\N{DEGREE SIGN}' )
    return streng

# Konverter fra Celsius til Reaumur
def c_til_r(c):
    reaumur = c * 0.8
    print('{:0.1f}'.format(reaumur), u'\N{DEGREE SIGN}Reaumur, eller ')
    
# Konverter fra Celsius til Kelvin
def c_til_k(c):
    kelvin = c + 273
    print('{:0.1f}'.format(kelvin), u'\N{DEGREE SIGN}Kelvin')
    
# Spørg efter temperatur der skal konverteres
c = float(input('Intast grader i celcius : '))
print()
print('********************')
print((c), u'\N{DEGREE SIGN}Celsius er ')
s = c_til_f(c)
print(s)
c_til_r(c)
c_til_k(c)
print('********************')

