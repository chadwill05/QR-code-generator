import os
import qrcode

img = qrcode.make(input("Input a link you would like to be turned into a QR code. : "))

img.save("qr.png", "PNG")
os.system("open qr.png")
