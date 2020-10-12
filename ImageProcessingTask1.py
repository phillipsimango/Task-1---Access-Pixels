# Image Processing Task 1
# Phillip Simango - C17341516

import cv2
from matplotlib import pyplot as plt

# 1. Read in the image
from matplotlib.pyplot import title

image = cv2.imread("/Users/phillipsimango/OneDrive/Image Processing/Task1/lightsource.jpg")

# 2. Converting the image to YUV
YUV = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
cv2.imwrite("/Users/phillipsimango/OneDrive/Image Processing/Task1/YUV lightsource.jpg", YUV)

# 3. Extracting the luminance colour channel
x = YUV.shape[0]
y = YUV.shape[1]
ychannel = YUV[0:x, 0:y, 0]
cv2.imwrite("/Users/phillipsimango/OneDrive/Image Processing/Task1/ychannel.jpg", ychannel)

# 4. Converting original image to grayscale
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("/Users/phillipsimango/OneDrive/Image Processing/Task1/Grayscale lightsource.jpg", grayscale)

# 5. Showing both luminance and grayscale on-screen
cv2.imshow("Ychannel", ychannel)
key = cv2.waitKey(0)
cv2.imshow("Grayscale lightsource", grayscale)
key = cv2.waitKey(0)

# 6. MatPlotLib Subplot
plt.subplot(2, 2, 1)
plt.imshow(ychannel)
title('Luminance')

plt.subplot(2, 2, 2)
plt.imshow(grayscale, cmap="gray")
title('Grayscale')

plt.show()
