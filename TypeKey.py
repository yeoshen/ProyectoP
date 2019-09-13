from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(2)

texto = "Esta es una secuencia de comandos escritas por python!!!\ntodo se simplifica con un modulo al importarse."

keyboard.type(texto)

"""for char in texto.upper():
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.12)
"""
