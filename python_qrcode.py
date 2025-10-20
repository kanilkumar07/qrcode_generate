import qrcode
from PIL import Image   #image ko import karege aur pil ko

qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
box_size = 10,border=4,)   #isme ham decide karege ki version, error correction,box size aur border variable bana ke

qr.add_data("kumarkanilmahto")  #jo hamko dikhana hai usko ham isme fill karege

qr.make(fit=True)  #agar sahi hoga to qr ban jayega

img=qr.make_image(fill_color="red", back_color="blue")  #isme ham qr ka color change kar saskte hai

img.save("kanil1.png")   #uske baad save karege than run