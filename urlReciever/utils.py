
def get_name_ext(filepath):
    import os
    fullName      = os.path.basename(filepath)
    filename, ext = os.path.splitext(fullName)
    return filename, ext

def media_upload_path(instance, filepath):
    
    return f"qrcodes/"

def make_my_QRcode_bitch(qrData:str, saveAbsoulutePath:str='qrcode', saveit:bool=False, format:str ='PNG'):

    from qrcode.image.pil import PilImage
    from qrcode.main import QRCode
    from random import randint
    myQrCode = QRCode(border=4, box_size=10, image_factory=PilImage)


    myQrCode.add_data(qrData)
    myQrCode.make()
    img = myQrCode.make_image()

    if saveit:

        if saveAbsoulutePath:
            img.save(stream=saveAbsoulutePath, format=format)
        else:
            name = f"{str(randint(1, 5000))}.{format}"
            img.save(stream=name, format=format)

    return img

image = make_my_QRcode_bitch('sag')


