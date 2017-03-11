#https://sourceforge.net/projects/opencvlibrary/?source=typ_redirect
#build/python/2.7/x32 or x 64/cv2.pyd 
#jogar o arquivo cv2.pyd dentro da pasta C:\Python27\Lib\site-packages\
import cv2 
# pip instal numpy
import numpy as np 

brejas = cv2.imread('brejas.png')
img_black_in_white = cv2.cvtColor(brejas, cv2.COLOR_BGR2GRAY)
breja = cv2.imread('breja.png',0)#template breja
width, height = breja.shape[::-1] #pega o tamanho do template breja
result = cv2.matchTemplate(img_black_in_white,breja,cv2.TM_CCOEFF_NORMED)
initial = 0.3
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html#numpy.where
precision = np.where( result >= initial)
color = (0,0,0)
margin = 1
for mat in zip(*precision[::-1]):#unpack ultima matriz 
    cv2.rectangle(brejas, mat, (mat[0] + width, mat[1] + height),color , margin)
cv2.imwrite('match.png',brejas)
