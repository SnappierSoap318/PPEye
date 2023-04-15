import cv2
from ultralytics import YOLO

import json

conf = 0.0
isWearingHardHat = False

model = YOLO('models/yolo8n-hard-hat-det.pt') # Fastest and more accurate

# Open the video file
video_path = "Dataset/videos/4.mp4"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
       
    if success:
        # Run YOLOv8 inference on the frame
        results = model.predict(frame, save_conf=True)[0]
        if results.boxes.shape[0] != 0:
            conf = float(results.boxes.conf)
            isWearingHardHat = True if int(results.boxes.cls) == 0 else False
            print(conf, isWearingHardHat)
            json.dump({'conf': conf, 'isWearingHardHat': isWearingHardHat}, open('data.json', 'w'))
    
        # Visualize the results on the frame
        annotated_frame = results.plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        key = cv2.waitKey(1)    
        # Break the loop if 'q' is pressed
        if key == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()