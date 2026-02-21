import os
import sys

# Permite importar desde src
sys.path.append(os.path.abspath("."))

from src.io import load_data
from src.features import (
    create_win_features,
    create_diff_features,
    create_dominance_score
)
from src.viz import (
    plot_team_comparison,
    plot_fill_between_diff,
    plot_3d_objectives,
    plot_dominance_score,
)


def main():

    # CARGA Y FEATURE ENGINEERING
    df = load_data("data/processed/datos_lol_limpio.csv")
    df = create_win_features(df)
    df = create_diff_features(df)
    df = create_dominance_score(df)

    print("Dataset cargado correctamente")
    print(f"Shape: {df.shape}")

    # COMPARACIONES BÁSICAS

    plot_team_comparison(
        df,
        'blueDragons',
        'redDragons',
        'Dragones promedio',
        'mean'
    )

    plot_team_comparison(
        df,
        'blueKills',
        'redKills',
        'Asesinatos promedio',
        'mean'
    )

    plot_team_comparison(
        df,
        'blueWins',
        'redWins',
        'Victorias totales',
        'sum'
    )

    # Diferencia acumulada de kills
    plot_fill_between_diff(df, 'killDiff', 'Kills')

    # Objetivos mayores en 3D
    plot_3d_objectives(df)

    # Score de dominancia
    plot_dominance_score(df)


if __name__ == "__main__":
    main()