import os
import time
import cv2
from enum import Enum
from gps import GPS
from obd import OBD
from pushover import Pushover
from detection import StopSignDetectionModel
from matplotlib import pyplot as plt 

class State(Enum):
    DetectStopSign = 1
    TrackVehicleSpeed = 2
    Pass = 3
    Fail = 4

def main():
    # init
    # gps = GPS()
    # obd = OBD()
    # pushover = Pushover()
    # model = StopSignDetectionModel()
    # cap = cv2.VideoCapture(0)

    state = State.DetectStopSign

    # main loop
    try:
        while True:
            time.sleep(0.1)
            
            if state == State.DetectStopSign:
                print("detecting stop sign...")
                state = State.TrackVehicleSpeed

            elif state == State.TrackVehicleSpeed:
                print("tracking vehicle speed...")
                state = State.Pass

            elif state == State.Pass:
                print("passed!")
                state = State.DetectStopSign

            elif state == State.Fail:
                print("failed!")
                state = State.DetectStopSign
            
    except KeyboardInterrupt:
        pass
    

if __name__ == "__main__":
    main()
