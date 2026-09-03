from pathlib import Path

import pandas as pd

ARCHIVO_ACTUAL = Path(__file__).resolve()
RAIZ_REPO = ARCHIVO_ACTUAL.parents[2]
RUTA_DATOS = RAIZ_REPO / "data/nyc-taxi/green_tripdata_2026-03.parquet"
viajes = pd.read_parquet(RUTA_DATOS)

#1. Imprimir el numro de las filas y las columnas 
print("_N. Filas y cols_")
print(f"Filas: {viajes.shape[0]:,}")
print(f"Columnas: {viajes.shape[1]}")

#2.Signifiado de una fila
print("\n_Ejemplo de una fila_")
print(viajes.iloc[0])

#3.Columnas usadas para calcular "duración_minutos"
viajes["duracion_minutos"] = (viajes["lpep_dropoff_datetime"] - viajes["lpep_pickup_datetime"]).dt.total_seconds() / 60
print("\n_Duración de minutos, se contruye con: _")
print("lpep_pickup_datetime y lpep_dropoff_datetime")

#4.Cantidad y porcentajde de viajes con duración entre 1 y 60 minutos
mask_valida = viajes["duracion_minutos"].between(1, 60)
viajes_validos = viajes[mask_valida].copy()
n_validos = len(viajes_validos)
print("\n_Viajes con duración entre 1 y 60 min_")
print(f"Cantidad: {n_validos:,}")
print(f"Porcentaje: {n_validos / len(viajes) * 100:.2f}%")

#5. mínimo, mediana, promedio y máximo de `trip_distance` y `duracion_minutos` después del filtro
print("\n_Estadísticas (despues-de-filtro)_")
for col in ["trip_distance", "duracion_minutos"]:
    s = viajes_validos[col]
    print(f"{col} -> mín: {s.min():.2f}, mediana: {s.median():.2f}, "
          f"promedio: {s.mean():.2f}, máx: {s.max():.2f}")
    
#6.
