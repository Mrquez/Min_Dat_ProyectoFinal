import pandas as pd
from sklearn.impute import KNNImputer

# Cargar los DataFrames desde los archivos CSV
resultados_semana = pd.read_csv('resultados_semana.csv')
nuevo_dataset = pd.read_csv('dfIpertencion.csv')

# Merge utilizando 'FOLIO_INT' como clave
merged_df = pd.merge(resultados_semana, nuevo_dataset, on='FOLIO_INT', how='outer')

# Imputar valores usando k-NN con 5 vecinos en todas las columnas
imputer = KNNImputer(n_neighbors=5)
imputed_values = imputer.fit_transform(merged_df.iloc[:, 1:])  # Excluye la columna 'FOLIO_INT' del ajuste
merged_df.iloc[:, 1:] = imputed_values  # Excluye la columna 'FOLIO_INT' de la asignación

# Guardar el DataFrame resultante
merged_df.to_csv('DataFinalHipertencion.csv', index=False)