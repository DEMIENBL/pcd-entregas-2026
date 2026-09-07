## Tarea

* Número y nombre: Tarea 3 — Comparación de dos modelos servidos por una API
* Ruta del entregable: tareas/tarea-03-api-prediccion/

## Qué realicé
Entrené dos pipelines con la misma preparación y las mismas 5 features
(distancia_km, pasajeros, hora_recoleccion, zona_origen, zona_destino) sobre
marzo de 2026, validados contra abril: una regresión lineal y un bosque
aleatorio (RandomForestRegressor, n_estimators=100, max_depth=12,
min_samples_leaf=5). Ambos comparten el mismo ColumnTransformer
(OneHotEncoder para zonas, passthrough para el resto). Expuse ambos modelos
en una API FastAPI que carga los dos artefactos una sola vez al iniciar.

## Cómo lo verifiqué
```bash
uv run python entrenar_modelo_lineal.py
uv run python entrenar_modelo_bosque.py
uv run fastapi dev
```
Probé ambos endpoints con [Postman / curl / /docs] y validé dos errores de
contrato: hora_recoleccion fuera de rango (422) y ausencia de zona_destino (422).

## Comparación

| Modelo | RMSE en abril (min) | Entrenamiento (s) | Tamaño del .pkl (MiB) |
|---|---|---|---|
| Regresión lineal | 5.11 | 0.48 | 0.01 |
| Bosque aleatorio | 4.52 | 10.59 | 10.80 |

El bosque aleatorio obtuvo menor RMSE (4.52 min vs 5.11 min), por lo que en promedio se equivoca menos por viaje que la regresión lineal. A cambio, tardó más de 20 veces más en entrenar (10.59 s vs 0.48 s) y su artefacto pesa 10.80 MiB frente a apenas 0.01 MiB de la regresión lineal, mil veces más grande. Para este ejercicio elegiría [la regresión lineal si priorizas velocidad/tamaño y el error extra es aceptable, o el bosque si priorizas precisión y el costo de entrenamiento/almacenamiento no es un problema] — Diria que en producción vale más la pena para mi ser más precisos, a final de cuentas nuestro trabajo es obtener esas predicciones, y yo me atrevería a sacrificar esa velocidad por precisión.

Ventajas de servir modelos con pickles locales: no depende de infraestructura externa ni de latencia de red, y la inferencia es prácticamente instantánea una vez cargado en memoria.
Limitaciones: el pickle está atado a la versión exacta de scikit-learn con la que se entrenó (puede fallar al cargar en otro entorno), no hay versionado ni rollback automático si el modelo se corrompe o queda obsleto, y rentrenar exige acceso manual al mismo servidor donde vive el artefacto.

## Evidencia
- [Predicción lineal (200)](evidencia/prediccion-lineal-200.png)
- [Predicción bosque (200)](evidencia/prediccion-bosque-200.png)
- [Validación hora_recoleccion (422)](evidencia/validacion-hora-422.png)
- [Validación zona_destino faltante (422)](evidencia/validacion-zona-422.png)

## Checklist
- [x] Trabajé en la rama indicada y el PR apunta a `main`.
- [x] El entregable está en la carpeta solicitada.
- [x] Revisé todos los archivos en Files changed.
- [x] Mi rama y mis commits siguen las convenciones indicadas para esta tarea.
- [x] No incluí credenciales, datos privados, soluciones ajenas ni archivos accidentales.
- [x] Completé todos los requisitos particulares de la tarea.
- [x] Revisé mi trabajo contra la rúbrica antes de fusionar.
- [x] Después de esta revisión, fusionaré el PR y confirmaré que aparezca como Merged y cerrado antes de entregar en Canvas.