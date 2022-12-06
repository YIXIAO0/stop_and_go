import serial
import cv2
import time
import os
import obd
from matplotlib import pyplot as plt 

stop_data = cv2.CascadeClassifier('stop_data.xml') 

def stop_sign_detection(image_path, image_num, f):
    # Opening image 
    # image_num = input("Enter the image num:")
    img = cv2.imread(image_path) 
    # OpenCV opens images as BRG  
    # but we want it as RGB We'll  
    # also need a grayscale version 
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    
    
    # Use minSize because for not  
    # bothering with extra-small  
    # dots that would look like STOP signs 
    # stop_data = cv2.CascadeClassifier('stop_data.xml') 
    found = stop_data.detectMultiScale(img_gray,  
                                    minSize =(20, 20)) 
    
    # Don't do anything if there's  
    # no sign 
    amount_found = len(found) 
    
    if amount_found != 0: 
        
        # There may be more than one 
        # sign in the image 
        for (x, y, width, height) in found: 
            
            f.write("Stop Sign Located: ({}, {}, {}, {}, {})".format(image_num, x, y, width, height) + '\n')
            
            # We draw a green rectangle around 
            # every recognized sign 
            cv2.rectangle(img_rgb, (x, y),  
                        (x + height, y + width),  
                        (0, 255, 0), 5)
            print("DETECTED!")
            print("Stop Sign Located: ({}, {}, {}, {})".format(x, y, width, height))
        
            # print("Stop Sign Located: (%(x)d, %(y)d, %(width)d, %(height)d)") 
            
    # Creates the environment of  
    # the picture and shows it 
    plt.subplot(1, 1, 1) 
    plt.imshow(img_rgb) 
    plt.show() 


# Opens the inbuilt camera of laptop to capture video.
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_POS_MSEC, 400)
i = 0

with open('gps.txt','a') as f:
    while (cap.isOpened()):
        time.sleep(0.1)
        success, frame = cap.read();
        
        # This condition prevents from infinite looping 
        
        # incase video ends.
        if success == False:
            break
        
        # Save Frame by Frame into disk using imwrite method
        
        # curr_path = os.getcwd()
        # curr_dir = os.path.join(curr_path, 'StopSignDetection')
        image_dir = 'Image'
        image_file = os.path.join(image_dir, 'image' + str(i) + '.jpg')
        print(image_file)
        cv2.imwrite(image_file, frame)
        i += 1
        
        stop_sign_detection(image_file, i, f)
        # cv2.waitKey()
        # os.remove(image_file)
        # i += 1
        # if (i > 0):
        #     break


            
cap.release()
cv2.destroyAllWindows()



