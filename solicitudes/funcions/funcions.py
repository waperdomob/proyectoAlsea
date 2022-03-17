import os
from django.core.files.storage import FileSystemStorage 

def handle_uploaded_file(name,f):
    with open('media/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def subirDocs(nombre,doc,rut):
    postfix=doc.name.split('.')[1]
    
    fs = FileSystemStorage()
    name1 = fs.save(nombre+rut+'.'+postfix,doc)
    url1 = fs.url(name1)
    
    return name1,url1

def subirDocs2(nombre,doc,rut):
    postfix=doc.name.split('.')[1]
    
    fs = FileSystemStorage()
    name1 = fs.save(nombre,doc)
    url1 = fs.url(name1)
    
    return name1,url1