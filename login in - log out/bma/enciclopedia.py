from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .imgur import auth as imgur_auth
from datetime import date, datetime

if settings.DEBUG:
    imgur_albums = {'evento_banner': 'OurC6', 'usuario_foto': 'OurC6'}
else:
    imgur_albums = {'evento_banner': 'abR3d', 'usuario_foto': 'rQU6a'}
imgur_client = imgur_auth.authenticate()


def uploadToImgur(imagem, album):
    fs = FileSystemStorage()
    filename = fs.save(imagem.name, imagem)
    uploaded_file_url = fs.path(filename)
    imgur_config = {'album': imgur_albums[album]}
    imgur_image = imgur_client.upload_from_path(uploaded_file_url, config=imgur_config, anon=False)
    fs.delete(filename)
    return imgur_image['link']

def getTodayDate():
    return datetime.now().strftime('%Y-%m-%d')

def getTimeNow():
    return datetime.now().strftime('%H:%M:%S')

def getDateTimeNow():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
def getIdade(born_date):
    today = date.today()
    return today.year - born_date.year - ((today.month, today.day) < (born_date.month, born_date.day))

def dateInput_para_sqlDate(data):
    dia,mes,ano = data.split('/')
    return ano+'-'+mes+'-'+dia
