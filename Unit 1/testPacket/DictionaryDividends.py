"""
    Definir un diccionario para un numero dado y su conjunto de divisores
"""
user_input = int(input("Introduce the number you wish to add with its dividends: "))
dictionary = {}

def divisors(number):
    return tuple(i for i in range(1, number+1) if not number % i)
    
while user_input != 0:
    dictionary.update({ user_input: divisors(user_input) })
    user_input = int(input("Do you wish to introduce another number's divisors? To exit introduce 0: "))

print(dictionary)
