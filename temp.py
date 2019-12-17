
#konverter fra Celsius til Fahrenheit
def c_til_f(c):
    fahrenheit = c * 1.8 + 32
    print('{:0.2f}'.format(fahrenheit),''+ u'\u2103')
'''
#konverter fra Fahrenheit til Celsius
def f_til_c(f):
   # t = u'\N{DEGREE SIGN}' 
    celsius = (f - 32) / 1.8
    print('{:0.2f}'.format(celsius),''+u'\u2103')
'''


c = float(input('Intast grader i celcius : '))
#f = float(input('Intast grader i fahrenheit: '))
c_til_f(c)
#f_til_c(f)


'''
#grd = u'\N{DEGREE SIGN}'
print('Hej Per '+ u'\u2103')

print("Det er 20 "+u'\u2103'+" i min stue ")
'''