import pandas as pd

df_empleados = pd.read_csv('./empleados.csv')

criterio = df_empleados["Departamento"] == "Ventas"

# print(df_empleados[ criterio ]["Salario"].sum()  )


# agrupar informacion

# suma por departamentos
# print(df_empleados.groupby("Departamento")["Salario"].sum() )

# suma y cantidad de empleados por departamento
df_conteo = df_empleados.groupby("Departamento")["Nombre"].count()
df_salario = df_empleados.groupby("Departamento")["Salario"].sum()

df_unificado = pd.concat([df_conteo, df_salario], axis=1)

# print(df_unificado)

# agrupar por mas de una columna
# print(df_empleados.groupby(["Ciudad", "Departamento"])["Salario"].sum())


# loc : hace referencia a las etiquetas de las filas y columnas, por el nombre de la columa
# iloc: hace referencia a la posicion de las filas y columnas, por la posicion de la fila

# print(df_empleados.iloc[:4, 3])  # No acepta el filtrado de columnas (por nombre)
# print(df_empleados.loc[:4, ["Nombre", "Salario"]])

# Ordenar los registros del dataframe

# print(df_empleados.sort_values(by="Salario", ascending=False))

# posibilidad de cambiar un nombre de columna, inplace=True para que se aplique en el dataframe original
df_empleados.rename(columns={"Salario": "Salario Mensual"}, inplace=True)
# print(df_empleados)

#condiciones con operadores logicos, cada expresion debe estar entre parentesis
# usar & para el operador and y | para el operador or
condicion =  ((df_empleados["Ciudad"] == "Madrid") | (df_empleados["Ciudad"] == "Barcelona")) & (df_empleados["Edad"] > 30)

print(df_empleados[condicion])







