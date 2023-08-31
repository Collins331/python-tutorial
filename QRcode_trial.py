import qrcode
from PIL import Image

# Data to encode in the QR code
data = "https://www.youtube.com/watch?v=eIho2S0ZahI&ab_channel=TED"

# Generate QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Create image from the QR code
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the image
qr_image.save("qr_code.png")

# Open the saved image
qr_image.show()
