import os
import time
import cv2
from enum import Enum
from collections import defaultdict
from gps import GPS
from obd2 import OBD
from pushover import Pushover
from detection import StopSignDetectionModel
from matplotlib import pyplot as plt 
from playsound import playsound

class State(Enum):
    DetectStopSign = 1
    StopSignGone = 2
    TrackVehicleSpeed = 3
    Pass = 4
    Fail = 5

def capture_and_detect(cap, model):
    success, frame = cap.read()
    if not success:
        return False
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    found = model.detect_frame(img_gray)
    return len(found) > 0
    
def main():
    # init
    gps = GPS()
    obd = OBD()
    pushover = Pushover()
    model = StopSignDetectionModel()
    cap = cv2.VideoCapture(1)

    # params
    state = State.DetectStopSign

    detected_count = 0
    not_detected_count = 0

    detect_threshold = 5
    not_detect_threshold = 5

    track_speed_count = 30
    
    last_coords = []
    stop_positions = defaultdict(str)
    nearby_alert_interval = 0

    # main loop
    try:
        while True:
            time.sleep(0.1)

            nearby_alert_interval += 1
            coords = gps.get_coordinate()
            if coords:
                last_coords = coords
                if stop_positions[coords[0][0:7] + coords[1][0:9]] == 1:
                    if nearby_alert_interval > 100:
                        print("There is a stop sign nearby")
                        playsound('./media/nearby.m4a')
                        nearby_alert_interval = 0

            if state == State.DetectStopSign:
                print("detecting stop sign...")
                detected = capture_and_detect(cap, model)
                if detected:
                    detected_count += 1
                else:
                    detected_count = 0

                if detected_count == detect_threshold:
                    stop_positions[last_coords[0][0:7] + last_coords[1][0:9]] = 1
                    state = State.StopSignGone
                    detected_count = 0
            
            elif state == State.StopSignGone:
                print("waiting stop sign gone...")
                detected = capture_and_detect(cap, model)
                if detected:
                    not_detected_count = 0
                else:
                    not_detected_count += 1
                
                if not_detected_count == not_detect_threshold:
                    state = State.TrackVehicleSpeed

            elif state == State.TrackVehicleSpeed:
                print("tracking vehicle speed...")
                speed = obd.get_speed()
                if str(speed) == '0.0 kph':
                    state = State.Pass
                    track_speed_count = 30
                
                track_speed_count -= 1
                if track_speed_count == 0:
                    state = State.Fail
                    track_speed_count = 30

            elif state == State.Pass:
                print("passed!")
                playsound('./media/pass.m4a')
                state = State.DetectStopSign

            elif state == State.Fail:
                print("failed!")
                playsound('./media/fail.m4a')
                pushover.send_message("Be careful! Someone is running a stop sign!")
                state = State.DetectStopSign
                
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
