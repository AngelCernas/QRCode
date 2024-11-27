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

        fraccionada = data.split(',')
        consecutivo = fraccionada[0]
        tarima = fraccionada[1]
        area = fraccionada[2]
        bloque = fraccionada[3]


    else:
        cv2.imshow('WebCam', frame)

capture.release()
cv2.destroyAllWindows()