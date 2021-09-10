from PIL import Image, ImageFilter, ImageEnhance
import cv2
from matplotlib import pyplot as plt
import numpy as np

# For RGB to Gray Conda
img = cv2.imread('C:/Users/Haseeb/Desktop/Image Processing/Input/Sample.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(8,8))
plt.imshow(gray,cmap="gray")
plt.axis('off')
plt.title("GrayScale Image")
plt.show()