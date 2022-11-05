from PIL import Image

img = Image.open('imagen.png')

grados = int(input('Ingrese la cantidad de grados: '))
out = img.rotate(grados)
out.save('rotada.png')