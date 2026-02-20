import pandas as pd
import numpy as np

df = pd.read_csv('data/datos_lol_sucio.csv')

def remove_duplicates(df):
    """Elimina duplicados"""
    return df.drop_duplicates()


def handle_missing(df):
    """Maneja valores nulos"""
    df['blueTotalGold'] = df['blueTotalGold'].fillna(df['blueTotalGold'].mean())
    df['redKills'] = df['redKills'].fillna(df['redKills'].median())
    return df


def clip_outliers(df):
    """Corrige outliers"""
    # Nivel máximo 18
    df['blueAvgLevel'] = df['blueAvgLevel'].clip(upper=18)
    df['redAvgLevel'] = df['redAvgLevel'].clip(upper=18)

    # Dragones máximos en minuto 10: 2
    df['blueDragons'] = df['blueDragons'].clip(upper=2)
    df['redDragons'] = df['redDragons'].clip(upper=2)

    # Número más real para el oro
    gold_99 = df['blueTotalGold'].quantile(0.99)
    df['blueTotalGold'] = np.where(
    df['blueTotalGold'] > gold_99,
    gold_99,
    df['blueTotalGold']
)
    return df

df.to_csv('data/processed/datos_lol_limpio.csv', index=False)

print("Hemos corregido los errores. Los datos ya están limpios.")