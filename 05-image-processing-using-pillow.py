from PIL import Image
# https://pillow.readthedocs.io/en/stable/reference/Image.html

# READING AN IMAGE
img = Image.open("images/test_image.jpg")

print(type(img)) # <class 'PIL.PngImagePlugin.PngImageFile'>
print(img.format) # PNG
print(img.mode) # RGBA
print(img.size) # (639, 511)

# RESIZING IMAGE
small_img = img.resize((200,300))
small_img.save("images/test_image_small.png")

img.thumbnail((200,300))
img.save("images/test_image_tmbnail.png")
print(img.size) # (200,160) compress image but keeping the aspect ratio

img.thumbnail((1200,1300))
img.save("images/test_image_tmbnail2.png")
print(img.size) # (639, 511) cant be bigger than original

# CROPPING AN IMAGE
cropped_img = img.crop((0, 0, 300 ,300)) # (left, top, right, bottom)
cropped_img.save("images/cropped_img.png")

img1 = img
print(img1.size) # (639, 511)
img2 = Image.open("images/monkey.jpg")
print(img2.size) # (220, 373)
img2.thumbnail((150,200))

# COPYING IMAGES
img1_copy = img1.copy()
img1_copy.paste(img2, (50,50))
img1_copy.save("images/pasted_image.png")

# IMAGE ROTATION
img90 = img.rotate(90)
img90.save("images/rotated90.png")
img45 = img.rotate(45, expand=True) # if expand = True, dont crop pixels
img45.save("images/rotated45.png")

# IMAGE FLIP 
img_flipLR = img2.transpose(Image.FLIP_LEFT_RIGHT)
img_flipLR.save("images/flippedLR.jpg")

img_flipTB = img2.transpose(Image.FLIP_TOP_BOTTOM)
img_flipTB.save("images/flippedTB.jpg")

# GRAYSCALE
grey_img = img2.convert("L")
grey_img.save("images/grey_monkey.jpg")

import glob

path = "images/test_images/aeroplane/*"

for file in glob.glob(path):
    print(file)
    a = Image.open(file)
    rotated45 = a.rotate(45, expand=True)
    rotated45.save(file+"_rotated45.png", "PNG")
    
    
    
    

