from ultralytics import YOLO
import cv2
import cvzone
import math
#from sort import *

def detect(port_n):
  cap=cv2.VideoCapture('cars_'+port_n+'.mp4')
  #cap.set(3,480)
  #cap.set(4,480)

  model=YOLO('yolov8n.pt')

  mask=cv2.imread('mask_'+port_n+'.png')

  classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

  
  success,img=cap.read()
  #print(img.shape)
  #print(mask.shape)
  img=cv2.resize(img,(700,400))
  mask=cv2.resize(mask,(700,400))
  imgregion=cv2.bitwise_and(mask,img)
  imggraphics=cv2.imread("graphics_1.png",cv2.IMREAD_UNCHANGED)
  #img=cvzone.overlayPNG(img,imggraphics,(0,0))
  results=model(imgregion,stream=True)
  #detections=np.empty((0, 5))
    
  cnt=0
  for r in results:
        boxes=r.boxes
        for box in boxes:
            #Bounding boxes
            x1,y1,x2,y2=box.xyxy[0]
            x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
            w,h=x2-x1,y2-y1
            
            #confidence
            conf=(math.ceil(box.conf[0]*100))/100
            #conf=str(conf)
            #cvzone.cornerRect(img,(x1,y1,w,h))
            #cv2.putText(img,conf,(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2,cv2.LINE_AA)
            #Classes
            cls=int(box.cls[0])
            #cv2.putText(img,str(classNames[cls]),(x1,y1+10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1,cv2.LINE_AA)

            if classNames[cls]=="car" or classNames[cls]=="truck" or classNames[cls]=="motorbike" or classNames[cls]=="bus" and conf>0.3:
                #cvzone.cornerRect(img, (x1, y1, w, h), l=5, rt=2)
                cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=0.8, thickness=1,offset=3)
                cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),1)
                cnt=cnt+1

                



    #  restracker=tracker.update(detections)

    #cv2.line(img,(limits[0],limits[1]),(limits[2],limits[3]),(0,0,255),3)



      #cvzone.putTextRect(img, f'Count:{len(totalcnt)}', (50,50))
          
  cv2.putText(img,str(cnt),(50,100),cv2.FONT_HERSHEY_PLAIN,5,(50,50,255),3)

  cv2.imshow('Lane '+port_n,img)
    #cv2.imshow('ImageRegion',imgregion)
  return cnt




  #cap.release()
  #cv2.destroyAllWindows()

if __name__=="__main__":
   detect('4')
