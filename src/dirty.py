import pandas as pd
import numpy as np

# Cargar dataset original
df = pd.read_csv('data/raw/datos_lol_crudo.csv')

# Introducción de valores nulos aleatorios en el oro del equipo azul
nan_indices_gold = np.random.choice(df.index, size=200, replace=False)
df.loc[nan_indices_gold, 'blueTotalGold'] = np.nan

# Más valores nulos aleatorios en los asesinatos del equipo rojo
nan_indices_kills = np.random.choice(df.index, size=150, replace=False)
df.loc[nan_indices_kills, 'redKills'] = np.nan

# Outliers: Valores desorbitados
outlier_indices = np.random.choice(df.index, size=20, replace=False)
df.loc[outlier_indices, 'blueTotalGold'] = 999999  # oro irreal

# Errores lógicos
df.loc[np.random.choice(df.index, 10, replace=False), 'blueDragons'] = 5  # imposible en 10 min
df.loc[np.random.choice(df.index, 10, replace=False), 'blueAvgLevel'] = 25   # nivel > 18

# Duplicados
df_sucio = pd.concat([df, df.iloc[:50]])

# Guardar dataset sucio
df_sucio.to_csv('data/datos_lol_sucio.csv', index=False)
print("Oh, no! Los datos han sido alterados! Debemos limpiarlos!")
