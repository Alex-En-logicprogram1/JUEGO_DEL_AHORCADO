# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:50:02 2026

@author: Alex
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 18:20:06 2026

@author: Alex
"""

import random
import os

# Función para limpiar la pantalla (compatibilidad con Windows y Unix)
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función que muestra el dibujo del ahorcado según los intentos restantes
def mostrar_ahorcado(intentos_restantes):
    dibujos = [
        # Intentos 6 (inicio)
        """
           -----
           |   |
               |
               |
               |
               |
        =========""",
        # Intentos 5
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========""",
        # Intentos 4
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========""",
        # Intentos 3
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========""",
        # Intentos 2
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========""",
        # Intentos 1
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========""",
        # Intentos 0 (fin)
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ========="""
    ]
    print(dibujos[6 - intentos_restantes])

# Función principal del juego
def jugar_ahorcado():
    # Lista de palabras secretas (se puede ampliar según necesidad)
    palabras_secretas = ["python", "programacion", "ahorcado", "diagrama", "flujo", "computadora"]
    palabra_secreta = random.choice(palabras_secretas).lower()
    letras_adivinadas = []
    intentos_maximos = 6
    intentos_restantes = intentos_maximos
    palabra_oculta = ["_"] * len(palabra_secreta)

    limpiar_pantalla()
    print("¡Bienvenido al Juego del Ahorcado!")
    print(f"Palabra secreta: {' '.join(palabra_oculta)}")

    while intentos_restantes > 0 and "_" in palabra_oculta:
        print("\n" + "-" * 30)
        mostrar_ahorcado(intentos_restantes)
        print(f"\nPalabra: {' '.join(palabra_oculta)}")
        print(f"Intentos restantes: {intentos_restantes}")
        print(f"Letras adivinadas: {', '.join(letras_adivinadas) if letras_adivinadas else 'Ninguna'}")

        # Solicitar y validar letra del usuario
        while True:
            letra = input("\nIngresa una letra: ").lower()
            if len(letra) != 1:
                print("Por favor, ingresa solo una letra.")
            elif not letra.isalpha():
                print("Por favor, ingresa un carácter alfabético válido.")
            elif letra in letras_adivinadas:
                print(f"Ya has ingresado la letra '{letra}'. Prueba con otra.")
            else:
                break

        letras_adivinadas.append(letra)
        limpiar_pantalla()

        # Actualizar palabra oculta si la letra es correcta
        if letra in palabra_secreta:
            print(f"¡Muy bien! La letra '{letra}' está en la palabra.")
            for indice, caracter in enumerate(palabra_secreta):
                if caracter == letra:
                    palabra_oculta[indice] = letra
        else:
            print(f"Lo siento, la letra '{letra}' no está en la palabra.")
            intentos_restantes -= 1

    # Mostrar resultado final
    print("\n" + "-" * 30)
    mostrar_ahorcado(intentos_restantes)
    if "_" not in palabra_oculta:
        print(f"\n¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
    else:
        print(f"\n¡Has perdido! La palabra secreta era: {palabra_secreta}")

    # Preguntar si desea jugar de nuevo
    jugar_nuevamente = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_nuevamente == "s":
        jugar_ahorcado()
    else:
        print("\n¡Gracias por jugar! Hasta la próxima.")

# Ejecutar el juego
if __name__ == "__main__":
    jugar_ahorcado()