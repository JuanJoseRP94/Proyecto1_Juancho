import pandas as pd
import numpy as np

df = pd.read_csv('data/datos_lol_sucio.csv')

# Eliminar duplicados
df = df.drop_duplicates()

# Manejar valores nulos
df['blueTotalGold'] = df['blueTotalGold'].fillna(df['blueTotalGold'].mean())
df['redKills'] = df['redKills'].fillna(df['redKills'].median())

# Corregir outliers (Nivel máximo 18)
df['blueAvgLevel'] = df['blueAvgLevel'].clip(upper=18)
df['redAvgLevel'] = df['redAvgLevel'].clip(upper=18)
# Dragones máximos en minuto 10: 2
df['blueDragons'] = df['blueDragons'].clip(upper=2)
df['redDragons'] = df['redDragons'].clip(upper=2)

gold_99 = df['blueTotalGold'].quantile(0.99)
df['blueTotalGold'] = np.where(
    df['blueTotalGold'] > gold_99,
    gold_99,
    df['blueTotalGold']
)

df.to_csv('data/processed/datos_lol_limpio.csv', index=False)

print("Hemos corregido los errores. Los datos ya están limpios.")

