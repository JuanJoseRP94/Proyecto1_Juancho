def add_gold_difference(df):
    """Añade la diferencia de oro como valor"""
    df['goldDiff'] = df['blueTotalGold'] - df['redTotalGold']
    return df

def add_kill_difference(df):
    """Añade la diferencia de asesinatos como valor"""
    df['killDiff'] = df['blueKills'] - df['redKills']
    return df

def create_win_features(df):
    df['redWins'] = 1 - df['blueWins']
    return df