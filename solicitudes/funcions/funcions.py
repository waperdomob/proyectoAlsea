
def handle_uploaded_file(f):
    with open('solicitudes/static/file/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)