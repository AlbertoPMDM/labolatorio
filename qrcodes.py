import segno
from PIL import Image, ImageDraw, ImageFont
import os
import shutil
from math import ceil, floor
from itertools import cycle

# a partir de que numero generar la hoja
start = 6

### Hoja A4
MARGINS = 7
PAGESIZE = (216,279)


PXPERMM = 12 # para ~300dpi en la impresion
QRSIZE = 29 * PXPERMM
QRMARGIN = 4 * PXPERMM
MMTOPX = QRSIZE / 22 # para qr M1-H

MARGINSPX = ceil(MARGINS*MMTOPX)
PAGESIZEPX = (ceil(PAGESIZE[0]*MMTOPX), ceil(PAGESIZE[1]*MMTOPX))
print(PAGESIZEPX, 29 * MMTOPX)
print(floor((PAGESIZEPX[0]-2*MARGINSPX)/QRSIZE))
print(floor((PAGESIZEPX[1]-2*MARGINSPX)/QRSIZE))
print(floor((PAGESIZEPX[0]-2*MARGINSPX)/QRSIZE)*floor((PAGESIZEPX[1]-2*MARGINSPX)/QRSIZE))

sheet = Image.new("RGB", PAGESIZEPX, "white")

os.mkdir("qr")

for i in range (start,start+floor((PAGESIZEPX[0]-2*MARGINSPX)/QRSIZE)*floor((PAGESIZEPX[1]-2*MARGINSPX)/QRSIZE)):
    segno.make(f"{i}", micro=False, error="H").save(f"qr/{i}.png", scale=PXPERMM)
    with Image.open(f"qr/{i}.png") as tmpimg:
        ImageDraw.Draw(tmpimg).text((QRMARGIN,0), f"{i}", font=ImageFont.truetype('arial.ttf', QRMARGIN), stroke_width=2)
        tmpimg.save(f"qr/{i}.png")


qrs = cycle([Image.open(f"qr/{i}.png") for i in range (start,start+floor((PAGESIZEPX[0]-2*MARGINSPX)/QRSIZE)*floor((PAGESIZEPX[1]-2*MARGINSPX)/QRSIZE))])



for i in range(0, floor((PAGESIZEPX[0]-2*MARGINSPX)/QRSIZE)):
    for j in range(0,floor((PAGESIZEPX[1]-2*MARGINSPX)/QRSIZE)):
        sheet.paste(next(qrs), (i*QRSIZE+MARGINSPX, j*QRSIZE+MARGINSPX))

sheet.save(f"{start}.pdf")

shutil.rmtree("qr")