# Import Statements
import os, sys
from PIL import Image, ImageFilter, ImageEnhance

# !!!----------------------------------------------------------------------------------------------------------------!!!
# !-------------------------------from the pillow tutorial on their website--------------------------------------------!
# !!!----------------------------------------------------------------------------------------------------------------!!!


im = Image.open("General\Images\Test.jpg")
"""
im.show()
"""

"""
size = (128, 128)
images = ["Images/NSFW.jpg", "Images/Test.jpg"]
for infile in images:
    outfile = os.path.splitext(infile)[0] + "thumbnail.jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.thumbnail(size)
                im.save(outfile, "JPEG")
        except OSError:
            print("cannot create thumbnail for", infile)
            """

# cropbox = (100, 100, 200, 200)
# cropbox = (0, 0, 1000, 1000)
# cropbox = (0, 0, 1, 1)
# im.crop(cropbox).show()

"""
# cropbox = (0, 0, 250, 250)
cropbox = (250, 250, 750, 750)
# cropbox = (0, 0, im.width, im.height)
region = im.crop(cropbox)
# region = region.transpose(Image.ROTATE_180)
# region = region.transpose(Image.ROTATE_270)
# region = region.transpose(Image.ROTATE_90)
im.paste(region, cropbox)
im.show()
"""

"""
im.resize((512, 256)).show()
"""

"""
im.rotate(45).show()
"""

"""
im.convert("L").show()
"""

"""BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SHARPEN, SMOOTH, SMOOTH_MORE
im.show()
im.filter(ImageFilter.DETAIL).show()
im.filter(ImageFilter.FIND_EDGES).show()
im.filter(ImageFilter.BLUR).show()
im.filter(ImageFilter.SMOOTH_MORE).show()
im.filter(ImageFilter.EDGE_ENHANCE_MORE).show()
im.filter(ImageFilter.EMBOSS).show()
im.filter(ImageFilter.CONTOUR).show()
"""

"""
im.point(lambda i:i * 1.2).show()
"""

"""
split_color = im.split()
# split_color[2].show()
low_red = split_color[0].point(lambda i: i < 100 and 255)
# low_red.show()
green = split_color[1].point(lambda i: i * 0.7)
# green.show()
split_color[1].paste(green, None, low_red)
# split_color[1].show()
im = Image.merge(im.mode, split_color)
im.show()
"""
"""color, contrast, brightness, sharpness
contrast = ImageEnhance.Contrast(im)
contrast.enhance(1.3).show()
color = ImageEnhance.Color(im)
color.enhance(0.4).show()
brightness = ImageEnhance.Brightness(im)
brightness.enhance(2).show()
sharpness = ImageEnhance.Sharpness(im)
sharpness.enhance(1.5).show()
"""

im = im.convert("RGB")
split = im.split()
r = split[0]
# r = r.point(lambda i: i * 1.2)
g = split[1]
# g = g.point(lambda i: i + 10)
b = split[2]
# b = b.point(lambda i: (i > 150 and 255) or 150)
# empty_k = Image.new("L", (r.size[0], r.size[1]), 0)
Image.merge("RGB", (r, g, b)).show()
Image.merge("RGB", (r, b, g)).show()
Image.merge("RGB", (b, r, g)).show()
Image.merge("RGB", (b, g, r)).show()
Image.merge("RGB", (g, r, b)).show()
Image.merge("RGB", (g, b, r)).show()
