import os
import sys
from src.io import load_data
from src.features import create_win_features
from src.viz import plot_team_comparison

# Permite importar desde src
sys.path.append(os.path.abspath("."))

def main():
    # Cargar datos
    df = load_data("data/processed/datos_lol_limpio.csv")

    # Crear nuevas features
    df = create_win_features(df)

    print("Dataset cargado correctamente")
    print(f"Shape: {df.shape}")

    # Visualizaciones principales

    # Dragones
    plot_team_comparison(
        df,
        'blueDragons',
        'redDragons',
        'Dragones promedio',
        'mean'
    )

    # Asesinatos
    plot_team_comparison(
        df,
        'blueKills',
        'redKills',
        'Asesinatos promedio',
        'mean'
    )

    # Victorias
    plot_team_comparison(
        df,
        'blueWins',
        'redWins',
        'Victorias',
        'sum'
    )


if __name__ == "__main__":
    main()