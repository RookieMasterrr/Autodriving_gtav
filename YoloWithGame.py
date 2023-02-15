import cv2
import numpy as np
import time
from grabscreen import grab_screen
import math

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
# net = cv2.dnn.readNet("yolov3-tiny.weights", "yolov3-tiny.cfg")
classes = []

with open("coco.names.txt", "r") as f:
    classes = [line.strip() for line in f.readlines()]

layersNames = net.getLayerNames()
outputlayer = [layersNames[i - 1] for i in net.getUnconnectedOutLayers()]

def theLenOfDiagonal(w,h):
    return math.sqrt(w*w+h*h)

def analyzeTheImg(img):

    tooClose = 0

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
            Diagonal=theLenOfDiagonal(w,h)

            cv2.putText(img,label,(x,y+30),cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,0),3)
            Diagonal=theLenOfDiagonal(w,h)
            if(int(Diagonal)>120):
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255))
                cv2.line(img,(x,y),(x+w,y+h),(0,0,255))
                cv2.putText(img,"TOO CLOSE!!!",(100,100),cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255),3)
                tooClose=1
                # print("WARNING")
            else:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0))
                cv2.line(img,(x,y),(x+w,y+h),(0,255,0))


    return img,tooClose


if __name__=='__main__':
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    # net = cv2.dnn.readNet("yolov3-tiny.weights", "yolov3-tiny.cfg")
    classes = []

    with open("coco.names.txt", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    layersNames = net.getLayerNames()
    outputlayer = [layersNames[i - 1] for i in net.getUnconnectedOutLayers()]


    # img = grab_screen(region=(0,40,800,620))
    # analyzeTheImg(img)
    # cv2.imshow("img",img)
    # cv2.waitKey(1)



    while True:
        img = grab_screen(region=(0,40,800,620))
        # img = cv2.resize(img,(160,120))
        analyzeTheImg(img)
        cv2.imshow("img",img)
        cv2.waitKey(1)
        # for i in range(0,2):
        #     # print('get in the car')
        #     # print(i)
        #     time.sleep(1)
