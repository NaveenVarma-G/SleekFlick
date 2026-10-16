from PIL import Image, ImageDraw, ImageFont
F="/usr/share/fonts/truetype/sand-box/google/Be Vietnam Pro/BeVietnamPro-"
def f(w,s): return ImageFont.truetype(F+w+".ttf",s)
W,H=1080,1350; M=90
BG="#0B0B0F"; Y="#FFE600"; WH="#FFFFFF"; G="#B4B4BE"; FT="#8A8A96"
SZ={"h":100,"h2":84,"big":200,"b":52,"s":40}
WT={"h":"Black","h2":"Black","big":"Black","b":"Medium","s":"Regular"}
def wrap(d,t,fo,mw):
    out=[]
    for para in t.split("\n"):
        line=""
        for w in para.split(" "):
            tt=(line+" "+w).strip()
            if d.textlength(tt,font=fo)<=mw: line=tt
            else: out.append(line); line=w
        out.append(line)
    return out
def layout(d,blocks):
    items=[];y=0
    for kind,t,*o in blocks:
        if kind=="gap": y+=t; continue
        sz=SZ[kind]; fo=f(WT[kind],sz)
        col=o[0] if o else (WH if kind in("h","h2","b") else Y if kind=="big" else G)
        for ln in wrap(d,t,fo,W-2*M):
            items.append((y,ln,fo,col)); y+=int(sz*1.2)
        y+=26
    return items,y-26
def slide(name,blocks,tag="",page="",source="",h=H,top=150,bottom=170):
    im=Image.new("RGB",(W,h),BG); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,18],fill=Y)
    off=(h-H)//2  # 4:5 safe area offset for tall canvases
    if tag: d.text((M,off+70),tag.upper(),font=f("Bold",32),fill=Y)
    if page: d.text((W-M,off+70),page,font=f("Bold",32),fill=G,anchor="ra")
    items,th=layout(d,blocks)
    area_top=off+top; area_bot=off+H-bottom
    y0=area_top+max(0,(area_bot-area_top-th)//2)
    for y,ln,fo,col in items: d.text((M,y0+y),ln,font=fo,fill=col)
    if False and source:  # source footers removed per user; sources live in drafts.md
        for i,ln in enumerate(wrap(d,"Source: "+source,f("Regular",28),W-2*M)):
            d.text((M,off+H-120+i*36),ln,font=f("Regular",28),fill=FT)
    im.save(name)
    assert y0+th<=area_bot+5, (name,"overflow")

def watermark(path, off=0):
    """Semi-transparent @SleekFlick_AI, bottom-right of the 4:5 (safe) area."""
    im=Image.open(path).convert("RGBA")
    lay=Image.new("RGBA",im.size,(0,0,0,0)); d=ImageDraw.Draw(lay)
    d.text((W-M,off+H-22),"@SleekFlick_AI",font=f("SemiBold",28),fill=(255,255,255,150),anchor="rd")
    Image.alpha_composite(im,lay).convert("RGB").save(path)
