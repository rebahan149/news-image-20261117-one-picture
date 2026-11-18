# Fit the repaired 1024x1536 front page into the competition gate:
# <=1024x1024 px and <=1 MiB PNG. Scales to height 1024, centres on a
# paper-coloured square canvas, quantizes if needed.
from PIL import Image
import os

SRC = 'patched-native.png'  # output of build/repair.py
im = Image.open(SRC)
nh = 1024
nw = round(im.width * nh / im.height)
res = im.resize((nw, nh), Image.LANCZOS)
cv = Image.new('RGB', (1024, 1024), (245, 234, 216))
cv.paste(res, ((1024 - nw) // 2, 0))
cv.save('entry.png')
if os.path.getsize('entry.png') > 1048576:
    cv.quantize(colors=256, method=Image.MEDIANCUT).save('entry.png', optimize=True)
cv.save('preview.jpg', quality=88)
print('entry.png:', cv.size, os.path.getsize('entry.png'), 'bytes')
