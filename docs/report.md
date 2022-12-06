# Table of Contents
* Abstract
* [Introduction](#1-introduction)
* [Related Work](#2-related-work)
* [Technical Approach](#3-technical-approach)
* [Evaluation and Results](#4-evaluation-and-results)
* [Discussion and Conclusions](#5-discussion-and-conclusions)
* [References](#6-references)

# Abstract

For our project, we strive to design an efficient technique to check the driver’s behavior (e.g. stop the car before the STOP sign) and remind them to follow the traffic law with a punishment and reward mechanism. In order to measure our success, we evaluate our final system in how well the various aspects of the stop sign detection and warning system can be implemented. This includes stop sign detection/locating, movement detection (car’s speed), formulation of the application system, punishment and rewarding notification, and etc. We capture real-time images through in-built method in python and then use existing methods in opencv as the foundation of our algorithm to detect STOP signs in real-time. We implement car motion/speed detection through OBD-II and car location tracking through GPS. We also integrate this work with a camera system, and have a main source where each component is controlled accordingly. Furthermore, we create our application system through a Finite State Machine and incorporate with a punishment and rewarding mechanism to make the user experience more exciting. Results are promising as the system performs correctly as there are STOP signs in the test road. However, it has possible improvements such as better STOP sign detection algorithms that could detect partially visible signs and give users more accurate and safe instructions. We believe this project could be a foundation for an more accurate and feasible application of STOP sign detection, and help users/drivers follow the traffic rules in a more scientific way. 


# 1. Introduction

This section should cover the following items:

* Motivation & Objective: What are you trying to do and why? (plain English without jargon)
* State of the Art & Its Limitations: How is it done today, and what are the limits of current practice?
* Novelty & Rationale: What is new in your approach and why do you think it will be successful?
* Potential Impact: If the project is successful, what difference will it make, both technically and broadly?
* Challenges: What are the challenges and risks?
* Requirements for Success: What skills and resources are necessary to perform the project?
* Metrics of Success: What are metrics by which you would check for success?

# 2. Related Work

# 3. Technical Approach

# 4. Evaluation and Results

# 5. Discussion and Conclusions

# 6. References
