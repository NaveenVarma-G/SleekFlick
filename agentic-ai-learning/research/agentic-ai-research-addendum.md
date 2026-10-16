# Research Addendum — "Learning AI from scratch to mastery in building agentic AI"

*This addendum responds to the 26 gaps Nova flagged in `/workspace/agentic-ai-notes.md`. Every source cited below was checked on 16 Oct 2026, using WebFetch or curl. Time figures marked **(estimate)** are my own estimates; figures from a provider are labelled as theirs. Each section gets one status:*
- **Resolved:** a source I checked answers the gap.
- **Partly resolved:** a source answers part of the gap, and the rest is listed under "Not sourced".
- **Unresolved:** I couldn't find a checked source.

| Status | Count |
|---|---|
| Resolved | 17 |
| Partly resolved | 8 (Gaps 3, 7, 11, 17, 23, 24, 25, 26) |
| Unresolved | 1 (Gap 22) |

**Fixes also applied to `/workspace/agentic-ai-learning-path.md`:**
- the corrected total (Gap 1);
- all 10 OWASP risks (Gap 20);
- the OpenAI Agents SDK labelled consistently in Stages 8 and 10 (Gap 26a).

---

## Gap 1 — The stage estimates don't add up to the stated total (notes line 33) — **Resolved**

Here is the arithmetic, taken from the original stage table:

| | Minimum | Maximum |
|---|---|---|
| Month-based stages (1, 2, 3, 7, 8, 10) | 2 + 1.5 + 1.5 + 1 + 1 + 1 = **8 mo** | 4 + 3 + 2.5 + 2 + 2 + 2 = **15.5 mo** |
| Week-based stages (4, 5, 6, 9) | 2 + 3 + 2 + 3 = **10 wk ≈ 2.3 mo** | 4 + 5 + 4 + 6 = **19 wk ≈ 4.4 mo** |
| **Done strictly one after another** | **≈ 10.3 mo** | **≈ 19.9 mo** |

**Corrected statement (estimate):** about **10–20 months** if you do the stages one after another at 8–10 hrs/week. Adding the new Stage 0 (Gap 2) makes it about **11–23 months**. Because Stages 4–10 overlap, you may finish sooner, but I have no source for how much sooner, so I don't state a shorter total.

---

## Gap 2 — No prerequisite check or on-ramp for someone who has never programmed (lines 35 and 79) — **Resolved**

### New Stage 0 — Programming from zero

**Who it's for:** anyone who has never written code.

**Prerequisite check (editorial):** skip Stage 0 if you can already write a short program that loops over a list, uses `if`/`else`, defines functions, and reads a file. Otherwise, start here.

**Resources (all checked):**

| Resource | Type | What the source says |
|---|---|---|
| [Python wiki – "Python for New Programmers" (BeginnersGuide/NonProgrammers)](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers) | Free | "If you've never programmed before, the tutorials on this page are recommended for you; they don't assume that you have previous experience." The page notes the wiki is being archived. Python.org points to this page in contrast to its Programmers page; the official Tutorial is for people who already program. |
| [CS50's Introduction to Programming with Python (Harvard, David J. Malan)](https://cs50.harvard.edu/python/) | Free (OpenCourseWare); paid verified certificate offered | "Designed for students with or without prior programming experience." Covers functions, variables, conditionals, loops, exceptions, debugging, unit tests, libraries, regular expressions, classes and file I/O. "No software required except for a web browser." |
| [Automate the Boring Stuff with Python (Al Sweigart)](https://automatetheboringstuff.com/) | Free to read under a Creative Commons license; print copy paid | The Python wiki above describes it as "Practical Programming for Total Beginners." |
| [Kaggle Learn – Python micro-course](https://www.kaggle.com/learn) | Free | Already in the original path. Good as a short bridge into pandas and ML. |

**Recommended order within Stage 0 (editorial):**
1. CS50P, for structured lessons and problem sets.
2. Automate the Boring Stuff, for practical projects.
3. The Kaggle Python and pandas courses.
4. Then the official Python Tutorial (Stage 1) as a reference.

**Projects (editorial):**
- A file-renaming script.
- A CSV summary tool.
- A tiny text-adventure game using functions and classes.

**Time (estimate):** 1–3 months. I found no provider-stated duration for CS50P.

---

## Gap 3 — Stage 1 terms aren't defined (line 58) — **Partly resolved**

| Term | Definition (source) |
|---|---|
| **PCA (principal component analysis)** | "A linear dimensionality reduction technique with applications in exploratory data analysis, visualization and data preprocessing." ([Wikipedia](https://en.wikipedia.org/wiki/Principal_component_analysis)) |
| **MLE (maximum likelihood estimation)** | "A method of estimating the parameters of an assumed probability distribution, given some observed data… by maximizing a likelihood function." ([Wikipedia](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation)) |
| **MAP (maximum a posteriori) estimate** | "The mode of the posterior density… employs an augmented optimization objective which incorporates a prior… MAP estimation is therefore a regularization of maximum likelihood estimation." ([Wikipedia](https://en.wikipedia.org/wiki/Maximum_a_posteriori_estimation)) |
| **Precision / recall** | "Performance metrics that apply to data retrieved from a collection, corpus or sample space." ([Wikipedia](https://en.wikipedia.org/wiki/Precision_and_recall)) |
| **F1 score (F-measure)** | "A measure that combines precision and recall is the harmonic mean of precision and recall, the traditional F-measure or balanced F-score." ([Wikipedia, Precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall)) |

**Not sourced:** separate definitions for every remaining Stage 1 term (vectors, eigenvalues, Bayes' rule, and so on). The 3Blue1Brown and Coursera math resources in Stage 1 cover these topics.

## Gap 4 — Stage 1 resources removed during checking, with no replacements (line 98) — **Resolved**

Two resources were removed. Two already-verified alternatives fill their roles:
- **Instead of *Hands-On Machine Learning*:** use [Dive into Deep Learning](https://d2l.ai/), a free interactive book with code (page title confirmed: "Dive into Deep Learning 1.0.3 documentation"), plus Kaggle Learn.
- **Instead of the Coursera Deep Learning Specialization:** use fast.ai's [Practical Deep Learning for Coders](https://course.fast.ai/), which is free, has 9 lessons of about 90 minutes each, and is checked.

I added no new paid replacement because I couldn't confirm one.

---

## Gap 5 — Stage 2 acronyms, and what "for context" means (line 118) — **Resolved**

| Term | Definition (source) |
|---|---|
| **MLP (multilayer perceptron)** | "A kind of modern feedforward neural network consisting of fully connected neurons with nonlinear activation functions, organized in layers." ([Wikipedia](https://en.wikipedia.org/wiki/Multilayer_perceptron)) |
| **SGD (stochastic gradient descent)** | "An iterative method for optimizing an objective function… replaces the actual gradient by an estimate thereof, calculated from a randomly selected subset of the data." ([Wikipedia](https://en.wikipedia.org/wiki/Stochastic_gradient_descent)) |
| **CNN (convolutional neural network)** | "A type of feedforward neural network that learns features via filter optimization… the de-facto standard… [for] computer vision… only recently replaced—in some cases—by… the transformer." ([Wikipedia](https://en.wikipedia.org/wiki/Convolutional_neural_network)) |
| **RNN (recurrent neural network)** | "Designed for processing sequential data… the output of a neuron at one time step is fed back as input… at the next time step." ([Wikipedia](https://en.wikipedia.org/wiki/Recurrent_neural_network)) |

**What "for context" means (editorial, based on the sources above):** CNNs and RNNs are background for understanding why transformers replaced earlier designs. The Wikipedia CNN entry and the RAG and Transformer papers present the transformer as the newer architecture. You don't need to master CNNs or RNNs for agent work.

## Gap 6 — micrograd, early stopping and Gradio aren't explained (line 152) — **Resolved**

- **micrograd:** "A tiny Autograd engine… Implements backpropagation (reverse-mode autodiff) over a dynamically built DAG and a small neural networks library on top of it with a PyTorch-like API… about 100 and 50 lines of code respectively." ([GitHub: karpathy/micrograd](https://github.com/karpathy/micrograd))
- **Early stopping:** "A form of regularization used to avoid overfitting when training a model with an iterative method, such as gradient descent… rules provide guidance as to how many iterations can be run before the learner begins to over-fit." ([Wikipedia](https://en.wikipedia.org/wiki/Early_stopping))
- **Gradio:** "An open-source Python package that allows you to quickly build a demo or web application for your machine learning model, API, or any arbitrary Python function… No JavaScript, CSS, or web hosting experience needed!" ([Gradio Quickstart](https://gradio.app/guides/quickstart))

---

## Gap 7 — Q/K/V, SFT, PEFT and LoRA aren't defined, nor are temperature and top-p (line 178) — **Partly resolved**

- **Q/K/V (query, key, value):** for each word, self-attention creates "a Query vector, a Key vector, and a Value vector… by multiplying the embedding by three matrices that we trained." Each score is "the dot product of the query vector with the key vector," divided by √d_k and passed through a softmax. That softmax weights the value vectors, which are then summed. ([The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/))
- **PEFT (Parameter-Efficient Fine-Tuning):** "A library for efficiently adapting large pretrained models… without fine-tuning all of a model's parameters… PEFT methods only fine-tune a small number of (extra) model parameters." ([Hugging Face PEFT docs](https://huggingface.co/docs/peft/index))
- **LoRA (Low-Rank Adaptation):** "Freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters." ([Hu et al., arXiv 2106.09685](https://arxiv.org/abs/2106.09685))
- **Fine-tuning:** "Adapting a computational model trained for one task to perform a different, usually more specific, task… a form of transfer learning." ([Wikipedia](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)))
- **SFT (supervised fine-tuning):** *AI Engineering* lists "Supervised Finetuning" and "Preference Finetuning" under Post-Training in Chapter 2 ([O'Reilly table of contents](https://www.oreilly.com/library/view/ai-engineering/9781098166298/)). The table of contents only names the topic; I found no checked definition beyond that, so I add none.
- **Temperature:** sourced. The Google ML Glossary defines it as a setting that controls how random a model's output is (see the Beginner basics glossary, [GG "temperature"]).
- **Top-p:** sits under "Sampling Strategies" in *AI Engineering* Chapter 2 (table of contents). **Not sourced:** I didn't check a page that explains exactly how top-p changes the output, so the mechanics are left out.

## Gap 8 — Number of chapters in the Hugging Face LLM Course (line 195) — **Resolved**

The course page describes Chapters 1–4, 5–8, 9 and 10–12, so there are **12 chapters**. At the provider's figure of about 1 week per chapter at 6–8 hrs/week, that works out to about **12 weeks, or roughly 72–96 hours** (my arithmetic from their figure). ([HF LLM Course](https://huggingface.co/learn/llm-course))

---

## Gap 9 — Prompting techniques aren't defined (line 232) — **Resolved**

The [DAIR.AI Prompt Engineering Guide](https://www.promptingguide.ai/) and Anthropic's [prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) cover these techniques. *AI Engineering* Chapter 5 covers "In-Context Learning: Zero-Shot and Few-Shot" and "Give the Model Time to Think" (table of contents). The ReAct paper's prompt appendix gives concrete examples ([arXiv 2210.03629](https://arxiv.org/abs/2210.03629)):
- **Standard few-shot:** question–answer exemplars only.
- **Chain-of-thought:** exemplars that include "Let's think step by step" reasoning before the answer.

**Zero-shot vs. few-shot:** zero-shot gives no examples; few-shot gives a few worked examples in the prompt. This matches *AI Engineering*'s "in-context learning" grouping.

## Gap 10 — Pydantic and red-teaming (line 261) — **Resolved**

- **Pydantic:** "The most widely used data validation library for Python… Define how data should be in pure, canonical Python 3.10+; validate it with Pydantic." ([Pydantic docs](https://pydantic.dev/docs/validation/latest/get-started/))
- **Red team:** "A group that simulates an adversary… then reports back so that the organization can improve their defenses." ([Wikipedia](https://en.wikipedia.org/wiki/Red_team)) The OWASP GenAI Security Project also has an "AI Red Teaming" initiative, listed in its site menu.

---

## Gap 11 — RAG terms (line 287) — **Partly resolved**

- **Parametric vs. non-parametric memory:** the RAG paper calls the pre-trained seq2seq model "parametric memory" and the "dense vector index of Wikipedia, accessed with a pre-trained neural retriever" "non-parametric memory." ([Lewis et al., arXiv 2005.11401](https://arxiv.org/abs/2005.11401))
- **Chunking:** in the RAG paper, "Each Wikipedia article is split into disjoint 100-word chunks, to make a total of 21M documents" (same paper).
- **ANN (approximate nearest neighbour) search:** the nearest-neighbour search problem is "finding the point in a given set that is closest to a given point" ([Wikipedia](https://en.wikipedia.org/wiki/Nearest_neighbor_search)). ANN algorithms "return approximately top k nearest neighbors to trade off a little accuracy lost for a huge speedup" ([Weng 2023](https://lilianweng.github.io/posts/2023-06-23-agent/)).
- **HNSW:** "An algorithm for approximate nearest neighbor search" ([Wikipedia](https://en.wikipedia.org/wiki/Hierarchical_navigable_small_world)). Weng's description: it "builds hierarchical layers of these small-world graphs… The layers in the middle create shortcuts to speed up search."
- **FAISS (Facebook AI Similarity Search):** "applies vector quantization by partitioning the vector space into clusters and then refining the quantization within clusters" (Weng). The RAG paper built its index "using FAISS… with a Hierarchical Navigable Small World approximation."
- **BM25:** "A ranking function used by search engines to estimate the relevance of documents to a given search query", based on the probabilistic retrieval framework of Robertson, Spärck Jones and others ([Wikipedia](https://en.wikipedia.org/wiki/Okapi_BM25)). The RAG paper calls it a "word overlap-based BM25 retriever."
- **Hybrid search (editorial):** combining sparse/keyword retrieval (BM25) with dense/embedding retrieval. The RAG paper's comparison of BM25 and dense retrieval shows that each wins on different tasks (BM25 was best on FEVER).
- **recall@k (editorial, following the Wikipedia precision/recall entry):** the share of the relevant documents that appear in the top *k* results.
- **Faithfulness and answer relevance:** these are Ragas metrics ([Ragas docs](https://docs.ragas.io/en/stable/)). **Not sourced:** I only checked the Ragas landing page, so I give no exact metric formulas.

## Gap 12 — Huyen's Chapter 6 is cited for both RAG and Agents (line 319) — **Resolved**

There's no error: Chapter 6 is titled **"RAG and Agents"** and has sub-sections for both RAG and Agents ([O'Reilly table of contents](https://www.oreilly.com/library/view/ai-engineering/9781098166298/)).

---

## Gap 13 — `tool_choice`, strict mode and JSON Schema (line 341) — **Resolved**

Source: [OpenAI function-calling guide](https://developers.openai.com/api/docs/guides/function-calling).
- **`tool_choice`** has five settings:
  - **Auto:** "Call zero, one, or multiple functions" (the default).
  - **Required:** "Call one or more functions."
  - **Forced:** call exactly one specific function.
  - **`allowed_tools`:** restrict calls to a subset.
  - **`none`:** imitates passing no functions.
- **Strict mode:** "Setting `strict` to `true` will ensure function calls reliably adhere to the function schema, instead of being best effort." It requires `additionalProperties: false` and that every field is listed as `required`. You mark optional fields by adding `null` as a type option.
- **JSON Schema:** "The vocabulary that enables JSON data consistency, validity, and interoperability" ([json-schema.org](https://json-schema.org/)). The OpenAI guide's `get_weather` example uses `type`, `properties`, `enum`, `required` and `additionalProperties`.

## Gap 14 — SWE-bench, Toolformer and API-Bank (line 355) — **Resolved**

- **SWE-bench:** "An evaluation framework consisting of 2,294 software engineering problems drawn from real GitHub issues" (Jimenez et al., arXiv 2310.06770, Oct 2023: https://arxiv.org/abs/2310.06770). Anthropic refers to "SWE-bench Verified" for agents that solve real GitHub issues.
- **Toolformer:** "A model trained to decide which APIs to call, when to call them, what arguments to pass" (the abstract is truncated in my check). In the authors' framing, LMs "can teach themselves to use external tools via simple APIs" (Schick et al., arXiv 2302.04761, Feb 2023: https://arxiv.org/abs/2302.04761).
- **API-Bank:** "A benchmark… for tool-augmented LLMs" (Li et al., arXiv 2304.08244, Apr 2023: https://arxiv.org/abs/2304.08244). Weng adds that it "contains 53 commonly used API tools… and 264 annotated dialogues that involve 568 API calls" and evaluates at three levels: call, retrieve, plan.

---

## Gap 15 — Workflows vs. agents, the five patterns, ToT, Reflexion, memory streams and Generative Agents (line 402) — **Resolved**

Definitions are from [Anthropic – Building effective agents](https://www.anthropic.com/engineering/building-effective-agents):
- **Workflows** are "systems where LLMs and tools are orchestrated through predefined code paths."
- **Agents** are "systems where LLMs dynamically direct their own processes and tool usage."

The five workflow patterns:
1. **Prompt chaining:** each LLM call processes the output of the previous one, with optional programmatic "gates."
2. **Routing:** classify the input and send it to a specialized follow-up.
3. **Parallelization:** "sectioning" (independent subtasks) or "voting" (the same task run several times).
4. **Orchestrator–workers:** a central LLM breaks down tasks dynamically, delegates them, and synthesizes the results.
5. **Evaluator–optimizer:** one LLM generates and another evaluates and gives feedback, in a loop.

Planning and memory methods:
- **Tree of Thoughts:** "Extends CoT by exploring multiple reasoning possibilities at each step… creating a tree structure", searched with BFS or DFS ([Weng 2023](https://lilianweng.github.io/posts/2023-06-23-agent/); Yao et al., arXiv 2305.10601, May 2023: https://arxiv.org/abs/2305.10601).
- **Reflexion:** "A framework to equip agents with dynamic memory and self-reflection capabilities." Reflections are added to working memory, up to three of them (Weng; Shinn et al., arXiv 2303.11366, Mar 2023: https://arxiv.org/abs/2303.11366).
- **Generative Agents and memory streams:** 25 LLM-controlled characters live in a Sims-like sandbox. A **memory stream** is "a long-term memory module (external database) that records a comprehensive list of agents' experience in natural language." Retrieval scores memories by recency, importance and relevance, and a reflection step turns memories into higher-level inferences (Weng; Park et al., arXiv 2304.03442, Apr 2023: https://arxiv.org/abs/2304.03442). This also supplies the missing citation.

## Gap 16 — ReAct's year, the ALFWorld and WebShop benchmarks, baselines, and the Agents Course chapter count (line 425) — **Resolved**

- **Year:** arXiv 2210.03629 dates the paper to Oct 2022. Weng cites it as "ICLR 2023."
- **ALFWorld:** "A synthetic text-based game designed to align with the embodied ALFRED benchmark", with 6 task types in a simulated household. The baseline was **BUTLER**, "an imitation learning agent trained on 10^5 expert trajectories."
- **WebShop:** "An online shopping website environment with 1.18M real-world products and 12k human instructions." The baselines were IL (1,012 human trajectories) and IL+RL. ([ReAct paper](https://arxiv.org/abs/2210.03629))
- **Hugging Face AI Agents Course structure:** Units 0–4 (Onboarding, Agent Fundamentals, Frameworks, Use Cases, Final Assignment) plus 3 bonus units (function-calling fine-tuning, observability & evaluation, agents in Pokémon games). At the provider's 3–4 hrs/week per chapter, the five main units come to about 15–20 hrs (my arithmetic). ([HF Agents Course](https://huggingface.co/learn/agents-course))

---

## Gap 17 — Durable state, checkpoints, guardrails, and the MCP client/server split (line 465) — **Partly resolved**

- **MCP roles** ([MCP architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)):
  - **Host:** the AI application, such as Claude Desktop or VS Code. It "coordinates and manages one or multiple MCP clients" and creates one client per server.
  - **MCP client:** "maintains a connection to an MCP server and obtains context from an MCP server for the MCP host to use."
  - **MCP server:** "a program that provides context to MCP clients."
  - **Transports:** local servers use STDIO and remote servers use Streamable HTTP.
- **Durable state / checkpoints:** LangGraph is "a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents", focused on "durable execution, streaming, human-in-the-loop" ([LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)). **Not sourced:** a formal definition of "checkpoint."
- **Guardrails:** the OpenAI Agents SDK describes them as running "input validation and safety checks in parallel with agent execution, and fail fast when checks do not pass" ([Agents SDK](https://openai.github.io/openai-agents-python/)).

## Gap 18 — Three resources have no descriptions, and no framework is recommended for beginners (line 512) — **Resolved**

| Resource | What the page says |
|---|---|
| [AI Agents in LangGraph](https://www.deeplearning.ai/courses/ai-agents-in-langgraph/) | Intermediate, 1h42m (re-checked on the course page, 16 Oct 2026), 9 video lessons, 6 code examples. Instructors: Harrison Chase (LangChain founder) and Rotem Weiss (Tavily founder). Covers LangGraph's components and agentic search. Enrolment is free; a graded accomplishment requires PRO. |
| [Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/courses/multi-ai-agent-systems-with-crewai/) | Beginner, 3h1m, 18 video lessons, 7 code examples. Instructor: João Moura. Covers designing a team of agents to automate multi-step tasks, such as tailoring a resume or event planning. |
| [Hugging Face MCP Course](https://huggingface.co/learn/mcp-course) | "Study Model Context Protocol in theory, design, and practice," use MCP SDKs, take part in challenges, and earn a certificate of completion. |

**Which framework a beginner should start with:** Anthropic advises starting "by using LLM APIs directly." LangGraph's own docs say it "is very low-level" and recommend LangChain's prebuilt agents "if you are just getting started with agents or want a higher-level abstraction."

**Editorial suggestion:** use raw APIs first, then the OpenAI Agents SDK or LangChain agents, then LangGraph when you need durable, stateful control. I found no independent, sourced comparison of the frameworks.

---

## Gap 19 — Bonus Unit 2 link points to the course homepage (line 564, part b) — **Resolved**

Direct link, with the title "AI Agent Observability & Evaluation" confirmed: https://huggingface.co/learn/agents-course/bonus-unit2/introduction

## Gap 20 — Only 7 of the 10 OWASP risks are named, and direct vs. indirect injection isn't explained (line 545) — **Resolved**

All 10 risks, from the [official OWASP 2025 list](https://genai.owasp.org/llm-top-10/):

| ID | Risk | OWASP's own summary (quoted from the official pages) |
|---|---|---|
| LLM01:2025 | Prompt Injection | "occurs when user prompts alter the…" |
| LLM02:2025 | Sensitive Information Disclosure | "can affect both the LLM and its application…" |
| LLM03:2025 | **Supply Chain** | "LLM supply chains are susceptible to various vulnerabilities…" |
| LLM04:2025 | **Data and Model Poisoning** | "occurs when pre-training, fine-tuning, or embedding data is…" |
| LLM05:2025 | Improper Output Handling | "insufficient validation, sanitization, and…" |
| LLM06:2025 | Excessive Agency | "An LLM-based system is often granted a degree of agency…" |
| LLM07:2025 | System Prompt Leakage | "refers to the risk that the system prompts or instructions used to steer the behavior of the model can also contain sensitive information that was not intended to be discovered" ([LLM07 page](https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/)) |
| LLM08:2025 | Vector and Embedding Weaknesses | "Vectors and embeddings vulnerabilities present significant security risks in systems utilizing Retrieval Augmented Generation (RAG) with Large Language Models (LLMs)." ([LLM08 page](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/); full text in "QA additions for notes") |
| LLM09:2025 | **Misinformation** | "Misinformation from LLMs poses a core vulnerability…" |
| LLM10:2025 | Unbounded Consumption | "Unbounded Consumption refers to the process where a Large Language Model (LLM) generates outputs based on input queries or prompts." ([LLM10 page](https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/)) |

**Direct vs. indirect prompt injection** ([OWASP LLM01 page](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)):
- *Direct* injections "occur when a user's prompt input directly alters the behavior of the model."
- *Indirect* injections "occur when an LLM accepts input from external sources, such as websites or files."
- Both can be intentional or unintentional. OWASP also notes that RAG and fine-tuning "do not fully mitigate prompt injection vulnerabilities" and that jailbreaking is "a form of prompt injection."

## Gap 21 — What ChemCrow is, and what it was compared with (line 564, part a) — **Resolved**

ChemCrow augments an LLM "with 13 expert-designed tools to accomplish tasks across organic synthesis, drug discovery, and materials design." It was implemented in LangChain using a ReAct/MRKL-style loop. It was compared with **GPT-4**: "LLM-based evaluation concluded that GPT-4 and ChemCrow perform nearly equivalently, [but] human evaluations with experts… showed that ChemCrow outperforms GPT-4 by a large margin." ([Weng 2023](https://lilianweng.github.io/posts/2023-06-23-agent/); Bran et al., arXiv 2304.05376, Apr 2023: https://arxiv.org/abs/2304.05376)

---

## Gap 22 — How model routing decides between models, and which queue tools to use (line 607) — **Unresolved**

What I could source:
- *AI Engineering* Chapter 10 has the step "Add Model Router and Gateway" (table of contents only).
- Anthropic's routing workflow sends "easy/common questions to smaller, cost-efficient models… and hard/unusual questions to more capable models."
- A message queue is a component "used for inter-process communication… [using] a queue for messaging" ([Wikipedia](https://en.wikipedia.org/wiki/Message_queue)).

**Not sourced:** specific router algorithms, and recommended queue products. I checked no page about any queueing tool, so I name none.

## Gap 23 — What "enhance context" and "gateway" mean in Huyen's architecture (line 624) — **Partly resolved**

The table of contents lists "Step 1. Enhance Context" and "Step 3. Add Model Router and Gateway," and Chapter 6 (RAG and Agents) is the context-building chapter. The full text is paywalled, so **I couldn't verify Huyen's exact definitions** of "enhance context" or "gateway."

## Gap 24 — No resources for secrets management, queues, caching or hosting (line 652) — **Partly resolved**

- **Caching:** "A hardware or software component that stores data so that future requests for that data can be served faster" ([Wikipedia](https://en.wikipedia.org/wiki/Cache_(computing))). *AI Engineering* Chapter 10 has "Reduce Latency with Caches." The OpenAI function-calling guide notes that `allowed_tools` lets you "maximize savings from prompt caching."
- **Queues:** the Wikipedia message-queue entry above.
- **Not sourced:** a secrets-management resource (the Wikipedia lookup returned nothing) and cloud hosting guides. These remain open.

## Gap 25 — Works named but missing from the source list (line 826) — **Partly resolved**

Citations now added, all checked through the arXiv API:

| Work | Citation |
|---|---|
| Generative Agents | arXiv 2304.03442 |
| Tree of Thoughts | arXiv 2305.10601 |
| Reflexion | arXiv 2303.11366 |
| Toolformer | arXiv 2302.04761 |
| API-Bank | arXiv 2304.08244 |
| ChemCrow | arXiv 2304.05376 |
| SWE-bench | arXiv 2310.06770 |
| LoRA | arXiv 2106.09685 |

**Not sourced:** I didn't check the ALFWorld or WebShop original papers. They are described here only through the ReAct paper.

## Gap 26 — The OpenAI Agents SDK is labelled differently in Stages 8 and 10 (line 654) — **Partly resolved**

Gap 26 covers the SDK labels. Nova's notes also flag several smaller items, and those are folded into this section as 26b.

**26a — SDK label: Resolved.** The SDK is open source under the **MIT License** ("Copyright (c) 2025 OpenAI"; [LICENSE](https://raw.githubusercontent.com/openai/openai-agents-python/main/LICENSE)). It "uses the Responses API by default for OpenAI models" ([SDK docs](https://openai.github.io/openai-agents-python/)). OpenAI's [pricing page](https://developers.openai.com/api/docs/pricing) lists model prices "per 1M tokens," so model calls are billed.

**Correct label in both stages:** "Free, open source (MIT); model API usage billed per token."

**26b — Smaller explanation gaps:**
- *Resolved:*
  - micrograd, early stopping, Gradio: see Gap 6.
  - Pydantic, red-teaming: see Gap 10.
  - The Bonus Unit 2 link: see Gap 19.
- *Still not sourced:*
  - how top-p changes the output (Gap 7; temperature is now sourced in the glossary);
  - the exact formulas for the Ragas metrics (Gap 11);
  - a formal definition of "checkpoint" (Gap 17).

---

## New sources added in this addendum (all checked 16 Oct 2026)

1. Python wiki – BeginnersGuide/NonProgrammers: https://wiki.python.org/moin/BeginnersGuide/NonProgrammers
2. CS50's Introduction to Programming with Python: https://cs50.harvard.edu/python/
3. Automate the Boring Stuff with Python: https://automatetheboringstuff.com/
4. Wikipedia – PCA: https://en.wikipedia.org/wiki/Principal_component_analysis
5. Wikipedia – MLE: https://en.wikipedia.org/wiki/Maximum_likelihood_estimation
6. Wikipedia – MAP: https://en.wikipedia.org/wiki/Maximum_a_posteriori_estimation
7. Wikipedia – MLP: https://en.wikipedia.org/wiki/Multilayer_perceptron
8. Wikipedia – SGD: https://en.wikipedia.org/wiki/Stochastic_gradient_descent
9. Wikipedia – CNN: https://en.wikipedia.org/wiki/Convolutional_neural_network
10. Wikipedia – RNN: https://en.wikipedia.org/wiki/Recurrent_neural_network
11. Wikipedia – Early stopping: https://en.wikipedia.org/wiki/Early_stopping
12. Wikipedia – Okapi BM25: https://en.wikipedia.org/wiki/Okapi_BM25
13. Wikipedia – Nearest neighbor search: https://en.wikipedia.org/wiki/Nearest_neighbor_search
14. Wikipedia – HNSW: https://en.wikipedia.org/wiki/Hierarchical_navigable_small_world
15. Wikipedia – Red team: https://en.wikipedia.org/wiki/Red_team
16. Wikipedia – Precision and recall: https://en.wikipedia.org/wiki/Precision_and_recall
17. Wikipedia – Fine-tuning (deep learning): https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)
18. Wikipedia – Message queue: https://en.wikipedia.org/wiki/Message_queue
19. Wikipedia – Cache (computing): https://en.wikipedia.org/wiki/Cache_(computing)
20. Hu et al. – LoRA: https://arxiv.org/abs/2106.09685
21. Yao et al. – Tree of Thoughts: https://arxiv.org/abs/2305.10601
22. Shinn et al. – Reflexion: https://arxiv.org/abs/2303.11366
23. Park et al. – Generative Agents: https://arxiv.org/abs/2304.03442
24. Schick et al. – Toolformer: https://arxiv.org/abs/2302.04761
25. Li et al. – API-Bank: https://arxiv.org/abs/2304.08244
26. Bran et al. – ChemCrow: https://arxiv.org/abs/2304.05376
27. Jimenez et al. – SWE-bench: https://arxiv.org/abs/2310.06770
28. karpathy/micrograd: https://github.com/karpathy/micrograd
29. Gradio Quickstart: https://gradio.app/guides/quickstart
30. Pydantic docs: https://pydantic.dev/docs/validation/latest/get-started/
31. Hugging Face PEFT docs: https://huggingface.co/docs/peft/index
32. JSON Schema: https://json-schema.org/
33. MCP architecture overview: https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture
34. OWASP LLM01:2025 Prompt Injection: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
35. OpenAI Agents SDK LICENSE (MIT): https://raw.githubusercontent.com/openai/openai-agents-python/main/LICENSE
36. OpenAI API pricing: https://developers.openai.com/api/docs/pricing
37. HF Agents Course – Bonus Unit 2: https://huggingface.co/learn/agents-course/bonus-unit2/introduction

Sources reused from the original path: the HF LLM and Agents courses, the OpenAI function-calling guide, the OpenAI Agents SDK, LangGraph, Anthropic's "Building effective agents", Lilian Weng's post, the ReAct and RAG papers, the Illustrated Transformer, *AI Engineering* (table of contents), the OWASP Top 10 list, the DeepLearning.AI course pages, the HF MCP course, d2l.ai and fast.ai.

---

## Beginner basics glossary

*These definitions are for someone who has never programmed. They are written in plain language, and each one is a paraphrase of the source cited next to it. I checked every source on 16 Oct 2026. Short abbreviations are used in the tables:*
- **[GG]** = [Google Machine Learning Glossary](https://developers.google.com/machine-learning/glossary)
- **[AG]** = [Anthropic glossary](https://platform.claude.com/docs/en/about-claude/glossary)
- **[W: …]** = the Wikipedia article named after the colon (the full URL is the article title with spaces as underscores, e.g. `https://en.wikipedia.org/wiki/Large_language_model`).

### The big ideas

| Term | Plain-language definition | Source |
|---|---|---|
| **AI (artificial intelligence)** | Computer systems that can do tasks we normally link to human intelligence, such as learning, reasoning, solving problems, perceiving things and making decisions. It is also the name of the research field that builds such systems. | [W: Artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence) |
| **Machine learning (ML)** | A part of AI where, instead of a person writing every rule by hand, a program learns patterns from data. It then uses those patterns to handle new data it has never seen. | [GG "machine learning"]; [W: Machine learning](https://en.wikipedia.org/wiki/Machine_learning) |
| **Generative AI** | AI that *creates* new things (text, images, audio, video or computer code) by learning the patterns in the data it was trained on. | [W: Generative artificial intelligence](https://en.wikipedia.org/wiki/Generative_AI) |
| **Algorithm** | A precise, step-by-step set of instructions that solves a problem and finishes after a limited number of steps, much like a recipe. | [W: Algorithm](https://en.wikipedia.org/wiki/Algorithm) |
| **Model** | The thing machine learning produces: a mathematical "machine" that takes some input and returns an output, such as a prediction. Google describes it as "the set of parameters and structure needed for a system to make predictions." | [GG "model"] |

### How models learn and get used

| Term | Plain-language definition | Source |
|---|---|---|
| **Dataset** | A collection of data, often arranged like a spreadsheet: each row is one record and each column is one kind of information (for example, height or weight). | [GG "dataset"]; [W: Data set](https://en.wikipedia.org/wiki/Data_set) |
| **Example** | One row of a dataset: the input values, and sometimes the correct answer. | [GG "example"] |
| **Label** | The "correct answer" attached to an example. For instance, "spam" or "not spam" for an email. | [GG "label"] |
| **Training** | Showing a model many examples so it gradually adjusts its internal numbers (its parameters) until its outputs are good. Each example may be used anywhere from a few times to billions of times. | [GG "training"] |
| **Parameters / weights** | The internal numbers a model learns during training. A *weight* is a value the model multiplies an input by. Training finds good weights, and inference uses them. | [GG "parameter", "weight"] |
| **Inference** | *Using* a trained model, as opposed to training it. For an LLM, inference means taking your prompt and generating a response. | [GG "inference"] |
| **Pretraining** | The first, very large training stage, where a language model reads a huge amount of unlabeled text and learns to predict the next word. | [AG "Pretraining"] |
| **Fine-tuning** | Taking a model that was already trained for one job and training it a bit more so it does a narrower, more specific job. | [W: Fine-tuning (deep learning)](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)) |
| **Overfitting** | When a model memorizes its training data too closely, so it does poorly on new data. It is like a student who memorized the practice test but can't answer new questions. | [W: Overfitting](https://en.wikipedia.org/wiki/Overfitting) |
| **Neural network** | A kind of model loosely inspired by how brain cells connect. It is built from layers of simple connected units, and a "deep" neural network has many layers. | [W: Neural network (machine learning)](https://en.wikipedia.org/wiki/Neural_network_(machine_learning)); [GG "neural network"] |
| **Embedding** | A way of turning something like a word or a document into a list of numbers. Things with similar meanings end up with similar numbers, so a computer can compare them. | [W: Embedding (machine learning)](https://en.wikipedia.org/wiki/Embedding_(machine_learning)) |

### Language models and chat AI

| Term | Plain-language definition | Source |
|---|---|---|
| **LLM (large language model)** | An AI model trained on a huge amount of text so it can generate, summarize, translate and analyze language. LLMs power chatbots such as ChatGPT, Claude, Gemini and Grok. | [W: Large language model](https://en.wikipedia.org/wiki/Large_language_model); [GG "large language model"] |
| **Chatbot** | A program or website you have a conversation with, by text or voice. Modern chatbots run on LLMs. | [W: Chatbot](https://en.wikipedia.org/wiki/Chatbot) |
| **Token** | The small chunk of text an LLM actually reads and writes. A token can be a whole word, part of a word, a single character, or even a byte. Usage and limits are usually counted in tokens, not words. | [AG "Tokens"]; [GG "token"] |
| **Context window** | The maximum number of tokens a model can take into account at one time, including your conversation and any documents. Anything beyond that limit, the model can't "see." | [W: Context window](https://en.wikipedia.org/wiki/Context_window); [GG "context window"] |
| **Prompt** | Any text you give an LLM as input to steer what it does. It can be one short phrase or something as long as a whole novel. | [GG "prompt"] |
| **Prompt engineering** | The skill of writing and structuring prompts so a generative AI model produces the output you want. | [W: Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering) |
| **Temperature** | A setting that controls how random a model's output is. Higher means more varied and surprising; lower means more predictable. | [GG "temperature"] |
| **Hallucination** | When an AI states something false or made-up as if it were fact. Google's example: a model claiming Barack Obama died in 1865. | [GG "hallucination"]; [W: Hallucination (AI)](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)) |
| **Tool use (function calling)** | Letting an AI model call functions or services, such as a web search or a weather lookup. The model decides when to call a tool based on your request and the tool's description, and the result is fed back to it so it can answer. | [Anthropic tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) |
| **Agent (AI agent)** | Software that can reason about what you ask, plan steps, and take actions for you, such as searching, running tools or sending requests, rather than only replying with text. | [GG "agent"]; [W: Intelligent agent](https://en.wikipedia.org/wiki/Intelligent_agent) |

### Programming and software words

| Term | Plain-language definition | Source |
|---|---|---|
| **Python** | A popular programming language that is designed to be easy to read and write. Most AI tools are built for it. | [W: Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language)) |
| **Source code (code)** | The human-readable text instructions that programmers write, which a computer then runs. | [W: Source code](https://en.wikipedia.org/wiki/Source_code) |
| **Library** | Ready-made code that other people wrote and you can reuse in your own program, so you don't start from scratch. | [W: Library (computing)](https://en.wikipedia.org/wiki/Library_(computing)) |
| **pip** | Python's tool for installing libraries ("packages"). It downloads them from a public online collection called PyPI. | [W: pip (package manager)](https://en.wikipedia.org/wiki/Pip_(package_manager)) |
| **Command line / terminal (CLI)** | A way of using a computer by typing text commands, one line at a time, instead of clicking buttons. | [W: Command-line interface](https://en.wikipedia.org/wiki/Command-line_interface) |
| **JSON** | A common, human-readable text format for storing and sending data as name–value pairs (e.g. `"city": "Paris"`). AI tools use it a lot. | [W: JSON](https://en.wikipedia.org/wiki/JSON) |
| **API (application programming interface)** | A defined way for one program to talk to another and use its services. For example, your code can send a prompt to an AI company's API and get the model's answer back. | [W: API](https://en.wikipedia.org/wiki/API) |
| **API key** | A secret code that identifies you to an API and proves you are allowed to use it, much like a password for your program. Keep it private. | [W: API key](https://en.wikipedia.org/wiki/API_key) |
| **SDK (software development kit)** | A bundle of tools, installed as one package, that makes it easier to build software for a particular platform or service. | [W: Software development kit](https://en.wikipedia.org/wiki/Software_development_kit) |
| **Open source** | Software published together with its source code, so anyone can use, study, change and share it, subject to its license (e.g. MIT). | [W: Open source](https://en.wikipedia.org/wiki/Open_source) |
| **Git** | Software that tracks every version of your code over time, so you can undo changes and work with others. | [W: Git](https://en.wikipedia.org/wiki/Git) |
| **Repository (repo)** | The place where a project's files and their full version history are stored, for example a project on GitHub. | [W: Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control)) |

### Hardware and infrastructure

| Term | Plain-language definition | Source |
|---|---|---|
| **GPU (graphics processing unit)** | A computer chip first built for graphics. It can do many calculations at once, which makes it much faster than an ordinary processor for training and running AI. | [W: Graphics processing unit](https://en.wikipedia.org/wiki/Graphics_processing_unit); [GG, "accelerator chip" entry] |
| **Cloud computing ("the cloud")** | Renting computers, storage and services over the internet on demand, instead of owning the machines yourself. | [W: Cloud computing](https://en.wikipedia.org/wiki/Cloud_computing) |

**Count:** 40 terms (Tool use added after QA review 01). Every term has a checked source; none are unsourced.

**Caveats:**
- For "Generative AI", the Wikipedia link redirects to the article "Generative AI."
- The Google Glossary has no standalone entry for "GPU", so I cited its "accelerator chip" mention and Wikipedia instead.
- The token example "dogs like cats" (three word tokens) comes from the Google Glossary; I didn't repeat it in the table.

---

## QA additions for notes

*Added after QA review 01 (Sage) so Nova can copy the full text into the notes. Every item below was checked on 16 Oct 2026.*

### 1. fast.ai prerequisite (full quote)

> "The only prerequisite is that you know how to code (a year of experience is enough), preferably in Python, and that you have at least followed a high school math course."

Source: [course.fast.ai](https://course.fast.ai/) (curl). **Takeaway for beginners:** fast.ai expects some coding experience, so a non-coder should do Stage 0/Stage 1 first.

### 2. OWASP LLM07, LLM08 and LLM10, full summaries

| ID | Risk | Summary (quoted from the official detail page) | Source |
|---|---|---|---|
| LLM07:2025 | System Prompt Leakage | "The system prompt leakage vulnerability in LLMs refers to the risk that the system prompts or instructions used to steer the behavior of the model can also contain sensitive information that was not intended to be discovered." "When discovered, this information can be used to facilitate other attacks. It's important to understand that the system prompt should not be considered a secret, nor should it be used as a security control." | [LLM07 detail page](https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/) (curl) |
| LLM08:2025 | Vector and Embedding Weaknesses | "Vectors and embeddings vulnerabilities present significant security risks in systems utilizing Retrieval Augmented Generation (RAG) with Large Language Models (LLMs). Weaknesses in how vectors and embeddings are generated, stored, or retrieved can be exploited by malicious actions (intentional or unintentional) to inject harmful content, manipulate model outputs, or access sensitive information." | [LLM08 detail page](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/) (WebFetch) |
| LLM10:2025 | Unbounded Consumption | "Unbounded Consumption occurs when a Large Language Model (LLM) application allows users to conduct excessive and uncontrolled inferences, leading to risks such as denial of service (DoS), economic losses, model theft, and service degradation. The high computational demands of LLMs, especially in cloud environments, make them vulnerable to resource exploitation and unauthorized usage." | [LLM10 detail page](https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/) (curl) |

**Status:** all four items are fully sourced. The LLM08 text that was cut off earlier is now complete, taken from its detail page.
