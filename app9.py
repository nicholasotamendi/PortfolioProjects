#QR code generator
#install all libraries needed 
#create a function that collects the link and converts it to a qr code 
#save the qr code as an image and run the function 

import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 13,
        border = 4
    )

    qr.add_data(text)
    qr.make()
    img = qr.make_image(fill_color = "blue", back_color = "pink")
    img.save("qrimg.png")


url = input("Enter your URL: ")
generate_qrcode(url)