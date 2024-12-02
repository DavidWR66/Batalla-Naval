import numpy as np

def crear_matriz(filas, columnas, valor_inicial=0):
    
    #Crea una matriz con el tamaño especificado y un valor inicial para todas las posiciones.
    
    return np.full((filas, columnas), valor_inicial)

def cambiar_valores(matriz, fila, columna, valor):
    
    #Define un valor en una posición específica de la matriz.
    
    if 0 <= fila < matriz.shape[0] and 0 <= columna < matriz.shape[1]:
        matriz[fila, columna] = valor
    else:
        raise IndexError("Índice fuera de rango.")

def sumar_valor(matriz, fila, columna, incremento=2): #funcion para atacar un barco

    if 0 <= fila < matriz.shape[0] and 0 <= columna < matriz.shape[1]:
        matriz[fila, columna] += incremento
    else:
        raise IndexError("Índice fuera de rango.")

# Ejemplo de uso
# Crear una matriz de 5x5 con valores iniciales de 0
matriz_n = crear_matriz(4, 4, valor_inicial=0)

# Definir algunos valores específicos
cambiar_valores(matriz_n, 2, 2, 1) #Cabiamos los valores de algunas celdas por 1
cambiar_valores(matriz_n, 2, 3, 1) #Los 0 representan espacios vacios, los 1 representan a los barcos
cambiar_valores(matriz_n, 2, 4, 1) #Los 2 representan espacios vacios que ya se impactactaron y los 3 son barcos impactados   



#ejemplo de como atacar un barco

while True:
    print(matriz_n)
    try:
        fila = int(input("Ingrese el índice de la fila (0 a 5): "))
        columna = int(input("Ingrese el índice de la columna (0 a 5): "))

        if matriz_n[fila,columna]<=1:
            sumar_valor(matriz_n, fila, columna, incremento=2)

            print("\nSe ha actualizado la matriz:")
            
    except ValueError:
        print("Por favor, ingrese un número válido.")
    except IndexError:
        print("Índice fuera de rango. Intente de nuevo.")
    
    # Preguntar si desea continuar
    continuar = input("¿Desea seleccionar otra celda? (s/n): ").lower()
    if continuar != 's':
        break