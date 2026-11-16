"""Draw the tab pictures of The Treasury and RogueLike Shop shops.

Gold on navy, the same colors as the mod icons (mod-icons/make_icons.py). Every picture is
408x256 (the size the trade screen shows a shop picture at), drawn 4x larger and scaled
down for smooth edges. Run `python tools/make_shop_icons.py`; it writes
graphics/factions/tes_shop_<key>.png. Not shipped; only the PNGs are.
"""
import math
import os

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "graphics", "factions")
W, H, S = 408, 256, 4
GOLD = (200, 170, 80, 255)
DARK_GOLD = (140, 115, 50, 255)
NAVY = (20, 30, 48, 255)
CX, CY = W / 2, H / 2


def p(*xy):
    """Scale 1x coordinates to the 4x canvas."""
    return [v * S for v in xy]


def pts(points):
    return [(x * S, y * S) for x, y in points]


def frame(d):
    d.rounded_rectangle(p(0, 0, W - 1, H - 1), radius=22 * S, fill=NAVY)
    d.rounded_rectangle(p(8, 8, W - 9, H - 9), radius=16 * S, outline=GOLD, width=5 * S)


def gem(d):
    top, mid, bot = 48, 100, 212
    outer = [(CX - 52, top), (CX + 52, top), (CX + 92, mid), (CX, bot), (CX - 92, mid)]
    d.polygon(pts(outer), fill=GOLD)
    line = dict(fill=NAVY, width=4 * S)
    d.line(pts([(CX - 92, mid), (CX + 92, mid)]), **line)
    for a, b in [((CX - 52, top), (CX - 30, mid)), ((CX - 30, mid), (CX, top)), ((CX, top), (CX + 30, mid)),
                 ((CX + 30, mid), (CX + 52, top)), ((CX - 30, mid), (CX, bot)), ((CX + 30, mid), (CX, bot))]:
        d.line(pts([a, b]), **line)


def blueprint(d):
    x0, y0, x1, y1 = CX - 120, 52, CX + 120, 204
    d.rectangle(p(x0, y0, x1, y1), outline=GOLD, width=5 * S)
    for i in range(1, 6):
        x = x0 + (x1 - x0) * i / 6
        d.line(p(x, y0, x, y1), fill=DARK_GOLD, width=1 * S)
    for i in range(1, 4):
        y = y0 + (y1 - y0) * i / 4
        d.line(p(x0, y, x1, y), fill=DARK_GOLD, width=1 * S)
    ship = [(CX + 80, CY), (CX + 20, CY - 26), (CX - 40, CY - 26), (CX - 60, CY - 50), (CX - 76, CY - 50),
            (CX - 68, CY - 14), (CX - 84, CY - 10), (CX - 84, CY + 10), (CX - 68, CY + 14),
            (CX - 76, CY + 50), (CX - 60, CY + 50), (CX - 40, CY + 26), (CX + 20, CY + 26)]
    d.polygon(pts(ship), outline=GOLD, width=4 * S)
    d.line(pts([(CX - 40, CY), (CX + 50, CY)]), fill=GOLD, width=3 * S)


def card(d, x0, y0, x1, y1):
    notch = 26
    d.polygon(pts([(x0, y0), (x1 - notch, y0), (x1, y0 + notch), (x1, y1), (x0, y1)]), fill=GOLD)
    for i in range(5):
        x = x0 + 22 + i * 18
        d.rectangle(p(x, y1 - 30, x + 10, y1 - 12), fill=NAVY)


def hexagon(cx, cy, r, rot=0):
    return [(cx + r * math.cos(math.radians(60 * i + rot)), cy + r * math.sin(math.radians(60 * i + rot)))
            for i in range(6)]


def modspec(d):
    card(d, CX - 90, 44, CX + 90, 212)
    d.polygon(pts(hexagon(CX, 112, 46, 30)), fill=NAVY)
    d.polygon(pts(hexagon(CX, 112, 30, 30)), fill=GOLD)
    d.polygon(pts(hexagon(CX, 112, 14, 30)), fill=NAVY)


def chip(d):
    x0, y0, x1, y1 = CX - 70, CY - 70, CX + 70, CY + 70
    for i in range(5):
        o = -56 + i * 28
        d.rectangle(p(x0 - 22, CY + o - 5, x0, CY + o + 5), fill=GOLD)
        d.rectangle(p(x1, CY + o - 5, x1 + 22, CY + o + 5), fill=GOLD)
        d.rectangle(p(CX + o - 5, y0 - 22, CX + o + 5, y0), fill=GOLD)
        d.rectangle(p(CX + o - 5, y1, CX + o + 5, y1 + 22), fill=GOLD)
    d.rounded_rectangle(p(x0, y0, x1, y1), radius=10 * S, fill=GOLD)
    d.rounded_rectangle(p(x0 + 12, y0 + 12, x1 - 12, y1 - 12), radius=6 * S, fill=NAVY)


def star(cx, cy, r_out, r_in, n=5, rot=-90):
    out = []
    for i in range(n * 2):
        r = r_out if i % 2 == 0 else r_in
        a = math.radians(rot + i * 180 / n)
        out.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return out


def exotic(d):
    chip(d)
    d.polygon(pts(star(CX, CY + 3, 44, 18)), fill=GOLD)


def upgrade(d):
    chip(d)
    for dy in (-22, 12):
        y = CY + dy
        d.line(pts([(CX - 34, y + 22), (CX, y - 8), (CX + 34, y + 22)]), fill=GOLD, width=10 * S, joint="curve")


def flask(d):
    neck_w, top = 22, 46
    d.rectangle(p(CX - neck_w - 8, top, CX + neck_w + 8, top + 14), fill=GOLD)
    body = [(CX - neck_w, top + 14), (CX + neck_w, top + 14), (CX + neck_w, top + 64), (CX + 76, 196),
            (CX + 66, 210), (CX - 66, 210), (CX - 76, 196), (CX - neck_w, top + 64)]
    d.polygon(pts(body), outline=GOLD, width=5 * S)
    liquid = [(CX - 50, 150), (CX + 50, 150), (CX + 76, 196), (CX + 66, 210), (CX - 66, 210), (CX - 76, 196)]
    d.polygon(pts(liquid), fill=GOLD)
    for x, y, r in [(CX - 12, 128, 6), (CX + 14, 112, 4), (CX + 2, 92, 3)]:
        d.ellipse(p(x - r, y - r, x + r, y + r), fill=GOLD)


def star_chart(d):
    for r in (40, 76, 108):
        d.ellipse(p(CX - r * 1.6, CY - r * 0.9, CX + r * 1.6, CY + r * 0.9), outline=DARK_GOLD, width=2 * S)
    nodes = [(CX - 120, CY + 40), (CX - 60, CY - 50), (CX + 10, CY + 10), (CX + 70, CY - 60), (CX + 130, CY + 30)]
    d.line(pts(nodes), fill=GOLD, width=3 * S)
    for i, (x, y) in enumerate(nodes):
        size = 20 if i == 2 else 12
        d.polygon(pts(star(x, y, size, size * 0.4, n=4, rot=0)), fill=GOLD)


def gear(d):
    teeth, r_out, r_in = 10, 86, 66
    poly = []
    for i in range(teeth * 4):
        a = math.radians(i * 360 / (teeth * 4))
        r = r_out if (i % 4) in (1, 2) else r_in
        poly.append((CX + r * math.cos(a), CY + r * math.sin(a)))
    d.polygon(pts(poly), fill=GOLD)
    d.ellipse(p(CX - 34, CY - 34, CX + 34, CY + 34), fill=NAVY)
    d.rectangle(p(CX - 20, CY - 20, CX + 20, CY + 20), fill=GOLD)
    d.rectangle(p(CX - 10, CY - 10, CX + 10, CY + 10), fill=NAVY)


def swarm(d):
    for i in range(70):
        t = i / 70
        a = t * 4.2 * math.pi
        r = 18 + t * 92
        x = CX + r * math.cos(a) * 1.25
        y = CY + r * math.sin(a) * 0.82
        size = 3 + 7 * (1 - t)
        d.ellipse(p(x - size, y - size, x + size, y + size), fill=GOLD)
    d.ellipse(p(CX - 16, CY - 16, CX + 16, CY + 16), fill=GOLD)


def engram(d):
    for r in (92, 62):
        d.polygon(pts(hexagon(CX, CY, r, 0)), outline=GOLD, width=5 * S)
    inner = hexagon(CX, CY, 32, 0)
    for x, y in inner:
        d.line(pts([(CX, CY), (x, y)]), fill=GOLD, width=3 * S)
    for (x0, y0), (x1, y1) in zip(inner, hexagon(CX, CY, 62, 0)):
        d.line(pts([(x0, y0), (x1, y1)]), fill=GOLD, width=3 * S)
    for x, y in inner + [(CX, CY)]:
        d.ellipse(p(x - 9, y - 9, x + 9, y + 9), fill=GOLD)


def cipher(d):
    cx, cy = CX - 70, CY
    d.ellipse(p(cx - 50, cy - 50, cx + 50, cy + 50), fill=GOLD)
    d.ellipse(p(cx - 22, cy - 22, cx + 22, cy + 22), fill=NAVY)
    d.rectangle(p(cx + 44, cy - 12, CX + 120, cy + 12), fill=GOLD)
    for x, h in [(CX + 70, 34), (CX + 98, 24)]:
        d.rectangle(p(x, cy + 12, x + 16, cy + 12 + h), fill=GOLD)


ICONS = {
    "specials": gem,
    "blueprints": blueprint,
    "modspecs": modspec,
    "exotics": exotic,
    "upgrades": upgrade,
    "rl_consumables": flask,
    "rl_star_charts": star_chart,
    "rl_hull_items": gear,
    "rl_nanoswarms": swarm,
    "rl_engrams": engram,
    "rl_ciphers": cipher,
}


def main():
    os.makedirs(OUT, exist_ok=True)
    for key, draw in ICONS.items():
        img = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        frame(d)
        draw(d)
        img = img.resize((W, H), Image.LANCZOS)
        path = os.path.join(OUT, "tes_shop_%s.png" % key)
        img.save(path, optimize=True)
        print(path)


if __name__ == "__main__":
    main()
