import os
import cv2
import time
from matplotlib import pyplot as plt 

class StopSignDetectionModel:
    def __init__(self):
        self.stop_data = cv2.CascadeClassifier('stop_data.xml') 

    def detect_frame(self, frame):
        return self.stop_data.detectMultiScale(frame, minSize =(20, 20))

        
def example():
    model = StopSignDetectionModel()
    cap = cv2.VideoCapture(0)

    i = 0
    try:
        while True:
            time.sleep(0.1)

            success, frame = cap.read()
            if not success:
                break
            
            img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
            img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 

            found = model.detect_frame(img_gray)

            if len(found) == 0:
                continue

            for (x, y, width, height) in found: 
                cv2.rectangle(img_rgb, (x, y),  
                            (x + height, y + width),  
                            (0, 255, 0), 5)
                print("Stop Sign Located: ({}, {}, {}, {})".format(x, y, width, height))

            plt.subplot(1, 1, 1) 
            plt.imshow(img_rgb) 
            plt.show() 
            # image_file = os.path.join('images', 'image' + str(i) + '.jpg')
            # cv2.imwrite(image_file, frame)
            # found = model.detect(image_file)
            i += 1

    except KeyboardInterrupt:
        pass
    
if __name__ == "__main__":
    example()