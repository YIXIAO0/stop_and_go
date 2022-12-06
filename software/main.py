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
                # check if a stop sign is detected
                # to do: determine when to start tracking vehicle speed (switch state)
                # to do: stop sign far away
                # to work around: frame drop
                # to work around: multiple stop sign detected (including ghost)
                state = State.TrackVehicleSpeed

            elif state == State.TrackVehicleSpeed:
                print("tracking vehicle speed...")
                # check if speed goes zero
                state = State.Pass

            elif state == State.Pass:
                print("passed!")
                # increase driver's credit
                state = State.DetectStopSign

            elif state == State.Fail:
                print("failed!")
                # play audio
                # send notification
                # decrease driver's credit
                state = State.DetectStopSign
            
    except KeyboardInterrupt:
        pass
    

if __name__ == "__main__":
    main()
