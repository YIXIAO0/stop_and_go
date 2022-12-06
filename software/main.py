import os
import time
import cv2
from gps import GPS
from obd import OBD
from pushover import Pushover
from detection import StopSignDetectionModel
from matplotlib import pyplot as plt 

def main():
    # init
    # gps = GPS()
    # obd = OBD()
    # pushover = Pushover()
    # model = StopSignDetectionModel()
    # cap = cv2.VideoCapture(0)


    # main loop
    try:
        while True:
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        pass
    

if __name__ == "__main__":
    main()
