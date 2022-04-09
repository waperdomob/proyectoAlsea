import base64, uuid
from unicodedata import name
from django.core.files.base import ContentFile

def get_report_image(data,i):
    _ ,str_image = data.split(';base64')
    decoded_img = base64.b64decode(str_image)
    img_name = str(uuid.uuid4())[:10] + '.png'
    data = ContentFile(decoded_img, name= img_name)
    with open("imagen"+str(i)+".png", "wb") as fh:
                fh.write(decoded_img)
    return data
