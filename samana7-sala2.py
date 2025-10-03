# Programa para calcular el promedio de notas de los 13 integrantes del grupo "Sala 2 Programación"
print("Bienvenido al programa de promedios para el grupo 'Sala 2 Programación'")
print("Se registrarán las notas de 13 integrantes (escala de 0 a 10).\n")
suma_notas = 0.0
nombres = []  # Lista para almacenar nombres (opcional, para mostrar al final)
notas = []    # Lista para almacenar notas (opcional)
for i in range(1, 14):  # Cambiado de 13 a 14 para incluir 13 personas
    nombre = input(f"Ingrese el nombre del integrante {i}: ").strip()
    nota = float(input(f"Ingrese la nota de {nombre} (0-10): "))
    
    nombres.append(nombre)
    notas.append(nota)
    suma_notas += nota
promedio = suma_notas / 13  # Cambiado de 12 a 13
# Mostrar resumen
print("\n--- Resumen de notas ---")
for i in range(13):  # Cambiado de 12 a 13
    print(f"{nombres[i]}: {notas[i]}")
print(f"\nPromedio general del grupo 'Sala 2 Programación': {promedio:.2f}/10")

