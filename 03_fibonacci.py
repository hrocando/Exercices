### Reto de Programación Nro. 3 ###
### La Sucesión de Fibonacci  ###

# Origen:

primero = 0
segundo = 1

while primero + segundo <= 50:
    print(primero + segundo)
    
    tmp = primero
    primero = segundo
    segundo =+ tmp + primero