# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 21:05:08 2016

@author: Caseny
"""

from PIL import Image

im=Image.open('7E1A1587B45E4DD2A19AE2D691A2797C.jpg')

w,h=im.size
print('Original image size:%sX%s.'%(w,h))