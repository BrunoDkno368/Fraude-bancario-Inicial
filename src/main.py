from carga import cargar_datos
from limpieza import limpiar_datos
from feature import generar_feature
from modelos_regla import clasificar

def main ():
    print("Iniciando proceso...")

    df = cargar_datos("data/creditcard.csv")
    print(type(df))
    df = limpiar_datos(df)
    print(type(df))
    df = generar_feature(df)
    print(type(df))
    df = clasificar (df)
    print(type(df))

    df.to_csv("output/dataset_final.csv", index=False)
    print("CSV generado correctamente")

if __name__ == '__main__':
    main()