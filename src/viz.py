import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def plot_gold_distribution(df):
    """
    Distribución del oro en el equipo azul
    """
    plt.figure(figsize=(8, 5))
    sns.histplot(df['blueTotalGold'], kde=True)
    plt.title("Distribución del Oro Total - Equipo Azul")
    plt.xlabel("Oro total")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()


def plot_gold_vs_win(df):
    """
    Oro total agrupado por victoria
    """
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='blueWins', y='blueTotalGold', data=df)
    plt.title("Oro Total vs Victoria")
    plt.xlabel("Victoria del equipo azul (0 = No, 1 = Sí)")
    plt.ylabel("Oro total")
    plt.tight_layout()
    plt.show()

def plot_pivot_heatmap(df, index_col, columns_col, value_col, aggfunc='mean', cmap='viridis', annot=False):
    """
    Genera un heatmap a partir de un pivot table (estilo moderno, cmap progresivo).
    
    Parametros:
        df (pd.DataFrame): DataFrame con los datos.
        index_col (str): Columna que irá en las filas del heatmap.
        columns_col (str): Columna que irá en las columnas del heatmap.
        value_col (str): Columna cuyos valores se agregan.
        aggfunc (str or function): Función de agregación ('mean', 'sum', etc.)
        cmap (str): Paleta de colores
        annot (bool): Mostrar números en los cuadrados (Por defecto no: False)
    """
    # Crear pivot table
    pivot = df.pivot_table(index=index_col, columns=columns_col, values=value_col, aggfunc=aggfunc)
    
    plt.figure(figsize=(8,5))
    sns.heatmap(pivot, cmap=cmap, annot=annot)
    plt.title(f"Heatmap: {value_col} ({index_col} × {columns_col})")
    plt.xlabel(columns_col)
    plt.ylabel(index_col)
    plt.tight_layout()
    plt.show()

def plot_team_comparison(df, blue_col, red_col, metric_name, aggfunc='mean'):
    """
    Grafica comparación directa Azul vs Rojo mediante barras.
    
    Parameters:
        df (pd.DataFrame): Dataset.
        blue_col (str): Columna del equipo azul.
        red_col (str): Columna del equipo rojo.
        metric_name (str): Nombre legible de la métrica.
        aggfunc (str): 'mean' o 'sum'.
    """
    
    if aggfunc == 'mean':
        blue_value = df[blue_col].mean()
        red_value = df[red_col].mean()
    elif aggfunc == 'sum':
        blue_value = df[blue_col].sum()
        red_value = df[red_col].sum()
    else:
        raise ValueError("aggfunc debe ser 'mean' o 'sum'")
    
    values = [blue_value, red_value]
    teams = ['Azul', 'Rojo']
    
    plt.figure(figsize=(6,4))
    bars = plt.bar(teams, values)
    
    # Colores manuales
    bars[0].set_color('blue')
    bars[1].set_color('red')
    
    plt.title(f"Comparación de {metric_name}: Azul vs Rojo")
    plt.ylabel(metric_name)
    plt.tight_layout()
    plt.show()

def plot_fill_between_diff(df, diff_column, title):
    """Diferencia entre diferentes columnas en varias partidas"""

    cumulative = df[diff_column].cumsum()

    plt.figure()
    x = np.arange(len(cumulative))

    plt.fill_between( # Esto determina el color de la gráfica
        # si está en positivo se colorea en azul, si es negativo en rojo.
        x,
        cumulative,
        where=(cumulative >= 0),
        color='blue',
        alpha=0.6
    )
    plt.fill_between(
        x,
        cumulative,
        where=(cumulative < 0),
        color='red', # Aqui colocamos color rojo cuando domina este equipo.
        alpha=0.6
    )

    plt.title(f'Diferencia acumulada de {title}')
    plt.xlabel('Partidas')
    plt.ylabel('Diferencia acumulada')
    plt.plot([], [], color='blue', label='Ventaja Blue')
    plt.plot([], [], color='red', label='Ventaja Red')
    plt.legend()
    plt.show()


def plot_objectives_3d(df):
    """Comparación en 3D de diferentes objetivos en la partida y su impacto en ella."""
    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(projection='3d')

    objectives = ['Dragons', 'Heralds', 'Elite Monsters']
    blue_means = [
        df['blueDragons'].mean(),
        df['blueHeralds'].mean(),
        df['blueEliteMonsters'].mean()
    ]
    red_means = [
        df['redDragons'].mean(),
        df['redHeralds'].mean(),
        df['redEliteMonsters'].mean()
    ]

    xpos = np.arange(len(objectives))
    zpos = np.zeros(len(objectives))

    dx = dy = 0.3  # reduce tamaño para que no se solapen ya que se tapan unas a otras

    # Barras azules un poco adelantadas en y
    ypos_blue = np.zeros(len(objectives))
    ax.bar3d(xpos, ypos_blue, zpos, dx, dy, blue_means, color='blue', alpha=0.7, label='Blue')

    # Barras rojas desplazadas para que no se tapen
    ypos_red = ypos_blue + dy + 0.05  # pequeño offset
    ax.bar3d(xpos, ypos_red, zpos, dx, dy, red_means, color='red', alpha=0.7, label='Red')

    # Ajuste ticks
    ax.set_xticks(xpos + dx/2)
    ax.set_xticklabels(objectives)
    ax.set_yticks([0.0, 0.45])  # aproximado según desplazamiento
    ax.set_yticklabels(['Blue', 'Red'])

    ax.set_zlabel('Media')
    ax.set_title('Comparación 3D de objetivos mayores')

    # Rotar vista para ver mejor las barras
    ax.view_init(elev=23, azim=60)

    plt.show()

def plot_dominance_score(df):
    """Dominancia promedio por equipo"""

    blue_mean = df['blueDominance'].mean()
    red_mean = df['redDominance'].mean()

    plt.figure()
    plt.bar(['Blue', 'Red'], [blue_mean, red_mean])

    plt.title('Dominancia promedio por equipo')
    plt.ylabel('Score de dominancia')

    plt.show()