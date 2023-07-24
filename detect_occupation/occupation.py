import cv2
import torch

cv2.namedWindow("preview")
web_cam = cv2.VideoCapture(0)

model = torch.hub.load(r'yolov5-master','custom', source='local', path=r'yolov5-master\best.pt')
model.iou=0.9
model.conf = 0.4


while web_cam.isOpened():
    rval, frame =web_cam.read()

    if rval:
        result = model(frame)
        # print(result.show())
        df = result.pandas().xyxy[0]
        for idx, row in df.iterrows():
            x1 = int (row["xmin"])
            y1 = int (row["ymin"])
            x2 = int (row["xmax"])
            y2 = int (row["ymax"])
            conf = round(row["confidence"], 2)
            class_name = row["name"]

            frame = cv2.rectangle(frame, (x1,y1),(x2,y2), (0,0,255), 1)
            frame = cv2.putText(frame, f'{class_name} {conf}', (x1-2, y1-5), 2, 1, (0,0,0), 1)
        cv2.imshow("preview", frame)
        key =cv2.waitKey(2)
        if key ==27:
            break

web_cam.release()
cv2.destroyWindow("preview")


result.save()