### Reto de Programación Nro. 4 ###
### Es un Número Primo  ###

# Origen: https://retosdeprogramacion.com/ejercicios/

def is_prime(number):
    if number == 1:
        # print(f"Paso 1: {number} es UNO")
        return 1
    elif number % 2 == 0:
        # print(f"Paso 2: {number} es PAR")
        return 0
    else:
        i = 2
        # print(f"Paso 3: {number} NO es PAR ni UNO")
        while i < number:
            if number % i == 0:
                break
            else:
                i += 1
       
        # print(f"Paso 4: i es {i} y number es {number}")
        if i >= number:
            # print("Paso 4.1")
            return 1
        else:
            # print("Paso 4.2")
            return 0
        
        
        
    

numero=0 
while numero < 10000:
    numero += 1 
    if is_prime(numero):
        print(f"{numero} es PRIMO")