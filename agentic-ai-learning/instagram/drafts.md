# Instagram Drafts 01: Learning AI to Agentic AI (rev. 3, after QA review-01)
Status: DRAFT. Not published anywhere. Sources: /workspace/agentic-ai-notes.md (updated) and /workspace/agentic-ai-research-addendum.md.
Images: carousel 1080x1350 (4:5); roadmap 1080x1350; Reel cover 1080x1920 (9:16) with the key text inside the central 1080x1350 safe area.

## Post 1: Carousel (7 slides): carousel-01.png … carousel-07.png
**Hook (slide 1):** 5 lessons from the research on building AI agents. From a 10-stage study path (+ optional Stage 0).

Slides and sources:
1. Hook. 10 stages + optional Stage 0: notes, Overview
2. Prompts are code; define success criteria and tests before prompt engineering: notes, Stage 4.2 (Anthropic's prompt engineering guide)
3. Spend more time on tools than on prompts. Anthropic says it spent more time optimizing tools than the overall prompt while building its SWE-bench agent. Tools let an LLM act: notes, Stage 6.2
4. Simple wins. "Finding the simplest solution possible, and only increasing complexity when needed." Architecture decides reliability, cost, latency: notes, Stage 7.2
5. AI judges can miss it. GPT-4 vs ChemCrow quote: notes, Stage 9.2; addendum, Gap 21 (Weng 2023; Bran et al., arXiv 2304.05376)
6. Errors compound; least privilege, sandboxing, human approval: notes, Stage 9.1 / 9.2 (Anthropic)
7. Stages 4–10 overlap; start building small agents early: notes, Overview

**Caption:**
Everyone obsesses over the perfect prompt. The people building real agents are focused on something else. 👀

1️⃣ Prompts are code. Your system prompt + tool descriptions ARE the program.
2️⃣ Anthropic says it spent more time optimizing tools than the overall prompt while building its SWE-bench agent.
3️⃣ Start simple. Add complexity only when needed.
4️⃣ LLM judges can miss what human experts catch.
5️⃣ Agents compound errors and take real actions, so sandbox them and gate irreversible moves behind a human.


Which one surprised you most? 👇 Save this for your build.

**Hashtags (13):** #AgenticAI #AIAgents #LLM #PromptEngineering #MachineLearning #ArtificialIntelligence #LearnAI #AIEngineering #GenerativeAI #AISafety #BuildInPublic #TechCareers #Python

## Post 2: Single image: single-roadmap.png
**Hook (on image):** Zero to AI agents. ~10–20 months part-time with Stages 1–10 back to back (8–10 hrs/wk). Add Stage 0: ~11–23 months.


**Caption:**
How long does it take to go from zero to building AI agents? 🤔

Do Stages 1–10 one after another and you're looking at about 10–20 months part-time (at 8–10 hrs/week). Never written code? Add a Stage 0 (about 1–3 months) and it's about 11–23 months. These are estimates, not a promise.

The path: (0) programming from zero → math & Python → deep learning → LLMs → prompting → RAG → tools → agent architectures → frameworks & MCP → evals & safety → deployment.

Not sure if you need Stage 0? Skip it if you can already write a short program that loops over a list, uses if/else, defines functions and reads a file.

Plot twist: stages 4–10 overlap heavily, so start building small agents early.


Which stage are you on? Drop the number 👇

**Hashtags (12):** #AIRoadmap #LearnAI #AgenticAI #AIAgents #MachineLearning #DeepLearning #LLM #RAG #Python #AIEngineering #StudyWithMe #TechSkills

## Post 3: Reel (25 s): cover reel-cover.png (1080x1920)
**Hook (0–3 s, on cover):** "Without tools, an LLM just writes text. Here's the 5-step loop that changes that."

| Time | On-screen text | Voiceover | Source |
|---|---|---|---|
| 0–3s | Without tools, an LLM just writes text. | "Your AI can talk. But can it act?" | notes, Stage 6.2 |
| 3–6s | Tools = how an LLM ACTS | "Tools are what let an LLM act, not just produce text." | notes, Stage 6.2 |
| 6–13s | 1 Request → 2 Tool call → 3 Execute → 4 Return output → 5 Final answer | "A request comes in, the model asks for a tool call, your app executes it, returns the output, and the model writes the final answer." | notes, Stage 6.1 / 6.2 |
| 13–17s | Not one request. A multi-step conversation. | "OpenAI's guide calls it a multi-step conversation between your app and the model." | notes, Stage 6.1 |
| 17–22s | Pro tip: < 20 functions at once | "That guide's advice: aim for fewer than 20 functions available at once." | notes, Stage 6.3 |
| 22–25s | Follow for Part 2: ReAct 🧠 | "Next: how agents think, act and observe. Follow." | notes, Stage 7.1 |

**Caption:**
Your AI can talk. But can it *do* anything? 🛠️

Tool calling is the 5-step loop that turns an LLM from a text generator into something that acts:
request → tool call → execute → return output → final answer.

Pro tip from OpenAI's function-calling guide: aim for fewer than 20 functions available at once.

Follow for Part 2: ReAct, where agents think → act → observe. 🧠


**Hashtags (11):** #AIAgents #AgenticAI #FunctionCalling #ToolCalling #LLM #AIEngineering #LearnAI #GenerativeAI #Python #CodingReels #TechReels

## Facts flagged as uncertain / handle with care
- Total time: these are estimates. The notes and addendum deliberately give no shorter total for the overlap, and neither do the drafts.
- Fast track (~3–5 months): removed from all drafts. QA H-1 found it unsupported. The notes were fixed in review 02 and no longer contain it.
- "Fewer than 20 functions" is OpenAI's best-practice advice, not a hard limit. QA verified it.
- The Reel's 5 steps follow the research's loop (notes 6.1). QA confirmed OpenAI's guide "describes the 5-step flow" but the notes don't list OpenAI's own wording.
- Source footers and caption 'Sources:' lines were removed at the user's request. Per-claim sources are kept in this file as internal documentation only.
