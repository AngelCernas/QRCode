import qrcode

img = qrcode.make("601036,1,TIMI,08B")
f = open("output.png", "wb")
img.save(f)
f.close()