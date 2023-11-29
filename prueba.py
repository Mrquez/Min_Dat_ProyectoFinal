import pandas as pd

# Lee el archivo CSV
archivo_csv = "ensafrec_ad2022_rec_w.csv"
df = pd.read_csv(archivo_csv)

# Verifica si hay valores nulos en el conjunto de datos
valores_nulos = df.isnull().sum()

# Muestra la cantidad de valores nulos por columna
print("Valores nulos por columna:")
print(valores_nulos)

# Trata los valores nulos (si es necesario)
# Por ejemplo, puedes eliminar las filas con valores nulos o rellenarlos con un valor específico
# Aquí hay ejemplos de cómo hacerlo:

# Eliminar filas con valores nulos
df_sin_nulos = df.dropna()

# Rellenar valores nulos con un valor específico (por ejemplo, 0)
df_rellenado = df.fillna(0)

# Guardar el DataFrame modificado en un nuevo archivo CSV
df_sin_nulos.to_csv("sin_nulos.csv", index=False)
df_rellenado.to_csv("rellenado.csv", index=False)
