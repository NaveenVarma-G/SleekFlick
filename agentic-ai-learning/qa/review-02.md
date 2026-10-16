# QA Review 02: re-review of the items that failed review 01

**Reviewer:** Sage (QA)
**Date:** 16 Oct 2026, 11:20–11:24 EDT
**Baseline:** /workspace/qa/review-01.md (written 11:11:45 EDT)

**Scope.** I re-reviewed the 5 items that failed review 01 (the learning path, the no-code course, the main notes, the main deck and instagram/drafts-01). I also checked slides 9 and 16 of the no-code deck for the Zapier change.

**Out of scope.** The 4 items that passed review 01 were not re-reviewed, and links were not rechecked. I did one content spot-check, of the new OWASP quotes. I did not edit any reviewed file.

**Method.**
- Compared file modification times with review-01.
- Grepped the review-01 locations.
- Re-rendered both decks and re-ran `check-overlap` and `check-fonts`.
- Re-scanned every slide's text, tables and speaker notes for time estimates.
- Viewed every Instagram image and checked its pixel size.

## 1. Summary

| Item | Owner | Modified (EDT) | Review-01 issues (H/M/L) | Fixed | Open | New | Verdict |
|---|---|---|---|---|---|---|---|
| agentic-ai-learning-path.md | Lucy | 11:15:07 | 1/1/3 | 5 | 0 | 0 | **PASS** |
| no-code-agentic-ai-course.md | Lucy | 11:15:07 | 1/2/2 | 5 | 0 | 0 | **PASS** |
| agentic-ai-notes.md | Nova | 11:19:04 | 1/3/2 | 6 | 0 | 0 | **PASS** |
| agentic-ai-deck.pptx | Pixel | 11:20:29 | 2/3/3 | 8 | 0 | 0 | **PASS**¹ |
| instagram/drafts-01/ | Echo | 11:14:20 | 1/4/6 | 11 | 0 | 2 (Low) | **PASS** |
| no-code deck, slides 9 & 16 (Zapier) | Pixel | 11:20:29 | M-1 | Updated | 0 | 1 (Low) | **Updated (not pending)** |

¹ **Main deck timing.** When I first checked (11:20), the main deck still had a pre-review timestamp (10:43). It was then saved at 11:20:29, during this re-review.
- The saved file is byte-identical to Pixel's working copy (`/workspace/slides/qa-fix-9emcoX/main/agentic-ai-deck.pptx`).
- Pixel's NOTES.md says "last phase: finish".
- The file was unchanged from 11:20:29 to 11:23:31.

Every review-01 issue is resolved in that version, so it is not PENDING. If Pixel saves the file again, it needs one more quick check.

**Open issues.**
- Critical, High and Medium: none.
- Low: 3, all new. See 2.5 N-1, 2.5 N-2 and 2.6 N-1.

**Out-of-scope observation.** The research addendum, beginner notes and beginner deck were also modified after review 01. They passed review 01, and per instructions I did not re-review them.

---

## 2. Item details

### 2.1 agentic-ai-learning-path.md (Lucy): PASS

| Review-01 issue | Status | Evidence |
|---|---|---|
| H-1 Fast track "~3–5 months" contradicts the stage table | **Fixed** | The fast-track line (old line 292) has been removed. No "fast track" or "3–5 months" text remains; the only "3–5" left is "3–5 weeks" for Stage 5. The pacing table ends at "Total (estimate): ~10–20 months sequential; ~11–23 months with Stage 0", which matches the stage sums. |
| M-1 fast.ai prerequisite quoted in part | **Fixed** | Line 54 now gives the site's full prerequisite: "The only prerequisite is that you know how to code (a year of experience is enough), preferably in Python, and that you have at least followed a high school math course." This matches course.fast.ai. |
| L-1 Ch. 6 titled "Agents" | **Fixed** | Line 182: `Ch. 6 "RAG and Agents" (Agents sections)`. |
| L-2 HF LLM Course prerequisite missing | **Fixed** | Line 80 now says it "Requires a good knowledge of Python" and "Is better taken after an introductory deep learning course". |
| L-3 Redirected URLs | **Fixed** | No old-form URLs remain (0 matches for docs.anthropic.com, platform.openai.com/docs, deeplearning.ai/short-courses, docs.pydantic.dev, old n8n paths, docs.voiceflow.com, 3blue1brown /topics). For example, 3Blue1Brown is now `?topic=`. I did not recheck the links themselves. |

**New issues:** none. Line 254 lists Huyen's architecture without step numbers, so it is consistent with the corrected notes.

### 2.2 no-code-agentic-ai-course.md (Lucy): PASS

| Review-01 issue | Status | Evidence |
|---|---|---|
| H-1 "6 modules and 17 lessons" but 20 lessons listed | **Fixed** | Line 18 now reads "6 modules and 20 lessons". I counted 20 lesson headings (1.1–1.3, 2.1–2.4, 3.1–3.3, 4.1–4.4, 5.1–5.3, 6.1–6.3). |
| M-1 "tool use" not in the glossary | **Fixed** | The addendum glossary now has a "Tool use (function calling)" entry (addendum line 404; count "40 terms", line 431). Course line 12 says "40 sourced, plain-language terms". |
| M-2 Zapier Agents free plan marked unverified | **Fixed** | Line 76: "✅ Verified (16 Oct 2026)… 'Agents Free … Free Forever'". The tools-table Zapier row is updated, and flagged item 1 (line 153) is struck through as "now verified". This matches what I saw on zapier.com/pricing in review 01. |
| L-1 Claude row cites L2.1 | **Fixed** | Line 133: "L1.2, L2.2". |
| L-2 Copilot Studio pricing URL redirects | **Fixed** | Lines 145 and 194 now use microsoft.com/en-us/copilot/pricing/copilot-studio. |

**New issues:** none. The fix moved the "capped number of activities" wording into the course but quotes no prices, which keeps the course's "no prices" rule.

### 2.3 agentic-ai-notes.md (Nova): PASS

| Review-01 issue | Status | Evidence |
|---|---|---|
| H-1 "~3–5 months" fast track | **Fixed** | Removed from both old line 31 and old line 861. Line 28 and line 862 give "about 10–20 months… or about 11–23 months including Stage 0". They also say that overlap "may shorten this, but the research has no source for how much", which is honest about the gap. |
| M-1 Huyen steps numbered 1–6 | **Fixed** | §10.2 (lines ~800–808) lists "five numbered steps" (1 Enhance context to 5 Add agent patterns). It then adds "Then, as follow-on topics rather than a numbered step: monitoring/observability, and user feedback." Stage 10 review question 1 now asks for "the five numbered steps… and… the two follow-on topics". |
| M-2 OWASP LLM07/08/10 summaries blank; gap note wrong | **Fixed** | Rows 712, 713 and 715 now have full quoted descriptions. I spot-checked all three against the OWASP detail pages, and each quoted sentence appears verbatim. The gap note (line ~725) now correctly says only LLM02–06 and LLM09 remain truncated. |
| M-3 fast.ai prerequisite quoted in part | **Fixed** | Lines 216 and 232 give the full quote. Line 219 adds the beginner takeaway: do Stage 0 or 1 first. Review question 2.2 tests it. |
| L-1 Ch. 6 titled inconsistently | **Fixed** | Lines 575 and 603 now read "RAG and Agents" (Agents sections). |
| L-2 No answer key | **Fixed** | Line 960 adds an answer-key convention, and all 62 review questions end with a "(See §x.y.)" pointer. Every cited section exists as a heading in the notes. |

**New issues:** none.

### 2.4 agentic-ai-deck.pptx (Pixel): PASS (see footnote 1)

**USER REQUIREMENT: time estimates.** I re-scanned all 20 slides (text, tables, speaker notes) for hours, minutes, h/m formats, days, weeks and months. **No matches.**

| Review-01 issue | Status | Evidence |
|---|---|---|
| H-1 Slide 12 notes: "(1h42m)" | **Fixed** | The slide 12 notes now read `Short courses: DeepLearning.AI "AI Agents in LangGraph" and "Multi AI Agent Systems with crewAI".` with no durations. |
| H-2 Slide 12 notes: "(3h1m)" | **Fixed** | Same line as above. |
| M-1 Slide 19: "one per phase" vs 6 questions; Q3/Q4 both "Act" | **Fixed** | The title is now "Review questions: six across five phases". The labels are "Q3 · Act (tools)" and "Q4 · Act (agents)", and the notes explain that "Act has two". |
| M-2 Slide 16: Huyen "Step 6" | **Fixed** | The render shows Steps 1–5 as a staircase plus a dashed "Then: Monitor and collect feedback · Not a numbered step" box. The notes explain why. |
| M-3 Slide 5: fast.ai prerequisite in part | **Fixed** | "Prerequisite: you know how to code, ideally in Python, plus high-school math." The notes quote the site directly. |
| L-1 Slide 11: "+34%/+10%" and arc labels | **Fixed** | Now "+34 pts" (ALFWorld) and "+10 pts" (WebShop), each label at the end of its own arc. A caption says "Absolute gains in success rate, in percentage points, over imitation/RL baselines". |
| L-2 Slide 2: "10 cumulative stages" with 11 nodes | **Fixed** | The title is "The roadmap: 10 stages + optional Stage 0". The Stage 0 node is dashed, and a footer says "Stage 0 is only for people who have never programmed." |
| L-3 check-overlap: 28 findings | **Fixed** | `check-overlap`: "no findings". `check-fonts`: Manrope only for visible text. The contact sheet shows no visual regressions. |

**New issues:** none.

### 2.5 instagram/drafts-01 (Echo): PASS (still DRAFT, nothing posted)

**Image sizes.** carousel-01…07 and single-roadmap.png are 1080×1350. reel-cover.png is 1080×1920.

| Review-01 issue | Status | Evidence |
|---|---|---|
| H-1 Post 2 repeats "~3–5 months" | **Fixed** | The roadmap image and caption now show "~10–20 months part-time, Stages 1–10 back to back (8–10 hrs/wk). Add Stage 0: ~11–23 months." No 3–5-month figure remains. drafts.md line 82 records the removal. |
| M-1 Roadmap leaves out Stage 0 | **Fixed** | single-roadmap.png has a "0 Programming from zero (if you've never coded) 1–3 mo" row, and the footer says "Stage 0 is optional." |
| M-2 "Tools beat prompts" overstates the source | **Fixed** | The carousel-03 headline is now "Spend more time on tools than on prompts.", with the attributed body "Anthropic says that while building its SWE-bench agent, it spent more time optimizing tools than the overall prompt." |
| M-3 Empty lower half on carousel slides | **Fixed** | The content blocks are now spread vertically on slides 2–7. Some bottom space remains on 4, 6 and 7, but the frame is no longer half empty. |
| M-4 Reel cover is 4:5 | **Fixed** | reel-cover.png is 1080×1920 (9:16). The key text sits in the central band. |
| L-1 Yellow highlight with no legend | **Fixed** | The Stage 4–10 highlight is gone. The only accent left is Stage 0's outline, which the row label and footer explain. |
| L-2 Subtitle crowds the Stage 1 row | **Fixed** | There is clear space between the subtitle and the first row. |
| L-3 Clickbait hook | **Fixed** | The hook is now "5 lessons from the research on building AI agents". |
| L-4 "10-stage study path" ignores Stage 0 | **Fixed** | Now "From a 10-stage study path (+ optional Stage 0)". |
| L-5 Reel planned as ~25 s but scripted 0–26 s | **Fixed** | The heading says "Reel (25 s)" and the script runs 0–25 s. |
| L-6 Vague source footer | **Fixed** | Footers and captions now name the primary sources (Anthropic, OpenAI function-calling guide, Lilian Weng 2023, Bran et al. 2023). drafts.md line 85 explains why there is no link: the notes aren't public. |

**New issues**

**N-1 (Low): stale status note.**
- **Location:** drafts.md line 82.
- **Evidence:** It says "the notes still contain it (line 31/861, Nova's fix pending)". The notes were fixed at 11:19 and no longer contain the figure (see 2.3).
- **Fix:** Change it to "notes fixed in review 02".
- **Owner:** Echo.

**N-2 (Low): cramped Stage 0 row.**
- **Location:** single-roadmap.png, Stage 0 row.
- **Evidence:** The label "Programming from zero (if you've never coded)" runs right up to the "1–3 mo" duration, with almost no gap. Every other row has clear space.
- **Fix:** Shorten the label (e.g. "Programming from zero (optional)") or reduce its size slightly.
- **Owner:** Echo.

### 2.6 no-code-agentic-ai-deck.pptx, slides 9 and 16 (Pixel): UPDATED

The review-01 item (2.8 M-1, Zapier Agents shown as unverified) is **fixed**. The file was modified at 11:20:29 and re-rendered.
- **Slide 9**, right panel, item 01: "Zapier Agents: free plan, 400 activities a month". The notes cite the Zapier pricing Agents tab, "checked 16 Oct 2026".
- **Slide 16:** the table's "Yes" row now reads "Zapier (incl. Agents), Make, Botpress". The old "Also unverified…" footer is replaced by "Zapier Agents: free plan, 400 activities a month (checked 16 Oct 2026)". This matches the zapier.com/pricing text I recorded in review 01 ("400 activities per month").
- **Whole deck:** `check-overlap` reports "no findings". A re-scan for time estimates found none.

**New issue**

**N-1 (Low): stale lesson mapping in the slide 16 notes.**
- **Location:** slide 16 speaker notes.
- **Evidence:** The notes say "Lessons per tool: Claude L1.2, L2.1, L2.2". The course now lists Claude for L1.2 and L2.2 only (course line 133, fixed in 2.2 L-1).
- **Fix:** Drop L2.1 from the notes.
- **Owner:** Pixel.

---

## 3. Status of review-01 issues across these items

| | Critical | High | Medium | Low |
|---|---|---|---|---|
| Review-01 issues in re-reviewed items | 0 | 6 | 14 | 16 |
| Fixed | 0 | 6 | 14 | 16 |
| Still open | 0 | 0 | 0 | 0 |
| New in review 02 | 0 | 0 | 0 | 3 |

The Medium count includes the no-code deck's Zapier item.

---

## Recheck of edited passed items

**Checked:** 16 Oct 2026, 11:25–11:30 EDT.

**Standards:** the same as review 01. Links were not rechecked. Content spot-checks used the live source pages. No files were edited.

| Item | Owner | Modified (EDT) | Review-01 issues (M/L) | Fixed | Open | New | Verdict |
|---|---|---|---|---|---|---|---|
| agentic-ai-research-addendum.md | Lucy | 11:16:21 | 2/3 | 5 | 0 | 2 (Low) | **PASS** |
| agentic-ai-notes-beginner.md | Nova | 11:19:04 | 2/3 | 5 | 0 | 1 (Low) | **PASS** |
| agentic-ai-deck-beginner.pptx | Pixel | 11:20:29 | 1/4 | 5 | 0 | 1 (Low) | **PASS** |

### R.1 agentic-ai-research-addendum.md (Lucy): PASS

| Review-01 issue | Status | Evidence |
|---|---|---|
| M-1 Gaps 7, 11 and 17 labelled "Resolved" despite unsourced parts | **Fixed** | All three headings now read "Partly resolved" (lines 107, 138, 203). The legend defines "Partly resolved", and the status table reads Resolved 17 / Partly resolved 8 / Unresolved 1. I re-tallied all 26 gap headings and the counts match the table. Section 26b lists the remaining unsourced parts for Gaps 7, 11 and 17. |
| M-2 OWASP LLM07/08/10 summaries empty | **Fixed** | The three rows now carry quotes with links to the detail pages. Spot-check: the LLM07, LLM08 and LLM10 sentences each appear verbatim on their OWASP detail pages. |
| L-1 Gap 7 says temperature is not sourced | **Fixed** | Gap 7 now reads "Temperature: sourced… Google ML Glossary". Section 26b repeats this. |
| L-2 Gap 13 says "four modes" but lists five | **Fixed** | It now reads "five settings": Auto, Required, Forced, `allowed_tools` and `none`. |
| L-3 LangGraph 1h42m unverified | **Fixed** | Line 217 now says "re-checked on the course page, 16 Oct 2026". My check of the page shows "Intermediate 1h42m · 9 Video Lessons · 6 Code Examples". |

**New issues**

**N-1 (Low): OWASP table header is now partly wrong.**
- **Location:** OWASP table header, "OWASP's own summary (truncated on the list page)".
- **Evidence:** Rows LLM07, LLM08 and LLM10 are now full quotes from the detail pages, so they are no longer truncated list-page text.
- **Fix:** Change the header to e.g. "OWASP's own summary (list page, truncated; LLM07/08/10 from detail pages)".
- **Owner:** Lucy.

**N-2 (Low): cross-file inconsistency on `tool_choice`.**
- **Location:** the addendum's Gap 13 versus agentic-ai-notes.md, lines 466 and 950 and review question 6.6 (line 1013).
- **Evidence:** The addendum now lists five `tool_choice` settings. The main notes still say "four modes" and leave out `none`.
- **Fix:** Align the main notes to the five settings, including the review question.
- **Owner:** Nova (main notes). The addendum itself is correct.

### R.2 agentic-ai-notes-beginner.md (Nova): PASS

| Review-01 issue | Status | Evidence |
|---|---|---|
| M-1 Huyen steps numbered 1–6 | **Fixed** | Lines 533–540 now say "five numbered steps", list Steps 1–5, and then say "Then: monitor the agent and collect user feedback… follow-on topics rather than a step of their own." |
| M-2 fast.ai prerequisite quoted in part | **Fixed** | Line 171 now has the full quote: "The only prerequisite is that you know how to code (a year of experience is enough), preferably in Python…". |
| L-1 ReAct 34% without "absolute" | **Fixed** | Line 394 now says "**absolute** success-rate gains… 'Absolute' means 34 and 10 percentage points, not a relative increase." |
| L-2 Formatting glitches (old lines 312 and 199) | **Fixed** | "**Time:** about 2–4 weeks (estimate)." is now its own paragraph (line 319). A blank line now precedes "**Adjusting a model cheaply**" (line 204). |
| L-3 Line 126 drops F1 | **Fixed** | Line 126 now says the app "reports its precision, recall and F1". |

**New issue**

**N-1 (Low): F1 gap note is inaccurate.**
- **Location:** line 129.
- **Evidence:** The gap note says "The sources don't define the F1 score." But the notes' own Source 58 (Wikipedia, "Precision and recall") defines it: "A measure that combines precision and recall is the harmonic mean of precision and recall, the traditional F-measure or balanced F-score." As a result, F1 is used in the notes without a definition, even though a source for one is already cited.
- **Fix:** Replace the gap note with a one-line plain definition cited to Source 58, e.g. "F1: a single score that balances precision and recall (their harmonic mean)".
- **Owner:** Nova.

### R.3 agentic-ai-deck-beginner.pptx (Pixel): PASS

**Time estimates.** None anywhere.
- I scanned all 23 slides, including grouped shapes, tables and speaker notes, for hours, minutes, h/m formats, days, weeks, months and years.
- I also grepped the raw slide and notes XML.
- Both scans found **zero matches**.

**Checks.** `check-overlap` found no findings. `check-fonts` reports Manrope only, installed. The contact sheet shows no visual regressions.

| Review-01 issue | Status | Evidence |
|---|---|---|
| M-1 Slide 17: Huyen 6 numbered steps | **Fixed** | The table shows Steps 1–5. A final unnumbered row reads "Then: monitor and get user feedback", in italics. |
| L-1 Slide 12 notes: ReAct "34%" without "absolute" | **Fixed** | The notes now read "absolute success-rate gains of 34 percentage points… and 10 percentage points". |
| L-2 Slide 20: mixed table alignment | **Fixed** | The header and body are both left-aligned in the render. |
| L-3 Slide 23: "Begin at Stage 0" conflicts with slide 3 | **Fixed** | Slide 23 now reads "Begin at Stage 0 if you've never coded; otherwise Stage 1." The notes match. |
| L-4 check-overlap: 13 findings (69% pill overlap on slide 23) | **Fixed** | `check-overlap` reports no findings. The slide 23 pill and its "0" badge no longer collide. |

**New issue**

**N-1 (Low): slide 23 step list contradicts the new pill text.**
- **Location:** slide 23, step row.
- **Evidence:** The row reads "1 Learn Python (Stage 0) · 2 Build a tiny agent early · 3 Keep the design simple". Step 1 reads as if everyone should do Stage 0, which conflicts with the pill text directly above it ("otherwise Stage 1").
- **Fix:** Change step 1 to e.g. "Learn Python (Stage 0 if new to code)".
- **Owner:** Pixel.

---

## Final check

**Checked:** 16 Oct 2026, ~11:27 EDT. These are the three Low issues raised earlier in this review.

| # | Issue | File modified (EDT) | Result | Evidence |
|---|---|---|---|---|
| 1 | instagram/drafts-01, drafts.md line 82: stale "Nova's fix pending" (2.5 N-1) | 11:25:12 | **Fixed** | Line 82 now reads: "Fast track (~3–5 months): removed from all drafts. QA H-1 found it unsupported. The notes were fixed in review 02 and no longer contain it." The word "pending" no longer appears anywhere in drafts.md. |
| 2 | single-roadmap.png: Stage 0 label running into "1–3 mo" (2.5 N-2) | 11:25:17 | **Fixed** | Viewed the image (still 1080×1350). The label is shortened to "Programming from zero (optional)", with clear space before "1–3 mo". The footer now reads "Stage 0 only if you have never coded. Stages 4–10 overlap: build early." No new layout problems. |
| 3 | no-code-agentic-ai-deck.pptx slide 16 notes: Claude listed for L2.1 (2.6 N-1) | 11:25:07 | **Fixed** | The slide 16 notes now read "Lessons per tool: Claude L1.2, L2.2; …", which matches course line 133. The deck was saved again, so I re-ran the checks on it: `check-overlap` found no findings, there are no time estimates on any of the 19 slides, and slides 9 and 16 still show "Zapier Agents: free plan, 400 activities a month". |

**After the final check:**
- All 3 Low issues from section 2 of this review are closed.
- The only open issues are the 4 new Lows from the recheck above: addendum N-1 and N-2, beginner notes N-1, and beginner deck N-1.
- There are no open Critical, High or Medium issues in any item.
