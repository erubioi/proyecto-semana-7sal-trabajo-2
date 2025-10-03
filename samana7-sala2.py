# Programa para calcular el promedio de notas de los 12 integrantes del grupo "Sala 2 Programación"
print("Bienvenido al programa de promedios para el grupo 'Sala 2 Programación'")
print("Se registrarán las notas de 12 integrantes (escala de 0 a 10).\n")
suma_notas = 0.0
nombres = []  # Lista para almacenar nombres (opcional, para mostrar al final)
notas = []    # Lista para almacenar notas (opcional)
for i in range(1, 13):
    nombre = input(f"Ingrese el nombre del integrante {i}: ").strip()
    nota = float(input(f"Ingrese la nota de {nombre} (0-10): "))
    
    nombres.append(nombre)
    notas.append(nota)
    suma_notas += nota
promedio = suma_notas / 12
# Mostrar resumen
print("\n--- Resumen de notas ---")
for i in range(12):
    print(f"{nombres[i]}: {notas[i]}")
print(f"\nPromedio general del grupo 'Sala 2 Programación': {promedio:.2f}/10")
