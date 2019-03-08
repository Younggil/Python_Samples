# -*- coding: utf-8 -*-
"""
Practice: 
    
    Read an image: use imageio module
    Check its coordinates
    
    Output: 
        an image that has been read
        white horizontal band to see the x-axis
        while vertical band to see the y-axis

@author: Y.Song
"""

### import
import matplotlib.pyplot as plt

import imageio
# about imageio: see http://imageio.github.io

#image name: Sample000.png

### read an image
imgsample = imageio.imread('Sample000.png')
# show the read image
plt.imshow(imgsample)

plt.axis('off')
plt.show()

### check axes
procimgx = imgsample

### white out 200<x<300 
procimgx[200:300,:,:]=255
plt.imshow(procimgx)
plt.show()

### white out 100<y<200
imgsample = imageio.imread('Sample000.png')
procimgy = imgsample
procimgy[:,100:200,:]=255

plt.imshow(procimgy)
plt.show()


