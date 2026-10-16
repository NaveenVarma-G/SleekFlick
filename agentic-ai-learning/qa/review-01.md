# QA Review 01 — Agentic AI learning materials

**Reviewer:** Sage (QA) · **Date:** 16 Oct 2026 · **Scope:** 9 items (3 research files, 2 notes files, 3 decks, 1 Instagram draft set)
**Method:**
- Read every file in full. Decks were rendered to images (`office render`), extracted to text (markitdown), and run through `check-overlap` and `check-fonts`.
- A regex scan covered all slide text, tables and speaker notes for time estimates.
- A curl status check covered all 137 cited URLs.
- Key claims were spot-checked against the live sources with WebFetch and curl.

No reviewed file was edited.

**Severity scale:**
- **Critical:** wrong or harmful content that blocks release.
- **High:** a factual error, a contradiction a learner will hit, or a breach of a user requirement. Any High means FAIL.
- **Medium:** misleading, incomplete or weak teaching. Fix before the next release.
- **Low:** polish.

---

## 1. Summary

| # | Item | Owner | Verdict | Critical | High | Medium | Low |
|---|---|---|---|---|---|---|---|
| 1 | agentic-ai-learning-path.md | Lucy | **FAIL** | 0 | 1 | 1 | 3 |
| 2 | agentic-ai-research-addendum.md | Lucy | **PASS** | 0 | 0 | 2 | 3 |
| 3 | no-code-agentic-ai-course.md | Lucy | **FAIL** | 0 | 1 | 2 | 2 |
| 4 | agentic-ai-notes.md | Nova | **FAIL** | 0 | 1 | 3 | 2 |
| 5 | agentic-ai-notes-beginner.md | Nova | **PASS** | 0 | 0 | 2 | 3 |
| 6 | agentic-ai-deck.pptx | Pixel | **FAIL** | 0 | 2 | 3 | 3 |
| 7 | agentic-ai-deck-beginner.pptx | Pixel | **PASS** | 0 | 0 | 1 | 4 |
| 8 | no-code-agentic-ai-deck.pptx | Pixel | **PASS** | 0 | 0 | 1 | 1 |
| 9 | instagram/drafts-01/ | Echo | **FAIL** | 0 | 1 | 4 | 6 |
| | **Total** | | **4 PASS / 5 FAIL** | **0** | **6** | **19** | **27** |

**Top issues:**
1. **Time estimates are still in the main deck.** The slide 12 speaker notes contain "(1h42m)" and "(3h1m)". This breaks the user requirement (H). The beginner and no-code decks are clean.
2. **The "~3–5 months" fast track contradicts the plan's own stage table.** Stages 4–10 alone add up to about 5.3–10.4 months. The claim appears in the learning path (line 292), in the notes (line 861) and in Instagram Post 2 (image and caption) (H ×3).
3. **The no-code course says "6 modules and 17 lessons" but lists 20 lessons** (H).
4. **Huyen's production steps are numbered as six.** The notes and two decks show them as 1–6, but the book's table of contents numbers only Steps 1–5. Monitoring/Observability and User Feedback are separate, unnumbered sections (M ×4).
5. **The fast.ai prerequisite is quoted only in part.** "High-school math is enough" leaves out the site's actual prerequisite: "you know how to code (a year of experience is enough)". This misleads beginners, and the claim appears in 4 places (M).

**Links:**
- No broken links: no 404 or 410 among the 137 URLs.
- Nine apparent 404s were false positives from my own URL parser. All of them returned 200 when re-checked in full.
- See Appendix A for 403s (unverifiable by curl) and redirects.

**Verified correct (sample):**
- ReAct reports absolute gains of 34% (ALFWorld) and 10% (WebShop).
- Anthropic spent more time optimising tools than the prompt for its SWE-bench agent.
- SWE-bench has 2,294 problems.
- OpenAI's function-calling guide suggests keeping fewer than 20 functions and describes the 5-step flow.
- fast.ai has 9 lessons of about 90 minutes.
- The Coursera pacing figures are correct.
- Hugging Face course time per chapter: 6–8 h/week (LLM course) and 3–4 h/week (Agents course).
- Pydantic requires "Python 3.10+".
- The CS50P quotes, the LangGraph "very low-level" quote and the MCP "USB-C" quote match their sources, as does the MCP "one MCP client for each MCP server" description.
- The OWASP 2025 LLM01–LLM10 names are correct.
- The Weng details are correct: ChemCrow uses 13 tools and API-Bank has 53 tools and 264 dialogues.
- Claude Projects are "Up to 5" on the Free plan.
- Make AI Agents is "Available on all plans".
- Copilot Studio: "An Azure subscription is required to use agents".
- n8n offers a "free trial, no credit card required".
- Gumloop offers a 14-day free trial.
- Botpress has a Free plan.
- The OpenAI help page says personal accounts can't create GPTs.
- The DeepLearning.AI crewAI course page lists "Beginner 3h1m".

---

## 2. Findings by item

### 2.1 agentic-ai-learning-path.md — Lucy — FAIL

**H-1. The fast-track "~3–5 months" estimate contradicts the stage table**
- **Location:** line 292 ("Fast track for experienced software engineers (estimate)").
- **Evidence:** The fast track starts at Stage 4. Using the file's own per-stage estimates, Stages 4–10 add up to about 10–19 weeks (≈2.3–4.4 months) plus 3–6 months, so ≈5.3–10.4 months in total. That is before any time is spent skimming Stages 1–3.
  - No source supports "3–5 months".
  - The figure is copied into agentic-ai-notes.md (line 861) and Instagram Post 2.
  - Echo already flagged it as suspect (drafts.md line 75).
- **Fix:** Do one of the following:
  - recompute the estimate from the stage table (e.g. "~5–10 months, estimate") and show the arithmetic;
  - or state which stages are compressed and by how much.
  
  Then tell Nova and Echo so they update their copies.
- **Owner:** Lucy.

**M-1. The fast.ai prerequisite is quoted in part**
- **Location:** line 54 (Stage 2 resources table).
- **Evidence:** The file says "The site says high-school math is enough." course.fast.ai says: "The only prerequisite is that you know how to code (a year of experience is enough), preferably in Python, and that you have at least followed a high school math course." The coding prerequisite is left out.
- **Fix:** Quote the full prerequisite: about a year of coding, preferably Python, plus high-school math.
- **Owner:** Lucy.

**L-1. Huyen's Chapter 6 title is wrong in Stage 7**
- **Location:** line 182: `Ch. 6 "Agents"`.
- **Evidence:** The O'Reilly table of contents titles Chapter 6 "RAG and Agents". The addendum's Gap 12 says the same.
- **Fix:** Change it to `Ch. 6 "RAG and Agents" (Agents sections)`.
- **Owner:** Lucy.

**L-2. The Hugging Face LLM Course prerequisite is missing**
- **Location:** Stage 3 resources (HF LLM Course row).
- **Evidence:** The course page says it "requires a good knowledge of Python" and is best taken after an introductory deep-learning course.
- **Fix:** Add a short prerequisite note to the row.
- **Owner:** Lucy.

**L-3. Several cited URLs now redirect**
- **Location:** throughout the file.
- **Evidence:** See Appendix A. Examples:
  - docs.anthropic.com now goes to platform.claude.com;
  - platform.openai.com/docs now goes to developers.openai.com/api/docs;
  - deeplearning.ai/short-courses now goes to /courses.
- **Fix:** Update the links to their canonical URLs.
- **Owner:** Lucy.

### 2.2 agentic-ai-research-addendum.md — Lucy — PASS

**M-1. Three gaps are labelled "Resolved" but still contain unsourced parts**
- **Location:** the headings of Gap 7 (line 107), Gap 11 (line 137) and Gap 17 (line 201), plus the status table at line 10 ("Resolved | 20").
- **Evidence:** Each of these gaps has "Not sourced" sub-points, and section 26b lists them as still unsourced. This goes against the legend at line 4 ("Resolved: a source I checked answers the gap").
- **Fix:** Relabel the three gaps as "Partly resolved" and update the counts in the status table.
- **Owner:** Lucy.

**M-2. The OWASP summary cells for LLM07, LLM08 and LLM10 are empty**
- **Location:** OWASP table, lines 233–244.
- **Evidence:** The genai.owasp.org/llm-top-10/ list page (checked 16 Oct 2026) shows summaries for all three:
  - LLM07: "The system prompt leakage vulnerability in LLMs refers to the…";
  - LLM08: "Vectors an[d]…";
  - LLM10: "Unbounded Consumption refers to the process where a Large Language…".
- **Fix:** Fill in the cells from the list page or, better, from each risk's detail page.
- **Owner:** Lucy. The notes inherit this; see 2.4 M-2.

**L-1. Gap 7 contradicts the glossary**
- **Location:** Gap 7.
- **Evidence:** Gap 7 says temperature is not sourced, but the addendum's glossary defines Temperature using the Google ML Glossary.
- **Fix:** Mark temperature as sourced in Gap 7.
- **Owner:** Lucy.

**L-2. Gap 13 miscounts the tool_choice modes**
- **Location:** Gap 13 (line 155).
- **Evidence:** It says "four modes" but lists four plus `none`.
- **Fix:** Change it to "five values" or list exactly four.
- **Owner:** Lucy.

**L-3. One course duration could not be verified**
- **Location:** the DeepLearning.AI "AI Agents in LangGraph" duration (1h42m).
- **Evidence:** The fetch confirmed 9 lessons and 6 code examples, but not the 1h42m total. The crewAI 3h1m figure was confirmed.
- **Fix:** Re-check the LangGraph duration or mark it unverified. The decks must not show it either way; see 2.6.
- **Owner:** Lucy.

### 2.3 no-code-agentic-ai-course.md — Lucy — FAIL

**H-1. The lesson count is wrong**
- **Location:** line 18: "6 modules and 17 lessons".
- **Evidence:** The file lists 20 lessons: 1.1–1.3, 2.1–2.4, 3.1–3.3, 4.1–4.4, 5.1–5.3 and 6.1–6.3. Pixel's no-code deck notes for slide 3 flag the same mismatch.
- **Fix:** Change it to "6 modules and 20 lessons".
- **Owner:** Lucy.

**M-1. A required glossary term does not exist in the glossary**
- **Location:** line 12, the "Read at least these" list.
- **Evidence:** "tool use" is not among the 39 glossary terms in the addendum. I checked every term.
- **Fix:** Either add a sourced "tool use" entry to the glossary, or drop it from the list (or point to the Anthropic/OpenAI tool-use docs instead).
- **Owner:** Lucy.

**M-2. "Zapier Agents on the free plan" is still marked unverified, but it can now be verified**
- **Location:** line 76 and line 153.
- **Evidence:** On zapier.com/pricing (checked 16 Oct 2026), the Agents tab lists "Agents Free … Free Forever … Run automated behaviors up to 400 times per month … 400 activities per month."
- **Fix:** Mark it as verified, with the quote and the access date. Keep the "plans change" caveat but do not include prices.
- **Owner:** Lucy. Pixel then updates the no-code deck; see 2.8.

**L-1. The tools table points Claude at the wrong lesson**
- **Location:** line 133 (Claude row: "L1.2, L2.1, L2.2").
- **Evidence:** Lesson 2.1 does not mention Claude.
- **Fix:** Remove L2.1 from the row, or add Claude to Lesson 2.1.
- **Owner:** Lucy.

**L-2. The Copilot Studio pricing link redirects**
- **Location:** line 145.
- **Evidence:** The URL redirects to microsoft.com/en-us/copilot/pricing/copilot-studio. The content is verified: the page says "An Azure subscription is required to use agents" and offers a free trial.
- **Fix:** Update the link to the canonical URL.
- **Owner:** Lucy.

### 2.4 agentic-ai-notes.md — Nova — FAIL

**H-1. The notes repeat the unsupported "~3–5 months" fast track**
- **Location:** line 861 (also referenced at line 31).
- **Evidence:** The figure is copied from the learning path (2.1 H-1) and contradicts the stage estimates in these same notes.
- **Fix:** Replace it with Lucy's corrected figure and show the arithmetic.
- **Owner:** Nova.

**M-1. Huyen's production steps are numbered 1–6**
- **Location:** lines ~795–810 (§10.2), item 6 at line 806: "Add monitoring/observability and user feedback". The Stage 10 review questions inherit the error.
- **Evidence:** The *AI Engineering* Chapter 10 table of contents numbers Steps 1–5 only. "Monitoring and Observability" and "User Feedback" are separate, unnumbered sections.
- **Fix:** Keep Steps 1–5 as numbered. Present monitoring and feedback as separate follow-on topics, and adjust the review question.
- **Owner:** Nova.

**M-2. The OWASP gap note is wrong**
- **Location:** line 725 ("LLM07, LLM08 and LLM10 have none") and table rows 711–714.
- **Evidence:** The OWASP list page shows summaries for all three risks (see 2.2 M-2).
- **Fix:** Fill in the summaries and rewrite the gap note.
- **Owner:** Nova.

**M-3. The fast.ai prerequisite is quoted in part**
- **Location:** lines 217 and 231.
- **Evidence:** This is the same partial quote as 2.1 M-1: the coding prerequisite ("a year of experience is enough") is left out.
- **Fix:** Quote the full prerequisite.
- **Owner:** Nova.

**L-1. Huyen's Chapter 6 has two different titles**
- **Location:** lines 574 and 602 say Ch. 6 "Agents"; line 442 correctly says "RAG and Agents".
- **Evidence:** The O'Reilly table of contents.
- **Fix:** Use "RAG and Agents" everywhere.
- **Owner:** Nova.

**L-2. The review questions have no answer key**
- **Location:** Review Questions, line 956 onward.
- **Evidence:** No answers or pointers to sections are given. Course-standard materials normally include them.
- **Fix:** Add brief answers, or section references for each question.
- **Owner:** Nova.

### 2.5 agentic-ai-notes-beginner.md — Nova — PASS

**M-1. Huyen's production steps are numbered 1–6**
- **Location:** line 524: "6. Add monitoring and user feedback."
- **Evidence:** This is the same error as 2.4 M-1.
- **Fix:** Use Steps 1–5 plus a separate "then monitor and collect feedback" note.
- **Owner:** Nova.

**M-2. The fast.ai prerequisite is quoted in part, in a "Beginner-friendly resources" list**
- **Location:** line 169.
- **Evidence:** The notes say "The site says high-school math is enough." The site's only prerequisite is about a year of coding, preferably Python, plus high-school math. For a non-coder this matters most.
- **Fix:** State the coding prerequisite and tell beginners to finish Stage 1 first.
- **Owner:** Nova.

**L-1. The ReAct gains could be misread as relative**
- **Location:** line 387: "success-rate gains of 34% … and 10%".
- **Evidence:** The paper reports absolute gains of 34% and 10%. Without "absolute", readers may take them as relative.
- **Fix:** Write "absolute gains of 34 and 10 percentage points".
- **Owner:** Nova.

**L-2. Two formatting glitches**
- **Location:** line 312 and line 199.
- **Evidence:**
  - Line 312: "**Time:** about 2–4 weeks (estimate)" is stuck to the end of the API-key bullet.
  - Line 199: "**Adjusting a model cheaply**" has no blank line before it, so it renders as part of the previous list.
- **Fix:** Put the Time line on its own line, and add a blank line before line 199.
- **Owner:** Nova.

**L-3. The example drops a metric**
- **Location:** line 126.
- **Evidence:** The example reports "precision and recall". The main notes (line 157) and the source project also include F1.
- **Fix:** Add F1 with a one-line plain definition, or say it is omitted on purpose.
- **Owner:** Nova.

### 2.6 agentic-ai-deck.pptx — Pixel — FAIL (20 slides)

**USER REQUIREMENT: time estimates.** I scanned all slide text, tables and speaker notes. There are no time estimates on the visible slides. The two below are in the speaker notes.

**H-1. Time estimate in the slide 12 notes (LangGraph course)**
- **Location:** slide 12, speaker notes.
- **Evidence:** `Short courses: DeepLearning.AI "AI Agents in LangGraph" (1h42m) …`
- **Fix:** Delete "(1h42m)".
- **Owner:** Pixel.

**H-2. Time estimate in the slide 12 notes (crewAI course)**
- **Location:** slide 12, speaker notes.
- **Evidence:** `… and "Multi AI Agent Systems with crewAI" (3h1m).`
- **Fix:** Delete "(3h1m)".
- **Owner:** Pixel.

**M-1. The "one question per phase" slide does not match its own content**
- **Location:** slide 19 (visible slide and notes: "Six questions… one per phase").
- **Evidence:** The slide shows six questions for five phases, and both Q3 and Q4 are labelled "Act".
- **Fix:** Either cut to five questions, one per phase, or retitle the slide ("six questions across five phases") and relabel Q3/Q4.
- **Owner:** Pixel.

**M-2. Huyen's production steps include a "Step 6"**
- **Location:** slide 16: "Step 6 Monitoring and user feedback".
- **Evidence:** The book numbers Steps 1–5 only (see 2.4 M-1).
- **Fix:** Show Steps 1–5 and add a separate unnumbered "Then: monitor and collect feedback" element.
- **Owner:** Pixel.

**M-3. The fast.ai prerequisite is quoted in part**
- **Location:** slide 5 ("High-school math is enough.") and its notes.
- **Evidence:** The coding prerequisite is left out (see 2.1 M-1).
- **Fix:** Change the text to "Needs ~1 year of coding (ideally Python) + high-school math."
- **Owner:** Pixel.

**L-1. The ReAct numbers look relative and the chart is unclear**
- **Location:** slide 11 ("+34%" / "+10%").
- **Evidence:** These are absolute gains. It is also unclear which ring arc belongs to which label.
- **Fix:** Label the numbers "+34 pts" and "+10 pts", and put each label next to its arc.
- **Owner:** Pixel.

**L-2. The stage count in the title does not match the graphic**
- **Location:** slide 2: title "10 cumulative stages".
- **Evidence:** The graphic shows 11 nodes (Stage 0–10).
- **Fix:** Retitle it, e.g. "10 stages + optional Stage 0", or style Stage 0 visibly as optional.
- **Owner:** Pixel.

**L-3. Overlapping text boxes reported by the checker**
- **Location:** slides 3, 5, 8, 9, 10, 11, 16, 18 and 19.
- **Evidence:** `check-overlap` reported 28 findings, mostly 7–30% overlaps between paired number and label boxes. None is visible in the render.
- **Fix:** Tighten the box bounds so future text edits don't collide.
- **Owner:** Pixel.

### 2.7 agentic-ai-deck-beginner.pptx — Pixel — PASS (23 slides)

- **Time estimates:** none found in slide text, tables or notes. ✔
- **Counts:** 99 glossary terms, 22 review questions and 109 sources, all matching the beginner notes. ✔

**M-1. Huyen's production steps are numbered 1–6**
- **Location:** slide 17.
- **Evidence:** This is the same error as 2.4 M-1.
- **Fix:** Show Steps 1–5 plus an unnumbered "then monitor and get feedback" element.
- **Owner:** Pixel.

**L-1. The ReAct gain could be misread as relative**
- **Location:** slide 12 notes ("34%").
- **Evidence:** The paper reports an absolute gain.
- **Fix:** Write "34 percentage points (absolute)".
- **Owner:** Pixel.

**L-2. Table alignment is mixed**
- **Location:** slide 20 table.
- **Evidence:** The header row is left-aligned while the body cells are centred.
- **Fix:** Use one alignment throughout (left is recommended for text).
- **Owner:** Pixel.

**L-3. The closing slide gives the wrong starting point**
- **Location:** slide 23 ("Begin at Stage 0").
- **Evidence:** This contradicts slide 3: "start at Stage 1 if you code".
- **Fix:** Change it to "Begin at Stage 0 if you've never coded; otherwise Stage 1."
- **Owner:** Pixel.

**L-4. Overlapping shapes reported by the checker**
- **Location:** several slides; slide 23 is the largest case.
- **Evidence:** `check-overlap` reported 13 findings, including a 69% pill/number overlap on slide 23. All render cleanly.
- **Fix:** Tidy the box geometry.
- **Owner:** Pixel.

### 2.8 no-code-agentic-ai-deck.pptx — Pixel — PASS (19 slides)

- **Time estimates:** none. ✔
- Slides 1 and 3 correctly avoid the "17 lessons" error, and the slide 3 notes flag the course's 17-vs-20 mismatch. ✔
- Slide 16's "Trial or credits" grouping matches the verified n8n, Lindy, Gumloop and Copilot Studio pages. ✔

**M-1. Zapier Agents is still shown as unverified**
- **Location:** slide 9 (right panel, item 01: "Zapier Agents on the free plan: unverified") and slide 16 (footer: "Also unverified…").
- **Evidence:** Zapier's pricing page now lists a free Agents plan with 400 activities per month (see 2.3 M-2).
- **Fix:** After Lucy updates the course, change both slides to "Free plan: 400 activities/month (checked 16 Oct 2026)". On slide 16, move Zapier Agents into a "Yes" row.
- **Owner:** Pixel.

**L-1. Overlapping shapes reported by the checker**
- **Location:** slide 19, among others.
- **Evidence:** `check-overlap` reported 14 findings, including a 69% pill overlap on slide 19. It renders fine.
- **Fix:** Tidy the box geometry.
- **Owner:** Pixel.

### 2.9 instagram/drafts-01/ — Echo — FAIL (not yet posted)

**Files reviewed:** drafts.md, carousel-01…07.png, single-roadmap.png and reel-cover.png. All images are 1080×1350. The hashtag counts (13/12/11) are correct.

**H-1. Post 2 publishes the unsupported "~3–5 months" fast track**
- **Location:** single-roadmap.png and the Post 2 caption (drafts.md line 41).
- **Evidence:** This is the same unsupported figure as 2.1 H-1. Echo's own flag at drafts.md line 75 calls it suspect, yet it is still on the image and in the caption. This post would be public.
- **Fix:** Remove the figure from the image and the caption, or replace it with Lucy's corrected figure. Do not post until this is resolved.
- **Owner:** Echo.

**M-1. The roadmap leaves out Stage 0**
- **Location:** single-roadmap.png.
- **Evidence:** The header says "Zero to AI agents", but the stage list starts at Stage 1. The research has an on-ramp Stage 0 for non-coders, which the caption's "~11–23 with Stage 0" figure even mentions.
- **Fix:** Add a "Stage 0 (if you've never coded)" row.
- **Owner:** Echo.

**M-2. The carousel headline overstates the source**
- **Location:** carousel slide 3, headline "Tools beat prompts".
- **Evidence:** Anthropic only says it spent more time optimising tools than the overall prompt for its SWE-bench agent. It does not claim that tools beat prompts.
- **Fix:** Use a headline such as "Spend more time on tools than on prompts" and attribute it to Anthropic.
- **Owner:** Echo.

**M-3. Most carousel slides leave half the frame empty**
- **Location:** carousel-02…07.
- **Evidence:** The lower roughly 40–50% of most slides is empty.
- **Fix:** Enlarge the type, centre the content block vertically, or add a supporting visual.
- **Owner:** Echo.

**M-4. The reel cover has the wrong aspect ratio**
- **Location:** reel-cover.png.
- **Evidence:** It is 1080×1350 (4:5). Reels are vertical 9:16.
- **Fix:** Export at 1080×1920 and keep the key text inside the central 4:5 safe area for the grid crop.
- **Owner:** Echo.

**L-1. The highlight has no legend**
- **Location:** single-roadmap.png.
- **Evidence:** Stages 4–10 are highlighted yellow without any explanation.
- **Fix:** Add a legend such as "fast-track stages", or remove the highlight.
- **Owner:** Echo.

**L-2. The subtitle crowds the first row**
- **Location:** single-roadmap.png.
- **Evidence:** The subtitle sits very close to the Stage 1 row.
- **Fix:** Add vertical space below the subtitle.
- **Owner:** Echo.

**L-3. The carousel hook is clickbait**
- **Location:** carousel-01, "5 things nobody tells you".
- **Evidence:** The wording is clickbait. Everything in it comes from public docs.
- **Fix:** Use a factual hook, e.g. "5 lessons from Anthropic & OpenAI's agent guides".
- **Owner:** Echo.

**L-4. "10-stage study path" ignores Stage 0**
- **Location:** carousel text "10-stage study path".
- **Evidence:** It leaves out the optional Stage 0.
- **Fix:** Write "10 stages (+ optional Stage 0)".
- **Owner:** Echo.

**L-5. The reel script is longer than planned**
- **Location:** drafts.md, reel plan.
- **Evidence:** The plan says "~25 s" but the script timings run 0–26 s.
- **Fix:** Trim 1 s or update the stated length.
- **Owner:** Echo.

**L-6. The source footer is vague**
- **Location:** all images.
- **Evidence:** The footer reads "study notes — learning AI to agentic AI", with no link and no named primary sources.
- **Fix:** Name the primary sources (e.g. Anthropic, OpenAI, ReAct paper) in the caption, and link to the notes if they are public.
- **Owner:** Echo.

---

## Appendix A — Link check (137 unique URLs, curl, 16 Oct 2026)

- **200 OK:** 123 URLs directly, plus 9 Wikipedia URLs that were false "404s" caused by my parser cutting the URL at "(". All 9 returned 200 when re-checked in full.
- **404/410 (broken):** none.
- **403 to curl (bot-blocked):**
  - Verified separately with WebFetch: help.openai.com (GPTs article), make.com/en/ai-agents and the oreilly.com *AI Engineering* page.
  - Still **unverifiable**: openai.com/chatgpt/pricing and make.com/en/pricing. Claims that rely only on these two pages were not spot-checked.
- **Redirects:** update these to canonical URLs (Low; owners: Lucy for research, Nova for notes, Pixel for deck source slides).

| Cited | Now |
|---|---|
| docs.anthropic.com/… | platform.claude.com/… |
| platform.openai.com/docs/… | developers.openai.com/api/docs/… |
| deeplearning.ai/short-courses/… | deeplearning.ai/courses/… |
| docs.n8n.io/advanced-ai/… | docs.n8n.io/build/integrate-ai/… |
| docs.n8n.io/hosting/… | docs.n8n.io/deploy/host-n8n/… |
| docs.pydantic.dev/… | pydantic.dev/docs/… |
| docs.voiceflow.com | voiceflow.com/docs |
| Copilot Studio pricing (microsoft-365-copilot path) | microsoft.com/en-us/copilot/pricing/copilot-studio |
| 3blue1brown.com/topics/neural-networks | 3blue1brown.com/?topic=neural-networks |
| modelcontextprotocol.io/… | versioned docs paths |

## Appendix B — Not spot-checked

- Zapier, Gemini and Relevance AI per-feature free-tier details, beyond what is quoted above.
- The ChatGPT pricing page and the Make pricing page (both 403).
- The 1h42m duration of the LangGraph course. This does not matter for the decks: the requirement is to remove it from the decks.
