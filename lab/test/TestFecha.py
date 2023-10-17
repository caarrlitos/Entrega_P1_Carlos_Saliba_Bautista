'''
Created on 17 oct 2023

@author: csbpr
'''
from __future__ import annotations
from lab.tipos.fecha import Fecha

#MÉTODO SUMAR DÍAS
def test_sumar_dias():
    print("test_sumar_dias:")
    fecha1 = Fecha.of(2023, 8, 15)
    fecha2 = fecha1.sumar_dias(121)
    print(f"{Fecha.dia_semana(fecha1.año, fecha1.mes, fecha1.dia)} {fecha1.dia} de {fecha1.nombre_mes} del {fecha1.año} + 121 días: {Fecha.dia_semana(fecha2.año, fecha2.mes, fecha2.dia)} {fecha2.dia} de {fecha2.nombre_mes} del {fecha2.año}")

    date1 = Fecha.of(2023, 8, 15)  # Usando la clase Fecha de tu paquete
    date2 = date1.sumar_dias(121)  # Llamar al método sumar_días de la clase Fecha
    print(f"{date1} + 121 días: {date2}")

if __name__ == '__main__':
    test_sumar_dias()
    
#RESTO DE DIAS
mi_fecha1 = Fecha(2023, 10, 17)
print(f"El nombre del mes es: {mi_fecha1.nombre_mes}")

mi_fecha2 = mi_fecha1.sumar_dias(5)
print(f"Fecha después de sumar 5 días: {mi_fecha2.año}-{mi_fecha2.mes}-{mi_fecha2.dia}")

mi_fecha3 = mi_fecha1.restar_dias(3)
print(f"Fecha después de restar 3 días: {mi_fecha3.año}-{mi_fecha3.mes}-{mi_fecha3.dia}")

fecha4 = Fecha(2023, 11, 1)
diferencia = mi_fecha1.diferencia_en_dias(fecha4)
print(f"Diferencia en días entre las dos fechas: {diferencia} días")

fecha_str = "2023-12-25"
mi_fecha5 = Fecha.parse(fecha_str)
print(f"Fecha parseada desde una cadena: {mi_fecha5.año}-{mi_fecha5.mes}-{mi_fecha5.dia}")

print(f"¿2024 es año bisiesto? {Fecha.es_año_bisiesto(2024)}")

print(f"Días en el mes de noviembre 2023: {Fecha.dias_en_mes(2023, 11)}")

print(f"Día de la semana para el 17 de octubre de 2023: {Fecha.dia_semana(2023, 10, 17)}")