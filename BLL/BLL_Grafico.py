import matplotlib.pyplot as plt
import seaborn as sns
import gc
from BLL import BLL_Dataframe_Personalizado
from matplotlib.dates import date2num
import pandas as pd

TOP = 10
file_path = "Imagenes/"

class Grafico(object):

    def __init__(self):
        pass

    def graficarBarras(self, df, columna_x, top):
        datos_agrupados = df.groupby(columna_x).size().reset_index(name="counts")
        datos_agrupados = datos_agrupados.sort_values("counts", ascending=True)
        datos_agrupados = datos_agrupados.head(top)
        fig, ax = plt.subplots(figsize = (10,5))
        ax.barh(datos_agrupados[columna_x], width=datos_agrupados["counts"])
        for i in ax.patches:
            plt.text(i.get_width()+0.2, i.get_y()+0.3, str(round((i.get_width()), 2)), fontsize=10, color='black')
        
        return fig
    
    def graficarBarrasContadas(self, df ,columna_x, top):
        df = df.head(top)
        df = df.sort_values("countdevicename", ascending=True)
        fig, ax = plt.subplots(figsize = (10,5))
        ax.barh(df[columna_x], width=df["countdevicename"])
        for i in ax.patches:
            plt.text(i.get_width()+0.2, i.get_y()+0.3, str(round((i.get_width()), 2)), fontsize=10, color='black')
        
        return fig


    ### grafico de tortas que devuelve la figura ###
    def graficarTorta(self, df, columna, top):
        datos_agrupados = df.groupby(columna).size().reset_index(name="counts")
        datos_agrupados = datos_agrupados.sort_values("counts", ascending=False)
        datos_agrupados = datos_agrupados.head(top)

        # Crear un gráfico de torta
        sns.set_style("darkgrid")
        plt.figure(figsize=(9,6))
        plt.pie(datos_agrupados["counts"], labels=datos_agrupados[columna], autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops={'edgecolor': 'white'})
        return plt



    def graficarHistograma(self, df):
        sns.set_style("darkgrid")
        plt.figure(figsize=(20,10))
        fig, ax = plt.subplots()
        ax = sns.lineplot(data=df, x='fecha', y='cantidad', marker='o', markersize=5, color='blue', linewidth = 0.5)
        ax.set_xlabel('')
        ax.set_ylabel('')
        for index, row in df.iterrows():
            ax.annotate(str(row['cantidad']), (row['fecha'], row['cantidad']), ha='center', va='bottom')

        fig.autofmt_xdate()

        fecha_min = df['fecha'].min()
        fecha_max = df['fecha'].max()
        fechas_completas = pd.date_range(start=fecha_min, end=fecha_max)
        # Convertir las fechas a numeros de dias para utilizar en el grafico
        fechas_num = date2num(fechas_completas)
        plt.xticks(fechas_num, fechas_completas.strftime("%Y-%m-%d"), rotation=45)

        return plt      
