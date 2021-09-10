from PIL import Image, ImageFilter, ImageEnhance


OriImage = Image.open('C:/Users/Haseeb/Desktop/Image Processing/Input/Sample.jpg')
OriImage.show()

gaussImage = OriImage.filter(ImageFilter.GaussianBlur(5))
gaussImage.show()
#Save blurImage Default
gaussImage.save('C:/Users/Haseeb/Desktop/Image Processing/Output/GaussianBlur Sample.jpg')