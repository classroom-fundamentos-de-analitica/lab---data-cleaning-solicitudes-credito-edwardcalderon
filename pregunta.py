"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import re
from datetime import datetime
import pandas as pd

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)
    # drop na y duplicados
    df.dropna(axis = 0, inplace = True)
    df.drop_duplicates(inplace = True)

    # minúsculas columnas y eliminar carácteres especiales.
    for columna in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']:
        df[columna] = df[columna].str.lower()
        df[columna] = df[columna].apply(lambda x: x.replace('_', ' '))
        df[columna] = df[columna].apply(lambda x: x.replace('-', ' '))

    # remplazar carácteres especiales
    df['monto_del_credito'] = df['monto_del_credito'].str.replace("\$[\s*]", "")
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(",", "")
    df['monto_del_credito'] = df['monto_del_credito'].str.replace("\.00", "")
    df['monto_del_credito'] = df['monto_del_credito'].astype(int)
    
    # columna comuna_ciudadano como float
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(float)

    # comuna_ciudadano a formato de fecha
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if (len(re.findall("^\d+/", x)[0]) - 1) == 4 else datetime.strptime(x, "%d/%m/%Y"))

    # elimianr duplicados
    df.drop_duplicates(inplace = True)

    return df
