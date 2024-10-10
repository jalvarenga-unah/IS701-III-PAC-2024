#pip install pandas
import pandas as pd

# DataFrames y Series

ciudades = [ 'Bogota', 'Medellin', 'Cali', 'Barranquilla', 'Cartagena', 'Santa Marta', 'Manizales' , 'Pereira' ]
poblacion = [ 7.4, 2.5, 2.2, 1.2, 1.0 , 0.5, 0.4, 0.3 ]

#Serie con los listados
poblacion_serie = pd.Series( poblacion, index=ciudades )

# print( poblacion_serie )
# print( poblacion_serie['Cali'])

ciudadesDict = {
    "ciudades": ciudades,
    "poblacion": poblacion
}

df = pd.DataFrame( poblacion_serie, columns=['Poblacion'] )
# print( df )

df_ciudades = pd.DataFrame( ciudadesDict )

# condicion para el filtrado
criterio_poblacion = df_ciudades['poblacion'] <= 2.0

# print con condiciones
# print(df_ciudades[ criterio_poblacion ])

#funciones basicas de DF que son utiles
print(df_ciudades.describe()) # descripcion estadistica
print(df_ciudades.head()) # primeros 5 registros
print(df_ciudades.tail()) # ultimos 5 registros
print(df_ciudades.info()) # informacion del dataframe
print(df_ciudades.columns) # columnas del dataframe


# alterar el dataframe

#para agregar, se hace referencia a la columna (para crearla)
# y el valor, puede ser estatico
# o calculado en base a otras columnas del dataframe
df_ciudades['pais'] = 'Colombia'
df_ciudades['poblacion_millones'] = df_ciudades['poblacion'] * 1000000

print(df_ciudades)

df_ciudades_copia = df_ciudades.drop('poblacion', axis=1) #inplace=True para modificar el dataframe original

print(df_ciudades)
print(df_ciudades_copia)
