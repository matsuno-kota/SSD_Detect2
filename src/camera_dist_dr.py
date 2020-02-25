import numpy as np
import cv2
from imageio import imread

def camera_dist(img):

    mtx = np.load('mtx_dr.npy')
    dist = np.load('dist_dr.npy')
    newcameramtx = np.load('distmtx_dr.npy')

    # undistort
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

    return dst
