#Transacciones por hora
def generar_feature(df):
    df = df.copy()

    df['tx_por_hora'] = df.groupby('hora')['monto'].transform('count')

    return df