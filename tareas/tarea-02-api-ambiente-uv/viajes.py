#
def estimar_duracion(
    distancia_km: float, pasajeros: int, fin_de_semana: bool
) -> float:
    """Estima la duración de un viaje en minutos."""
    if distancia_km <= 0:
        raise ValueError("distancia_km debe ser un valor positivo")

    duracion = distancia_km * 4 + 2

    if pasajeros > 2:
        duracion += 3

    if fin_de_semana:
        duracion *= 0.9

    return round(duracion, 1)


def resumir_viajes(viajes: list[dict]) -> list[dict]:
    """Devuelve una copia de `viajes` agregando la duración estimada."""
    resumen = []
    for viaje in viajes:
        viaje_resumido = dict(viaje)
        viaje_resumido["duracion_estimada_min"] = estimar_duracion(
            distancia_km=viaje_resumido["distancia_km"],
            pasajeros=viaje_resumido["pasajeros"],
            fin_de_semana=viaje_resumido["fin_de_semana"],
        )
        resumen.append(viaje_resumido)
    return resumen


VIAJES: list[dict] = [
    {
        "origen": "Centro",
        "destino": "Chapultepec",
        "distancia_km": 3.2,
        "pasajeros": 1,
        "fin_de_semana": False,
    },
    {
        "origen": "ITESO",
        "destino": "Centro",
        "distancia_km": 12.5,
        "pasajeros": 3,
        "fin_de_semana": False,
    },
    {
        "origen": "Tlaquepaque",
        "destino": "Aeropuerto",
        "distancia_km": 15.8,
        "pasajeros": 2,
        "fin_de_semana": True,
    },
]