import datetime
from PIL import Image

img = Image.open('imagen.png')

grados = int(input('Ingrese la cantidad de grados: '))
out = img.rotate(grados)

# creo una hora para agregarla al nombre
hora = datetime.datetime.now().strftime("%H-%M-%S-%p")
out.save('salidas/rotada-'+hora+'.png')