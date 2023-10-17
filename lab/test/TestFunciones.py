'''
Created on 16 oct 2023

@author: csbpr
'''
from lab.funciones.funciones import expresion_3, main, coeficiente_binomial, calcular_diferencias, encontrar_cadena_mas_larga
#EJERCICIO 1
if __name__ == "__main__":
    main()

#EJERCICIO 2
n = 5
k = 2
resultado = coeficiente_binomial(n, k)
print(f"C({n}, {k}) = {resultado}")

#EJERCICIO 3
n = int(input("Ingresa el valor de n: "))
k = int(input("Ingresa el valor de k: "))
solucion = expresion_3(n, k)
print("El resultado de expresion_3({}, {}) es: {}".format(n, k, solucion))

#EJERCICIO 4
lista_de_numeros = [1, 5, 7, 10, 15]
resultado = calcular_diferencias(lista_de_numeros)
print(f"Las diferencias de la lista son {resultado}")

#EJERCICIO 5
lista_de_cadenas = ["gato", "perro", "elefante", "ratón", "ballena"]
cadena_mas_larga = encontrar_cadena_mas_larga(lista_de_cadenas)
print(f'La cadena más larga es {cadena_mas_larga}')