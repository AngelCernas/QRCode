import cv2
import numpy as np
import time
import pandas as pd

capture = cv2.VideoCapture(0)

while(capture.isOpened()):
    ret, frame = capture.read()

    if (cv2.waitKey(1) == ord('s')):
        break

    qrDetector = cv2.QRCodeDetector()
    data,bbox, rectifiedImage = qrDetector.detectAndDecode(frame)


    if len(data) > 0:
       # print(f'Dato{data}')
        cv2.imshow('WebCam',rectifiedImage)

        fraccionada = data.split(',')
        consecutivo = fraccionada[0]
        tarima = fraccionada[1]
        area = fraccionada[2]
        bloque = fraccionada[3]
        print(consecutivo)
        print(tarima)
        print(area)
        print(bloque)
        time.sleep(3)

        parametros = {
            'Consecutivo': [f'{consecutivo}'],
            'Tarima': [f'{tarima}'],
            'Area': [f'{area}'],
            'Bloque': [f'{bloque}']
        }
        df = pd.DataFrame(parametros)
        df.to_excel('inventario.xlsx', index=False)  # index=False para no incluir los índices en el archivo

    else:
        cv2.imshow('WebCam', frame)

capture.release()
cv2.destroyAllWindows()