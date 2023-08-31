import qrcode

img = qrcode.make("https://www.linkedin.com/in/collins-ochieng-9b2303251/")
img.save("Linkedin.png")
img.show()
