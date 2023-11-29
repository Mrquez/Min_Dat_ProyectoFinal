import pandas as pd

# Lee el archivo CSV
df = pd.read_csv('alimentos.csv')

# Convierte las columnas relevantes a números
df['pa1'] = pd.to_numeric(df['pa1'], errors='coerce')
df['pa2'] = pd.to_numeric(df['pa2'], errors='coerce')
df['Energia(kcal)'] = pd.to_numeric(df['Energia(kcal)'], errors='coerce')
df['Proteina(g)'] = pd.to_numeric(df['Proteina(g)'], errors='coerce')
df['CarboHidratos(g)'] = pd.to_numeric(df['CarboHidratos(g)'], errors='coerce')
df['Lipidos(g)'] = pd.to_numeric(df['Lipidos(g)'], errors='coerce')

# Crea nuevas columnas para calcular la ingesta semanal
df['Calorias_semana'] = df['pa1'] * df['pa2'] * df['Energia(kcal)']
df['Proteina_semana'] = df['pa1'] * df['pa2'] * df['Proteina(g)']
df['CarboHidratos_semana'] = df['pa1'] * df['pa2'] * df['CarboHidratos(g)']
df['Lipidos_semana'] = df['pa1'] * df['pa2'] * df['Lipidos(g)']

# Agrupa por 'FOLIO_INT' y suma los valores semanales
resultados_semana = df.groupby('FOLIO_INT').agg({
    'Calorias_semana': 'sum',
    'Proteina_semana': 'sum',
    'CarboHidratos_semana': 'sum',
    'Lipidos_semana': 'sum'
}).reset_index()

# Guarda los resultados en un nuevo archivo CSV
resultados_semana.to_csv('resultados_semana.csv', index=False)

# Muestra los resultados
print(resultados_semana)
