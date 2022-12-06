# STOP and GO!
This is the Project for UCLA ECEM202A/CSM213A (Fall 2022)

## Abstract
Currently, we do not have a mature system to monitor driver’s behavior before a STOP sign. There are plenty of drivers who don’t make a complete stop at the stop sign, since manually observing and making actions to the STOP sign is not easy for human beings. So we want to design an efficient technique to check the driver's behavior and remind them to obey the law, with a punishment and reward mechanism.

## Team
* Ziyang Ji
* Chih-Chun Hsu
* Yi Xiao

## Technique approach: 
### Capture Imagine
Our first goal is to detect the stop sign on the road, we use the camera to capture the picture and send it to our computer in real time, running the pre-trained model to get the result. With each frame we captured, there is a bounding box showing if there is a stop sign detected. Then we will start tracking the change of the car speed and record the GPS coordinate accordingly for further implementation. 

### Car speed tracking
By connecting the OBD-II device to the car, we can get the speed info of the car in a real-time format. So, when the stop sign is detected, we can then start to estimate the change of the speed by checking whether the speed reaches 0. Also, by tracking the size of the bounding box, we can estimate the distance from the car to the stop sign.

### Location recording
For each stop sign we meet, we want to record the position of it. We connect a GPS tracker to our computer and stick it on the roof of the vehicle. We collect the GPS info from the background in real-time. When the stop sign is detected, we can record the current GPS location. Due to the latency of the GPS, we have to record the coordinate when we first detect the stop sign. We want to put these coordinates to a dictionary and when the next time we are nearby the stop sign we visited, we can get a reminder that there is a stop sign.

