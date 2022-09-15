import pytesseract as ocr
import argparse
import numpy as np
import cv2

from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to input image to be OCRed')
ap.add_argument('-d', '--digits', type=int, default=1, help='OCR digits only')
args = vars(ap.parse_args())

imagem = Image.open(args['image'])
options = ''

if args['digits'] > 0:
    options = 'outputbase digits'

npimagem = np.asarray(imagem).astype(np.uint8)
npimagem[:, :,0] = 0
npimagem[:, :,2] = 0

im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY)
ret, thresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
binimagem = Image.fromarray(thresh)

#binimagem.save('resultado.jpg')

phrase = ocr.image_to_string(imagem, config=options)
#, config='digits'
print(phrase)

