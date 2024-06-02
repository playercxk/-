# %%
from pyzbar.pyzbar import decode
from PIL import Image,ImageEnhance
import os

def qrcode_recongnize(filepath,filename):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  
        image_type = []
        try:
            # 读取图片
            img = Image.open(filepath + filename).convert('RGB')
            # 增加亮度
            img = ImageEnhance.Brightness(img).enhance(1.0)
            # 锐利化
            img = ImageEnhance.Sharpness(img).enhance(1.5)
            # 增加对比度
            img = ImageEnhance.Contrast(img).enhance(2.0)
            # 灰度化
            img = img.convert('L')
            # 解码二维码
            result = decode(img)
            if len(result)>0:
                image_type.append('qrcode')
                os.makedirs(filepath+'qrcode',exist_ok=True)
                img.save(filepath+'qrcode/'+filename)
            else:
                image_type.append('unqrcode')
        except:
            image_type.append('unqrcode')
        return image_type
    
    else:
        return 'not image'

if __name__ == '__main__':

    filepath="D:/desktop/code/py/数字图像处理/"#图片路径，调试时应更换成自己的图片文件夹
    for parent,dirnames,filenames in os.walk(filepath):
     for filename in filenames:
        kk=qrcode_recongnize(filepath,filename)
        print(filename,kk)
# %%
