from datetime import date
pi = 3.1416
print(date.today().strftime('Hoy es %d de %b del %Y'))
print('Inserte el radio del circulo para calcular el area:')
radius = input("Radio: ")

print('El area es : ' + str( float(radius) * float(radius) * pi))
