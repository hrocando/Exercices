### Reto de Programación Nro. 2 ###
### Anagram ###

# Origen: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge1.kt

def are_anagram(first_word: str, second_word: str):
    second_word = second_word[::-1]
    
    if first_word == second_word:
        return True
    else:
        return False

primera, segunda = "arroz", "zorra"

if are_anagram(primera, segunda):
    print(f' ATENCION: {primera} y {segunda} si son Anagrama')
else:
    print(f' ATENCION: {primera} y {segunda} no son Anagrama')