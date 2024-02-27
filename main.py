import qrcode

features = qrcode.QRCode (
  version=1, 
  box_size=40, 
  border=3
)

features.add_data("https://github.com/SinchanaBPgit/QR-code-generation")
features.make(fit=True)
qr_code = features.make_image(fill_color="black", back_color="white")
qr_code.save('qrcode.png')
