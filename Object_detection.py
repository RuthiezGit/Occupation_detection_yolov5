import torch

model = torch.hub.load(r'C:\Users\USER\Desktop\RAIN\Extra_classes\ML & DL\yolov5-master', source='local', model='yolov5l')
# model.conf = 0.4
model.iou=0.9
# print(model.iou)
result = model(r'C:\Users\USER\Pictures\Camera Roll/photo anniversary 1.jpg')
print(result.show())
print(result.pandas().xyxy[0])