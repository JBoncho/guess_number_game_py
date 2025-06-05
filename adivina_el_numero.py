# Juego adivinanza, generar un número del 1 al 100 y el usuario debe ir adivinándolo, el programa le debe decir si es mayor o menor

import random


def number_guess_game():
    secret_number = random.randint(1, 100)
    tries = 0
    condition_to_wim = False

    # Bienvenida al juego
    print("¡Bienvenid@ al juego 'adivinan el número'!")
    print("Debes adivinar un número entre el 1 y el 100")
    print("¡Inténtalo!")

    while not condition_to_wim:
        # Pedir el número
        number_guess = input("Introduce un número del 1 al 100: ")

        # Castear el número a entero
        if number_guess.isdigit():
            number_guess = int(number_guess)
            tries += 1

            if number_guess < secret_number:
                print(f"El número secreto es mayor que {number_guess}, inténtalo de nuevo.")
            elif number_guess > secret_number:
                print(f"El número secreto es menor que {number_guess}, inténtalo de nuevo.")
            else:
                print(f"¡Felicitaciones!, has adivinado el número {secret_number} en {tries} intentos")
                condition_to_wim = True

        else:
            print("Por favor, introduce un número entero entre 1 y 100")


number_guess_game()