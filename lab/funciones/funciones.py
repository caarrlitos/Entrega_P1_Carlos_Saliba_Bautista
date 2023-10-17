'''
Created on 16 oct 2023

@author: csbpr
'''
#EJERCICIO 1
 
def primo(numero):
    return numero > 1 and all(numero % i for i in range(2, int(numero**0.5) + 1))

def main():
    numero = int(input("Ingresa un número entero: "))
    
    if primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
    
#EJERCICIO 2    
def factorial(num):
    if num == 0:
        return 1
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def coeficiente_binomial(n, k):
    if n < k:
        return 0  # Asegurarse de que n sea mayor o igual que k
    result = 1  # Inicializar result a 1
    for i in range(1, k + 1):
        result = (result * (n - k + i)) // i
    return result

#EJERCICIO 3
def expresion_3(n, k):
    if n >= k:
        solucion = 0
        
        for i in range(k+1):
            solucion += ((-1) ** i) * coeficiente_binomial(k, i) * (2 ** (k - i)) * factorial(k - i)
            
            return (1 /factorial(k)) * solucion
    else:
        return("n debe ser mayor a k para poder realizar la operación")

#EJERCICIO 4
def calcular_diferencias(lista):
    diferencias = []
    for i in range(1, len(lista)):
        diferencia = lista[i] - lista[i - 1]
        diferencias.append(diferencia)
    return diferencias

#EJERCICIO 5
def encontrar_cadena_mas_larga(lista_de_cadenas):
    if not lista_de_cadenas:
        return None  # Devolver None si la lista está vacía
    cadena_mas_larga = lista_de_cadenas[0]  # Inicializamos con la primera cadena
    for cadena in lista_de_cadenas:
        if len(cadena) > len(cadena_mas_larga):
            cadena_mas_larga = cadena
    return cadena_mas_larga

