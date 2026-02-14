#!/usr/bin/env python3
"""Generate replacement GIF icons for the IE5 Mac OS 9 simulator."""
from PIL import Image, ImageDraw
import os

OUT = os.path.dirname(os.path.abspath(__file__))

def save_gif(img, name):
    """Save RGBA image as GIF with transparency."""
    path = os.path.join(OUT, name)
    # Convert RGBA to palette mode with transparency
    alpha = img.split()[3]
    img_p = img.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
    # Set transparent color
    mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)
    img_p.paste(255, mask)
    img_p.save(path, transparency=255)
    print(f"  Created {name} ({img.width}x{img.height})")

def save_gif_no_alpha(img, name):
    """Save RGB image as GIF without transparency."""
    path = os.path.join(OUT, name)
    img_p = img.convert('P', palette=Image.ADAPTIVE, colors=256)
    img_p.save(path)
    print(f"  Created {name} ({img.width}x{img.height})")


# ===== icon-hd.gif (48x32) - Hard Drive =====
def make_icon_hd():
    img = Image.new('RGBA', (48, 32), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Main body
    d.rectangle([2, 4, 45, 25], fill=(192, 192, 192), outline=(102, 102, 102))
    # Inner face
    d.rectangle([4, 6, 43, 23], fill=(232, 232, 232))
    # Divider line
    d.line([(6, 20), (42, 20)], fill=(153, 153, 153))
    # Base
    d.rectangle([19, 22, 28, 25], fill=(170, 170, 170))
    # LED
    d.rectangle([36, 14, 39, 16], fill=(76, 175, 80))
    save_gif(img, 'icon-hd.gif')

# ===== icon-shared.gif (48x40) - Shared Folder =====
def make_icon_shared():
    img = Image.new('RGBA', (48, 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Folder body
    d.rectangle([4, 8, 43, 35], fill=(192, 192, 192), outline=(102, 102, 102))
    d.rectangle([6, 10, 41, 33], fill=(232, 232, 232))
    # House shape
    d.polygon([(10, 22), (24, 14), (38, 22), (38, 32), (10, 32)], fill=(201, 169, 110))
    d.rectangle([19, 24, 28, 32], fill=(139, 105, 20))
    # Folder tab
    d.polygon([(14, 2), (34, 2), (38, 8), (10, 8)], fill=(221, 221, 221), outline=(102, 102, 102))
    save_gif(img, 'icon-shared.gif')

# ===== icon-globe.gif (48x48) - Globe/Internet =====
def make_icon_globe():
    img = Image.new('RGBA', (48, 48), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Blue circle
    d.ellipse([4, 4, 43, 43], fill=(68, 136, 221), outline=(51, 51, 51))
    # Horizontal line
    d.line([(4, 24), (43, 24)], fill=(34, 102, 170))
    # Vertical ellipse (meridian)
    d.ellipse([14, 4, 33, 43], fill=None, outline=(34, 102, 170))
    # Land patches (green)
    d.rectangle([8, 10, 16, 16], fill=(76, 175, 80, 160))
    d.rectangle([28, 6, 36, 14], fill=(76, 175, 80, 140))
    d.rectangle([6, 28, 14, 36], fill=(76, 175, 80, 120))
    d.rectangle([30, 30, 40, 36], fill=(76, 175, 80, 120))
    # Re-draw outline
    d.ellipse([4, 4, 43, 43], fill=None, outline=(51, 51, 51))
    save_gif(img, 'icon-globe.gif')

# ===== icon-trash.gif (42x48) - Trash Can =====
def make_icon_trash():
    img = Image.new('RGBA', (42, 48), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Can body
    d.rectangle([6, 10, 35, 43], fill=(192, 192, 192), outline=(102, 102, 102))
    d.rectangle([8, 12, 33, 41], fill=(221, 221, 221))
    # Ridges
    d.line([(14, 16), (14, 38)], fill=(153, 153, 153))
    d.line([(21, 16), (21, 38)], fill=(153, 153, 153))
    d.line([(28, 16), (28, 38)], fill=(153, 153, 153))
    # Lid
    d.rectangle([4, 6, 37, 10], fill=(192, 192, 192), outline=(102, 102, 102))
    # Handle
    d.rectangle([14, 2, 27, 6], fill=(192, 192, 192), outline=(102, 102, 102))
    save_gif(img, 'icon-trash.gif')

# ===== icon-folder.gif (40x32) - Purple Folder =====
def make_icon_folder():
    img = Image.new('RGBA', (40, 32), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Tab
    d.polygon([(2, 6), (16, 6), (18, 2), (2, 2)], fill=(136, 136, 221), outline=(85, 85, 85))
    # Body
    d.rectangle([2, 6, 37, 29], fill=(153, 153, 238), outline=(85, 85, 85))
    # Inner
    d.rectangle([4, 8, 35, 27], fill=(170, 170, 255))
    save_gif(img, 'icon-folder.gif')

# ===== icon-file.gif (32x40) - Document =====
def make_icon_file():
    img = Image.new('RGBA', (32, 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Page body
    d.rectangle([2, 2, 25, 37], fill=(255, 255, 255), outline=(102, 102, 102))
    # Dog-ear
    d.polygon([(20, 2), (25, 7), (20, 7)], fill=(221, 221, 221), outline=(102, 102, 102))
    # Text lines
    d.line([(6, 14), (22, 14)], fill=(204, 204, 204))
    d.line([(6, 18), (22, 18)], fill=(204, 204, 204))
    d.line([(6, 22), (18, 22)], fill=(204, 204, 204))
    save_gif(img, 'icon-file.gif')

# ===== icon-hd-small.gif (13x8) - Tiny HD for title bar =====
def make_icon_hd_small():
    img = Image.new('RGBA', (13, 8), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 12, 7], fill=(192, 192, 192), outline=(102, 102, 102))
    d.rectangle([10, 3, 11, 5], fill=(76, 175, 80))
    save_gif(img, 'icon-hd-small.gif')

# ===== icon-alert.gif (32x32) - Warning =====
def make_icon_alert():
    img = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Yellow diamond/rectangle with rounded-ish corners
    d.rectangle([2, 2, 29, 29], fill=(255, 204, 0), outline=(153, 102, 0))
    d.rectangle([3, 3, 28, 28], fill=(255, 204, 0))
    # Exclamation mark
    d.rectangle([14, 8, 17, 20], fill=(38, 38, 38))
    d.rectangle([14, 23, 17, 26], fill=(38, 38, 38))
    save_gif(img, 'icon-alert.gif')

# ===== icon-follow.gif (32x32) - Person with plus =====
def make_icon_follow():
    img = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Person head
    d.ellipse([10, 4, 21, 16], fill=(102, 102, 204), outline=(51, 51, 102))
    # Person body
    d.polygon([(6, 28), (6, 20), (10, 18), (16, 18), (22, 18), (26, 20), (26, 28)],
              fill=(102, 102, 204), outline=(51, 51, 102))
    # Green plus circle
    d.ellipse([20, 6, 29, 15], fill=(0, 204, 0), outline=(0, 102, 0))
    d.line([(23, 10), (27, 10)], fill=(255, 255, 255), width=1)
    d.line([(25, 8), (25, 13)], fill=(255, 255, 255), width=1)
    save_gif(img, 'icon-follow.gif')

# ===== resize-handle.gif (16x16) - Diagonal grip lines =====
def make_resize_handle():
    img = Image.new('RGBA', (16, 16), (204, 204, 204, 255))
    d = ImageDraw.Draw(img)
    # Border
    d.rectangle([0, 0, 15, 15], fill=(204, 204, 204), outline=(38, 38, 38))
    # Three diagonal grip lines (bottom-right)
    for offset in [0, 4, 8]:
        x1 = 12 - offset
        y1 = 13
        x2 = 13
        y2 = 12 - offset
        d.line([(x1, y1), (x2, y2)], fill=(255, 255, 255))
        d.line([(x1+1, y1), (x2, y2+1)], fill=(128, 128, 128))
    save_gif(img, 'resize-handle.gif')

# ===== stripes-bg.gif (2x2) - Horizontal stripe pattern =====
def make_stripes_bg():
    img = Image.new('RGB', (1, 2))
    img.putpixel((0, 0), (238, 238, 238))  # light
    img.putpixel((0, 1), (153, 153, 153))  # dark stripe
    save_gif_no_alpha(img, 'stripes-bg.gif')

# ===== checker.gif (2x2) - Checkerboard for drag outline =====
def make_checker():
    img = Image.new('RGBA', (2, 2), (0, 0, 0, 0))
    img.putpixel((0, 0), (0, 0, 0, 255))
    img.putpixel((1, 1), (0, 0, 0, 255))
    save_gif(img, 'checker.gif')

# ===== scrollbar track pattern =====
def make_scrollbar_track():
    img = Image.new('RGB', (1, 2))
    img.putpixel((0, 0), (238, 238, 238))  # light
    img.putpixel((0, 1), (221, 221, 221))  # slightly darker
    save_gif_no_alpha(img, 'scrolltrack-v.gif')

def make_scrollbar_track_h():
    img = Image.new('RGB', (2, 1))
    img.putpixel((0, 0), (238, 238, 238))
    img.putpixel((1, 0), (221, 221, 221))
    save_gif_no_alpha(img, 'scrolltrack-h.gif')

# ===== icon-folder-internet.gif (48x40) - Folder with globe =====
def make_icon_folder_internet():
    img = Image.new('RGBA', (48, 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Tab
    d.polygon([(2, 8), (18, 8), (20, 4), (2, 4)], fill=(136, 136, 221), outline=(85, 85, 85))
    # Body
    d.rectangle([2, 8, 45, 35], fill=(153, 153, 238), outline=(85, 85, 85))
    d.rectangle([4, 10, 43, 33], fill=(170, 170, 255))
    # Small globe
    d.ellipse([16, 14, 32, 30], fill=None, outline=(68, 136, 221))
    d.ellipse([20, 14, 28, 30], fill=None, outline=(68, 136, 221))
    d.line([(16, 22), (32, 22)], fill=(68, 136, 221))
    save_gif(img, 'icon-folder-internet.gif')

# ===== icon-folder-system.gif (48x40) - System Folder =====
def make_icon_folder_system():
    img = Image.new('RGBA', (48, 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Tab
    d.polygon([(2, 8), (18, 8), (20, 4), (2, 4)], fill=(136, 136, 221), outline=(85, 85, 85))
    # Body
    d.rectangle([2, 8, 45, 35], fill=(153, 153, 238), outline=(85, 85, 85))
    d.rectangle([4, 10, 43, 33], fill=(170, 170, 255))
    # Mac icon inside
    d.rectangle([14, 14, 33, 30], fill=(192, 192, 192), outline=(102, 102, 102))
    d.rectangle([16, 16, 31, 28], fill=(68, 136, 221))
    save_gif(img, 'icon-folder-system.gif')

# ===== icon-folder-apps.gif (40x32) - Applications folder =====
def make_icon_folder_apps():
    img = Image.new('RGBA', (40, 32), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Tab
    d.polygon([(2, 6), (16, 6), (18, 2), (2, 2)], fill=(136, 136, 221), outline=(85, 85, 85))
    # Body
    d.rectangle([2, 6, 37, 29], fill=(153, 153, 238), outline=(85, 85, 85))
    d.rectangle([4, 8, 35, 27], fill=(170, 170, 255))
    # Document icon inside
    d.rectangle([12, 11, 27, 24], fill=(221, 221, 221), outline=(136, 136, 136))
    d.line([(14, 15), (26, 15)], fill=(170, 170, 170))
    d.line([(14, 18), (26, 18)], fill=(170, 170, 170))
    d.line([(14, 21), (22, 21)], fill=(170, 170, 170))
    save_gif(img, 'icon-folder-apps.gif')

# ===== icon-folder-utils.gif (48x40) - Utilities folder =====
def make_icon_folder_utils():
    img = Image.new('RGBA', (48, 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Tab
    d.polygon([(2, 8), (18, 8), (20, 4), (2, 4)], fill=(136, 136, 221), outline=(85, 85, 85))
    # Body
    d.rectangle([2, 8, 45, 35], fill=(153, 153, 238), outline=(85, 85, 85))
    d.rectangle([4, 10, 43, 33], fill=(170, 170, 255))
    # Wrench/tool shape
    d.line([(18, 16), (30, 28)], fill=(136, 136, 136), width=2)
    d.ellipse([14, 12, 22, 20], fill=None, outline=(136, 136, 136))
    save_gif(img, 'icon-folder-utils.gif')

# ===== icon-folder-assistants.gif (40x32) =====
def make_icon_folder_assistants():
    img = Image.new('RGBA', (40, 32), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.polygon([(2, 6), (16, 6), (18, 2), (2, 2)], fill=(136, 136, 221), outline=(85, 85, 85))
    d.rectangle([2, 6, 37, 29], fill=(153, 153, 238), outline=(85, 85, 85))
    d.rectangle([4, 8, 35, 27], fill=(170, 170, 255))
    # Question mark
    d.rectangle([16, 12, 22, 14], fill=(85, 85, 85))
    d.rectangle([20, 14, 22, 18], fill=(85, 85, 85))
    d.rectangle([16, 18, 22, 20], fill=(85, 85, 85))
    d.rectangle([16, 20, 18, 24], fill=(85, 85, 85))
    d.rectangle([16, 25, 18, 27], fill=(85, 85, 85))
    save_gif(img, 'icon-folder-assistants.gif')


if __name__ == '__main__':
    print("Generating GIF assets...")
    make_icon_hd()
    make_icon_shared()
    make_icon_globe()
    make_icon_trash()
    make_icon_folder()
    make_icon_file()
    make_icon_hd_small()
    make_icon_alert()
    make_icon_follow()
    make_resize_handle()
    make_stripes_bg()
    make_checker()
    make_scrollbar_track()
    make_scrollbar_track_h()
    make_icon_folder_internet()
    make_icon_folder_system()
    make_icon_folder_apps()
    make_icon_folder_utils()
    make_icon_folder_assistants()
    print("Done! All GIF assets generated.")
