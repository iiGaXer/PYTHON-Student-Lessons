import cv2
import numpy as np
from matplotlib import pyplot as plt

#! IMREAD_whatever turns the image's color; making it's data change 
image = cv2.imread("M.I Learning/Imaging/Images/Eligoes.PNG", cv2.IMREAD_GRAYSCALE)
plt.imshow(image, cmap= "gray"), plt.axis("off")
plt.show()

# * Prints out the image's data
print(image)
print(image.shape)

# ! The values of the dataset in this matrix correspond to the intensity of colors; black and white. 
# ! RGB: 0 - 255
for i in range(len(image) % 2):
    print(image[i])

# ! Due to resizing pixels, changing data, it makes some information, or data, reduced; making it more
# ! -unrecongnizable.
ver1_img = cv2.resize(image, (50, 50))
plt.imshow(ver1_img, cmap= "gray"), plt.axis("off")
plt.show()
