# STOP and GO!
This is the Project for UCLA ECEM202A/CSM213A (Fall 2022)

## Abstract
Currently, we do not have a mature system to monitor driver’s behavior before a STOP sign. There are plenty of drivers who don’t make a complete stop at the stop sign, since manually observing and making actions to the STOP sign is not easy for human beings. So we want to design an efficient technique to check the driver's behavior and remind them to obey the law, with a punishment and reward mechanism.

## Team
* Ziyang Ji
* Chih-Chun Hsu
* Yi Xiao

## Instructions

#### Hardware
- A GPS tracker
- An USB webcam
- An OBD-II reader

#### Required packages
```
$ pip install opencv-python
$ pip install obd
$ pip install playsound
```

#### Before running it
- Run ```scan_port.py``` to get GPS tracker port and OBD-II port
- Modify port strings in both ```gps.py``` and ```obd2.py```

#### How to run it
```
$ python main.py
```
