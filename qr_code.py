import qrcode
from PIL import image
#data to encode in the QR code
data = "https://www.youtube.com/watch?v=eIho2S0ZahI&ab_channel=TED"

#generate QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

#Create image from the QR code
image = qr.make_image(fill='black', back_color="white")

# Save the image
image.save("qr_code.png")
image.open("qr_code.png")