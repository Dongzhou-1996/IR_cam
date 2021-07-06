import cv2
import time
cap = cv2.VideoCapture('rtsp://admin:admin@192.168.1.123:554/cam/realmonitor?channel=1&subtype=0')
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
writer = cv2.VideoWriter('ir_video.mp4', fourcc, 20.0, (640, 512), True)

while True:
    ret, frame = cap.read()

    if ret:
        print('=> frame shape: {}'.format(frame.shape))
        cv2.imshow('ir image', frame)
        writer.write(frame)
    else:
        print('=> time {}: failed to load IR image'.format(time.time()))

    if cv2.waitKey(1) == 27:
        break
writer.release()
cap.release()