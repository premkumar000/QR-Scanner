import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

data = "https://www.linkedin.com/in/prem-kumarkaatukuri-7aba882b1"
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")
img.save("test.png")