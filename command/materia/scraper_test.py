import requests
from bs4 import BeautifulSoup
import imgkit
from PIL import Image

#test
imgkit.from_url('https://horarios.fime.me/dependencia/2316/periodo/3376097/materias/c/maestros/455', 'out.jpg')

def crop(image_path, coords, saved_location):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    cropped_image.show()

if __name__ == '__main__':
    image = 'out.jpg'
    im = Image.open('out.jpg')
    width, height = im.size
    #print("Width: {} - Height: {}".format(width, height))
    crop(image, (0, 640, width, height-207), 'out-cropped.jpg')
