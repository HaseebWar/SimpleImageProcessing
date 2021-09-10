from PIL import Image

#Resizing Image Conda
image = Image.open('C:/Users/Haseeb/Desktop/Image Processing/Input/Sample.jpg')
new_image = image.resize((400, 400))
new_image.save('C:/Users/Haseeb/Desktop/Image Processing/Output/Resize Image.jpg')