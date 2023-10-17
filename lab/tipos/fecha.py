'''
Created on 17 oct 2023

@author: csbpr
'''
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass(frozen=True, order=True)
class Fecha:
    # Lista auxiliar con los nombres de los doce meses
    nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    año: int
    mes: int
    dia: int
    
    def __str__(self):
        return f"{self.año}-{self.mes:02d}-{self.dia:02d}"

    @property
    def nombre_mes(self):
        return self.nombres_meses[self.mes - 1]

    def sumar_dias(self, dias):
        fecha_actual = datetime(self.año, self.mes, self.dia)
        fecha_nueva = fecha_actual + timedelta(days=dias)
        return Fecha(fecha_nueva.year, fecha_nueva.month, fecha_nueva.day)

    def restar_dias(self, dias):
        fecha_actual = datetime(self.año, self.mes, self.dia)
        fecha_nueva = fecha_actual - timedelta(days=dias)
        return Fecha(fecha_nueva.year, fecha_nueva.month, fecha_nueva.day)

    def diferencia_en_dias(self, otra_fecha):
        fecha1 = datetime(self.año, self.mes, self.dia)
        fecha2 = datetime(otra_fecha.año, otra_fecha.mes, otra_fecha.dia)
        diferencia = fecha2 - fecha1
        return diferencia.days

    @staticmethod
    def of(año, mes, dia):
        return Fecha(año, mes, dia)

    @staticmethod
    def parse(fecha_str):
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        return Fecha(fecha.year, fecha.month, fecha.day)

    @staticmethod
    def es_año_bisiesto(año):
        return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

    @staticmethod
    def dias_en_mes(año, mes):
        if mes == 2:
            return 29 if Fecha.es_año_bisiesto(año) else 28
        elif mes in [4, 6, 9, 11]:
            return 30
        else:
            return 31

    @staticmethod
    def dia_semana(año, mes, dia):
        if mes < 3:
            mes += 12
            año -= 1
        k = año % 100
        j = año // 100
        h = (dia + 13 * (mes + 1) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
        dias_semana = ["Sábado", "Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        return dias_semana[h]
