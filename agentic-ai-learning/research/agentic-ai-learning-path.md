# Learning AI from scratch to mastery in building agentic AI

*A structured, beginner-to-mastery learning path. Compiled 16 Oct 2026.*

**Notes before you start**
- **All time estimates are rough *estimates* (assuming roughly 8–10 hrs/week)** unless they are marked as the provider's own figure.
- I checked every link on 16 Oct 2026. Links whose content I couldn't confirm were removed.
- "Paid" means the resource costs money. I don't quote prices here because they change; check the provider page.
- The path is cumulative, but stages 4–10 overlap heavily in practice. Start building small agents early. Don't wait until "mastery" of the earlier stages.

**Total path (estimate): ~10–20 months if done sequentially at 8–10 hrs/week (≈11–23 months including Stage 0 from the addendum); overlap between Stages 4–10 may shorten this.** See `/workspace/agentic-ai-research-addendum.md`.

---

## Stage 1 — Foundations: math, Python, ML basics

**Key concepts**
- *Linear algebra:* vectors, matrices, dot products, matrix multiplication, linear transformations, eigenvalues/eigenvectors, PCA.
- *Calculus:* derivatives, partial derivatives, gradients, the chain rule, gradient descent.
- *Probability & statistics:* distributions (binomial, Gaussian), expectation, Bayes' rule, MLE/MAP, hypothesis testing.
- *Python:* data structures, functions, classes, modules, exceptions, virtual environments/pip, JSON, NumPy/pandas.
- *ML basics:* supervised vs. unsupervised learning, linear and logistic regression, train/dev/test splits, over/underfitting, decision trees and ensembles, evaluation metrics.

**Why it matters:** Embeddings, attention and similarity search are linear algebra. Training is calculus plus optimization. LLM outputs are probability distributions over tokens. Almost every agent framework and LLM SDK is Python-first. You can't debug or evaluate these systems well without this base.

**Resources**
| Resource | Type | Notes |
|---|---|---|
| [3Blue1Brown – Linear Algebra (Essence of LA)](https://www.3blue1brown.com/?topic=linear-algebra) | Free | Visual intuition for vectors and transformations. |
| [The Python Tutorial (official docs)](https://docs.python.org/3/tutorial/) | Free | The docs say it is aimed at people who already program but are new to Python. It covers control flow, data structures, classes, venv/pip. |
| [Kaggle Learn](https://www.kaggle.com/learn) | Free | Short, hands-on micro-courses (Python, pandas, intro ML). |
| [Mathematics for Machine Learning and Data Science Specialization (DeepLearning.AI / Coursera)](https://www.coursera.org/specializations/mathematics-for-machine-learning-and-data-science) | Paid (financial aid available) | Linear algebra, calculus, probability and statistics, with Python labs. Provider figure: "12 weeks … at 5 hours a week." |
| [Machine Learning Specialization (Andrew Ng, DeepLearning.AI + Stanford Online / Coursera)](https://www.coursera.org/specializations/machine-learning-introduction) | Paid (financial aid available) | Beginner level, 3 courses, NumPy/scikit-learn/TensorFlow. Provider figure: "2 months at 10 hours a week." |
| [Deep Learning book, Part I (Goodfellow, Bengio, Courville)](https://www.deeplearningbook.org/) | Free online (print edition paid) | Chapters 2–5 cover linear algebra, probability, numerical computation and ML basics, all at a rigorous level. |

**Hands-on projects**
1. Implement linear regression with gradient descent in pure NumPy, then check it against scikit-learn.
2. Do a PCA on a small dataset from scratch (eigendecomposition) and plot the result.
3. Build a CLI Python app that reads a CSV or JSON file, cleans it with pandas, and trains a classifier. Report precision, recall and F1.

**Time estimate (estimate):** 2–4 months. Less if you already code in Python.

---

## Stage 2 — Deep learning

**Key concepts:** neurons and MLPs, activation functions, backpropagation, loss functions (cross-entropy), SGD/Adam, regularization (weight decay, dropout), CNNs and RNNs (for context), embeddings, transfer learning, PyTorch tensors and training loops.

**Why it matters:** LLMs are deep neural networks. Knowing how training, loss and backprop work helps you reason about fine-tuning, embeddings, tokenization quirks and model behaviour.

**Resources**
| Resource | Type | Notes |
|---|---|---|
| [fast.ai – Practical Deep Learning for Coders](https://course.fast.ai/) | Free | 9 lessons of about 90 minutes each, using PyTorch, fastai, Hugging Face Transformers and Gradio. Prerequisite, quoted from the site: "The only prerequisite is that you know how to code (a year of experience is enough), preferably in Python, and that you have at least followed a high school math course." |
| [Andrej Karpathy – Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) | Free | Builds backprop (micrograd) and then language models up to GPT, from scratch in code. |
| [3Blue1Brown – Neural Networks](https://www.3blue1brown.com/?topic=neural-networks) | Free | Visual intuition for backprop and, later, transformers. |
| [Dive into Deep Learning (d2l.ai)](https://d2l.ai/) | Free | Interactive book with runnable code. |
| [Deep Learning book, Part II](https://www.deeplearningbook.org/) | Free online | Theory reference for feedforward nets, regularization, optimization and CNNs/RNNs. |

**Hands-on projects**
1. Build micrograd following Karpathy, then train a tiny MLP with it.
2. Fine-tune a pretrained image or text classifier (fast.ai lessons 1–2) and deploy it as a Gradio demo.
3. Write a full PyTorch training loop by hand, with a validation split and early stopping.

**Time estimate (estimate):** 1.5–3 months.

---

## Stage 3 — LLMs and transformers

**Key concepts:** tokenization, embeddings, self-attention (Q/K/V), multi-head attention, positional encoding, encoder vs. decoder vs. encoder–decoder, next-token prediction, sampling (temperature, top-p), context windows, pretraining vs. post-training (SFT, preference tuning), fine-tuning and PEFT/LoRA, the Hugging Face ecosystem.

**Why it matters:** The LLM is the "brain" of every agent. Its strengths and limits drive every design decision you make later: context windows, hallucination, and how reliably it produces structured output.

**Resources**
| Resource | Type | Notes |
|---|---|---|
| [Attention Is All You Need (Vaswani et al., 2017)](https://arxiv.org/abs/1706.03762) | Free paper | The original Transformer paper. |
| [The Illustrated Transformer (Jay Alammar)](https://jalammar.github.io/illustrated-transformer/) | Free | Step-by-step visual walkthrough of self-attention, multi-head attention, positional encoding and the decoder. |
| [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) | Free | Transformers, Datasets and Tokenizers, then fine-tuning and reasoning models. Provider figure: each chapter is about 1 week at 6–8 hrs. Prerequisite (course page): it "Requires a good knowledge of Python" and "Is better taken after an introductory deep learning course". |
| [Stanford CS224N – NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) | Free materials | University-level NLP and deep learning course. |
| [Karpathy – Zero to Hero (GPT lectures)](https://karpathy.ai/zero-to-hero.html) | Free | Builds a GPT-style model from scratch. |
| [AI Engineering – Chip Huyen (O'Reilly, Dec 2024)](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) | Paid book | Ch. 2 covers foundation models (sampling, post-training, structured outputs). This book is used again in later stages. |

**Hands-on projects**
1. Implement a single self-attention head and a tiny character-level GPT, following Karpathy.
2. Load an open model with Hugging Face `transformers`, compare greedy decoding with temperature/top-p sampling, and look at the tokenization.
3. LoRA fine-tune a small model on a narrow task and compare it with prompting alone.

**Time estimate (estimate):** 1.5–2.5 months.

---

## Stage 4 — Prompt engineering

**Key concepts:** clear instructions, system vs. user prompts, zero-shot and few-shot prompting, chain-of-thought / "time to think," structured output (XML or JSON), role prompting, prompt chaining, building evals *before* you optimize, prompt versioning, defensive prompting against injection.

**Why it matters:** In an agent, the system prompt and the tool descriptions *are* the program. Anthropic's prompt-engineering guide recommends defining success criteria and a way to test against them before you start prompt engineering.

**Resources**
| Resource | Type | Notes |
|---|---|---|
| [Prompt Engineering Guide (DAIR.AI)](https://www.promptingguide.ai/) | Free | Techniques, papers, model-specific guides. |
| [Anthropic – Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) | Free | Links to best practices, a metaprompt generator, and interactive tutorials. |
| [Anthropic courses (GitHub)](https://github.com/anthropics/courses) | Free | Anthropic's educational notebooks, including the prompt-engineering tutorial. |
| [AI Engineering (Huyen), Ch. 5](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) | Paid | Prompting best practices, defensive prompt engineering, jailbreaking and prompt injection. |

**Hands-on projects**
1. Build a small eval set (20–50 cases) for an extraction task. Iterate on the prompt and track the score for each prompt version.
2. Get structured JSON out reliably and validate it with Pydantic.
3. Red-team your own prompt with injection attempts and document what defenses you added.

**Time estimate (estimate):** 2–4 weeks, then ongoing practice.

---

## Stage 5 — Retrieval-Augmented Generation (RAG)

**Key concepts:** parametric vs. non-parametric memory, chunking, embeddings, vector indexes and ANN search (HNSW, FAISS), BM25 and hybrid search, re-ranking, query rewriting, citations/grounding, RAG evaluation (retrieval recall, faithfulness, answer relevance).

**Why it matters:** RAG lets a model use private or fresh knowledge without retraining. The original RAG paper showed that swapping the retrieval index updates what the model knows. Agent "long-term memory" is usually built from the same pieces.

**Resources**
| Resource | Type | Notes |
|---|---|---|
| [Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (2020)](https://arxiv.org/abs/2005.11401) | Free paper | The paper that introduced RAG. |
| [Sentence Transformers (SBERT) docs](https://www.sbert.net/) | Free | Computing embeddings and doing semantic search. |
| [LlamaIndex framework docs](https://developers.llamaindex.ai/python/framework/) | Free (open source) | Data and RAG-focused framework. The old URL `docs.llamaindex.ai/en/stable/` still resolves. |
| [Ragas docs](https://docs.ragas.io/en/stable/) | Free (open source) | Library for evaluating RAG and LLM apps. |
| [AI Engineering (Huyen), Ch. 6](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) | Paid | RAG architecture, retrieval algorithms and optimization. |

**Hands-on projects**
1. Build "chat with your docs" from scratch: chunk the docs, embed them, store them in FAISS or a vector DB, retrieve, and generate answers with citations.
2. Compare dense, BM25 and hybrid retrieval on 30 hand-labeled questions. Measure recall@k.
3. Add a re-ranker and run a Ragas-style faithfulness eval.

**Time estimate (estimate):** 3–5 weeks.

---

## Stage 6 — Tool use and function calling

**Key concepts:** tool and function definitions with JSON Schema, the tool-calling loop (request → tool call → execute → return output → final answer), `tool_choice`, parallel tool calls, strict/structured outputs, error handling, designing good tools (the "agent-computer interface").

**Why it matters:** Tools are what let an LLM *act*. OpenAI's guide describes tool calling as a multi-step conversation between your app and the model. Anthropic reports that while building its SWE-bench agent it spent more time optimizing tools than the overall prompt.

**Resources**
| Resource | Type | Notes |
|---|---|---|
| [OpenAI – Function calling guide](https://developers.openai.com/api/docs/guides/function-calling) | Free docs (API usage paid) | The 5-step tool-calling flow, strict mode, tool_choice, parallel calls, and best practices such as aiming for fewer than 20 functions available at once. |
| [Anthropic – Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | Free | How to design tools for agents. |
| [Anthropic – Building effective agents, Appendix 2 "Prompt engineering your tools"](https://www.anthropic.com/engineering/building-effective-agents) | Free | Covers ACI design and "poka-yoke" (mistake-proof) tools. |
| [Toolformer / API-Bank summaries in Lilian Weng's "LLM Powered Autonomous Agents"](https://lilianweng.github.io/posts/2023-06-23-agent/) | Free | Research background on tool-augmented LLMs. |

**Hands-on projects**
1. Write a raw tool-calling loop with no framework, using 3 tools (calculator, web search, file read). Add retries and handle malformed arguments.
2. Build a "SQL analyst" that inspects the schema, writes queries, runs them read-only, and explains the results.
3. Measure tool-selection accuracy as you go from 3 to 20 tools.

**Time estimate (estimate):** 2–4 weeks.

---

## Stage 7 — Agent architectures: planning, memory, multi-agent

**Key concepts**
- *Workflows vs. agents* (Anthropic's distinction). Workflow patterns: prompt chaining, routing, parallelization, orchestrator–workers, evaluator–optimizer.
- *Planning:* task decomposition, CoT, Tree of Thoughts, ReAct (interleaved thought → action → observation), Reflexion / self-reflection.
- *Memory:* short-term memory (the context window) vs. long-term memory (a vector store), memory streams, and retrieval by recency, importance and relevance (Generative Agents).
- *Multi-agent:* handoffs, manager/specialist structures, agents-as-tools.
- *Stopping conditions,* human-in-the-loop checkpoints.

**Why it matters:** Architecture decides reliability, cost and latency. Anthropic advises "finding the simplest solution possible, and only increasing complexity when needed." Weng lists finite context, long-horizon planning, and the reliability of natural-language interfaces as core challenges.

**Resources**
| Resource | Type | Notes |
|---|---|---|
| [Anthropic – Building effective agents (Dec 2024)](https://www.anthropic.com/engineering/building-effective-agents) | Free | Defines the workflow patterns and when to use agents. The page itself notes that parts of the tooling landscape have changed since it was published. |
| [Lilian Weng – LLM Powered Autonomous Agents (2023)](https://lilianweng.github.io/posts/2023-06-23-agent/) | Free | Canonical survey of planning, memory and tool use. |
| [ReAct paper (Yao et al.)](https://arxiv.org/abs/2210.03629) | Free paper | The reasoning + acting paradigm. Reports absolute success-rate gains of 34% on ALFWorld and 10% on WebShop over imitation/RL baselines. |
| [Hugging Face AI Agents Course](https://huggingface.co/learn/agents-course) | Free (free certificate) | Agent fundamentals, then smolagents / LlamaIndex / LangGraph, use cases and a final benchmark. Provider figure: about 3–4 hrs/week per chapter. |
| [AI Engineering (Huyen), Ch. 6 "RAG and Agents" (Agents sections)](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) | Paid | Tools, planning, agent failure modes, memory. |

**Hands-on projects**
1. Implement all five workflow patterns from the Anthropic post as small scripts.
2. Build a ReAct research agent with a step budget and a reflection step. Log each trajectory.
3. Add long-term memory (vector store plus recency/importance scoring) to a personal assistant agent.
4. Build a 3-agent system (planner → researcher → writer) and compare it with a single agent on the same tasks.

**Time estimate (estimate):** 1–2 months.

---

## Stage 8 — Frameworks and protocols

**Key concepts:** graph or state-machine orchestration, durable state and checkpoints, handoffs, guardrails, tracing, sessions, and MCP clients and servers. Know when *not* to use a framework.

**Why it matters:** Frameworks speed up the plumbing. Anthropic warns that they "create extra layers of abstraction that can obscure the underlying prompts and responses" and suggests starting with the LLM APIs directly. Learn one framework deeply, and learn MCP, because MCP is how tools are increasingly plugged into agents.

**Resources**
| Resource | Type | Notes |
|---|---|---|
| [LangGraph overview (LangChain docs)](https://docs.langchain.com/oss/python/langgraph/overview) | Free (open source) | Stateful, graph-based agent orchestration. |
| [DeepLearning.AI – AI Agents in LangGraph](https://www.deeplearning.ai/courses/ai-agents-in-langgraph/) | Free short course | |
| [LlamaIndex framework](https://developers.llamaindex.ai/python/framework/) | Free (open source) | Strong for data- and RAG-centric agents. |
| [AutoGen (Microsoft)](https://microsoft.github.io/autogen/stable/) | Free (open source) | AgentChat for conversational single- and multi-agent apps; Core for event-driven, scalable systems; Studio is a no-code UI; extensions include an MCP workbench. |
| [CrewAI docs](https://docs.crewai.com/) | Free OSS (Enterprise tier exists) | Agents, crews, flows, guardrails, memory. |
| [DeepLearning.AI – Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/courses/multi-ai-agent-systems-with-crewai/) | Free short course | |
| [OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/) | Free, open source (MIT); model API usage billed per token | Agents, handoffs/agents-as-tools, guardrails, sessions, MCP tool calling, built-in tracing. `pip install openai-agents`. |
| [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) | Free open standard | "Like a USB-C port for AI applications". Build servers and clients. |
| [Hugging Face MCP Course](https://huggingface.co/learn/mcp-course) | Free | |
| [DeepLearning.AI short courses catalog](https://www.deeplearning.ai/courses/) | Free | Many 1–2 hr framework-specific courses. |

**Hands-on projects**
1. Re-implement your Stage 7 research agent in LangGraph and in the OpenAI Agents SDK. Compare lines of code, debuggability and traces.
2. Build an MCP server that exposes your own tools (e.g. notes or a database) and connect it to an MCP-capable client.
3. Build a CrewAI or AutoGen multi-agent crew for a content pipeline, with a human-approval step.

**Time estimate (estimate):** 1–2 months. Go deep on one framework and survey the rest.

---

## Stage 9 — Evaluation and safety

**Key concepts**
- *Evaluation:* task success rates, trajectory/step-level evals, tool-call accuracy, LLM-as-judge (and its limits), human evals, regression suites, cost and latency budgets, observability/tracing.
- *Safety and security:* the OWASP Top 10 for LLMs (2025): LLM01 prompt injection (direct and indirect), LLM02 sensitive information disclosure, LLM03 supply chain, LLM04 data and model poisoning, LLM05 improper output handling, LLM06 excessive agency, LLM07 system prompt leakage, LLM08 vector and embedding weaknesses, LLM09 misinformation, LLM10 unbounded consumption. Also: least privilege, sandboxing, human approval for irreversible actions, guardrails.

**Why it matters:** Agents compound errors across steps and take real actions. Anthropic notes "higher costs, and the potential for compounding errors" and recommends "extensive testing in sandboxed environments." Weng cites ChemCrow, where LLM-based evaluation rated the systems as roughly equal but expert human evaluation strongly preferred ChemCrow. That is a warning about relying blindly on LLM judges.

**Resources**
| Resource | Type | Notes |
|---|---|---|
| [OWASP Top 10 for LLM & GenAI Apps (2025)](https://genai.owasp.org/llm-top-10/) | Free | Threat model checklist. |
| [Inspect (UK AI Security Institute)](https://inspect.aisi.org.uk/) | Free (open source) | Framework for LLM and agent evaluations. |
| [Ragas](https://docs.ragas.io/en/stable/) | Free (open source) | RAG and LLM app evaluation metrics. |
| [Langfuse docs](https://langfuse.com/docs) | Free OSS / paid cloud | Open-source tracing, evals and prompt management. |
| [Hugging Face Agents Course – Bonus Unit 2: Agent Observability & Evaluation](https://huggingface.co/learn/agents-course) | Free | |
| [AI Engineering (Huyen), Ch. 3–4 & 10](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) | Paid | Evaluation methodology, AI-as-a-judge, guardrails, monitoring. |

**Hands-on projects**
1. Build an eval harness for your agent: 50+ tasks with pass/fail checks, cost and latency tracking, run in CI on every prompt change.
2. Run an indirect-prompt-injection test: plant malicious instructions in a document your RAG agent retrieves, then add defenses and measure again.
3. Implement least-privilege tools plus a human-approval gate for destructive actions, and record "excessive agency" test cases.

**Time estimate (estimate):** 3–6 weeks, then continuous.

---

## Stage 10 — Deploying real agents

**Key concepts:** serving agents behind an API (FastAPI), containerization (Docker), async/streaming responses, durable state and resumable runs, queues for long-running tasks, secrets management, rate limiting and cost caps (OWASP LLM10), model routing and caching, tracing and monitoring in production, user feedback loops, versioning prompts, tools and models.

**Why it matters:** A demo agent and a production agent are very different things. Huyen's AI Engineering, Ch. 10, lays out a production architecture: enhance context, add guardrails, add a model router and gateway, cache to cut latency, add agent patterns, then monitoring/observability and user feedback.

**Resources**
| Resource | Type | Notes |
|---|---|---|
| [FastAPI docs](https://fastapi.tiangolo.com/) | Free | Python API framework for serving agents. |
| [Docker – Get started](https://docs.docker.com/get-started/) | Free | Containerize and ship. |
| [OpenAI Agents SDK – sessions, tracing, human-in-the-loop, sandbox agents](https://openai.github.io/openai-agents-python/) | Free, open source (MIT); model API usage billed per token | Production-oriented runtime features. |
| [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) | Free | Durable, stateful orchestration. |
| [Langfuse](https://langfuse.com/docs) | Free OSS / paid cloud | Production tracing and monitoring. |
| [AI Engineering (Huyen), Ch. 9–10](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) | Paid | Inference optimization, architecture, monitoring, user feedback. |

**Hands-on projects (capstones)**
1. **Customer-support agent:** RAG over a knowledge base, tools for order lookup and refund *requests* gated by human approval, an eval suite, deployed with FastAPI + Docker, with tracing and per-conversation cost caps. Anthropic names customer support as a strong agent use case.
2. **Coding/ops agent in a sandbox:** reads the repo, runs tests and proposes patches as PRs (never pushing directly), with test pass rate as the eval. Anthropic's other highlighted use case is coding agents.
3. **MCP-powered personal assistant:** connects to 2–3 MCP servers, with memory, a scheduled background job, and a dashboard of traces and evals.

**Time estimate (estimate):** 1–2 months for a first production-grade capstone. Mastery comes from shipping and iterating.

---

## Suggested pacing summary (all estimates)

| Stage | Estimate |
|---|---|
| 1. Foundations | 2–4 months |
| 2. Deep learning | 1.5–3 months |
| 3. LLMs & transformers | 1.5–2.5 months |
| 4. Prompt engineering | 2–4 weeks |
| 5. RAG | 3–5 weeks |
| 6. Tool use | 2–4 weeks |
| 7. Agent architectures | 1–2 months |
| 8. Frameworks & MCP | 1–2 months |
| 9. Evaluation & safety | 3–6 weeks |
| 10. Deployment | 1–2 months |

*Total (estimate): ~10–20 months sequential; ~11–23 months with Stage 0.*


---

## Sources

All links were checked on 16 Oct 2026. The facts quoted above come from these pages.

1. 3Blue1Brown – Linear Algebra: https://www.3blue1brown.com/?topic=linear-algebra
2. 3Blue1Brown – Neural Networks: https://www.3blue1brown.com/?topic=neural-networks
3. Python Tutorial (official): https://docs.python.org/3/tutorial/
4. Kaggle Learn: https://www.kaggle.com/learn
5. Coursera – Mathematics for ML and Data Science Specialization: https://www.coursera.org/specializations/mathematics-for-machine-learning-and-data-science
6. Coursera – Machine Learning Specialization: https://www.coursera.org/specializations/machine-learning-introduction
7. Goodfellow, Bengio, Courville – Deep Learning: https://www.deeplearningbook.org/
8. fast.ai – Practical Deep Learning for Coders: https://course.fast.ai/
9. Karpathy – Neural Networks: Zero to Hero: https://karpathy.ai/zero-to-hero.html
10. Dive into Deep Learning: https://d2l.ai/
11. Vaswani et al. – Attention Is All You Need: https://arxiv.org/abs/1706.03762
12. Jay Alammar – The Illustrated Transformer: https://jalammar.github.io/illustrated-transformer/
13. Hugging Face LLM Course: https://huggingface.co/learn/llm-course
14. Stanford CS224N: https://web.stanford.edu/class/cs224n/
15. Chip Huyen – AI Engineering (O'Reilly, 2024): https://www.oreilly.com/library/view/ai-engineering/9781098166298/
16. DAIR.AI Prompt Engineering Guide: https://www.promptingguide.ai/
17. Anthropic – Prompt engineering overview: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
18. Anthropic courses (GitHub): https://github.com/anthropics/courses
19. Lewis et al. – Retrieval-Augmented Generation: https://arxiv.org/abs/2005.11401
20. Sentence Transformers: https://www.sbert.net/
21. LlamaIndex framework docs: https://developers.llamaindex.ai/python/framework/
22. Ragas: https://docs.ragas.io/en/stable/
23. OpenAI – Function calling guide: https://developers.openai.com/api/docs/guides/function-calling
24. Anthropic – Writing effective tools for AI agents: https://www.anthropic.com/engineering/writing-tools-for-agents
25. Anthropic – Building effective agents: https://www.anthropic.com/engineering/building-effective-agents
26. Lilian Weng – LLM Powered Autonomous Agents: https://lilianweng.github.io/posts/2023-06-23-agent/
27. Yao et al. – ReAct: https://arxiv.org/abs/2210.03629
28. Hugging Face AI Agents Course: https://huggingface.co/learn/agents-course
29. LangGraph overview: https://docs.langchain.com/oss/python/langgraph/overview
30. DeepLearning.AI – AI Agents in LangGraph: https://www.deeplearning.ai/courses/ai-agents-in-langgraph/
31. AutoGen: https://microsoft.github.io/autogen/stable/
32. CrewAI docs: https://docs.crewai.com/
33. DeepLearning.AI – Multi AI Agent Systems with crewAI: https://www.deeplearning.ai/courses/multi-ai-agent-systems-with-crewai/
34. OpenAI Agents SDK: https://openai.github.io/openai-agents-python/
35. Model Context Protocol: https://modelcontextprotocol.io/
36. Hugging Face MCP Course: https://huggingface.co/learn/mcp-course
37. DeepLearning.AI short courses: https://www.deeplearning.ai/courses/
38. OWASP Top 10 for LLM & GenAI (2025): https://genai.owasp.org/llm-top-10/
39. Inspect (UK AISI): https://inspect.aisi.org.uk/
40. Langfuse docs: https://langfuse.com/docs
41. FastAPI: https://fastapi.tiangolo.com/
42. Docker – Get started: https://docs.docker.com/get-started/

*Removed during checking:* O'Reilly's "Hands-On Machine Learning" page (returned 403, content not confirmed) and Coursera's Deep Learning Specialization page (returned 200, but the content couldn't be confirmed).
