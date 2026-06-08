# Ejemplo de uso de la instrucción match en Python
# La instrucción match permite comparar el valor de una variable contra varios patrones, similar a switch en otros lenguajes.
# Este ejemplo muestra cómo usar match para identificar el tipo de día según un número.
# escribiendo desde gibhub

from typing import Match #

dia = int(input("Ingresa un número del 1 al 7 para el día de la semana: "))

match dia:
	case 1:
		print("Lunes: ¡Inicio de semana!")
	case 2:
		print("Martes: Segundo día de la semana.")
	case 3:
		print("Miércoles: Mitad de semana.")
	case 4:
		print("Jueves: Casi viernes.")
	case 5:
		print("Viernes: Fin de la semana laboral.")
	case 6 | 7:
		print("Fin de semana: ¡A descansar!")
	case _:
		print("Número no válido. Debe ser entre 1 y 7.")

# Explicación:
# - match dia: inicia la comparación del valor de 'dia'.
# - case 1: si dia es 1, ejecuta el bloque correspondiente.
# - case 6 | 7: si dia es 6 o 7, ejecuta ese bloque (fin de semana).
# - case _: es el caso por defecto, si ningún patrón anterior coincide.
