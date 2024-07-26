### Reto de Programación Nro. 1 ###
### Fizz Buzz ###

# Origen: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge0.kt

counter = 1

while  counter <= 100:
    if counter % 3 == 0 and counter % 5 == 0:
        print(f"El contador vale {counter} --> fizzbuzz")
    elif counter % 3 == 0:
        print(f"El contador vale {counter} --> fizz")
    elif counter % 5 == 0:
        print(f"El contador vale {counter} --> buzz")
    counter += 1