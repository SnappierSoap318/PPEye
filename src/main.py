import cv2
from ultralytics import YOLO
import base64
import json

conf = 0.0
isWearingHardHat = False

model = YOLO('models/yolo8n-hard-hat-det.pt') # Fastest and more accurate

# Open the video file
video_path = "Dataset/videos/2.mp4"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
       
    if success:
        # Run YOLOv8 inference on the frame
        results = model.predict(frame, save_conf=True, stream=True)
        for result in results:
            if result.boxes.shape[0] != 0:
                conf = float(result.boxes.conf[0])
                isWearingHardHat = True if int(result.boxes.cls[0]) == 0 else False
                print(conf, isWearingHardHat)
        
            # Visualize the results on the frame
            annotated_frame = result.plot()
            
            retval, buffer = cv2.imencode('.png', annotated_frame)
            png_as_text = base64.b64encode(buffer)
            
            with open('./data.json', 'w') as f:
                json.dump({'conf': conf, 'isWearingHardHat': isWearingHardHat, 'image': png_as_text.decode('utf-8')}, f)
            
            # Display the annotated frame
            cv2.imshow("Annotated Frame", annotated_frame)

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