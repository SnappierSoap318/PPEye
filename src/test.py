from ultralyticsplus import YOLO
import numpy as np 

# imgs = ['Dataset/images/1/190.png', 'Dataset/images/2/130.png']

model = YOLO('models/yolo8n-hard-hat-det.pt')
results = model.predict('Dataset/videos/2.mp4', show = True, save_conf = True, stream = True)
for result in results:
    if result.boxes.shape[0] != 0:
        print(float(result.boxes.conf), int(result.boxes.cls))

