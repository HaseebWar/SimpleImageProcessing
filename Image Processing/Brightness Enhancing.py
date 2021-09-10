from PIL import Image, ImageFilter, ImageEnhance

# For Brightness Conda
im = Image.open("C:/Users/Haseeb/Desktop/Image Processing/Input/Sample.jpg")
#image brightness enhancer
enhancer = ImageEnhance.Brightness(im)
factor = 1 #gives original image
im_output = enhancer.enhance(factor)
im_output.save('C:/Users/Haseeb/Desktop/Image Processing/Output/Original.png')
factor = 0.5 #darkens the image
im_output = enhancer.enhance(factor)
im_output.save('C:/Users/Haseeb/Desktop/Image Processing/Output/Dark Image.png')
factor = 1.5 #brightens the image
im_output = enhancer.enhance(factor)
im_output.save('C:/Users/Haseeb/Desktop/Image Processing/Output/Bright Image.png')