import cv2
import numpy as np
import time
import pandas as pd
from datetime import datetime
from openpyxl import load_workbook


capture = cv2.VideoCapture(0)
fecha_hora = datetime.now().strftime("%Y-%m-%d")

while(capture.isOpened()):
    ret, frame = capture.read()

    if (cv2.waitKey(1) == ord('s')):
        break

    qrDetector = cv2.QRCodeDetector()
    data,bbox, rectifiedImage = qrDetector.detectAndDecode(frame)


    if len(data) > 0:
       # print(f'Dato{data}')
        fila_insert = 2
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

        #Formato del archivo
        df_existente = pd.read_excel('formato.xlsx')

        time.sleep(3)
        parametros = {
            consecutivo,
            tarima,
            area,
            bloque,
            Px,
            Py,
            Pz,
            bultos,
            peso,
            cubicaje,
            marca,
            embalaje

        }
        df = pd.DataFrame(parametros)

        df_concatenador =  pd.concat([df_existente, df], ignore_index=True)
        #df_concatenador.to_excel(f'{fecha_hora}.xlsx', index=False)
        df.to_excel(f'{fecha_hora}.xlsx', index=False)  # index=False para no incluir los índices en el archivo

    else:
        cv2.imshow('WebCam', frame)

capture.release()
cv2.destroyAllWindows()