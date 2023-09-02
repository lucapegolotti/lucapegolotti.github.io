from PIL import Image, ImageOps
import pathlib

# image = Image.open('img/lp.jpg')
# image.save('img/lp-lq.jpg',quality=20,optimize=True)

directory = pathlib.Path('img')
files = list(directory.rglob('*'))

for f in files:
    f = str(f)
    if ('.jpg' in f or '.jpeg' in f) and '-lq.' not in f:
        image = Image.open(f)
        image = ImageOps.exif_transpose(image)
        if '.jpg' in f:
            new_fname = f.replace('.jpg', '-lq.jpg')
        else:
            new_fname = f.replace('.jpeg', '-lq.jpeg')
        image.save(new_fname,quality=20, optimize=True)

# headshot
image = Image.open('img/lp.jpg')
image = ImageOps.exif_transpose(image)
image.save('lp-lq.jpg',quality=100, optimize=False)