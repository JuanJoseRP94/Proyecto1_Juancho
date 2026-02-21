def create_win_features(df):
    """Función para calcular la diferencia de victorias"""
    df['redWins'] = 1 - df['blueWins']
    return df


def create_diff_features(df):
    """Calculamos la diferencia para varios objetivos al mismo tiempo"""
    df['killDiff'] = df['blueKills'] - df['redKills']
    df['dragonDiff'] = df['blueDragons'] - df['redDragons']
    df['heraldDiff'] = df['blueHeralds'] - df['redHeralds']
    df['eliteMonstersDiff'] = df['blueEliteMonsters'] - df['redEliteMonsters']
    return df


def create_dominance_score(df):
    """Puntuación de dominancia para cada equipo"""
    df['blueDominance'] = (
        df['blueKills'] +
        df['blueDragons'] * 2 +
        df['blueEliteMonsters'] * 3 +
        df['blueTowersDestroyed']
    )

    df['redDominance'] = (
        df['redKills'] +
        df['redDragons'] * 2 +
        df['redEliteMonsters'] * 3 +
        df['redTowersDestroyed']
    )

    return df

def add_gold_difference(df):
    """Añade la diferencia de oro como valor"""
    df['goldDiff'] = df['blueTotalGold'] - df['redTotalGold']
    return df

def add_kill_difference(df):
    """Añade la diferencia de asesinatos como valor"""
    df['killDiff'] = df['blueKills'] - df['redKills']
    return df