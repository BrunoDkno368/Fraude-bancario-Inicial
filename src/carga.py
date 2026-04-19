import pandas as pd 

def cargar_datos(path):
    df = pd.read_csv(path)
    return(df)


