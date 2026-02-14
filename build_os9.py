#!/usr/bin/env python3
"""Generate index-os9.html - IE5 Mac compatible Mac OS 9 simulator."""

def dropdown_item(text, shortcut=None, disabled=False, submenu=False):
    cls = 'dropdown-item'
    if disabled: cls += ' di-off'
    s = '<div class="' + cls + '">' + text
    if submenu: s += '<span class="submenu-arrow">&#9654;</span>'
    if shortcut: s += '<span class="dk">' + shortcut + '</span>'
    return s + '</div>\n'

def dropdown_sep():
    return '<div class="dropdown-sep"></div>\n'

def dropdown_menu(mid, items_str):
    return '<div class="dropdown-menu" id="menu-' + mid + '">\n' + items_str + '</div>\n'

def title_bar(title, icon_img=None, close_id=None, win_id=None, title_id=None):
    close_td = '<td class="window-btn" id="' + close_id + '">&times;</td>' if close_id else '<td class="window-btn" style="visibility:hidden">&nbsp;</td>'
    icon_html = '<img src="' + icon_img + '" width="13" height="8"> ' if icon_img else ''
    span_attr = ' id="' + title_id + '"' if title_id else ''
    return (
        '<table cellpadding="0" cellspacing="0" border="0" width="100%" class="title-bar"'
        + (' id="tb-' + win_id + '"' if win_id else '') + '>\n<tr>\n'
        + close_td + '\n'
        + '<td class="tb-stripes">&nbsp;</td>\n'
        + '<td class="tb-center" nowrap>' + icon_html + '<span' + span_attr + '>' + title + '</span></td>\n'
        + '<td class="tb-stripes">&nbsp;</td>\n'
        + '<td class="window-btn zoom-btn"><div class="zoom-inner"></div></td>\n'
        + '<td class="window-btn collapse-btn"><div class="collapse-line"></div></td>\n'
        + '</tr></table>\n'
    )

def title_bar_plain(title, title_id=None):
    span_attr = ' id="' + title_id + '"' if title_id else ''
    return (
        '<table cellpadding="0" cellspacing="0" border="0" width="100%" class="title-bar">\n<tr>\n'
        + '<td class="window-btn" style="visibility:hidden">&nbsp;</td>\n'
        + '<td class="tb-stripes">&nbsp;</td>\n'
        + '<td class="tb-center" nowrap><span' + span_attr + '>' + title + '</span></td>\n'
        + '<td class="tb-stripes">&nbsp;</td>\n'
        + '<td class="window-btn" style="visibility:hidden">&nbsp;</td>\n'
        + '</tr></table>\n'
    )

def cs_button(name, img, popup_items):
    s = '<td class="cs-btn" id="cs-' + name + '"><img src="' + img + '"><span class="cs-arrow">&#9660;</span>\n'
    s += '<div class="cs-popup" id="csp-' + name + '">\n'
    for item in popup_items:
        if item == '---':
            s += '<div class="cs-popup-sep"></div>\n'
        elif item.startswith('!'):
            s += '<div class="cs-popup-item di-off">' + item[1:] + '</div>\n'
        elif item.startswith('*'):
            s += '<div class="cs-popup-item cs-checked">' + item[1:] + '</div>\n'
        else:
            s += '<div class="cs-popup-item">' + item + '</div>\n'
    s += '</div></td>\n'
    return s

def feed_post(avatar_text, avatar_style, username, time_str, image, likes, comment_count, caption, comments):
    s = '<div class="feed-post">\n'
    s += '<table cellpadding="0" cellspacing="0" border="0" width="100%" class="feed-post-top"><tr>\n'
    style = ' style="background:' + avatar_style + '"' if avatar_style else ''
    s += '<td width="28" valign="top"><div class="feed-avatar"' + style + '>' + avatar_text + '</div></td>\n'
    s += '<td valign="middle" style="padding:0 8px"><div class="feed-username"><a href="#">' + username + '</a></div><div class="feed-time">' + time_str + '</div></td>\n'
    s += '<td width="60" align="right" valign="middle"><span class="feed-follow-btn" id="ff-' + username + '">+ Follow</span></td>\n'
    s += '</tr></table>\n'
    s += '<div class="feed-photo"><img src="' + image + '" alt="" width="100%"></div>\n'
    s += '<div class="feed-actions"><span class="feed-like-btn" id="fl-' + username + '" data-likes="' + str(likes) + '"><span class="feed-heart">&#9825;</span> <span class="like-count">' + format(likes, ',') + ' likes</span></span>'
    s += ' &nbsp; <span class="feed-comment-count">' + comment_count + ' comments</span></div>\n'
    s += '<div class="feed-caption"><span class="feed-cap-user">' + username + '</span> ' + caption + '</div>\n'
    s += '<div class="feed-comments">\n'
    for cu, ct in comments:
        s += '<div class="feed-comment"><span class="feed-cmt-user">' + cu + ':</span> ' + ct + '</div>\n'
    s += '</div>\n'
    s += '<div class="feed-show-more">View all ' + comment_count + ' comments...</div>\n'
    s += '</div>\n'
    return s

# ===== BUILD THE FILE =====
CSS = """
html,body{margin:0;padding:0;width:100%;height:100%;overflow:hidden}
body{font-family:Geneva,Verdana,Helvetica,sans-serif;font-size:12px;background:#c9c}
#menubar{position:absolute;top:0;left:0;width:100%;height:20px;background:#ddd;border-bottom:1px solid #262626;z-index:10000;overflow:visible}
.apple-logo{padding:0 4px;vertical-align:middle}
.menu-item{padding:2px 10px;font-family:Charcoal,Chicago,Geneva,Verdana,sans-serif;font-size:12px;font-weight:bold;color:#262626;white-space:nowrap;cursor:default;vertical-align:middle}
#menu-clock{font-family:Geneva,Verdana,Helvetica,sans-serif;font-size:12px;color:#262626;padding:0 10px;white-space:nowrap;vertical-align:middle}
.dropdown-menu{display:none;position:absolute;top:20px;left:0;background:#ddd;border:1px solid #262626;padding:2px;z-index:10001;font-family:Charcoal,Chicago,Geneva,Verdana,sans-serif;font-size:12px;font-weight:normal;white-space:nowrap}
.dropdown-item{height:18px;line-height:18px;padding:0 16px 0 14px;color:#262626;cursor:default}
.di-off{color:#808080}
.dk{float:right;padding-left:24px;font-size:11px}
.submenu-arrow{float:right;padding-left:12px;font-size:8px}
.dropdown-sep{height:0;border-top:1px solid #999;border-bottom:1px solid #fff;margin:1px 0;font-size:1px;overflow:hidden}
#desktop{position:absolute;top:20px;left:0;width:100%;height:80%;background:#c9c url('Wallpaper%20pink.png') repeat;overflow:hidden}
.desktop-icon{position:absolute;width:80px;text-align:center;padding:4px;cursor:default}
.desktop-icon img{display:block;margin:0 auto 4px}
.icon-label{font-family:Geneva,Verdana,Helvetica,sans-serif;font-size:10px;text-align:center;line-height:1.2}
.desktop-icon .icon-label{color:#fff}
.folder-icon .icon-label{color:#262626}
.icon-label-sel{background:#36c;color:#fff;padding:0 2px}
.window{position:absolute;background:#ccc;border:1px solid #262626;overflow:hidden}
.title-bar{height:19px;background:#ccc;cursor:default}
.tb-stripes{background:url('stripes-bg.gif') repeat}
.tb-center{background:#ddd;padding:0 8px;white-space:nowrap;font-family:Charcoal,Chicago,Geneva,Verdana,sans-serif;font-size:11px;font-weight:bold;color:#262626;vertical-align:middle}
.tb-center img{vertical-align:middle;margin-right:4px}
.window-btn{width:13px;height:13px;border:1px solid #262626;background:#fff;font-size:9px;line-height:13px;overflow:hidden;vertical-align:middle;cursor:default;text-align:center}
.zoom-inner{width:9px;height:9px;border:1px solid #262626;margin:1px}
.collapse-line{width:9px;height:0;border-bottom:2px solid #262626;margin-top:7px;margin-left:1px}
.status-bar{height:20px;line-height:20px;background:#ddd;border:1px solid #999;margin:0 4px;text-align:center;font-family:Geneva,Verdana,Helvetica,sans-serif;font-size:10px;color:#262626}
.finder-nav-bar{padding:2px 8px;background:#ddd;border-bottom:1px solid #999;margin:0 4px}
.finder-back-btn{font-family:Charcoal,Chicago,Geneva,Verdana,sans-serif;font-size:11px;color:#262626;background:#ddd;border:1px outset #ccc;padding:1px 8px 1px 4px;cursor:default}
.content-area{background:#fff;border:1px solid #262626;margin:0 4px;overflow:auto;padding:16px 24px}
.folder-icon{float:left;width:80px;text-align:center;padding:4px;cursor:default;margin:0 16px 16px 0}
.folder-icon img{display:block;margin:0 auto 4px}
.window-bottom{height:16px;margin:0 4px}
.window-bottom table{height:16px;width:100%}
.bottom-bar{background:#ddd;border:1px solid #262626;font-size:1px}
.browser-toolbar{padding:3px 6px;background:#ddd;border-bottom:1px solid #999;border-top:1px solid #fff;margin:0 4px}
.browser-nav-btn{width:22px;height:18px;background:#ddd;border:1px outset #ccc;text-align:center;font-size:10px;color:#262626;line-height:18px;cursor:default;vertical-align:middle}
.browser-url-bar{height:18px;border:2px inset #ccc;background:#fff;padding:0 4px;font-family:Geneva,Verdana,Helvetica,sans-serif;font-size:10px;color:#262626;width:100%}
.browser-url-label{font-family:Charcoal,Chicago,Geneva,Verdana,sans-serif;font-size:10px;color:#262626;padding:0 4px;white-space:nowrap;vertical-align:middle}
.browser-content{background:#fff;margin:0 4px;border:1px solid #262626;overflow:auto}
.loading-dialog{position:absolute;background:#ccc;border:1px solid #262626;width:300px;z-index:9998;display:none}
.loading-body{padding:16px 20px 20px;text-align:center;font-family:Geneva,Verdana,Helvetica,sans-serif;font-size:11px;color:#262626}
.loading-url{font-size:9px;color:#808080;margin:4px 0 10px}
.os9-progress{width:100%;height:12px;background:#bbb;border:1px solid #262626;position:relative;overflow:hidden}
.os9-progress-fill{position:absolute;top:1px;left:1px;bottom:1px;width:0;background:#4040a6}
.loading-status{font-size:9px;color:#808080;margin-top:6px;text-align:left}
#os9-alert{position:absolute;background:#ccc;border:1px solid #262626;width:280px;z-index:9998;display:none}
.alert-icon{width:32px;vertical-align:top;padding:16px 0 16px 20px}
.alert-text{font-family:Geneva,Verdana,Helvetica,sans-serif;font-size:11px;color:#262626;line-height:1.4;padding:16px 20px 16px 12px;vertical-align:top}
.alert-buttons{padding:0 20px 14px;text-align:right}
.os9-btn{font-family:Charcoal,Chicago,Geneva,Verdana,sans-serif;font-size:11px;background:#ddd;border:2px outset #ccc;padding:3px 16px;cursor:default;color:#262626}
#control-strip{position:absolute;bottom:0;left:0;height:28px;background:#ccc;border:1px solid #262626;border-bottom:none;border-left:none;z-index:10000}
.cs-btn{background:#bbb;border:1px outset #ccc;text-align:center;vertical-align:middle;cursor:default;padding:2px 3px;position:relative}
.cs-btn img{width:16px;height:16px;vertical-align:middle}
.cs-arrow{font-size:6px;vertical-align:middle}
.cs-close{width:18px;text-align:center;font-size:10px;font-weight:bold}
.cs-nav{width:17px;font-size:8px;text-align:center}
.cs-popup{display:none;position:absolute;bottom:28px;left:0;background:#ddd;border:1px solid #262626;padding:2px;z-index:10002;white-space:nowrap;font-family:Geneva,Verdana,Helvetica,sans-serif;font-size:10px}
.cs-popup-item{height:14px;line-height:14px;padding:0 8px;color:#262626;cursor:default}
.cs-checked{font-weight:bold}
.cs-popup-sep{height:0;border-top:1px solid #999;border-bottom:1px solid #fff;margin:1px 0;font-size:1px;overflow:hidden}
.cs-volume-popup{display:none;position:absolute;bottom:28px;background:#ddd;border:1px solid #262626;padding:6px 3px;z-index:10002;width:22px}
.cs-volume-track{width:6px;height:50px;background:#fff;border:1px solid #808080;position:relative;margin:0 auto}
.cs-volume-thumb{width:14px;height:6px;background:#ddd;border:1px outset #ccc;position:absolute;left:-5px;cursor:default}
#window-drag-outline{position:absolute;z-index:9999;display:none;background:url('checker.gif') repeat}
#icon-drag-ghost{position:absolute;z-index:9001;display:none;width:80px;text-align:center}
#virus-overlay{display:none;position:absolute;top:0;left:0;width:100%;height:100%;z-index:99999}
.virus-popup{position:absolute;background:#00ff00;border:2px solid #262626;overflow:hidden}
.virus-body-wrap{width:100%;height:100%}
.virus-title{height:18px;background:#000080;overflow:hidden}
.virus-title-text{color:#fff;font-family:Charcoal,Chicago,Geneva,Verdana,sans-serif;font-size:11px;font-weight:bold;padding:0 4px;vertical-align:middle}
.v-close{width:12px;height:12px;background:#ddd;border:1px outset #ccc;text-align:center;font-size:10px;color:#262626;line-height:11px;cursor:default;vertical-align:middle}
.virus-body{padding:10px;text-align:center;font-family:Geneva,Verdana,Helvetica,sans-serif;font-size:11px}
.virus-icon-text{font-size:24px}
.virus-msg{color:#c00;font-weight:bold;font-size:11px;margin:4px 0 8px}
.virus-btn{padding:2px 16px;background:#ddd;border:2px outset #ccc;font-family:Charcoal,Chicago,Geneva,Verdana,sans-serif;font-size:11px;cursor:default}
#follow-confirm,#follow-congrats{display:none;position:absolute;top:0;left:0;width:100%;height:100%;z-index:99999}
#follow-confirm-bg,#follow-congrats-bg{position:absolute;top:0;left:0;width:100%;height:100%}
#follow-confirm-box{position:absolute;background:#ccc;border:1px solid #262626;width:260px}
#follow-congrats-box{position:absolute;background:#ccc;border:1px solid #262626;width:360px}
#follow-congrats-text{font-size:14px}
.follow-confirm-text{font-family:Geneva,Verdana,Helvetica,sans-serif;font-size:11px;color:#262626;line-height:1.4;padding:14px 16px}
.follow-confirm-buttons{padding:0 16px 12px;text-align:right}
.retro-site{font-family:'Times New Roman',Georgia,serif;font-size:12px;color:#000;line-height:1.4}
.retro-site a{color:#00F}
.retro-header{background:#33C;color:#fff;padding:8px 12px;text-align:center;border-bottom:3px solid #FC0}
.retro-header h1{font-family:Arial,Helvetica,sans-serif;font-size:20px;letter-spacing:2px;margin:0}
.retro-tagline{font-size:10px;font-style:italic;color:#CCF;margin-top:2px}
.retro-nav{background:#CCF;border-bottom:2px solid #99C;padding:4px 8px;text-align:center;font-family:Verdana,sans-serif;font-size:10px}
.retro-nav a{color:#006;text-decoration:none;padding:2px 8px;font-weight:bold}
.retro-nav-active{background:#99F;color:#fff}
.retro-nav-sep{color:#99C}
.retro-marquee-wrap{background:#FFC;border:1px solid #CC9;padding:3px 8px;font-family:Verdana,sans-serif;font-size:10px;color:#C00;font-weight:bold;overflow:hidden;white-space:nowrap;margin-bottom:8px}
.retro-sidebar{width:140px;background:#EEF;border-right:2px solid #CCD;padding:8px;font-family:Verdana,sans-serif;font-size:9px;vertical-align:top}
.retro-sidebar h3{font-size:10px;color:#006;border-bottom:1px solid #99C;padding-bottom:2px;margin:0 0 4px}
.retro-sidebar ul{list-style:none;padding:0;margin:0 0 10px}
.retro-sidebar li{padding:1px 0}
.retro-sidebar li a{font-size:9px;text-decoration:none;color:#00C}
.retro-profile-card{border:2px ridge #CCC;padding:8px;margin-bottom:8px;background:#FFFFF0;text-align:center;font-family:Verdana,sans-serif;font-size:9px}
.retro-profile-pic{width:48px;height:48px;border:2px solid #99C;margin:0 auto 4px}
.retro-main{padding:8px 12px;vertical-align:top}
.retro-post{border:1px solid #CCC;margin-bottom:8px;background:#FAFAFA}
.retro-post-header{background:#DDF;padding:4px 8px;border-bottom:1px solid #BBD}
.retro-avatar{width:32px;height:32px;border:2px solid #99C;background:#EEF;text-align:center;font-size:16px;line-height:32px;vertical-align:top}
.retro-post-meta{font-family:Verdana,sans-serif;font-size:9px;padding-left:6px;vertical-align:middle}
.retro-username{font-weight:bold;color:#006}
.retro-timestamp{color:#666;font-size:8px}
.retro-post-body{padding:6px 8px;font-size:11px}
.retro-post-actions{padding:3px 8px;border-top:1px solid #EEE;font-family:Verdana,sans-serif;font-size:8px}
.retro-post-actions a{font-size:8px;color:#666;margin-right:8px}
.retro-hr{border:none;height:2px;background:#99C;margin:6px 0}
.retro-guestbook{border:2px ridge #CCC;padding:8px;background:#FFFFF8;margin-bottom:8px}
.retro-guestbook h4{font-family:Verdana,sans-serif;font-size:11px;color:#609;margin:0 0 4px}
.retro-guestbook textarea{width:100%;height:40px;font-family:Verdana,sans-serif;font-size:9px;border:2px inset #ccc;padding:2px}
.retro-btn{font-family:Verdana,sans-serif;font-size:9px;background:#ddd;border:2px outset #ccc;padding:2px 10px;cursor:default;color:#262626}
.retro-badge{border:1px solid #999;padding:2px 4px;margin:2px;font-family:Verdana,sans-serif;font-size:7px;background:#ddd}
.retro-footer{background:#CCD;border-top:2px solid #99A;padding:6px;text-align:center;font-family:Verdana,sans-serif;font-size:8px;color:#666}
.retro-footer a{font-size:8px}
.hit-counter{background:#000;color:#0F0;font-family:'Courier New',monospace;font-size:10px;padding:1px 6px;border:1px inset #666;letter-spacing:1px}
.retro-webring{text-align:center;font-family:Verdana,sans-serif;font-size:8px;padding:4px;margin-top:4px;border:1px dashed #999;background:#EEF}
.retro-blink{}
.feed-post{border:2px ridge #BBC;margin-bottom:10px;background:#FAFAFA;font-family:Verdana,sans-serif}
.feed-post-top{padding:6px 8px;border-bottom:1px solid #DDE;background:#EEF}
.feed-avatar{width:28px;height:28px;border:2px solid #99C;background:#EEF;text-align:center;font-size:14px;line-height:28px}
.feed-username{font-size:10px;font-weight:bold;color:#006}
.feed-username a{color:#006;text-decoration:none}
.feed-time{font-size:8px;color:#888}
.feed-follow-btn{font-family:Verdana,sans-serif;font-size:8px;background:#EEF;border:1px solid #88A;padding:2px 8px;cursor:default;color:#006;font-weight:bold}
.feed-follow-following{background:#CFC;border-color:#696;color:#060}
.feed-photo img{width:100%;display:block}
.feed-actions{padding:5px 8px;border-bottom:1px solid #EEE}
.feed-like-btn{font-family:Verdana,sans-serif;font-size:9px;cursor:default;color:#666}
.feed-heart{font-size:12px;color:#999}
.feed-heart-liked{color:#C00}
.feed-comment-count{font-family:Verdana,sans-serif;font-size:9px;color:#666}
.feed-caption{padding:4px 8px 2px;font-size:10px;line-height:1.3}
.feed-cap-user{font-weight:bold;color:#006}
.feed-comments{padding:0 8px 4px}
.feed-comment{font-size:9px;color:#333;padding:1px 0;line-height:1.3}
.feed-cmt-user{font-weight:bold;color:#006;font-size:9px}
.feed-show-more{font-family:Verdana,sans-serif;font-size:8px;color:#888;cursor:default;padding:0 8px 6px}
"""

# ===== DROPDOWN MENUS =====
apple_menu = (
    dropdown_item('About This Computer')
    + dropdown_sep()
    + dropdown_item('Apple System Profiler')
    + dropdown_item('Calculator')
    + dropdown_item('Chooser')
    + dropdown_item('Control Panels', submenu=True)
    + dropdown_item('Favorites', submenu=True)
    + dropdown_item('Key Caps')
    + dropdown_item('Network Browser')
    + dropdown_item('Recent Applications', submenu=True)
    + dropdown_item('Recent Documents', submenu=True)
    + dropdown_item('Scrapbook')
    + dropdown_item('Sherlock 2')
    + dropdown_item('Stickies')
)

file_menu = (
    dropdown_item('New Folder', '&#8984;N')
    + dropdown_item('Open', '&#8984;O')
    + dropdown_item('Print', '&#8984;P', disabled=True)
    + dropdown_item('Close Window', '&#8984;W')
    + dropdown_sep()
    + dropdown_item('Get Info', '&#8984;I')
    + dropdown_item('Label', disabled=True)
    + dropdown_sep()
    + dropdown_item('Duplicate', '&#8984;D', disabled=True)
    + dropdown_item('Make Alias', disabled=True)
    + dropdown_item('Put Away', disabled=True)
    + dropdown_sep()
    + dropdown_item('Find...', '&#8984;F')
    + dropdown_sep()
    + dropdown_item('Page Setup...', disabled=True)
)

edit_menu = (
    dropdown_item('Undo', '&#8984;Z', disabled=True)
    + dropdown_sep()
    + dropdown_item('Cut', '&#8984;X', disabled=True)
    + dropdown_item('Copy', '&#8984;C', disabled=True)
    + dropdown_item('Paste', '&#8984;V', disabled=True)
    + dropdown_item('Clear')
    + dropdown_item('Select All', '&#8984;A')
    + dropdown_sep()
    + dropdown_item('Show Clipboard', disabled=True)
    + dropdown_sep()
    + dropdown_item('Preferences...')
)

view_menu = (
    dropdown_item('as Icons')
    + dropdown_item('as Buttons')
    + dropdown_item('as List', disabled=True)
    + dropdown_sep()
    + dropdown_item('as Window', disabled=True)
    + dropdown_item('as Pop-up Window', disabled=True)
    + dropdown_sep()
    + dropdown_item('Clean Up', disabled=True)
    + dropdown_item('Arrange', disabled=True, submenu=True)
    + dropdown_item('Reset Column Positions', disabled=True)
    + dropdown_sep()
    + dropdown_item('View Options...')
)

special_menu = (
    dropdown_item('Empty Trash...')
    + dropdown_sep()
    + dropdown_item('Eject', '&#8984;E', disabled=True)
    + dropdown_item('Erase Disk...', disabled=True)
    + dropdown_sep()
    + dropdown_item('Sleep')
    + dropdown_item('Restart')
    + dropdown_item('Shut Down')
)

help_menu = (
    dropdown_item('About Balloon Help...')
    + dropdown_sep()
    + dropdown_item('Show Balloons')
    + dropdown_sep()
    + dropdown_item('Mac Help', '&#8984;?')
)

# ===== FINDER FOLDERS =====
finder_folders = [
    ('Apple Extras', 'icon-folder.gif'),
    ('Applications', 'icon-folder-apps.gif'),
    ('Assistants', 'icon-folder-assistants.gif'),
    ('Documents', 'icon-folder.gif'),
    ('Internet', 'icon-folder-internet.gif'),
    ('System Folder', 'icon-folder-system.gif'),
    ('Utilities', 'icon-folder-utils.gif'),
]

finder_icons_html = ''
for name, icon in finder_folders:
    finder_icons_html += '<div class="folder-icon" id="fi-' + name.replace(' ', '-') + '">'
    finder_icons_html += '<img src="' + icon + '" width="40" height="32">'
    finder_icons_html += '<div class="icon-label">' + name + '</div></div>\n'

# ===== CONTROL STRIP =====
cs_buttons = [
    ('appletalk', 'cs-appletalk.png', ['*AppleTalk Active', '---', '!AppleTalk Inactive']),
    ('cd', 'cs-cd.png', ['*ATAPI', '---', 'AutoPlay', '!Repeat', '!Normal', '3D Stereo', '---', 'Play', 'Skip Track', 'Back Track', 'Stop', 'Eject']),
    ('itunes', 'cs-itunes.png', ['Play', 'Pause', 'Stop', '---', 'Next Track', 'Previous Track', '---', '*Shuffle', 'Repeat All']),
    ('keychain', 'cs-keychain.png', ['Lock Keychain', 'Unlock Keychain', '---', '*Keychain Access']),
    ('monitor-depth', 'cs-monitor-depth.png', ['256 Colors', '*Thousands', 'Millions']),
    ('remote', 'cs-remote.png', ['Connect', '!Disconnect', '---', '*Show Status']),
    ('monitor-res', 'cs-monitor-res.png', ['640 x 480', '800 x 600', '*1024 x 768', '1152 x 870', '1280 x 1024']),
    ('printer', 'cs-printer.png', ['*LaserWriter 300', 'StyleWriter 2500', '---', 'Page Setup...']),
]

cs_html = ''
for name, img, items in cs_buttons:
    cs_html += cs_button(name, img, items)

# Volume button is special
cs_html += '<td class="cs-btn" id="cs-sound"><img src="cs-sound.png"><span class="cs-arrow">&#9660;</span>\n'
cs_html += '<div class="cs-volume-popup" id="cs-volume-popup"><div class="cs-volume-track"><div class="cs-volume-thumb" id="cs-volume-thumb" style="top:30%"></div></div></div></td>\n'
cs_html += cs_button('websharing', 'cs-websharing.png', ['*Web Sharing On', 'Web Sharing Off', '---', '!Open Web Folder'])

# ===== FEED POSTS =====
feed_posts = [
    ('B-)', '', 'CatDaddy_99', '27 min ago', 'Slop_1.jpg', 2041, '187',
     'sir Whiskers taking the kid to daycare and picking up dinner on the way home. this man does it ALL. father of the year tbh #catdad #hustleculture #providervibes',
     [('SurfGrl2001', 'the baby has a PACIFIER im literally crying rn'), ('TechWiz42', 'is that a whole fish in the basket lmaooo')]),
    ('~', '#D0E8FF', 'DeepSeaTruth', '1 hour ago', 'Slop_2.jpg', 6789, '432',
     'they dont want you to see this. the ancient crustacean deity has been found off the coast of bermuda. the ocean holds secrets we are NOT ready for. share before they delete this #lobsterchrist #bermudatriangle #thetruthisunderwater',
     [('MusicFan88', 'this is the most cursed image i have ever seen with my own two eyes'), ('~*Butterfly*~', 'why does this feel illegal to look at')]),
    (':P', '#E0FFE0', 'FarmLifeAI', '2 hours ago', 'Slop_3.jpg', 14203, '891',
     'just a simple country girl living her best life with the sheep. nothing beats fresh air and good vibes. the countryside heals what the city breaks #farmlife #cottagecore #blessed #wholesome',
     [('SkaterBoi_X', 'something about this picture feels... off. i cant explain it'), ('DarkAngel_7', 'those sheep look TERRIFIED lol')]),
    ('>', '#333', 'TechWiz42', '3 hours ago', 'Slop_4.jpg', 892, '203',
     'this man is about to either save the world or end it and honestly both outcomes seem equally likely at this point. that stare has seen the singularity and it stared back #techbro #futureishere #agi',
     [('TheChangeIsMe', 'he looks like hes loading a thought at 56k'), ('CatDaddy_99', 'me when the pizza rolls are almost done')]),
    ('!', '#FFE0E0', 'CircusFreak666', '5 hours ago', 'Slop_5.jpg', 1337, '256',
     'when someone asks how ur doing and u say "fine" but this is what it actually looks like inside. monday mornings be like. anyway who wants coffee #clownlife #existentialcoffee #sendhelp',
     [('~*Butterfly*~', 'this is going to appear in my nightmares and i accept that'), ('MusicFan88', 'the polka dots match his outfit im losing it')]),
    ('*', '#E8E0F0', 'PuppetMaster_X', '7 hours ago', 'Slop_6.jpg', 504, '78',
     'he knows what you did last summer. he knows what you did ALL the summers. that smile has witnessed civilizations rise and fall and hes still vibing. absolute legend #cursed #nostalgia #90skids',
     [('SurfGrl2001', 'i remember this guy!! he used to scare me SO bad as a kid omg'), ('DarkAngel_7', 'this energy is immaculate honestly')]),
    ('!', '#FFD700', 'EaglePatriot1776', '9 hours ago', 'Slop_7.jpg', 45210, '8,432',
     'if this doesnt give u goosebumps u might not have a pulse. they should put this in every history book from now until forever. the eagles are a nice touch too. grandma shared this 47 times already #epic #majestic #lionking #aiart',
     [('TechWiz42', 'u can literally see the watermark from the AI site in the corner lol'), ('SkaterBoi_X', 'why does the lion look sad tho')]),
    ('^_^', '#FFE0F0', 'FreshPrinceFan', '12 hours ago', 'Slop_8.jpg', 3287, '341',
     'LOV U FRESH PRINT. they made a sign and everything. this is what real dedication looks like. the fresh prince fandom never dies it only gets stronger #freshprince #willsmith #belairforever #90s',
     [('TheChangeIsMe', 'PRINT lmaooo they tried so hard and thats what matters'), ('MusicFan88', 'the heart drawing is sending me')]),
    ('?', '#FFFACD', 'PokeSlop_Daily', 'Yesterday', 'Slop_9.jpg', 7654, '512',
     'new pokemon just dropped?? this little guy is giving platypus meets beaver meets dragon and honestly hes my whole personality now. i would protect him with my life #pokemon #fakemon #hedgehogcore',
     [('CatDaddy_99', 'he looks like he just remembered he left the oven on'), ('~*Butterfly*~', 'the CLAWS omg what type is he?? water/ground??')]),
    (':D', '#FFD4B8', 'MonkeyBusiness', '2 days ago', 'Slop_10.jpg', 9102, '674',
     'airport selfie!! first class baby. they said i couldnt fly but they never said anything about BOOKING THE FLIGHT MYSELF. vacation mode activated #jetset #monkeytravel #firstclass #livingmybestlife',
     [('SurfGrl2001', 'his outfit is better than anything in my closet and im not even mad'), ('SkaterBoi_X', 'this monkey has a better life than me and i need to sit with that for a minute')]),
    ('X', '#1a1a1a;color:#c00', 'Doodseskader', '3 days ago', 'Slop_11.jpg', 6660, '666',
     'We are beyond excited to be bringing a whole new live show to you all next year!! New music, new visuals, new energy - so embrace the change and join us. We had so much fun making "The Change Is Me" and we know it\'ll be even better bringing it to life on stage.',
     [('DarkAngel_7', 'this goes so unbelievably hard. preordered three copies'), ('CircusFreak666', 'finally some REAL music on this cursed timeline')]),
]

feed_html = ''
for avatar, astyle, user, time_s, img, likes, ccount, caption, cmts in feed_posts:
    feed_html += feed_post(avatar, astyle, user, time_s, img, likes, ccount, caption, cmts)

# ===== RETRO SITE HOME TAB =====
home_posts = [
    ('B-)', '', 'SkaterBoi_X', 'Today at 2:31 PM EST',
     'just landed a kickflip at the park!! tony hawk pro skater 3 comes out this year whos hyped?!?! <br><span style="font-size:9px;color:#999">mood: stoked // listening to: blink-182 - All The Small Things</span>',
     'Give Kudos (12)', 'Reply (4)'),
    ('^_^', 'background:#FFE0F0', 'SurfGrl2001', 'Today at 1:15 PM EST',
     'Does anyone know how to make a <b>scrolling marquee</b> on their homepage?? I want to add one with glitter text!! Also check out my <a href="#">new profile layout</a> I worked on it ALL weekend<br><span style="font-size:9px;color:#999">mood: creative // listening to: Destiny\'s Child - Survivor</span>',
     'Give Kudos (8)', 'Reply (7)'),
    (':P', 'background:#E0FFE0', 'MusicFan88', 'Today at 11:42 AM EST',
     'Has anyone tried Napster?? I downloaded like 200 songs this week lol. My mom is mad because the phone line was busy all night<br><b>TOP 5 songs rn:</b><br>1. Linkin Park - In The End<br>2. Gorillaz - Clint Eastwood<br>3. Crazy Town - Butterfly<br>4. Outkast - Ms. Jackson<br>5. Daft Punk - One More Time<br><span style="font-size:9px;color:#999">mood: jammin\' // listening to: ALL OF THE ABOVE</span>',
     'Give Kudos (23)', 'Reply (11)'),
    ('>', 'background:#333;color:#0f0', 'TechWiz42', 'Yesterday at 9:18 PM EST',
     'Just upgraded to Mac OS 9.2!! The Sherlock search is amazing. Also got my iMac DV to connect to AIM and SlopZone at the same time. Living in the FUTURE.<br><span style="font-size:9px;color:#999">mood: nerdy // listening to: Moby - Porcelain</span>',
     'Give Kudos (5)', 'Reply (3)'),
]

home_posts_html = ''
for avatar, astyle, user, ts, body, kudos, reply in home_posts:
    style_attr = ' style="' + astyle + '"' if astyle else ''
    home_posts_html += '<div class="retro-post"><table cellpadding="0" cellspacing="0" border="0" class="retro-post-header" width="100%"><tr>'
    home_posts_html += '<td class="retro-avatar"' + style_attr + '>' + avatar + '</td>'
    home_posts_html += '<td class="retro-post-meta"><div class="retro-username"><a href="#">' + user + '</a></div><div class="retro-timestamp">' + ts + '</div></td>'
    home_posts_html += '</tr></table>'
    home_posts_html += '<div class="retro-post-body">' + body + '</div>'
    home_posts_html += '<div class="retro-post-actions"><a href="#">' + kudos + '</a><a href="#">' + reply + '</a><a href="#">Forward to a Friend</a></div></div>\n'


# ===== JAVASCRIPT =====
JS = r"""
// ===== UTILITY FUNCTIONS =====
function hasClass(el,c){return(' '+el.className+' ').indexOf(' '+c+' ')>-1}
function addClass(el,c){if(!hasClass(el,c))el.className=el.className?el.className+' '+c:c}
function removeClass(el,c){el.className=(' '+el.className+' ').replace(' '+c+' ',' ').replace(/^\s+|\s+$/g,'')}
function getAbsPos(el){var l=0,t=0;while(el){l+=el.offsetLeft||0;t+=el.offsetTop||0;el=el.offsetParent}return{left:l,top:t}}
function getAncestor(el,cls){while(el){if(el.className&&hasClass(el,cls))return el;el=el.parentNode}return null}
function padLeft(s,n,ch){s=s+'';while(s.length<n)s=ch+s;return s}
function formatNum(n){var s=n+'',r='';for(var i=s.length-1,c=0;i>=0;i--,c++){if(c>0&&c%3==0)r=','+r;r=s.charAt(i)+r}return r}
var $=function(id){return document.getElementById(id)};

// ===== CACHE DOM ELEMENTS =====
var desktop=$('desktop');
var finderWin=$('finder-window');
var browserWin=$('browser-window');
var contentArea=$('content-area');
var browserContent=$('browser-content-area');
var dragOutline=$('window-drag-outline');
var iconDragGhost=$('icon-drag-ghost');
var alertEl=$('os9-alert');
var alertTitle=$('alert-title');
var alertMsg=$('alert-message');
var clockEl=$('menu-clock');
var urlBar=$('url-bar');
var tabHome=$('tab-home');
var tabFeed=$('tab-feed');
var navHome=$('nav-home');
var navFeed=$('nav-feed');
var feedContainer=$('feed-posts-container');
var followConfirm=$('follow-confirm');
var followConfirmBox=$('follow-confirm-box');
var followConfirmText=$('follow-confirm-text');
var followCongrats=$('follow-congrats');
var followCongratsBox=$('follow-congrats-box');
var followCongratsText=$('follow-congrats-text');
var virusOverlay=$('virus-overlay');
var hitCounterEl=$('hit-counter');
var csTable=$('cs-table');
var loadDialog=$('loading-dialog');
var progressFill=$('progress-fill');
var loadStatus=$('loading-status');
var finderTitle=$('finder-title');
var finderStatus=$('finder-status');
var finderBackBtn=$('finder-back-btn');
var iconHd=$('icon-hd');
var iconInternet=$('icon-internet');
var iconShared=$('icon-shared');
var iconTrash=$('icon-trash');

// ===== SHARED STATE =====
var topZ=100;
function bringToFront(win){topZ++;win.style.zIndex=topZ}

// ===== CLOCK =====
function updateClock(){
  var now=new Date(),h=now.getHours(),m=padLeft(now.getMinutes(),2,'0');
  var ampm=h>=12?'PM':'AM';h=h%12;if(h==0)h=12;
  clockEl.innerHTML=h+':'+m+' '+ampm;
}
updateClock();setInterval(updateClock,15000);

// ===== DROPDOWN MENUS =====
var activeMenu=null;
var menuKeys=['apple','file','edit','view','special','help'];
var menuEls={},triggerEls={};
for(var i=0;i<menuKeys.length;i++){
  menuEls[menuKeys[i]]=$('menu-'+menuKeys[i]);
  triggerEls[menuKeys[i]]=$('mt-'+menuKeys[i]);
}

function closeAllMenus(){
  for(var k in menuEls){menuEls[k].style.display='none'}
  for(var k in triggerEls){triggerEls[k].style.background='';triggerEls[k].style.color=''}
  activeMenu=null;
}
function showMenu(key){
  closeAllMenus();
  menuEls[key].style.left=triggerEls[key].offsetLeft+'px';
  menuEls[key].style.display='block';
  triggerEls[key].style.background='#262626';triggerEls[key].style.color='#fff';
  activeMenu=key;
}

for(var i=0;i<menuKeys.length;i++){
  (function(key){
    triggerEls[key].onmousedown=function(e){
      e=e||window.event;
      if(e.stopPropagation)e.stopPropagation();else e.cancelBubble=true;
      if(activeMenu==key){closeAllMenus();return}
      showMenu(key);
    };
    triggerEls[key].onmouseover=function(){if(activeMenu)showMenu(key)};
  })(menuKeys[i]);
}

// Dropdown + CS popup item hover & click (single pass over divs)
var allDI=document.getElementsByTagName('div');
var csPopupEls=[];
for(var i=0;i<allDI.length;i++){
  var d=allDI[i];
  if(hasClass(d,'cs-popup')||hasClass(d,'cs-volume-popup')){
    csPopupEls.push(d);
  }
  if((hasClass(d,'dropdown-item')||hasClass(d,'cs-popup-item'))&&!hasClass(d,'di-off')){
    (function(el){
      el.onmouseover=function(){el.style.background='#339';el.style.color='#fff'};
      el.onmouseout=function(){el.style.background='';el.style.color=''};
    })(d);
  }
  if(hasClass(d,'dropdown-item')&&!hasClass(d,'di-off')){
    (function(el){
      el.onclick=function(){
        var t=el.innerHTML.replace(/<[^>]*>/g,'').replace(/\s+/g,' ').replace(/^\s+|\s+$/g,'');
        t=t.replace(/[\u25BA\u25B6]$/,'').replace(/^\s+|\s+$/g,'');
        handleDropdownClick(t);
      };
    })(d);
  }
}

function handleDropdownClick(text){
  closeAllMenus();
  if(text=='About This Computer')showAlert('About This Computer','Mac OS 9.2.2\nMemory: 256 MB\nVirtual Memory: 512 MB');
  else if(text=='Close Window'){if(finderWin.style.display!='none')finderWin.style.display='none';else if(browserWin.style.display!='none')browserWin.style.display='none'}
  else if(text=='Empty Trash...')showAlert('Trash','The trash is empty.');
  else if(text=='Shut Down'){desktop.style.background='#000';desktop.innerHTML=''}
  else if(text=='Restart')location.reload();
  else if(text=='Sleep'){desktop.style.visibility='hidden';document.onclick=function(){desktop.style.visibility='visible';document.onclick=null}}
  else if(text=='About Balloon Help...')showAlert('Balloon Help','Balloon Help displays explanations of items on the screen.');
  else if(text=='Mac Help')showAlert('Mac Help','Mac Help is not available.');
  else if(text=='Find...')showAlert('Sherlock 2','Sherlock 2 is not available.');
  else if(text=='Calculator')showAlert('Calculator','Calculator is not available.');
  else if(text=='New Folder')showAlert('New Folder','A new folder cannot be created here.');
  else if(text=='Preferences...')showAlert('Preferences','Preferences are not available.');
  else if(text=='View Options...')showAlert('View Options','View Options are not available.');
}

// ===== DESKTOP HEIGHT =====
function updateDesktopHeight(){
  var h=document.body.clientHeight||document.documentElement.clientHeight||window.innerHeight||600;
  desktop.style.height=(h-20)+'px';
}
updateDesktopHeight();
window.onresize=updateDesktopHeight;

// ===== WINDOW CONTENT HEIGHT =====
function updateContentHeight(win,el,fixedH){
  if(win.style.display=='none')return;
  var h=win.offsetHeight-fixedH;
  if(h<50)h=50;
  el.style.height=h+'px';
}
function updateAllLayouts(){
  updateContentHeight(finderWin,contentArea,85);
  updateContentHeight(browserWin,browserContent,67);
}
updateAllLayouts();

// ===== WINDOW DRAGGING =====
var winDrag={active:false,win:null,ox:0,oy:0};

function startWinDrag(e,win){
  e=e||window.event;
  if(e.preventDefault)e.preventDefault();
  bringToFront(win);
  winDrag.active=true;winDrag.win=win;
  winDrag.ox=e.clientX-win.offsetLeft;
  winDrag.oy=e.clientY-win.offsetTop;
  dragOutline.style.left=win.offsetLeft+'px';
  dragOutline.style.top=win.offsetTop+'px';
  dragOutline.style.width=win.offsetWidth+'px';
  dragOutline.style.height=win.offsetHeight+'px';
  dragOutline.style.display='block';
  win.style.visibility='hidden';
}

// ===== WINDOW RESIZING =====
var winResize={active:false,win:null,el:null,sx:0,sy:0,sw:0,sh:0,fixedH:0};

function startResize(e,win,el,fixedH){
  e=e||window.event;
  if(e.preventDefault)e.preventDefault();
  if(e.stopPropagation)e.stopPropagation();else e.cancelBubble=true;
  bringToFront(win);
  winResize.active=true;winResize.win=win;winResize.el=el;
  winResize.sx=e.clientX;winResize.sy=e.clientY;
  winResize.sw=win.offsetWidth;winResize.sh=win.offsetHeight;
  winResize.fixedH=fixedH;
}

// ===== ICON SELECTION =====
var selectedLabel=null;
function clearSelections(){
  if(selectedLabel){removeClass(selectedLabel,'icon-label-sel');selectedLabel=null}
}
function selectIcon(iconEl){
  clearSelections();
  var labels=iconEl.getElementsByTagName('div');
  for(var i=0;i<labels.length;i++){
    if(hasClass(labels[i],'icon-label')){addClass(labels[i],'icon-label-sel');selectedLabel=labels[i];break}
  }
}

// ===== DESKTOP ICON DRAGGING =====
var iconDrag={active:false,icon:null,ox:0,oy:0,sx:0,sy:0,moved:false};

function startIconDrag(e,iconEl){
  e=e||window.event;
  if(e.preventDefault)e.preventDefault();
  if(e.stopPropagation)e.stopPropagation();else e.cancelBubble=true;
  selectIcon(iconEl);
  iconDrag.active=true;iconDrag.icon=iconEl;
  iconDrag.sx=e.clientX;iconDrag.sy=e.clientY;
  iconDrag.ox=e.clientX-iconEl.offsetLeft;
  iconDrag.oy=e.clientY-iconEl.offsetTop;
  iconDrag.moved=false;
}

// ===== UNIFIED MOUSE HANDLERS =====
document.onmousemove=function(e){
  e=e||window.event;
  if(winDrag.active){
    dragOutline.style.left=(e.clientX-winDrag.ox)+'px';
    dragOutline.style.top=(e.clientY-winDrag.oy)+'px';
  }else if(winResize.active){
    var nw=winResize.sw+(e.clientX-winResize.sx);
    var nh=winResize.sh+(e.clientY-winResize.sy);
    if(nw<300)nw=300;if(nh<200)nh=200;
    winResize.win.style.width=nw+'px';
    winResize.win.style.height=nh+'px';
    updateContentHeight(winResize.win,winResize.el,winResize.fixedH);
  }else if(iconDrag.active){
    var dx=e.clientX-iconDrag.sx,dy=e.clientY-iconDrag.sy;
    if(!iconDrag.moved&&Math.abs(dx)<4&&Math.abs(dy)<4)return;
    if(!iconDrag.moved){
      iconDrag.moved=true;
      iconDragGhost.innerHTML=iconDrag.icon.innerHTML;
      iconDragGhost.style.display='block';
    }
    iconDragGhost.style.left=(e.clientX-iconDrag.ox)+'px';
    iconDragGhost.style.top=(e.clientY-iconDrag.oy)+'px';
  }
};

document.onmouseup=function(e){
  e=e||window.event;
  if(winDrag.active){
    winDrag.win.style.left=dragOutline.style.left;
    winDrag.win.style.top=dragOutline.style.top;
    dragOutline.style.display='none';
    winDrag.win.style.visibility='visible';
    winDrag.active=false;
    updateAllLayouts();
  }else if(winResize.active){
    winResize.active=false;
  }else if(iconDrag.active){
    if(iconDrag.moved){
      iconDrag.icon.style.right='auto';iconDrag.icon.style.bottom='auto';
      iconDrag.icon.style.left=(e.clientX-iconDrag.ox)+'px';
      iconDrag.icon.style.top=(e.clientY-iconDrag.oy)+'px';
      iconDragGhost.style.display='none';iconDragGhost.innerHTML='';
    }
    iconDrag.active=false;iconDrag.moved=false;
  }
};

// Close button handlers
$('close-finder').onclick=function(){finderWin.style.display='none'};
$('close-browser').onclick=function(){browserWin.style.display='none'};

// Title bar drag handlers
function isTitleBtn(t){return t.className&&(t.className.indexOf('window-btn')>-1||t.className.indexOf('zoom')>-1||t.className.indexOf('collapse')>-1)}
$('tb-finder').onmousedown=function(e){e=e||window.event;if(!isTitleBtn(e.target||e.srcElement))startWinDrag(e,finderWin)};
$('tb-browser').onmousedown=function(e){e=e||window.event;if(!isTitleBtn(e.target||e.srcElement))startWinDrag(e,browserWin)};

// Resize handlers
$('resize-finder').onmousedown=function(e){startResize(e,finderWin,contentArea,85)};
$('resize-browser').onmousedown=function(e){startResize(e,browserWin,browserContent,67)};

// Bring window to front on click
finderWin.onmousedown=function(){bringToFront(finderWin)};
browserWin.onmousedown=function(){bringToFront(browserWin)};

// Close menus on click outside
document.onmousedown=function(e){
  e=e||window.event;
  var t=e.target||e.srcElement;
  if(activeMenu&&!getAncestor(t,'dropdown-menu')&&!getAncestor(t,'menu-item')&&!getAncestor(t,'apple-logo')){
    closeAllMenus();
  }
  if(activeCSPopup&&!getAncestor(t,'cs-btn')){
    closeAllCSPopups();
  }
  if(t==desktop||t.id=='desktop'){clearSelections()}
};

// ===== ALERT DIALOG =====
function showAlert(title,msg){
  alertTitle.innerHTML=title;
  alertMsg.innerHTML=msg.replace(/\n/g,'<br>');
  alertEl.style.display='block';
  var dw=desktop.offsetWidth,dh=desktop.offsetHeight;
  alertEl.style.left=Math.floor((dw-280)/2)+'px';
  alertEl.style.top=Math.floor((dh-150)/2)+'px';
}
$('alert-ok-btn').onclick=function(){alertEl.style.display='none'};

// ===== FINDER NAVIGATION =====
var finderHistory=[];
var folderContents={
  'Mac OS 45 HD':{items:['Apple Extras','Applications','Assistants','Documents','Internet','System Folder','Utilities'],status:'7 items, 12.44 GB available'},
  'Apple Extras':{items:['AppleScript','Mac OS Runtime for Java'],status:'2 items, 12.44 GB available'},
  'Applications':{items:['Internet Explorer 5','SimpleText','Stickies','Calculator','Sherlock 2'],status:'5 items, 12.44 GB available'},
  'Assistants':{items:['Internet Setup Assistant','Mac OS Setup Assistant'],status:'2 items, 12.44 GB available'},
  'Documents':{items:['ReadMe.txt','About This Mac.txt'],status:'2 items, 12.44 GB available'},
  'Internet':{items:['Internet Explorer 5','Outlook Express','Netscape Communicator'],status:'3 items, 12.44 GB available'},
  'System Folder':{items:['Appearance','Apple Menu Items','Control Panels','Extensions','Fonts','Preferences'],status:'6 items, 12.44 GB available'},
  'Utilities':{items:['Disk Utility','Disk First Aid','Drive Setup','Apple System Profiler'],status:'4 items, 12.44 GB available'}
};

var folderImgHTML='<img src="icon-folder.gif" width="40" height="32">';
var fileImgHTML='<img src="icon-file.gif" width="32" height="40">';

function navigateFolder(name){
  var folder=folderContents[name];
  if(!folder){showAlert(name,'This folder is empty.');return}
  finderHistory.push(finderTitle.innerHTML);
  finderTitle.innerHTML=name;
  finderStatus.innerHTML=folder.status;
  contentArea.innerHTML='';
  for(var i=0;i<folder.items.length;i++){
    var item=folder.items[i];
    var isFolder=!!folderContents[item];
    var div=document.createElement('div');
    div.className='folder-icon';
    div.innerHTML=(isFolder?folderImgHTML:fileImgHTML)+'<div class="icon-label">'+item+'</div>';
    (function(d,nm,isF){
      d.onmousedown=function(ev){
        ev=ev||window.event;
        if(ev.stopPropagation)ev.stopPropagation();else ev.cancelBubble=true;
        selectIcon(d);
      };
      d.ondblclick=function(){
        if(isF)navigateFolder(nm);
        else showAlert(nm,'The file "'+nm+'" could not be opened.');
      };
    })(div,item,isFolder);
    contentArea.appendChild(div);
  }
  finderBackBtn.style.color=finderHistory.length>0?'#262626':'#999';
}

// Attach double-click to initial folder icons
var initFolders=contentArea.getElementsByTagName('div');
for(var i=0;i<initFolders.length;i++){
  if(hasClass(initFolders[i],'folder-icon')){
    (function(el){
      var labels=el.getElementsByTagName('div');
      var nm='';
      for(var j=0;j<labels.length;j++){
        if(hasClass(labels[j],'icon-label')){nm=labels[j].innerHTML;break}
      }
      el.onmousedown=function(ev){
        ev=ev||window.event;
        if(ev.stopPropagation)ev.stopPropagation();else ev.cancelBubble=true;
        selectIcon(el);
      };
      el.ondblclick=function(){navigateFolder(nm)};
    })(initFolders[i]);
  }
}

finderBackBtn.onclick=function(){
  if(finderHistory.length>0){
    var prev=finderHistory.pop();
    navigateFolder(prev);
    finderHistory.pop();
    finderBackBtn.style.color=finderHistory.length>0?'#262626':'#999';
  }
};

// ===== OPEN WINDOWS =====
function openWindow(win){
  win.style.display='block';
  bringToFront(win);
  updateAllLayouts();
}

// ===== DOUBLE-CLICK DESKTOP ICONS =====
iconHd.ondblclick=function(){openWindow(finderWin)};
iconInternet.ondblclick=function(){openBrowser()};
iconShared.ondblclick=function(){showAlert('Shared Folder','File sharing is not enabled.')};
iconTrash.ondblclick=function(){showAlert('Trash','The trash is empty.')};
iconHd.onmousedown=function(e){startIconDrag(e||window.event,iconHd)};
iconInternet.onmousedown=function(e){startIconDrag(e||window.event,iconInternet)};
iconShared.onmousedown=function(e){startIconDrag(e||window.event,iconShared)};
iconTrash.onmousedown=function(e){startIconDrag(e||window.event,iconTrash)};

// ===== BROWSER LOADING =====
var browserLoading=false;
var loadSteps=[
  {pct:8,text:'Contacting host...'},
  {pct:15,text:'Looking up www.slopzone.com...'},
  {pct:25,text:'Host contacted. Waiting for reply...'},
  {pct:35,text:'Connected to www.slopzone.com'},
  {pct:45,text:'Transferring data from www.slopzone.com...'},
  {pct:55,text:'Reading data... (2 of 14 items)'},
  {pct:65,text:'Reading data... (7 of 14 items)'},
  {pct:75,text:'Reading data... (11 of 14 items)'},
  {pct:85,text:'Formatting page...'},
  {pct:92,text:'Loading images...'},
  {pct:100,text:'Document: Done.'}
];

function shuffleFeed(){
  var posts=[];
  var children=feedContainer.childNodes;
  for(var i=children.length-1;i>=0;i--){
    if(children[i].nodeType==1)posts.push(feedContainer.removeChild(children[i]));
  }
  for(var i=posts.length-1;i>0;i--){
    var j=Math.floor(Math.random()*(i+1));
    var tmp=posts[i];posts[i]=posts[j];posts[j]=tmp;
  }
  for(var i=0;i<posts.length;i++)feedContainer.appendChild(posts[i]);
}

function openBrowser(){
  if(browserLoading)return;
  if(browserWin.style.display!='none'&&browserWin.style.display!=''){bringToFront(browserWin);return}
  shuffleFeed();
  browserLoading=true;
  progressFill.style.width='0';loadStatus.innerHTML='Contacting host...';
  loadDialog.style.display='block';
  var dw=desktop.offsetWidth,dh=desktop.offsetHeight;
  loadDialog.style.left=Math.floor((dw-300)/2)+'px';
  loadDialog.style.top=Math.floor((dh-120)/2)+'px';
  var step=0;
  function nextStep(){
    if(step>=loadSteps.length){
      loadDialog.style.display='none';
      openWindow(browserWin);
      browserLoading=false;
      return;
    }
    progressFill.style.width=loadSteps[step].pct+'%';
    loadStatus.innerHTML=loadSteps[step].text;
    step++;
    setTimeout(nextStep,200+Math.floor(Math.random()*400));
  }
  setTimeout(nextStep,300);
}

// ===== BROWSER TAB SWITCHING =====
function switchTab(tab){
  if(tab=='feed'){
    tabHome.style.display='none';tabFeed.style.display='block';
    navHome.style.background='';navHome.style.color='';
    navFeed.style.background='#99F';navFeed.style.color='#fff';
  }else{
    tabHome.style.display='block';tabFeed.style.display='none';
    navFeed.style.background='';navFeed.style.color='';
    navHome.style.background='#99F';navHome.style.color='#fff';
  }
  urlBar.value=tab=='feed'?'http://www.slopzone.com/feed':'http://www.slopzone.com/home';
}

navHome.onclick=function(){switchTab('home');return false};
navFeed.onclick=function(){switchTab('feed');return false};
$('browser-back').onclick=function(){switchTab('home')};
$('browser-forward').onclick=function(){switchTab('feed')};

// ===== LIKE BUTTONS =====
var allSpans=document.getElementsByTagName('span');
for(var i=0;i<allSpans.length;i++){
  if(hasClass(allSpans[i],'feed-like-btn')){
    (function(btn){
      btn.onclick=function(){
        var count=parseInt(btn.getAttribute('data-likes'))||0;
        var heart=btn.getElementsByTagName('span')[0];
        var countEl=btn.getElementsByTagName('span')[1];
        if(hasClass(heart,'feed-heart-liked')){
          count--;removeClass(heart,'feed-heart-liked');heart.innerHTML='&#9825;';
        }else{
          count++;addClass(heart,'feed-heart-liked');heart.innerHTML='&#9829;';
        }
        btn.setAttribute('data-likes',count);
        countEl.innerHTML=formatNum(count)+' likes';
      };
    })(allSpans[i]);
  }
}

// ===== FOLLOW BUTTONS =====
var pendingFollowBtn=null;
for(var i=0;i<allSpans.length;i++){
  if(hasClass(allSpans[i],'feed-follow-btn')){
    (function(btn){
      btn.onclick=function(){
        if(hasClass(btn,'feed-follow-following')){
          removeClass(btn,'feed-follow-following');
          btn.innerHTML='+ Follow';return;
        }
        pendingFollowBtn=btn;
        var user=btn.id.replace('ff-','');
        followConfirmText.innerHTML='Are you sure you want to subscribe to <b>'+user+'</b>\'s updates? You will receive email notifications for new posts.';
        followConfirm.style.display='block';
        followConfirmBox.style.left=Math.floor((browserWin.offsetWidth-260)/2)+'px';
        followConfirmBox.style.top=Math.floor((browserWin.offsetHeight-150)/2)+'px';
      };
    })(allSpans[i]);
  }
}

$('follow-ok-btn').onclick=function(){
  if(pendingFollowBtn){addClass(pendingFollowBtn,'feed-follow-following');pendingFollowBtn.innerHTML='Following'}
  followConfirm.style.display='none';
  followCongratsText.innerHTML='Congrats! You\'re a subscriber to a shit for brains';
  followCongrats.style.display='block';
  followCongratsBox.style.left=Math.floor((browserWin.offsetWidth-360)/2)+'px';
  followCongratsBox.style.top=Math.floor((browserWin.offsetHeight-180)/2)+'px';
  pendingFollowBtn=null;
};
$('follow-cancel-btn').onclick=function(){followConfirm.style.display='none';pendingFollowBtn=null};
$('follow-confirm-bg').onclick=function(){followConfirm.style.display='none';pendingFollowBtn=null};
$('follow-congrats-ok').onclick=function(){followCongrats.style.display='none'};
$('follow-congrats-bg').onclick=function(){followCongrats.style.display='none'};

// ===== HIT COUNTER =====
var hitCount=4721;
setInterval(function(){
  hitCount+=Math.floor(Math.random()*3);
  var s=padLeft(hitCount+'',6,'0');
  hitCounterEl.innerHTML=s.replace(/(\d)(?=(\d{3})+$)/g,'$1,');
},8000);

// ===== CONTROL STRIP =====
var activeCSPopup=null;
function closeAllCSPopups(){
  for(var i=0;i<csPopupEls.length;i++)csPopupEls[i].style.display='none';
  activeCSPopup=null;
}

var csBtns=['cs-appletalk','cs-cd','cs-itunes','cs-keychain','cs-monitor-depth','cs-remote','cs-monitor-res','cs-printer','cs-sound','cs-websharing'];
for(var i=0;i<csBtns.length;i++){
  (function(id){
    var btn=$(id);
    if(!btn)return;
    btn.onclick=function(e){
      e=e||window.event;
      if(e.stopPropagation)e.stopPropagation();else e.cancelBubble=true;
      var popup=btn.getElementsByTagName('div')[0];
      if(!popup)return;
      if(activeCSPopup==id){closeAllCSPopups();return}
      closeAllCSPopups();
      popup.style.display='block';
      activeCSPopup=id;
    };
  })(csBtns[i]);
}

$('cs-close').onclick=function(){
  var cells=csTable.getElementsByTagName('td');
  for(var i=0;i<cells.length;i++){
    if(cells[i].id!='cs-close')cells[i].style.display=cells[i].style.display=='none'?'':'none';
  }
};

// Volume slider
(function(){
  var thumb=$('cs-volume-thumb');
  if(!thumb)return;
  var track=thumb.parentNode;
  var dragging=false;
  thumb.onmousedown=function(e){
    e=e||window.event;
    if(e.stopPropagation)e.stopPropagation();else e.cancelBubble=true;
    if(e.preventDefault)e.preventDefault();
    dragging=true;
  };
  var oldMove=document.onmousemove;
  document.onmousemove=function(e){
    e=e||window.event;
    if(dragging){
      var tPos=getAbsPos(track);
      var y=e.clientY-tPos.top;
      var pct=y/track.offsetHeight;
      if(pct<0)pct=0;if(pct>1)pct=1;
      thumb.style.top=(pct*100)+'%';
    }
    if(oldMove)oldMove(e);
  };
  var oldUp=document.onmouseup;
  document.onmouseup=function(e){
    dragging=false;
    if(oldUp)oldUp(e);
  };
})();

// ===== WALLPAPER SCROLL ANIMATION =====
var wpOffset=0;
setInterval(function(){
  wpOffset=(wpOffset+14)%1440;
  desktop.style.backgroundPosition='0 '+wpOffset+'px';
},200);

// ===== BLINK TEXT ANIMATION =====
var blinkEls=[];
for(var i=0;i<allSpans.length;i++){
  if(hasClass(allSpans[i],'retro-blink'))blinkEls.push(allSpans[i]);
}
var blinkOn=true;
setInterval(function(){
  blinkOn=!blinkOn;
  for(var i=0;i<blinkEls.length;i++){
    blinkEls[i].style.visibility=blinkOn?'visible':'hidden';
  }
},500);

// ===== VIRUS POPUPS =====
var virusActive=false;
var virusPopups=[];
var virusMessages=[
  {icon:'\u26A0',title:'WARNING',msg:'Your system has been infected with W32.BlasterWorm!'},
  {icon:'\u2620',title:'CRITICAL ERROR',msg:'A fatal exception 0E has occurred at 0028:C0034B03'},
  {icon:'\u26A0',title:'VIRUS ALERT',msg:'Trojan.Horse.Win32 detected in System Folder!'},
  {icon:'\u2622',title:'DANGER',msg:'Memory overflow in sector 0x4F21. Data corrupted.'},
  {icon:'\u274C',title:'SYSTEM FAILURE',msg:'Hard drive formatting in progress... 23% complete'},
  {icon:'\u26A0',title:'ALERT',msg:'Your files are being uploaded to an unknown server!'},
  {icon:'\u2620',title:'FATAL ERROR',msg:'Cannot find HIMEM.SYS. Your RAM is gone.'},
  {icon:'\u2622',title:'MALWARE DETECTED',msg:'ILOVEYOU.VBS is spreading through your contacts!'},
  {icon:'\u26A0',title:'SECURITY BREACH',msg:'Hackers have gained access to your Macintosh HD!'},
  {icon:'\u274C',title:'ERROR 666',msg:'The application "Finder" has unexpectedly quit. (again)'},
  {icon:'\u2620',title:'OH NO',msg:'Your desktop icons are escaping. Please remain calm.'},
  {icon:'\u26A0',title:'HELP',msg:'The trash can is full. It is VERY full. Too full.'}
];

var virusPresets={
  F1:[{l:15.3,t:3.8,w:30.8,h:45.6},{l:43.3,t:10,w:41,h:44.4},{l:46.7,t:48,w:30.3,h:46.8},{l:5.5,t:27.9,w:42.5,h:68.8}],
  F2:[{l:4.5,t:4.4,w:42.2,h:67.6},{l:58.3,t:3.6,w:38.7,h:44.4},{l:43.7,t:41.3,w:30.3,h:42.6},{l:23,t:48,w:30.3,h:46.8}],
  F3:[{l:7.9,t:4.1,w:30.3,h:42.6},{l:27.8,t:16.3,w:42.2,h:67.6},{l:63,t:5.2,w:30.3,h:46.8},{l:12.6,t:52.9,w:38.7,h:44.4}],
  F4:[{l:11.3,t:5.6,w:44.9,h:45.8},{l:50,t:8.3,w:30.3,h:46.8},{l:6.2,t:26,w:42.2,h:67.6},{l:53.2,t:39.8,w:30.3,h:42.6}]
};

function spawnVirusPopup(cfg){
  var msg=virusMessages[Math.floor(Math.random()*virusMessages.length)];
  var popup=document.createElement('div');
  popup.className='virus-popup';
  var vw=document.body.clientWidth||800;
  var vh=document.body.clientHeight||600;
  popup.style.left=Math.floor(cfg.l/100*vw)+'px';popup.style.top=Math.floor(cfg.t/100*vh)+'px';
  popup.style.width=Math.floor(cfg.w/100*vw)+'px';popup.style.height=Math.floor(cfg.h/100*vh)+'px';
  popup.innerHTML='<div class="virus-title"><table cellpadding="0" cellspacing="0" border="0" width="100%"><tr>'
    +'<td class="v-close">&times;</td>'
    +'<td class="virus-title-text">'+msg.title+'</td></tr></table></div>'
    +'<table cellpadding="0" cellspacing="0" border="0" class="virus-body-wrap"><tr><td valign="middle" align="center">'
    +'<div class="virus-body"><div class="virus-icon-text">'+msg.icon+'</div>'
    +'<div class="virus-msg">'+msg.msg+'</div>'
    +'<span class="virus-btn">OK</span></div>'
    +'</td></tr></table>';
  var titleEl=popup.getElementsByTagName('div')[0];
  titleEl.onmousedown=function(e){
    e=e||window.event;
    var t=e.target||e.srcElement;
    if(t.className&&t.className.indexOf('v-close')>-1)return;
    if(e.preventDefault)e.preventDefault();
    var sx=e.clientX,sy=e.clientY;
    var ol=parseInt(popup.style.left)||0,ot=parseInt(popup.style.top)||0;
    var oldM=document.onmousemove,oldU=document.onmouseup;
    document.onmousemove=function(ev){
      ev=ev||window.event;
      popup.style.left=(ol+ev.clientX-sx)+'px';
      popup.style.top=(ot+ev.clientY-sy)+'px';
      if(oldM)oldM(ev);
    };
    document.onmouseup=function(ev){
      document.onmousemove=oldM;
      document.onmouseup=oldU;
      if(oldU)oldU(ev);
    };
  };
  var dismissPopup=function(e){
    e=e||window.event;
    if(e.stopPropagation)e.stopPropagation();else e.cancelBubble=true;
    for(var i=0;i<virusPopups.length;i++){if(virusPopups[i]==popup){virusPopups.splice(i,1);break}}
    popup.parentNode.removeChild(popup);
    if(virusPopups.length==0)stopVirus();
  };
  popup.getElementsByTagName('td')[0].onclick=dismissPopup;
  var btns=popup.getElementsByTagName('span');
  for(var i=0;i<btns.length;i++){
    if(hasClass(btns[i],'virus-btn'))btns[i].onclick=dismissPopup;
  }
  virusOverlay.appendChild(popup);
  virusPopups.push(popup);
}

function startVirus(preset){
  if(virusActive)return;
  virusActive=true;virusOverlay.style.display='block';
  var layouts=virusPresets[preset]||virusPresets.F1;
  for(var i=0;i<layouts.length;i++){
    (function(cfg,delay){setTimeout(function(){spawnVirusPopup(cfg)},delay)})(layouts[i],i*150);
  }
}
function stopVirus(){
  virusActive=false;virusOverlay.style.display='none';
  virusOverlay.innerHTML='';virusPopups=[];
}

// Numpad 1-4 triggers virus, Escape dismisses
document.onkeydown=function(e){
  e=e||window.event;
  var key=e.keyCode||0;
  if(key==97){if(e.preventDefault)e.preventDefault();stopVirus();startVirus('F1')}
  else if(key==98){if(e.preventDefault)e.preventDefault();stopVirus();startVirus('F2')}
  else if(key==99){if(e.preventDefault)e.preventDefault();stopVirus();startVirus('F3')}
  else if(key==100){if(e.preventDefault)e.preventDefault();stopVirus();startVirus('F4')}
  else if(key==27){if(virusActive){if(e.preventDefault)e.preventDefault();stopVirus()}}
};

"""

# ===== ASSEMBLE HTML =====
HTML = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<title>Mac OS 9</title>
<style type="text/css">""" + CSS + """</style>
</head>
<body>
<!-- MENU BAR -->
<div id="menubar">
<table cellpadding="0" cellspacing="0" border="0" width="100%"><tr>
<td class="apple-logo" id="mt-apple"><img src="apple-logo.png" width="14" height="16" style="vertical-align:middle"></td>
<td class="menu-item" id="mt-file">File</td>
<td class="menu-item" id="mt-edit">Edit</td>
<td class="menu-item" id="mt-view">View</td>
<td class="menu-item" id="mt-special">Special</td>
<td class="menu-item" id="mt-help">Help</td>
<td width="100%">&nbsp;</td>
<td id="menu-clock" nowrap>&nbsp;</td>
<td><div style="width:1px;height:14px;background:#999;font-size:1px;margin:0 4px">&nbsp;</div></td>
<td><img src="finder-icon.png" width="16" height="16" style="vertical-align:middle;margin-right:4px"></td>
<td class="menu-item" style="font-weight:bold">Finder</td>
</tr></table>
""" + dropdown_menu('apple', apple_menu) + dropdown_menu('file', file_menu) + dropdown_menu('edit', edit_menu) + dropdown_menu('view', view_menu) + dropdown_menu('special', special_menu) + dropdown_menu('help', help_menu) + """</div>

<!-- DESKTOP -->
<div id="desktop">

<!-- Desktop Icons -->
<div class="desktop-icon" id="icon-hd" style="right:20px;top:40px">
<img src="icon-hd.gif" width="48" height="32"><div class="icon-label">MacOS 9HD</div></div>

<div class="desktop-icon" id="icon-shared" style="right:20px;top:140px">
<img src="icon-shared.gif" width="48" height="40"><div class="icon-label">Shared Folder</div></div>

<div class="desktop-icon" id="icon-internet" style="right:16px;top:244px">
<img src="icon-globe.gif" width="48" height="48"><div class="icon-label">Browse the Internet</div></div>

<div class="desktop-icon" id="icon-trash" style="right:24px;bottom:30px">
<img src="icon-trash.gif" width="42" height="48"><div class="icon-label">Trash</div></div>

<!-- FINDER WINDOW -->
<div class="window" id="finder-window" style="left:280px;top:80px;width:520px;height:360px">
""" + title_bar('Mac OS 45 HD', 'icon-hd-small.gif', 'close-finder', 'finder', 'finder-title') + """
<div class="status-bar" id="finder-status-wrap"><span id="finder-status">7 items, 12.44 GB available</span></div>
<div class="finder-nav-bar"><span class="finder-back-btn" id="finder-back-btn" style="color:#999">&#9664; Back</span></div>
<div class="content-area" id="content-area">
""" + finder_icons_html + """</div>
<div class="window-bottom"><table cellpadding="0" cellspacing="0" border="0"><tr>
<td class="bottom-bar" width="100%">&nbsp;</td>
<td width="16"><img src="resize-handle.gif" width="16" height="16" id="resize-finder"></td>
</tr></table></div>
<div style="height:4px"></div>
</div>

<!-- ALERT DIALOG -->
<div id="os9-alert">
""" + title_bar_plain('Alert', 'alert-title') + """
<table cellpadding="0" cellspacing="0" border="0"><tr>
<td class="alert-icon"><img src="icon-alert.gif" width="32" height="32"></td>
<td class="alert-text" id="alert-message">Message</td>
</tr></table>
<div class="alert-buttons"><span class="os9-btn" id="alert-ok-btn">OK</span></div>
</div>

<!-- LOADING DIALOG -->
<div class="loading-dialog" id="loading-dialog">
""" + title_bar_plain('Connecting...') + """
<div class="loading-body">
<div>Opening Internet Explorer 5...</div>
<div class="loading-url">http://www.slopzone.com/home</div>
<div class="os9-progress"><div class="os9-progress-fill" id="progress-fill"></div></div>
<div class="loading-status" id="loading-status">Contacting host...</div>
</div>
</div>

<!-- BROWSER WINDOW -->
<div class="window" id="browser-window" style="left:20px;top:20px;width:920px;height:1032px;display:none">
""" + title_bar('Internet Explorer 5 - SlopZone', None, 'close-browser', 'browser') + """
<div class="browser-toolbar"><table cellpadding="0" cellspacing="2" border="0" width="100%"><tr>
<td width="22"><div class="browser-nav-btn" id="browser-back">&#9664;</div></td>
<td width="22"><div class="browser-nav-btn" id="browser-forward">&#9654;</div></td>
<td width="22"><div class="browser-nav-btn">&#8635;</div></td>
<td width="22"><div class="browser-nav-btn">&#8962;</div></td>
<td class="browser-url-label">Address:</td>
<td><input class="browser-url-bar" id="url-bar" type="text" value="http://www.slopzone.com/home" readonly></td>
</tr></table></div>
<div class="browser-content" id="browser-content-area">
<div class="retro-site">
<!-- Header -->
<div class="retro-header"><h1>SlopZone</h1><div class="retro-tagline">Connect with your friends in cyberspace! &trade; Est. 1999</div></div>
<!-- Nav -->
<div class="retro-nav">
<a href="#" id="nav-home" style="background:#99F;color:#fff">Home</a> <span class="retro-nav-sep">|</span>
<a href="#" id="nav-feed">Photo Feed</a> <span class="retro-nav-sep">|</span>
<a href="#">My Profile</a> <span class="retro-nav-sep">|</span>
<a href="#">Friends</a> <span class="retro-nav-sep">|</span>
<a href="#">Messages (3)</a> <span class="retro-nav-sep">|</span>
<a href="#">Chat Rooms</a> <span class="retro-nav-sep">|</span>
<a href="#">Help</a>
</div>
<!-- Marquee -->
<div class="retro-marquee-wrap"><marquee scrollamount="3">*** Welcome back, TheChangeIsMe! You have 3 new messages and 2 friend requests! Check out the NEW chat rooms! ***</marquee></div>

<!-- HOME TAB -->
<div id="tab-home">
<table cellpadding="0" cellspacing="0" border="0" width="100%"><tr>
<td class="retro-sidebar" valign="top">
<div class="retro-profile-card">
<div class="retro-profile-pic" style="background:url('Avatar.png') center no-repeat;background-size:48px 48px"></div>
<div style="font-weight:bold;color:#006;font-size:11px">TheChangeIsMe</div>
<div style="color:#666;font-style:italic;font-size:8px;margin-top:2px">~*Until all is 45*~</div>
<div style="margin-top:4px"><span style="color:#090;font-weight:bold">Online</span></div>
</div>
<h3>My Stats</h3><ul><li>Friends: <b>47</b></li><li>Posts: <b>312</b></li><li>Kudos: <b>89</b></li><li>Member since: <b>'99</b></li></ul>
<h3>Buddies Online</h3><ul>
<li><font color="#0C0">&#9679;</font> <a href="#">SurfGrl2001</a></li>
<li><font color="#0C0">&#9679;</font> <a href="#">SkaterBoi_X</a></li>
<li><font color="#0C0">&#9679;</font> <a href="#">MusicFan88</a></li>
<li><font color="#C00">&#9679;</font> <a href="#">DarkAngel_7</a></li>
<li><font color="#C00">&#9679;</font> <a href="#">TechWiz42</a></li>
<li><font color="#C00">&#9679;</font> <a href="#">~*Butterfly*~</a></li>
</ul>
<h3>Cool Links</h3><ul><li><a href="#">Free Cursors!</a></li><li><a href="#">MIDI Music</a></li><li><a href="#">Guestbook</a></li><li><a href="#">Web Awards</a></li></ul>
<div class="retro-webring"><b>SlopZone WebRing</b><br><a href="#">&lt;&lt; Prev</a> | <a href="#">Random</a> | <a href="#">Next &gt;&gt;</a></div>
</td>
<td class="retro-main" valign="top">
<h3 style="font-family:Verdana,sans-serif;font-size:13px;color:#006;margin:0 0 6px">
<span class="retro-blink">*</span> My SlopZone Feed <span class="retro-blink">*</span></h3>
<hr class="retro-hr">
""" + home_posts_html + """
<hr class="retro-hr">
<div class="retro-guestbook">
<h4>&#9997; Sign My Guestbook!</h4>
<div style="font-size:9px;font-family:Verdana,sans-serif;margin:0 0 4px">Leave a message for TheChangeIsMe:</div>
<textarea placeholder="Type your message here... (max 500 chars)"></textarea>
<div style="margin-top:4px"><span class="retro-btn">Post Message</span> <span class="retro-btn">Add Smiley :-)</span></div>
</div>
<div style="text-align:center;margin-top:6px">
<span class="retro-badge">Best viewed with Internet Explorer 5.0</span>
<span class="retro-badge">800x600 resolution</span>
<span class="retro-badge">Made on a Mac</span>
<span class="retro-badge">HTML 4.0</span>
</div>
</td></tr></table>
</div>

<!-- FEED TAB -->
<div id="tab-feed" style="display:none">
<div style="padding:8px 12px">
<h3 style="font-family:Verdana,sans-serif;font-size:13px;color:#006;margin:0 0 8px;text-align:center">
<span class="retro-blink">*</span> Photo Feed <span class="retro-blink">*</span></h3>
<hr class="retro-hr">
<div id="feed-posts-container">
""" + feed_html + """
</div>
</div></div>

<!-- Footer -->
<div class="retro-footer">
<div>&copy; 2001 SlopZone Inc. All rights reserved. | <a href="#">Terms</a> | <a href="#">Privacy</a> | <a href="#">Contact</a></div>
<div>You are visitor #<span class="hit-counter" id="hit-counter">004,721</span></div>
<div style="margin-top:3px"><span class="retro-badge">Netscape Now!</span> <span class="retro-badge">GeoCities</span> <span class="retro-badge">Y2K compliant</span></div>
</div>
</div>
</div>

<!-- Follow Confirm -->
<div id="follow-confirm" style="display:none">
<div id="follow-confirm-bg"></div>
<div id="follow-confirm-box">
""" + title_bar_plain('Confirm') + """
<table cellpadding="0" cellspacing="0" border="0"><tr>
<td style="padding:14px 0 14px 16px;vertical-align:top"><img src="icon-follow.gif" width="32" height="32"></td>
<td class="follow-confirm-text" id="follow-confirm-text">Are you sure?</td>
</tr></table>
<div class="follow-confirm-buttons"><span class="os9-btn" id="follow-cancel-btn">Cancel</span> <span class="os9-btn" id="follow-ok-btn" style="font-weight:bold">Subscribe</span></div>
</div></div>

<!-- Follow Congrats -->
<div id="follow-congrats" style="display:none">
<div id="follow-congrats-bg"></div>
<div id="follow-congrats-box">
""" + title_bar_plain('Congratulations!') + """
<table cellpadding="0" cellspacing="0" border="0"><tr>
<td style="padding:14px 0 14px 16px;vertical-align:top"><img src="icon-alert.gif" width="32" height="32"></td>
<td class="follow-confirm-text" id="follow-congrats-text">Congrats!</td>
</tr></table>
<div class="follow-confirm-buttons"><span class="os9-btn" id="follow-congrats-ok" style="font-weight:bold">OK</span></div>
</div></div>

<div class="window-bottom"><table cellpadding="0" cellspacing="0" border="0"><tr>
<td class="bottom-bar" width="100%">&nbsp;</td>
<td width="16"><img src="resize-handle.gif" width="16" height="16" id="resize-browser"></td>
</tr></table></div>
<div style="height:4px"></div>
</div>

<!-- Drag outlines -->
<div id="window-drag-outline"></div>
<div id="icon-drag-ghost"></div>

<!-- CONTROL STRIP -->
<div id="control-strip">
<table cellpadding="0" cellspacing="1" border="0" id="cs-table"><tr>
<td class="cs-close" id="cs-close" style="background:#bbb;border:1px outset #ccc;cursor:default;width:18px;text-align:center;font-weight:bold;font-size:10px">&times;</td>
<td class="cs-nav" style="background:#bbb;border:1px outset #ccc;cursor:default" id="cs-nav-left">&#9664;</td>
""" + cs_html + """
<td class="cs-nav" style="background:#bbb;border:1px outset #ccc;cursor:default" id="cs-nav-right">&#9654;</td>
<td class="cs-nav" style="background:#bbb;border:1px outset #ccc;cursor:default" id="cs-expand">&#9650;</td>
</tr></table>
</div>

</div><!-- end desktop -->

<!-- VIRUS OVERLAY -->
<div id="virus-overlay"></div>

<script type="text/javascript">
// Hidden span for alert title
var _alertTitleEl=document.createElement('span');_alertTitleEl.id='alert-title';_alertTitleEl.style.display='none';document.body.appendChild(_alertTitleEl);
// Hidden span for finder title
var _finderTitleEl=document.createElement('span');_finderTitleEl.id='finder-title';
// Find the finder title bar center span
var tbCenterEls=document.getElementsByTagName('span');
for(var i=0;i<tbCenterEls.length;i++){
  if(tbCenterEls[i].parentNode&&tbCenterEls[i].parentNode.className=='tb-center'&&tbCenterEls[i].innerHTML=='Mac OS 45 HD'){
    tbCenterEls[i].id='finder-title';break;
  }
}

// Close button handlers
document.getElementById('close-finder').onclick=function(){document.getElementById('finder-window').style.display='none'};
document.getElementById('close-browser').onclick=function(){document.getElementById('browser-window').style.display='none'};

// Title bar drag handlers
document.getElementById('tb-finder').onmousedown=function(e){
  e=e||window.event;var t=e.target||e.srcElement;
  if(t.className&&(t.className.indexOf('window-btn')>-1||t.className.indexOf('zoom')>-1||t.className.indexOf('collapse')>-1))return;
  startWinDrag(e,'finder-window');
};
document.getElementById('tb-browser').onmousedown=function(e){
  e=e||window.event;var t=e.target||e.srcElement;
  if(t.className&&(t.className.indexOf('window-btn')>-1||t.className.indexOf('zoom')>-1||t.className.indexOf('collapse')>-1))return;
  startWinDrag(e,'browser-window');
};

// Resize handlers
document.getElementById('resize-finder').onmousedown=function(e){startResize(e,'finder-window','content-area',85)};
document.getElementById('resize-browser').onmousedown=function(e){startResize(e,'browser-window','browser-content-area',67)};

// Bring window to front on click
document.getElementById('finder-window').onmousedown=function(){bringToFront(document.getElementById('finder-window'))};
document.getElementById('browser-window').onmousedown=function(){bringToFront(document.getElementById('browser-window'))};

""" + JS + """
</script>
</body>
</html>"""

# Write the file
outpath = '/Users/lnnt/Desktop/macos9/index-os9.html'
with open(outpath, 'w') as f:
    f.write(HTML)
print("Generated " + outpath)
print("Total size: " + str(len(HTML)) + " bytes")
