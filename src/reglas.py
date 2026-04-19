def regla_monto_alto (df):
    return df['monto'] > 2000

def regla_frecuencia (df):
    return df['tx_por_hora'] > 50

def regla_horario_inusual(df):
    return (df['hora'] <6) | (df['hora'] > 22)

