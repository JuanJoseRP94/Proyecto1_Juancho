import os
import sys

# Permite importar desde src
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.io import load_data
from src.features import (
    create_win_features,
    create_diff_features,
    create_dominance_score
)
from src.viz import (
    plot_team_comparison,
    plot_fill_between_diff,
    plot_objectives_3d,   # <-- nombre correcto
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

    # DIFERENCIAS ACUMULADAS
    plot_fill_between_diff(df, 'killDiff', 'Kills')
    plot_fill_between_diff(df, 'dragonDiff', 'Dragones')
    plot_fill_between_diff(df, 'eliteMonstersDiff', 'Monstruos de élite')

    # OBJETIVOS EN 3D
    plot_objectives_3d(df)

    # Gráfico de dominancia por equipos
    plot_dominance_score(df)


if __name__ == "__main__":
    main()