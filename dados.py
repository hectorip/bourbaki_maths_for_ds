import random

# Número de experimentos
experimentos = 1_000_000_000

# Contador para el número de veces que sale al menos un dos
exito = 0

for _ in range(experimentos):
    # Lanzamos dos dados (cada uno con valores del 1 al 6)
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    
    # Verificamos si al menos uno de los dados muestra 2
    if dado1 == 2 or dado2 == 2:
        exito += 1

# Calculamos la probabilidad experimental
probabilidad = exito / experimentos

print("Probabilidad experimental de obtener al menos un dos:", probabilidad)
print("Probabilidad teórica:", 11/36)