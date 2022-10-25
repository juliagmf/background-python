
from rembg import remove
# fornece ao interpretador python recursos de edição de imagem
from PIL import Image

img_entrada = 'dragon.jpg'
img_saida = 'output.png'
input = Image.open(img_entrada)
output = remove(input)
#salvando a imagem
output.save(img_saida)
