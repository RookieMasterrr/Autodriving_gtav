import cv2
import numpy as np
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
# net = cv2.dnn.readNet("yolov3-tiny.weights", "yolov3-tiny.cfg")
classes = []

with open("coco.names.txt", "r") as f:
    classes = [line.strip() for line in f.readlines()]

layersNames = net.getLayerNames()
outputlayer = [layersNames[i - 1] for i in net.getUnconnectedOutLayers()]

img = cv2.imread("testImg.png")

height,width,channels = img.shape

blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

net.setInput(blob)
outs = net.forward(outputlayer)


boxes=[]
confidences=[]
class_ids=[]

for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.6:
            center_x = int(detection[0]*width)
            center_y = int(detection[1]*height)
            w = int(detection[2]*width)
            h = int(detection[3]*height)

            x = int(center_x-w/2)
            y = int(center_y-h/2)

            boxes.append([x,y,w,h])
            confidences.append(confidence)
            class_ids.append(class_id)    
            


indexes = cv2.dnn.NMSBoxes(boxes,confidences,0.5,0.4)

for i in range(len(boxes)):
    if i in indexes:    
        x,y,w,h=boxes[i]
        label = classes[class_ids[i]]
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0))
            # print(type(classes[class_id])
        cv2.putText(img,label,(x,y+30),cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,0),3)


cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()