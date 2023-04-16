# PPEye
Use cases may apply in construction worksites, industrial Manufacturing plants, Industries with high personal risks where PPE's are a must. Here The EHS advisors can crossverify the data collected and help in ensuring a reliable safety structure and personal protection of the employees.This also eases the job of human intervention in case of non-PPE conditions. 

# Hard Hat Detection
###### Model used is [YOLOV8 Hard Hat Detection by Keremberk](https://huggingface.co/keremberke/yolov8s-hard-hat-detection)


# Files
###### Not in any particular order
- `src/main.py`
  - This runs the main chunk of the object detection code and saves the confidence value and the flag to a JSON file.
- `server.py`
  - This script takes the data from the main.py's JSON file and servers it on a socket connection through FastAPI annd socketIO
- `app.html`
  - Page which server.py serves to clients 
- `Models/yolo8m-ppe.pt`
  - Yolo8m saved model trained specifically on Personal Protective Equipement Dataset (PPE)
- `Models/yolo8n-hard-hat-det.pt`
  - Yolo8n saved model trained specifically on Hard hats dataset (PPE)
  - slower and has a bit worse result than yolo8s
- `Models/yolo8s-hard-hat-det.pt`
  - Yolo8s saved model trained specifically on Hard hats dataset (PPE)
  - around 100ms faster (on my machine) and has better accuracy than yolo8n
- `Dataset/Videos/1 -> 4.mp4`
  - Videos to test use and non usage of PPE in different eviornments.

# Installation
###### have only tested on windows 11 22H2
## Windows 11 
```powershell
pip install ultralyticsplus ultralytics opencv-python fastapi fastapi-socketio

```
