import datetime 
from django.core.files.storage import FileSystemStorage 

def handle_uploaded_file(f):
    with open('solicitudes/static/file/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def subirDocs(nombre,doc):
    
    fecha_actual=datetime.datetime.now()
    f1_str = fecha_actual.strftime('%d/%m/%Y')

    fs = FileSystemStorage()
    name1 = fs.save(nombre+'.pdf',doc)
    url1 = fs.url(name1)

    return name1,url1