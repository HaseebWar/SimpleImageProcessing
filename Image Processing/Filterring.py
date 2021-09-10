import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from IPython.display import display, Image


def compare_image(image1, image2):
  plt.figure(figsize=(9,9))
  plt.subplot(1,2,1)
  plt.imshow(image1)
  plt.title('Orignal')
  plt.axis('off')

  plt.subplot(1,2,2)
  plt.imshow(image2)
  plt.title('Modified')
  plt.axis('off')

  plt.tight_layout()

park = cv2.imread('C:/Users/Haseeb/Desktop/Image Processing/Input/Sample.jpg')
park = cv2.cvtColor(park,cv2.COLOR_BGR2RGB)
edge = cv2.Canny(park,100,200)
compare_image(park,edge)


display(Image(park))

# plt.imshow(mpimg.imread(park))
# plt.imshow(mpimg.imread(edge))

# img = cv2.imread('C:/Users/Haseeb/Desktop/Image Processing/Input/Sample.jpg')
# img2 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# compare_image(img2,img)
# compare_image.save('C:/Users/Haseeb/Desktop/Image Processing/Input/Filter.jpg')
