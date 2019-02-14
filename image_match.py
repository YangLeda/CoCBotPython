# Image template matching using opencv

import cv2 
import numpy as np 


def image_match(source_filepath, template_filepath, threshold = 0.7, cvt_gray = False):

    # Source image 
    img_source = cv2.imread(source_filepath)
    #img_source_gray = cv2.cvtColor(img_source, cv2.COLOR_BGR2GRAY) 

    # Template image 
    img_template = cv2.imread(template_filepath)
    #img_template_gray = cv2.cvtColor(img_template, cv2.COLOR_BGR2GRAY)


    # Store width and heigth of template in w and h 
    w, h = img_template.shape[:2] 
      
    # Perform match operations. 
    res = cv2.matchTemplate(img_source,img_template,cv2.TM_CCOEFF_NORMED) 

      
    # Store the coordinates of matched area in a numpy array 
    loc = np.where( res >= threshold)  

    # Draw a rectangle around the matched region. 
    for pt in zip(*loc[::-1]): 
        cv2.rectangle(img_source, pt, (pt[0] + w, pt[1] + h), (0,0,255), 3)

    result_save_marked = cv2.imwrite("marked.jpg", img_source)

    return result_save_marked
