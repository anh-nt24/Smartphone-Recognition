from PIL import Image
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def recognizer(filename):
    #################
    # PREPROCESSING #
    #################

    # Resize image
    img = Image.open(filename)
    img = img.resize((600,400))
    width, height = img.size

    # Convert to grayscale image: Average method
    avg_img = img.convert()
    for i in range(width):
        for j in range(height):
            r,g,b = img.getpixel((i,j))
            gray = (r+g+b)//3
            avg_img.im.putpixel((i,j), (gray,)*3)

    # gray_img = np.array(avg_img,dtype='uint8')

    ##################
    # EDGE DETECTION #
    ##################
    # Edge detection using Roberts Cross Gradient with threshoding 150
    def edge_detection(img,window,thres):
        Sx, Sy = window
        m= np.array(img).shape
        new_img = np.zeros([m[1],m[0]])
        # print(new_img.shape)
        for i in range(1,width-1):
            for j in range(1,height-1):
                xred, yred = 0,0
                for k in range(i-1,i+2):
                    for h in range(j-1,j+2):
                        r = avg_img.getpixel((k,h))[0]
                        xred += r*Sx[i-(k-1), j-(h-1)]
                        yred += r*Sy[i-(k-1), j-(h-1)]
                magnitude = np.sqrt(xred**2 + yred**2)
                magnitude = 0 if magnitude < thres else 255
                # new_img.im.putpixel((i,j), (magnitude,)*3)
                new_img[i,j] = magnitude
        return np.array(new_img,dtype='uint8').T

    G_x = np.array([[0,0,0],[0,-1,0],[0,0,1]])
    G_y = np.array([[0,0,0],[0,0,-1],[0,1,0]])

    roberts_cross = edge_detection(avg_img, [G_x,G_y],55)

    ####################
    # FINDING CONTOURS #
    ####################
    img = np.uint8(img)
    contours, _ = cv.findContours(roberts_cross.copy(), mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)
    cnt = []
    contours = sorted(contours, key=cv.contourArea, reverse=True)
    for i in contours:
        p = cv.arcLength(i,True)
        appr = cv.approxPolyDP(i,0.05*p, True)
        if len(appr) == 4 and (50000 < cv.contourArea(i) < 60000 or 35000 < cv.contourArea(i) < 44000 and np.array(cnt)[np.array(cnt)>50000].size == 0):
            # print(cv.contourArea(i))
            cnt.append(appr)
    s = ''
    if len(cnt) != 0:
        cv.drawContours(img, contours=cnt, contourIdx=-1, color=(0, 255,0), thickness=3)
        s = 'RECOGNIZE SUCCESSFULLY'
    else:
        s = 'UNABLE TO RECOGNIZE'

    return img, s
    # fig = plt.figure(figsize=(10,5))
    # ax1 = fig.subplots(1,1)
    # ax1.imshow(img)
    # plt.title(s, fontsize=25, color = 'r')
    # plt.show()