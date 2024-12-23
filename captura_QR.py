import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while(capture.isOpened()):
    ret, frame = capture.read()

    if (cv2.waitKey(1) == ord('s')):
        break

    qrDetector = cv2.QRCodeDetector()
    data,bbox, rectifiedImage = qrDetector.detectAndDecode(frame)


    if len(data) > 0:
        print(f'Dato{data}')
        cv2.imshow('WebCam',rectifiedImage)
    else:
        cv2.imshow('WebCam', frame)

capture.release()
cv2.destroyAllWindows()