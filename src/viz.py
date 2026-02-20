import matplotlib.pyplot as plt
import seaborn as sns


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