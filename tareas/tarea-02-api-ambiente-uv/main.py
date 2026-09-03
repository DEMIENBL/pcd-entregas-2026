from fastapi import FastAPI

from viajes import VIAJES, estimar_duracion, resumir_viajes

app = FastAPI(title="API local de viajes")


@app.get("/")
def raiz() -> dict:
    return {"mensaje": "API local de viajes en Guadalajara"}


@app.get("/api/v1/viajes")
def obtener_viajes() -> dict:
    return {"viajes": resumir_viajes(VIAJES)}


@app.get("/api/v1/duracion/{distancia_km}")
def obtener_duracion(
    distancia_km: float, pasajeros: int = 1, fin_de_semana: bool = False
) -> dict:
    duracion = estimar_duracion(distancia_km, pasajeros, fin_de_semana)
    return {
        "distancia_km": distancia_km,
        "pasajeros": pasajeros,
        "fin_de_semana": fin_de_semana,
        "duracion_estimada_min": duracion,
    }