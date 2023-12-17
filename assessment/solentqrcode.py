import pyqrcode
import png
link = "www.solent.ac.uk"
qr_code = pyqrcode.create(link)
qr_code.png("solentscaids.png", scale=5)