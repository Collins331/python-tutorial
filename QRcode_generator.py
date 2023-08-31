import qrcode

data = "https://www.instagram.com/collins.linc/"
qr = qrcode.QRCode(
    version=1,  # QR code version (1 to 40, higher is more complex)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box/pixel in the QR code
    border=4,  # Border size around the QR code
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("Instagram_QRCode.png")  # Save the QR code image to a file
