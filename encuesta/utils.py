
import uuid, base64

from matplotlib import markers
from encuesta.models import Encuestas, MarcasTiendas, Ciudades
from io import BytesIO
import seaborn as sns
import matplotlib.pyplot as plt

def get_ciudad_from_id(val):
    ciudad = Ciudades.objects.get(id=val)
    return ciudad

def get_marca_from_id(val):
    marca = MarcasTiendas.objects.get(id=val)
    return marca

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type, data,titulos, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(5,3))
    if (chart_type=='#1'):
        plt.title(titulos)
        
        data.plot(kind='bar',
                figsize=(5,3),
                title=titulos,
                ylabel='Calificación',)
                
        #sns.barplot(x=x_values, y='amabilidad', data=data)
    elif (chart_type=='#2'):
        print('pie chart')
        plt.title(titulos)
        mylabels = ["Soporte", "Amabilidad",  "Efectividad"]
        plt.pie(data,labels = mylabels)
        plt.legend(title = "Promedio de respuestas")

    elif (chart_type=='#3'): 
        plt.title(titulos)     
        plt.plot(data,linewidth = '2.5', marker='o',linestyle='dashed')
    else:
        print('Ups... failed to identify the chart type')
    
    plt.tight_layout()
    chart = get_graph()
    return chart