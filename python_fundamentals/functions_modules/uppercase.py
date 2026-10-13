#!/usr/bin/env python3

def uppercase(str):
    resultado = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            resultado += chr(ord(c) - 32)
        else:
            resultado += c
    print(resultado)
