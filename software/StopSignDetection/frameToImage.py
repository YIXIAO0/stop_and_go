import cv2
from matplotlib import pyplot as plt 
import os

def stop_sign_detection(image_path):
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
    stop_data = cv2.CascadeClassifier(os.path.join('StopSignDetection' , 'stop_data.xml')) 
    found = stop_data.detectMultiScale(img_gray,  
                                    minSize =(20, 20)) 
    
    # Don't do anything if there's  
    # no sign 
    amount_found = len(found) 
    
    if amount_found != 0: 
        
        # There may be more than one 
        # sign in the image 
        for (x, y, width, height) in found: 
            
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
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_POS_MSEC, 400)
i = 0

while (cap.isOpened()):
    success, frame = cap.read();
    
    # This condition prevents from infinite looping 
    
    # incase video ends.
    if success == False:
        break
    
    # Save Frame by Frame into disk using imwrite method
    
    # curr_path = os.getcwd()
    # curr_dir = os.path.join(curr_path, 'StopSignDetection')
    image_dir = os.path.join('StopSignDetection', 'Image') 
    image_file = os.path.join(image_dir, 'image' + str(i) + '.jpg')
    print(image_file)
    cv2.imwrite(image_file, frame)
    stop_sign_detection(image_file)
    cv2.waitKey()
    # os.remove(image_file)
    i += 1
    if (i > 0):
        break
    
cap.release()
cv2.destroyAllWindows()



