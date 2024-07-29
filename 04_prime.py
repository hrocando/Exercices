### Reto de Programación Nro. 4 ###
### Es un Número Primo  ###

# Origen: https://retosdeprogramacion.com/ejercicios/

def is_prime_v1(number):
    if number == 1:
        return True
    elif number % 2 == 0:
        return False
    else:
        i = 2
        while i < number:
            if number % i == 0:
                break
            else:
                i += 1
       
        if i >= number:
            return True
        else:
            return False

def is_prime_v2(number):
    if number < 2:
        return False
    else:
        counter = 1
        while counter < number:
            if number % counter == 0:
                return False
                break
            else:
                counter += 1            
        return True

        
numero = 0 
while numero < 100:
    numero += 1 
    if is_prime_v1(numero):
        print(f"{numero}")