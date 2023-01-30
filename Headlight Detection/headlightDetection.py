from shutil import which
import numpy as np
from matplotlib import pyplot as plt
import cv2, time

def wait(t):
    time.sleep()

#List includes path for images representing differenct scenarios
mlist = ['bus_coming.hpg','going.jpg','both.jpg']

#codition: no vehicle
def scenario(condition):
    image = cv2.imread(condition)
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imwrite('gray_image.png',gray_image)
    cv2.imshow('color_image',image)
    blur_image = cv2.blur(gray_image,(15,15))
    cv2.imwrite('blur_image.png',blur_image)
    ret , thresh = cv2.threshold(blur_image,150,255,0)
    contour_image , contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drwaContours(blur_image,contours,-1,(0,255,0),3)
    cv2.imshow('blur_image.png',blur_image)
    moments = [cv2.moments(cnt) for cnt in contours]
    y_centroids = [int(round(m['m01']/m['m00'])) for m in moments]
    x = len(y_centroids)
    i=0
    while i<x:
        y_centroids[i] = y_centroids[i]//10