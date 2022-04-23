
import uuid, base64
import numpy as np
from encuesta.models import Encuestas, MarcasTiendas, Ciudades
from io import BytesIO
import matplotlib as mpl
import matplotlib.pyplot as plt


palette={"primary":"#FEF702",
         "background": "#252525",
         "primary_chart":"#F1F1F1",
         "text_color": "#FFFFFF",
         }

#Remove all axis
mpl.rcParams["axes.spines.bottom"] = True
mpl.rcParams["axes.spines.left"] = False
mpl.rcParams["axes.spines.right"] = False
mpl.rcParams["axes.spines.top"] = False
 
#color and format for axis labels and tick
mpl.rcParams['xtick.color']= '#FFFFFF'
mpl.rcParams['ytick.color']= '#FFFFFF'
mpl.rcParams['xtick.bottom'] = False
mpl.rcParams['ytick.left'] = False
 
#Grid format
mpl.rcParams["axes.grid"] = True
mpl.rcParams['grid.linestyle'] = '--'
mpl.rcParams['grid.linewidth'] = 1
mpl.rcParams["axes.grid.axis"] = 'y'
mpl.rcParams["grid.color"] = "#404040"

#Text elements---------------------------------------------
#Title format
mpl.rcParams["figure.titlesize"] = 18
mpl.rcParams["figure.titleweight"] = "regular"
 
#Subtitle format
mpl.rcParams["axes.titlesize"] = 12
mpl.rcParams["axes.titlelocation"]="left"
mpl.rcParams['axes.titleweight'] = "regular"
mpl.rcParams['axes.titlecolor']= '#FFFFFF'
mpl.rcParams['axes.titlelocation']= 'left'
 
#Other text elements
mpl.rcParams['font.weight'] = "medium"
mpl.rcParams['font.size'] = 10
mpl.rcParams['text.color'] = "#FFFFFF"

#Color for charts elements---------------------------------
#Background color
mpl.rcParams["figure.facecolor"] = palette["background"]
mpl.rcParams["axes.facecolor"] = palette["background"]
mpl.rcParams["savefig.facecolor"] = palette["background"]
mpl.rcParams['axes.labelcolor']= palette["text_color"]

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
        plt.title(titulos,
             horizontalalignment = 'left',
             x=0.05,
             y=0.92,
             transform=fig.transFigure,
             color=palette["background"],
             bbox=dict(facecolor=palette["primary"], edgecolor="none", pad=8.0)
        )        
        data.plot(kind='barh',
                figsize=(5,3),)        
        plt.xlabel("CALIFICACIÓN")

    elif (chart_type=='#2'):

        def func(pct, allvalues):
            absolute = float(pct / 100.*np.sum(allvalues))
            return "{:.1f}%\n({:0.2f} )".format(pct, absolute)
        plt.title(titulos,
             horizontalalignment = 'left',
             x=0.05,
             y=0.90,
             transform=fig.transFigure,
             color=palette["background"],
             bbox=dict(facecolor=palette["primary"], edgecolor="none", pad=8.0))
        mylabels = ["SOPORTE", "AMABILIDAD",  "EFECTIVIDAD"]

        plt.pie(data,autopct = lambda pct: func(pct, data),labels = mylabels)
       
    
    else:
        print('Ups... failed to identify the chart type')
    
    plt.tight_layout()
    chart = get_graph()
    return chart