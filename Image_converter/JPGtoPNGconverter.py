import sys
import os
from PIL import Image

# grab first and second argument
jpg_folder = sys.argv[1]
png_folder = sys.argv[2]
# check if new directory exists, if not create
if not os.path.exists(png_folder):
    os.mkdir(png_folder)
    # loop through directory of pokedex
pictures_to_convert = os.listdir(jpg_folder)
for picture in pictures_to_convert:
    jpg_picture = Image.open(f'{jpg_folder}{picture}')
    png_ext = picture.replace('.jpg', '.png')
    png_picture = jpg_picture.save(f'{png_folder}{png_ext}', 'png')
    # png_picture = Image.save()
# conver images to png
# save to new folder
