"""
Edge Scripts architecture illustration — generates PNG in presentation style.
Run: python generate_arch.py
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

# ── Canvas ──────────────────────────────────────────────────────────────────
W, H = 1400, 780
OUT = "images/q1-2026/edge-scripts-illustration.png"

# ── Palette (matches presentation HTML) ─────────────────────────────────────
BG        = (7,   7,   7)
RED       = (242, 46,  13)
RED_DIM   = (160, 28,  8)
RED_GLOW  = (242, 46,  13, 55)
WHITE     = (255, 255, 255)
GREY      = (148, 156, 161)
GREY_DIM  = (70,  70,  70)
GREEN     = (0,   204, 102)
CLOUD_BG  = (28,  6,   6)
GW_BG     = (16,  16,  16)
DEV_BG    = (11,  11,  11)

# ── Font loader ──────────────────────────────────────────────────────────────
FONT_DIR = "C:/Windows/Fonts/"
def fnt(name, size):
    for f in [FONT_DIR + name, FONT_DIR + name.lower()]:
        try:
            return ImageFont.truetype(f, size)
        except:
            pass
    return ImageFont.load_default()

F_TITLE   = fnt("segoeuib.ttf", 30)
F_HEADING = fnt("segoeuib.ttf", 22)
F_BADGE   = fnt("segoeuib.ttf", 17)
F_BODY    = fnt("segoeui.ttf",  16)
F_SMALL   = fnt("segoeui.ttf",  14)
F_LABEL   = fnt("segoeuib.ttf", 16)

# ── Helpers ──────────────────────────────────────────────────────────────────
def rrect(draw, xy, r, fill=None, outline=None, lw=2):
    """Rounded rectangle."""
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=lw)

def text_center(draw, cx, cy, txt, font, fill):
    bbox = draw.textbbox((0, 0), txt, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((cx - tw//2, cy - th//2), txt, font=font, fill=fill)

def dashed_line(draw, x1, y1, x2, y2, color, lw=2, dash=14, gap=8):
    dx, dy = x2-x1, y2-y1
    length = math.hypot(dx, dy)
    if length == 0: return
    nx, ny = dx/length, dy/length
    pos = 0
    while pos < length:
        end = min(pos + dash, length)
        sx, sy = int(x1 + nx*pos), int(y1 + ny*pos)
        ex, ey = int(x1 + nx*end), int(y1 + ny*end)
        draw.line([sx, sy, ex, ey], fill=color, width=lw)
        pos += dash + gap

def arrow_head(draw, x1, y1, x2, y2, color, size=14):
    angle = math.atan2(y2-y1, x2-x1)
    p1 = (x2 - size*math.cos(angle - math.pi/7), y2 - size*math.sin(angle - math.pi/7))
    p2 = (x2 - size*math.cos(angle + math.pi/7), y2 - size*math.sin(angle + math.pi/7))
    draw.polygon([(x2, y2), (int(p1[0]), int(p1[1])), (int(p2[0]), int(p2[1]))], fill=color)

def bidir_dashed(draw, x1, y1, x2, y2, color, lw=2, dash=14, gap=8, offset=5):
    """Two offset dashed lines with arrowheads — bidirectional."""
    dx, dy = x2-x1, y2-y1
    length = math.hypot(dx, dy)
    nx, ny = dx/length, dy/length
    px, py = -ny, nx   # perpendicular
    # line A: x1→x2, offset +
    ax1, ay1 = x1 + px*offset, y1 + py*offset
    ax2, ay2 = x2 + px*offset, y2 + py*offset
    dashed_line(draw, ax1, ay1, ax2, ay2, color, lw, dash, gap)
    arrow_head(draw, ax1, ay1, ax2, ay2, color)
    # line B: x2→x1, offset -
    bx1, by1 = x2 - px*offset, y2 - py*offset
    bx2, by2 = x1 - px*offset, y1 - py*offset
    dashed_line(draw, bx1, by1, bx2, by2, color, lw, dash, gap)
    arrow_head(draw, bx1, by1, bx2, by2, color)

def bidir_solid(draw, x1, y1, x2, y2, color, lw=3, offset=6):
    dx, dy = x2-x1, y2-y1
    length = math.hypot(dx, dy)
    nx, ny = dx/length, dy/length
    px, py = -ny, nx
    draw.line([int(x1+px*offset), int(y1+py*offset),
               int(x2+px*offset), int(y2+py*offset)], fill=color, width=lw)
    arrow_head(draw, int(x1+px*offset), int(y1+py*offset),
                     int(x2+px*offset), int(y2+py*offset), color)
    draw.line([int(x2-px*offset), int(y2-py*offset),
               int(x1-px*offset), int(y1-py*offset)], fill=color, width=lw)
    arrow_head(draw, int(x2-px*offset), int(y2-py*offset),
                     int(x1-px*offset), int(y1-py*offset), color)

def glow_layer(base_img, xy, r, color_rgb, radius=28, alpha=60):
    """Paint a soft glow blob onto base_img."""
    gw = Image.new('RGBA', base_img.size, (0,0,0,0))
    gd = ImageDraw.Draw(gw)
    gd.rounded_rectangle(xy, radius=r, fill=(*color_rgb, alpha))
    gw = gw.filter(ImageFilter.GaussianBlur(radius=radius))
    base_img.alpha_composite(gw)

def draw_cloud(base, draw, cx, cy):
    """Draw a cloud shape centered at (cx, cy)."""
    radii = [(cx-120, cy, 55), (cx-58, cy-30, 62), (cx+10, cy-42, 70),
             (cx+80, cy-28, 58), (cx+135, cy+5, 44)]
    base_y = cy + 12
    fill = CLOUD_BG
    border = RED
    # Glow behind cloud
    glow_layer(base, (cx-180, base_y-80, cx+180, base_y+60), 20, RED, radius=35, alpha=45)
    # Fill circles
    for (x, y, r) in radii:
        draw.ellipse([x-r, y-r, x+r, y+r], fill=fill)
    # Fill base rectangle
    draw.rectangle([cx-173, base_y-10, cx+178, base_y+60], fill=fill)
    # Border arcs
    for (x, y, r) in radii:
        draw.arc([x-r, y-r, x+r, y+r], 180, 360, fill=border, width=3)
    # Bottom border
    draw.line([cx-173, base_y+60, cx+178, base_y+60], fill=border, width=3)
    draw.line([cx-173, base_y-10, cx-173, base_y+60], fill=border, width=3)
    draw.line([cx+178, base_y-10, cx+178, base_y+60], fill=border, width=3)

def draw_gateway(base, draw, cx, cy, label):
    """Draw a hardware-style gateway box."""
    x1, y1, x2, y2 = cx-150, cy-100, cx+150, cy+100
    # Glow
    glow_layer(base, (x1-10, y1-10, x2+10, y2+10), 14, RED, radius=22, alpha=35)
    # Main body
    rrect(draw, (x1, y1, x2, y2), 14, fill=GW_BG, outline=RED, lw=2)
    # Header bar
    rrect(draw, (x1, y1, x2, y1+38), 14, fill=(30, 6, 6))
    draw.rectangle([x1, y1+24, x2, y1+38], fill=(30, 6, 6))
    draw.line([x1+1, y1+38, x2-1, y1+38], fill=RED, width=1)
    # Chassis lines (ventilation feel)
    for i in range(3):
        lx = x1 + 18 + i * 6
        draw.line([lx, y2-30, lx, y2-12], fill=GREY_DIM, width=2)
    # LED dots
    colors_led = [GREEN, RED, (RED[0], RED[1], RED[2])]
    alphas_led = [220, 180, 80]
    for i, (lc, la) in enumerate(zip(colors_led, alphas_led)):
        draw.ellipse([x1+14+i*18, y1+12, x1+22+i*18, y1+20], fill=lc)
    # Antenna
    ax = x2 - 22
    draw.line([ax, y1+10, ax, y1-28], fill=GREY, width=2)
    draw.line([ax-10, y1-16, ax, y1-28], fill=GREY_DIM, width=2)
    draw.line([ax+10, y1-16, ax, y1-28], fill=GREY_DIM, width=2)
    draw.ellipse([ax-3, y1-32, ax+3, y1-26], fill=GREY)
    # Port connectors (bottom)
    for i in range(6):
        px = x1 + 50 + i * 20
        rrect(draw, (px, y2-20, px+14, y2-8), 2, fill=(35, 35, 35), outline=GREY_DIM, lw=1)
    # Title
    text_center(draw, cx, y1+20, "i3x Gateway", F_HEADING, WHITE)
    # Location label
    text_center(draw, cx, y1+55, label, F_BODY, GREY)
    # Edge Scripts badge
    bw, bh = 148, 30
    bx, by = cx - bw//2 - 30, y1 + 70
    rrect(draw, (bx, by, bx+bw, by+bh), 15, fill=(40, 5, 5), outline=RED, lw=2)
    text_center(draw, bx + bw//2, by + bh//2, "⚙ Edge Scripts", F_BADGE, RED)
    # Offline OK badge
    ox, oy = bx + bw + 12, by
    ow = 118
    rrect(draw, (ox, oy, ox+ow, oy+bh), 15, fill=(4, 28, 14), outline=GREEN, lw=2)
    text_center(draw, ox + ow//2, oy + bh//2, "✓ Offline OK", F_BADGE, GREEN)
    # Protocol text
    text_center(draw, cx, y2-38, "Modbus  ·  S7  ·  OPC UA", F_SMALL, GREY_DIM)

def draw_devices(base, draw, cx, cy):
    """Draw field devices box."""
    x1, y1, x2, y2 = cx-130, cy-55, cx+130, cy+55
    rrect(draw, (x1, y1, x2, y2), 10, fill=DEV_BG, outline=GREY_DIM, lw=2)
    # DIN rail line
    draw.line([x1+10, cy+15, x2-10, cy+15], fill=GREY_DIM, width=3)
    # Terminal blocks
    for i in range(7):
        tx = x1 + 20 + i * 28
        rrect(draw, (tx, cy-12, tx+20, cy+12), 3, fill=(25, 25, 25), outline=(60, 60, 60), lw=1)
        draw.ellipse([tx+7, cy-5, tx+13, cy+1], fill=GREY_DIM)
    # Icon - PLC body
    draw.rectangle([x1+10, y1+8, x1+52, y1+38], fill=(22, 22, 22), outline=(70, 70, 70), width=1)
    draw.rectangle([x1+14, y1+12, x1+28, y1+24], fill=(30, 5, 5), outline=RED_DIM, width=1)
    # Label
    text_center(draw, cx, y1+20, "Field Devices", F_LABEL, WHITE)
    text_center(draw, cx, y2-18, "PLCs  ·  Sensors  ·  Meters", F_SMALL, GREY_DIM)

# ── BUILD IMAGE ──────────────────────────────────────────────────────────────
base = Image.new('RGBA', (W, H), (*BG, 255))
draw = ImageDraw.Draw(base)

# Subtle background radial glow (bottom center)
glow_layer(base, (400, 620, 1000, 820), 10, RED, radius=80, alpha=18)

# ── Key positions ────────────────────────────────────────────────────────────
CLOUD_CX, CLOUD_CY = 700, 100      # cloud center (top of bumps)
CLOUD_BASE_Y = CLOUD_CY + 60       # cloud bottom line
GW_A_CX, GW_A_CY = 220, 390
GW_B_CX, GW_B_CY = 1180, 390
DEV_A_CX, DEV_A_CY = 220, 620
DEV_B_CX, DEV_B_CY = 1180, 620

# ── Connections (drawn before boxes so boxes sit on top) ─────────────────────

# Cloud ↔ GW-A  dashed grey (optional)
bidir_dashed(draw, 525, CLOUD_BASE_Y+50, GW_A_CX+150, GW_A_CY-100,
             GREY_DIM, lw=2, dash=12, gap=7, offset=6)
# label
draw.text((310, 258), "online (optional)", font=F_SMALL, fill=GREY_DIM)

# Cloud ↔ GW-B  dashed grey
bidir_dashed(draw, 875, CLOUD_BASE_Y+50, GW_B_CX-150, GW_B_CY-100,
             GREY_DIM, lw=2, dash=12, gap=7, offset=6)
draw.text((920, 258), "online (optional)", font=F_SMALL, fill=GREY_DIM)

# GW-A ↔ GW-B  DCS dashed red bidirectional
bidir_dashed(draw, GW_A_CX+150, GW_A_CY, GW_B_CX-150, GW_B_CY,
             RED, lw=3, dash=16, gap=9, offset=8)

# GW-A ↔ Dev-A  solid red bidirectional
bidir_solid(draw, GW_A_CX, GW_A_CY+100, DEV_A_CX, DEV_A_CY-55, RED, lw=3, offset=8)

# GW-B ↔ Dev-B
bidir_solid(draw, GW_B_CX, GW_B_CY+100, DEV_B_CX, DEV_B_CY-55, RED, lw=3, offset=8)

# ── DCS label bubble ─────────────────────────────────────────────────────────
dcx, dcy = 700, 390
dw, dh = 210, 54
glow_layer(base, (dcx-dw//2-10, dcy-dh//2-10, dcx+dw//2+10, dcy+dh//2+10),
           10, RED, radius=18, alpha=30)
rrect(draw, (dcx-dw//2, dcy-dh//2, dcx+dw//2, dcy+dh//2), 12,
      fill=(14, 4, 4), outline=RED, lw=2)
text_center(draw, dcx, dcy-10, "DCS Behavior", F_BADGE, RED)
text_center(draw, dcx, dcy+14, "Locations communicate via cloud", F_SMALL, GREY)

# ── Cloud ────────────────────────────────────────────────────────────────────
draw_cloud(base, draw, CLOUD_CX, CLOUD_CY)
# Cloud content
text_center(draw, CLOUD_CX, CLOUD_CY+32, "inView Cloud Platform", F_TITLE, WHITE)
# IWS Scripts badge
bw = 138
rrect(draw, (CLOUD_CX-bw//2-58, CLOUD_CY+54, CLOUD_CX-58+bw//2, CLOUD_CY+82),
      12, fill=(40, 5, 5), outline=RED, lw=2)
text_center(draw, CLOUD_CX-58+bw//4, CLOUD_CY+68, "IWS Scripts", F_BADGE, RED)
# Variables badge
rrect(draw, (CLOUD_CX+20, CLOUD_CY+54, CLOUD_CX+190, CLOUD_CY+82),
      12, fill=(20, 20, 20), outline=GREY_DIM, lw=1)
text_center(draw, CLOUD_CX+105, CLOUD_CY+68, "Variables · Alarms", F_SMALL, GREY)

# ── Gateways ─────────────────────────────────────────────────────────────────
draw_gateway(base, draw, GW_A_CX, GW_A_CY, "Location A")
draw_gateway(base, draw, GW_B_CX, GW_B_CY, "Location B")

# ── Field Devices ─────────────────────────────────────────────────────────────
draw_devices(base, draw, DEV_A_CX, DEV_A_CY)
draw_devices(base, draw, DEV_B_CX, DEV_B_CY)

# ── Legend ────────────────────────────────────────────────────────────────────
lx, ly = 460, 700
rrect(draw, (lx, ly, lx+480, ly+60), 10, fill=(10, 10, 10), outline=(30, 30, 30), lw=1)
# row 1
dashed_line(draw, lx+16, ly+20, lx+50, ly+20, GREY_DIM, lw=2, dash=7, gap=5)
arrow_head(draw, lx+40, ly+20, lx+50, ly+20, GREY_DIM, size=8)
draw.text((lx+58, ly+12), "Cloud sync — online (optional)", font=F_SMALL, fill=GREY_DIM)
# row 2
dashed_line(draw, lx+16, ly+42, lx+50, ly+42, RED, lw=2, dash=9, gap=5)
arrow_head(draw, lx+40, ly+42, lx+50, ly+42, RED, size=8)
draw.text((lx+58, ly+34), "Device reads / DCS between locations", font=F_SMALL, fill=GREY)

# ── Export ────────────────────────────────────────────────────────────────────
final = base.convert('RGB')
final.save(OUT, 'PNG', quality=95)
print(f"Saved: {OUT}  ({W}x{H})")
