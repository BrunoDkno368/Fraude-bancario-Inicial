from reglas import (
    regla_monto_alto,
    regla_frecuencia,
    regla_horario_inusual
)

def clasificar (df):
    df=  df.copy()
    df['score'] = 0
    df.loc[regla_monto_alto(df), 'score'] +=1
    df.loc[regla_horario_inusual(df), 'score'] +=1
    df.loc[regla_frecuencia(df), 'score'] +=1

    df['decision'] = 'Aprobar'
    df.loc[df['score'] == 1, 'decision' ] = 'Revisar'
    df.loc[df['score'] >= 2, 'decision' ] = 'Rechazar'

    return df