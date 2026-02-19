import pandas as pd
import numpy as np
from pathlib import Path


def find_input_file(root: Path, filename: str) -> Path:
    candidates = [root / 'data' / filename, root / 'data' / 'raw' / filename]
    for p in candidates:
        if p.exists():
            return p
    raise FileNotFoundError(
        f"No se encontró '{filename}'. Buscado en: {', '.join(str(x) for x in candidates)}"
    )


PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_NAME = 'datos_lol_crudo.csv'
OUT_NAME = 'datos_lol_sucio.csv'

input_path = find_input_file(PROJECT_ROOT, INPUT_NAME)

# Cargar dataset original
df = pd.read_csv(input_path)

# Introducción de valores nulos aleatorios en el oro del equipo azul
nan_indices_gold = np.random.choice(df.index, size=200, replace=False)
df.loc[nan_indices_gold, 'blueGold'] = np.nan

# Más valores nulos aleatorios en los asesinatos del equipo rojo
nan_indices_kills = np.random.choice(df.index, size=150, replace=False)
df.loc[nan_indices_kills, 'redKills'] = np.nan


# Outliers: Valores desorbitados
outlier_indices = np.random.choice(df.index, size=20, replace=False)
df.loc[outlier_indices, 'blueGold'] = 999999  # oro irreal

# Errores lógicos
df.loc[np.random.choice(df.index, 10, replace=False), 'blueDragons'] = 5  # imposible en 10 min
df.loc[np.random.choice(df.index, 10, replace=False), 'blueLevel'] = 25   # nivel > 18

# Duplicados
df_sucio = pd.concat([df, df.iloc[:50]])

# Guardar dataset sucio (asegurar que la carpeta exista)
output_path = PROJECT_ROOT / 'data' / OUT_NAME
output_path.parent.mkdir(parents=True, exist_ok=True)
df_sucio.to_csv(output_path, index=False)
print(f"Dataset sucio creado: {output_path}")
