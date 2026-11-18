from PIL import Image, ImageDraw, ImageFont
from collections import Counter
import statistics, os

SRC = '/home/hatch/workspace/user/media_library/image/e2a5bb25-d97a-4db1-bafb-58092fc1b35e.png'
OUT = '/home/hatch/workspace/makefun/news-image-20261117-userb'
im = Image.open(SRC).convert('RGB')
d = ImageDraw.Draw(im)
INK = (30, 27, 24)

def serif(size, bold=True):
    return ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSerif-%s.ttf' % ('Bold' if bold else 'Regular'), size)
def sans(size):
    return ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf', size)

# paper = mode color of the list interior in the ORIGINAL
region = im.crop((508, 918, 1013, 1470)).resize((120, 120))
PAPER = Counter(region.getdata()).most_common(1)[0][0]
orange_pts = [im.getpixel((x, y)) for x in range(300, 405, 7) for y in range(212, 238, 4)
              if im.getpixel((x, y))[0] > 200 and 80 < im.getpixel((x, y))[1] < 180 and im.getpixel((x, y))[2] < 80]
ORANGE = tuple(int(statistics.median([p[i] for p in orange_pts])) for i in range(3))
print('PAPER', PAPER, 'ORANGE', ORANGE)

# TAG
d.rectangle((262, 205, 413, 243), fill=ORANGE)
f = sans(33)
word = 'EUROPE'
tw = d.textlength(word, font=f)
tb = d.textbbox((0, 0), word, font=f)
d.text((262 + (151 - tw) / 2, 224 - (tb[3] - tb[1]) / 2 - tb[1]), word, font=f, fill=(255, 255, 255))

# PANELS
def panel(box, hx, head, dek):
    d.rectangle(box, fill=PAPER)
    d.line([(hx, 494), (box[2] - 6, 494)], fill=(90, 80, 70), width=2)
    fh = serif(27)
    for i, ln in enumerate(head):
        d.text((hx, 404 + i * 30), ln, font=fh, fill=INK)
    fd = serif(18, False)
    for i, ln in enumerate(dek):
        d.text((hx, 500 + i * 22), ln, font=fd, fill=INK)

panel((216, 400, 416, 556), 222, ["1,441 drones", "downed in a", "single night"], ["Moscow counts the", "overnight barrage."])
panel((624, 400, 824, 556), 630, ["US base struck", "in Bahrain as", "Hormuz flares"], ["Amid rising tensions", "in the Hormuz strait."])

# PANEL 6 dek
d.rectangle((22, 818, 130, 845), fill=PAPER)
d.text((24, 820), 'President', font=serif(20, False), fill=INK)

# LIST redraw
d.rectangle((508, 918, 1013, 1470), fill=PAPER)
LEFT = [
    "Serbia's student list\nprepares to take seats",
    "US measles elimination\nstatus is lost",
    "UK sanctions settlement\nentities",
    "Settler gunfire kills\nwoman near Jericho",
    "Germany urges more aid\ninto Gaza",
    "Jordan blocks Telegram",
    "Yemen bolsters defenses\nnear Aden",
    "Iraq resumes oil exports\nvia Turkey pipeline",
    "Mozambique opposition\nMondlane goes on trial",
    "UN talks on autonomous\nweapons face deadlock",
    "EU debates Ukraine peace\n-talk representation",
    "Mongolia's Khurelsukh\nfaces party revolt",
    "Sudan: 2,230 civilians\nkilled this year — UN",
    "France-Malaysia\nrare-earth partnership",
    "US chip access\nrestrictions tighten",
]
RIGHT = [
    "Earthquake prompts rescue\nalert in Indonesia",
    "Oil shipping disruptions\nraise energy fears",
    "Siberia plane crash\nkills 19 on board",
    "Kahana bill passes\nin Israel's Knesset",
    "Opposition Sözcü TV\nseized in Türkiye",
    "Canada backs Ukraine\nwith new aid package",
    "Turkey mediates\nBlack Sea talks",
    "Mexico boosts border\nsecurity measures",
    "India's GDP growth\nbeats forecasts",
    "World Court Myanmar\nruling in focus",
    "Iran's nuclear talks\nremain stalled",
    "France: 100,000-plus\nmarch for better pay",
    "Xi and Carney agree\nmore tariff cuts",
    "FIFA expands 2026\nWorld Cup plans",
    "G20 calls for stronger\nclimate action",
]
PALETTE = [(31, 95, 168), (210, 60, 40), (46, 139, 87), (232, 134, 46), (123, 79, 166), (146, 52, 44)]
fn = sans(14)

def draw_fit(x, y, text, maxw, base=16):
    size = base
    while size > 12 and d.textlength(text, font=serif(size)) > maxw:
        size -= 1
    d.text((x, y), text, font=serif(size), fill=INK)

def draw_entry(num, lines, bx, tx, top, maxw):
    col = PALETTE[(num - 11) % len(PALETTE)]
    d.ellipse([bx - 13, top - 2, bx + 13, top + 24], fill=col)
    s = str(num)
    tw = d.textlength(s, font=fn)
    tb = d.textbbox((0, 0), s, font=fn)
    d.text((bx - tw / 2, top + 11 - (tb[3] - tb[1]) / 2 - tb[1]), s, font=fn, fill=(255, 255, 255))
    for i, ln in enumerate(lines.split('\n')):
        draw_fit(tx, top + i * 21, ln, maxw)

for i, e in enumerate(LEFT):
    draw_entry(11 + i, e, 545, 575, 922 + i * 36, 187)
for i, e in enumerate(RIGHT):
    draw_entry(26 + i, e, 820, 845, 922 + i * 36, 163)

im.save(os.path.join(OUT, 'patched-native.png'))
print('patched v3 saved')
