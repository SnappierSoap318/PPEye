import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
# model = YOLO('models/yolo8s-hard-hat-det.pt') # slightly slower but kinda accurate
model = YOLO('models/yolo8n-hard-hat-det.pt') # Fastest and more accurate
# model = YOLO('models/yolo8m-ppe.pt') # More personal protective equipment (PPE) detection, very low accuracy and slow.

# Open the video file
video_path = "Dataset/videos/4.mp4"
cap = cv2.VideoCapture(video_path)
# cap = cv2.VideoCapture(0)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
       
    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame, stream = True)

        for result in results:
            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            print(result.probs)

            # Display the annotated frame
            cv2.imshow("YOLOv8 Inference", annotated_frame)

        key = cv2.waitKey(1)    
        # Break the loop if 'q' is pressed
        if key == ord("q"):
            break
        if key == ord("s"):
            cv2.waitKey(-1)
            cv2.imwrite("Dataset/images/screenshots/1.png", annotated_frame)

        if key == ord("p"):
            cv2.waitKey(-1)
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()