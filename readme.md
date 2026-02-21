# Proyecto 1 Juancho Romero

## Objetivo:
### Trabajar con datos de league of legends para comprobar qué impacto tiene un equipo u otro en diferentes escenarios.

### Dataset:
[Link del dataset elegido:] (https://www.kaggle.com/datasets/bobbyscience/league-of-legends-diamond-ranked-games-10-min/data)
Nº Filas: 4.527.990.640
Nº Columnas: 40
Variables clave:  
**Tótem guardián**: Un objeto que un jugador puede colocar en el mapa para revelar el área cercana.  
**Esbirros**: PNJ que pertenecen a ambos equipos. Otorgan oro al ser eliminados por jugadores.  
**Esbirros de la jungla**: PNJ que no pertenecen a ningún equipo. Otorgan oro y beneficios al ser eliminados por jugadores.  
**Monstruos de élite**: Monstruos con altos puntos de vida/daño que otorgan una gran bonificación (oro/EXP/estadísticas) al ser eliminados por un equipo.  
**Dragones**: Monstruo de élite que otorga una bonificación de equipo al ser eliminado. El cuarto dragón eliminado por un equipo otorga una enorme bonificación de estadísticas. El quinto dragón (Dragón Anciano) ofrece una gran ventaja al equipo.  
**Heraldo**: Monstruo de élite que otorga bonificación de estadísticas al ser eliminado por el jugador.  
**Torres**: Estructuras que debes destruir para alcanzar el Nexo enemigo. Otorgan oro.  
**Nivel**: Campeón. Empieza en 1. Máximo 18.  

---

**Preguntas interesantes:**

**¿Cuanto oro se consigue de promedio en los 10 primeros minutos?** (histograma o boxplot)

**¿Tener más oro implica mayor probabilidad de victoria? O ¿El equipo ganador suele tener más oro que el perdedor?**(Barplot / Lineplot)

**¿Tener más asesinatos implica mayor oro en la partida?**(Barplot)

**¿Qué equipo suele hacer más objetivos? ¿Y cuales?**(Heatmap)

### Problemas dataset y reparaciones

**1º: El dataset venía extremadamente limpio ->** tuve que crear un archivo "dirty.py" que pudiera ensuciar el código artificialmente. Le añadí valores nulos, valores desorbitados, errores lógicos, etc.

**2º: Limpieza del dataset ->** Al tener sucio el dataset tuve que crear métodos para limpiarlos, y eso hice en el archivo "cleaning.py" eliminando los valores nulos y los demás problemas que llevaba el dataset.

**3º El dataset mostraba solo victorias del equipo azul(si perdia se consideraba victoria de equipo rojo) pero eso hacía muy dificil comparar ambos equipos ->** Decidí crear un features para añadir la columna "redWins", además de otras columnas adicionales como "dragonDiff", "eliteMonstersDiff" etc y asi poder comparar mejor a ambos equipos.

### Pipeline
data/raw/        → Datos originales
src/dirty.py     → Ensuciar (simulación de errores)
src/cleaning.py  → Limpieza
notebooks/eda.ipynb → Análisis
README.md        → Explicación del proceso

### Hallazgos

- **Insight 1:** *Se obtiene con más frecuencia un término medio de oro entre 15000 y 17000*(ver Gráfico 1).

- **Insight 2:** *A mayor oro -> Mayor probabilidad de victoria* (ver Gráfico 2).

- **Insight 3:** *El equipo rojo suele tener una mejor puntuación de objetivos frente a azul, pero la probabilidad de victoria de ambos equipos está muy pareja* (ver los últimos 5 gráficos).

### Estructura del proyecto

- `data/`
  - `raw/` contiene los datos originales.
  - `processed/` contiene los datos limpios generados por el pipeline.

- `src/`
  Contiene funciones reutilizables organizadas por responsabilidad:
  - `io.py` → funciones de carga y guardado.
  - `cleaning.py` → limpieza y validación de datos.
  - `features.py` → creación de nuevas variables.
  - `viz.py` → funciones de visualización.

- `notebooks/`
  - `eda.ipynb` contiene el análisis exploratorio.

- `main.py`
  Ejecuta el pipeline completo de forma end-to-end.

### Cómo ejecutar

1. Clonar el repositorio:

   git clone <url-del-repo>
   cd Proyecto1_Juancho

2. Crear entorno virtual:

   python -m venv .venv
   .venv\Scripts\activate   (Windows)

3. Instalar dependencias:

   pip install -r requirements.txt

4. Ejecutar el pipeline completo:

   python main.py

5. Abrir el análisis exploratorio:

   jupyter notebook notebooks/eda.ipynb