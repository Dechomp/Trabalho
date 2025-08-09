import random

def mediaAluno():
    notas = [0.0] * 4

    i = 0
    media = 0

    while i < 4:
        notas[i] = random.uniform(0.0 , 10.0)
        
        media += notas[i]
        i += 1
    
    media /= i

    return media