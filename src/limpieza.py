def limpiar_datos(df):
    df = df.copy()
    df['hora'] = df['Time'] / 3600

    df = df.rename(columns={
        'Amount': 'monto',
        'Class': 'fraude'
    })

    return df