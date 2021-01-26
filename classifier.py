import os
import cv2
import numpy as np

unikey = "wper0185"
path = "C:/Users/JP/Downloads/OpenCVProofSet/OpenCVProofSet"




def find_colour(pixel):
    yellow = 255, 250, 0
    red = 255, 29, 0
    purple = 178, 0, 255
    blue = 0, 38, 255
    green = 0, 255, 33
    orange = 255, 114, 0
    black = 0, 0, 0
    # cream = 255, 216, 0

    blue_comp = pixel[0]
    green_comp = pixel[1]
    red_comp = pixel[2]
    # print(green_comp)

    if blue_comp == yellow[2] and (green_comp == yellow[1] or green_comp == (yellow[1]-34)) and red_comp == yellow[0]:
        return "yellow"
    
    if blue_comp == red[2] and (green_comp >= 0 and green_comp <= 29) and red_comp == red[0]:
        return "red"

    if blue_comp == purple[2] and green_comp == purple[1] and red_comp == purple[0]:
        return "purple"

    if blue_comp == blue[2] and (green_comp == blue[1] or green_comp == (blue[1]-13))and red_comp == blue[0]:
        return "blue"

    if blue_comp == green[2] and green_comp == green[1] and red_comp == green[0]:
        return "green"

    if blue_comp == orange[2] and (green_comp == orange[1] or green_comp == (orange[1] - 8))  and red_comp == orange[0]:
        return "orange"

    if blue_comp == black[2] and green_comp == black[1] and red_comp == black[0]:
        return "black"

    return "green"

def find_shape(image):
    edges = cv2.Canny(image,100,200)

    contours, hierarchy = cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

    
    
    for contour in contours:
        
        approx = cv2.approxPolyDP(contour,0.001*cv2.arcLength(contour,True),True)
        approx_length = len(approx)

        if 8 == approx_length:
            return "square"

        if approx_length >= 74 and approx_length <= 114:
            return "circle"

        if approx_length >= 29 and approx_length <= 49:
            return "star"

        return "triangle"




    
    

    


    

    



for letter in unikey:
    count = 0
    while count < 100:
        old_path = f"{path}/{letter}/{str(count)}.png"
        frame = cv2.imread(old_path)
            

        mid_pixel = frame[100,100]
        # print(mid_pixel)
        
        colour = find_colour(mid_pixel)
        shape = find_shape(frame)
        new_path = f"{path}/{letter}/{str(count)}_{colour}_{shape}.png"
        # print(new_path)
        os.rename(old_path, new_path)


        count += 1 

        
    

