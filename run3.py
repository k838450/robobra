import roombaSimAPI
import time
import cv2

rmb = roombaSimAPI.RoombaSim()

cv2.namedWindow("camera")
count = 0

def run(x,w):
    global count
    if 125<x<145 and 35 < w:
        t1=time.time()
        while 1:
            t2=time.time()
            if int(t2)-int(t1)<=1:
                rmb.drive_direct(-160.0,160.0)
            elif 1<int(t2)-int(t1)<7:
                rmb.drive_direct(700.0,700.0)
            else:
                break
        count = count+1
        print(count)
    #elif 40 < w:
        #rmb.drive_direct(-10,-10)
    elif x<=125 or 145<=x:
        rmb.drive_direct(30.0,-30.0)
        if 125<x<145:
            pass
    else :
        rmb.drive_direct(550,550)
    #if im!=None:
        #cv2.imshow("camera", im)
    print(x,w)


while True:
    x,y,w,h,im =  rmb.detect_col("red") 
    x2,y2,w2,h2,im2 = rmb.detect_col("blue")

    if count<4:
        run(x,w)
    elif 4<=count<=11:
        run(x2,w2)
    elif 11<count:
        print("end")
        rmb.drive_direct(0,0)

    key = cv2.waitKey(30)

    if key==ord('q'):
        break


