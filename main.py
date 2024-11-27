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
        Px = fraccionada[4]
        Py = fraccionada[5]
        Pz = fraccionada[6]
        bultos = fraccionada[7]
        peso = fraccionada[8]
        cubicaje = fraccionada[9]
        marca = fraccionada[10]
        embalaje = fraccionada[11]

        print(consecutivo)
        print(tarima)
        print(area)
        print(bloque)
        print(Px)
        print(Py)
        print(Pz)
        print(bultos)
        print(peso)
        print(cubicaje)
        print(marca)
        print(embalaje)


        time.sleep(3)

        parametros = {
            'Consecutivo': [f'{consecutivo}'],
            'Tarima': [f'{tarima}'],
            'Area': [f'{area}'],
            'Bloque': [f'{bloque}'],
            'Posicion X': [f'{Px}'],
            'Posicion y': [f'{Py}'],
            'Posicion Z': [f'{Pz}'],
            'Bultos': [f'{bultos}'],
            'Peso': [f'{peso}'],
            'Cubicaje': [f'{cubicaje}'],
            'Marca': [f'{marca}'],
            'Embalaje': [f'{embalaje}']

        }
        df = pd.DataFrame(parametros)
        df.to_excel('inventario.xlsx', index=False)  # index=False para no incluir los índices en el archivo

    else:
        cv2.imshow('WebCam', frame)

capture.release()
cv2.destroyAllWindows()