


def make_my_QRcode_bitch(qrData:str, saveAdress:str='', format:str ='PNG', saveit:bool=False):

    from qrcode.image.pil import PilImage
    from qrcode.main import QRCode

    myQrCode = QRCode(border=4, box_size=10, image_factory=PilImage)


    myQrCode.add_data(qrData)
    myQrCode.make()
    img = myQrCode.make_image()

    if saveit:
        img.save(stream=saveAdress, format=format)

    return img


