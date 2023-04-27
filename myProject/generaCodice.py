import random

caratteri = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def genera():
    codice = ''

    for x in range(20):
        codice+= random.choice(caratteri)

    return codice