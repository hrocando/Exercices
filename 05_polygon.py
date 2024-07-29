### Reto de Programación Nro. 5 ###
### Area de un Poligono ###

# Origen: https://retosdeprogramacion.com/ejercicios/

# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.


import math


def area(poligono, m1, m2):
    if poligono == 'CIR':
        return m1 + math.pi
    elif poligono == 'TRI':
        return m1 * m2 / 2
    elif poligono == 'CUA':
        return m1 * m2
    else:
        return 0

radio = 2
base = 3
altura = 4

print(f"El área del circulo de radio {radio} es {area('CIR', radio, 0)}")
print(f"El área del tringulo de base {base} y altura {altura} es {area('TRI', base, altura)}")
print(f"El área del cuadrado de base {base} y altura {altura} es {area('CUA', base, altura)}")