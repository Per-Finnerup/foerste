def adder(tal1, tal2):
    res = tal1 + tal2
    print(res)

def subtraher(tal1, tal2):
    res = tal1 - tal2
    print(res)
    
def multiplicer(tal1, tal2):
    res = tal1 * tal2
    print(res)

def dele(tal1, tal2):
    res = tal1 / tal2
    print('{0:.2f}'.format(res))

tal1 = int(input('Intast et tal: '))
tal2 = int(input('Intast et tal: '))

adder(tal1, tal2)
subtraher(tal1, tal2)
multiplicer(tal1, tal2)
dele(tal1, tal2)