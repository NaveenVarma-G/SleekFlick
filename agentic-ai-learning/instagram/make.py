from render import *
slide("carousel-01.png",[("h","5 lessons from the research on building AI agents"),("gap",30),("b","From a 10-stage study path\n(+ optional Stage 0)",Y),("gap",60),("s","Swipe",Y)],"Agentic AI","1/7","study notes + research addendum")
slide("carousel-02.png",[("big","#1"),("h2","Prompts are code."),("b","In an agent, the system prompt and the tool descriptions ARE the program."),("gap",10),("s","Define success criteria and a way to test them BEFORE you start prompt engineering.")],"Stage 4 · Prompt engineering","2/7","Anthropic's prompt engineering guide (via study notes, Stage 4)")
slide("carousel-03.png",[("big","#2"),("h2","Spend more time on tools than on prompts."),("b","Anthropic says that while building its SWE-bench agent, it spent more time optimizing tools than the overall prompt."),("gap",10),("s","Tools are what let an LLM act, not just produce text.")],"Stage 6 · Tool use","3/7","Anthropic (via study notes, Stage 6)")
slide("carousel-04.png",[("big","#3"),("h2","Simple wins."),("b","“Finding the simplest solution possible, and only increasing complexity when needed.”"),("gap",10),("s","Anthropic's guiding principle. Architecture decides reliability, cost and latency.")],"Stage 7 · Agent architectures","4/7","Anthropic (via study notes, Stage 7)")
slide("carousel-05.png",[("big","#4"),("h2","AI judges can miss it."),("b","LLM-based evaluation said GPT-4 and ChemCrow perform nearly equivalently. Expert humans found ChemCrow outperforms GPT-4 by a large margin."),("gap",10),("s","Don't rely blindly on LLM judges.")],"Stage 9 · Evaluation","5/7","Lilian Weng (2023); Bran et al. (2023), via study notes, Stage 9")
slide("carousel-06.png",[("big","#5"),("h2","Errors compound."),("b","Agents compound errors across steps and take real actions."),("gap",10),("s","Defenses: least privilege, sandboxing, human approval for irreversible actions.")],"Stage 9 · Safety","6/7","Anthropic; study notes, Stage 9")
slide("carousel-07.png",[("h","Don't wait for “mastery.”"),("gap",20),("b","Stages 4–10 overlap heavily in practice. Start building small agents early."),("gap",50),("s","Save this. Follow for the full roadmap.",Y)],"Takeaway","7/7","study notes (Overview)")
# Roadmap
im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im); d.rectangle([0,0,W,18],fill=Y)
d.text((M,62),"THE ROADMAP",font=f("Bold",30),fill=Y)
d.text((M,104),"Zero to AI agents",font=f("Black",84),fill=WH)
d.text((M,214),"~10–20 months part-time, Stages 1–10 back to back",font=f("Medium",31),fill=Y)
d.text((M,254),"(8–10 hrs/wk). Add Stage 0: ~11–23 months.",font=f("Medium",31),fill=Y)
st=[("0","Programming from zero (optional)","1–3 mo"),("1","Foundations: math, Python, ML","2–4 mo"),("2","Deep learning","1.5–3 mo"),("3","LLMs & transformers","1.5–2.5 mo"),("4","Prompt engineering","2–4 wk"),("5","RAG","3–5 wk"),("6","Tool use & function calling","2–4 wk"),("7","Agent architectures","1–2 mo"),("8","Frameworks & MCP","1–2 mo"),("9","Evaluation & safety","3–6 wk"),("10","Deploying real agents","1–2 mo")]
y=330
for n,t,e in st:
    opt=n=="0"
    if opt: d.rounded_rectangle([M,y,W-M,y+70],radius=16,outline=Y,width=3,fill=BG)
    else: d.rounded_rectangle([M,y,W-M,y+70],radius=16,fill="#1C1C24")
    d.ellipse([M+14,y+9,M+66,y+61],fill=Y)
    d.text((M+40,y+35),n,font=f("Black",28),fill=BG,anchor="mm")
    d.text((M+88,y+35),t,font=f("Bold",29 if opt else 31),fill=WH,anchor="lm")
    d.text((W-M-22,y+35),e,font=f("Medium",28),fill=G,anchor="rm"); y+=78
d.text((M,y+14),"Stage 0 only if you have never coded. Stages 4–10 overlap: build early.",font=f("Medium",27),fill=WH)
im.save("single-roadmap.png"); assert y+50<H-70
# Reel cover 1080x1920, key text inside central 1080x1350 safe area
slide("reel-cover.png",[("h","Without tools, an LLM just writes text."),("gap",30),("h2","Here's the 5-step loop that changes that.",Y)],"Reel · Tool calling","","OpenAI function-calling guide; study notes, Stage 6",h=1920)

for p in [f"carousel-0{i}.png" for i in range(1,8)]+["single-roadmap.png"]: watermark(p)
watermark("reel-cover.png",off=(1920-H)//2)
