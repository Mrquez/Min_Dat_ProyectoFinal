import pandas as pd

# Leer los datasets
df1 = pd.read_csv('resultados_semana.csv')
df2 = pd.read_csv('dfDiabetes.csv')

#-----------------------------------------------------------------------------------
# Obtener folios únicos para los conjuntos de datos por separado
folios_unicos_df1 = len(df1['FOLIO_INT'].unique())
folios_unicos_df2 = len(df2['FOLIO_INT'].unique())


#-----------------------------------------------------------------------------------

# Mostrar la cantidad de folios únicos por conjunto de datos
print("Cantidad de folios únicos en el primer Dataset:", folios_unicos_df1)
print("Cantidad de folios únicos en el segundo Dataset:", folios_unicos_df2)

#-----------------------------------------------------------------------------------

# Combinar los cinco conjuntos de datos en base a la columna FOLIO_INT
merged_df = pd.merge(df1, df2, on='FOLIO_INT', how='inner', suffixes=('_df1', '_df2'))
merged_df.to_csv('AlimentosDiabetes.csv', index=False)
print(merged_df)