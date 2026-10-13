#!/usr/bin/env python3

def uppercase(str):
    resultado = ""
    for c in str:
        # Si el carácter es una minúscula, lo convertimos a mayúscula restando 32
        if ord('a') <= ord(c) <= ord('z'):
            resultado += chr(ord(c) - 32)
        else:
            resultado += c
    print(resultado)
