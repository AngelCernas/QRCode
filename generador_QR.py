import qrcode

#"601036,1,TIMI,08B"

def generador_qr (texto):
    qr = qrcode.make(texto)
    qr.save("QR.png")

texto = "601036,1,TIMI,08B"
generador_qr(texto)