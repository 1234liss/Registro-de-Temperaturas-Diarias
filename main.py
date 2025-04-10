import numpy as np

# Definir las ciudades, días de la semana y número de semanas
ciudades = ["Guayaquil", "Quito", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 4

# Crear la matriz 3D para almacenar las temperaturas
# La dimensión será (ciudades, semanas, días_semana)
temperaturas = np.random.randint(18, 32, size=(len(ciudades), num_semanas, len(dias_semana)))

# Calcular el promedio de temperaturas por ciudad y semana
promedios_por_ciudad_semana = {}

for i, ciudad in enumerate(ciudades):
    promedios_por_ciudad_semana[ciudad] = {}
    for j in range(num_semanas):
        total_temperatura_semana = 0
        for k in range(len(dias_semana)):
            total_temperatura_semana += temperaturas[i, j, k]
        promedio_semanal = total_temperatura_semana / len(dias_semana)
        promedios_por_ciudad_semana[ciudad][f"Semana {j+1}"] = f"{promedio_semanal:.2f} °C"

# Mostrar el promedio de temperaturas por ciudad y semana
print("Promedio de temperaturas por ciudad y semana:")
for ciudad, promedios_semanales in promedios_por_ciudad_semana.items():
    print(f"\nCiudad: {ciudad}")
    for semana, promedio in promedios_semanales.items():
        print(f"  {semana}: {promedio}")