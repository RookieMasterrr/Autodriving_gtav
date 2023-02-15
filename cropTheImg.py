from grabscreen import grab_screen
import cv2

while True:

    screen = grab_screen(region=(0,40,800,620))
    img = screen[0:450,200:600]
    # cv2.line(img,(200,0),(200,600),(0,0,255))
    # cv2.line(img,(600,0),(600,600),(0,0,255))
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imshow('img',img)
    cv2.waitKey(1)& 0xFF == ord('q')
