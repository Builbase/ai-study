#!/usr/bin/env python3
"""images/raw/ の原本に矩形のボカシをかけて images/ に書き出す。座標は原本のピクセル。"""
import subprocess, sys
B = {
 'cal-01-editor.png': [(690,325,215,80),(1280,8,92,50)],
 'cal-02-guest-add.png': [(628,268,340,100),(1210,8,162,50)],
 'cal-03-find-time.png': [(870,325,240,80),(518,412,250,26),(518,525,125,60),(1210,8,162,50)],
 'cal-04-recurrence-menu.png': [(690,325,215,80),(1280,8,92,50)],
 'cal-07-guest-popup.png': [(125,735,440,70),(125,810,60,60)],
 'cal-08-propose-time.png': [(1495,8,60,55),(925,180,65,60),(1320,150,200,36),(1455,180,70,55)],
 'cal-09-organizer-edit.png': [(690,390,215,75),(1280,8,92,50)],
 'cal-09-organizer-edit-top.png': [(690,390,215,75)],
 'cal-10-guest-edit.png': [(80,530,210,40),(770,415,260,80),(1495,8,60,55)],
 'cal-10-guest-edit-top.png': [(80,530,210,40),(770,415,260,80)],
 'cal-11-organizer-menu.png': [(115,780,65,65),(115,870,330,60)],
 'cal-13-guest-permission.png': [(30,245,60,70),(30,325,370,65)],
 'cal-14-external-guest.png': [(480,148,290,44)],
 'cal-15-organizer-popup.png': [(125,855,80,70),(125,950,360,65)],
 'docs-01-share-dialog.png': [(55,415,410,90)],
 'docs-02-general-access.png': [(55,415,410,90)],
 'docs-04-suggestion.png': [(555,400,125,48),(1095,355,60,60),(1095,560,60,65),(1095,620,320,42)],
 'docs-05-comment.png': [(555,400,125,48),(1095,155,60,60),(1095,330,60,60),(1095,465,60,60),(1095,520,320,45)],
 'docs-06-at-menu.png': [(205,82,240,118)],
 'docs-07-smart-chip.png': [(970,615,185,44)],
 'docs-08-gemini.png': [(535,528,95,26),(955,280,50,50),(955,440,50,50),(955,550,50,50),(1260,8,55,45),(1045,452,290,26)],
 'meet-01-more-menu.png': [(730,320,105,105),(1450,8,55,45)],
 'meet-03-tools.png': [(730,320,105,105),(1450,8,55,45)],
 'docs-09-version-history.png': [(662,638,88,32)],
 'cal-16-booking-page.png': [(1270,8,46,60)],
 'meet-04-companion.png': [(890,20,220,45),(1110,18,55,50)],
 'meet-05-companion-incall.png': [],
}
for f, boxes in B.items():
    if not boxes:
        subprocess.run(['cp',f'raw/{f}',f]); print('ok  '+f+' (no mask)'); continue
    fc=''; last='[0:v]'
    for i,(x,y,w,h) in enumerate(boxes):
        fc += f'[0:v]crop={w}:{h}:{x}:{y},scale={max(2,w//10)}:{max(2,h//10)},scale={w}:{h}:flags=neighbor[b{i}];{last}[b{i}]overlay={x}:{y}[o{i}];'
        last=f'[o{i}]'
    fc=fc.rstrip(';')
    r=subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'raw/{f}','-filter_complex',fc,'-map',last,f],capture_output=True,text=True)
    print(('ok  ' if r.returncode==0 else 'ERR ')+f, r.stderr.strip()[:200])
