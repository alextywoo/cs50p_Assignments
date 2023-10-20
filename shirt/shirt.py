from os.path import splitext
import sys
from PIL import Image, ImageOps

def imagelayover(path):
    try:
        im = Image.open(path)
    except FileNotFoundError:
        sys.exit('Input does not exist')
    shirtfile = Image.open('shirt.png')
    size = shirtfile.size
    muppet = ImageOps.fit(im, size)
    muppet.paste(shirtfile, shirtfile)
    muppet.save(sys.argv[2])


def main():
    if len(sys.argv) < 3:
        sys.exit('Too few arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many arguments')
    if not splitext(sys.argv[1])[1].lower() in ['.jpg', '.jpeg', '.png']:
        sys.exit('Not a photo input file')
    if not splitext(sys.argv[2])[1].lower() in ['.jpg', 'jpeg', '.png']:
        sys.exit('Not a photo output file')
    if not splitext(sys.argv[1])[1].lower() == splitext(sys.argv[2])[1].lower():
        sys.exit('Files are not consistent')
    imagelayover(sys.argv[1])

if __name__ == "__main__":
    main()