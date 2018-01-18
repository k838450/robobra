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
    elif x<=125 or 145<=x:
        rmb.drive_direct(30.0,-30.0)
        if 125<x<145:
            pass
    else :
        rmb.drive_direct(550,550)


while True:
    x,y,w,h,im =  rmb.detect_col("red") 

    if count<=3:
        run(x,w)
    elif 3<count:
        print("end")
        rmb.drive_direct(0,0)

    key = cv2.waitKey(30)

    if key==ord('q'):
        break
