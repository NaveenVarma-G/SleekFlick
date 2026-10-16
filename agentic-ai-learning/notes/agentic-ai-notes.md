# Study Notes: Learning AI from Scratch to Building Agentic AI

*College-grade study notes based on Lucy's research file "Learning AI from scratch to mastery in building agentic AI" (compiled 16 Oct 2026) and her research addendum (sources checked 16 Oct 2026). Every fact below comes from those two files. Where the research is still thin or unclear, a note marked **Gap** says so.*

---

## Overview

These notes follow a cumulative learning path: an optional on-ramp (Stage 0) for people who have never programmed, then 10 stages. It runs from programming, mathematical and ML foundations, through deep learning and large language models (LLMs), to designing, evaluating, securing and deploying agentic AI systems.

| Stage | Topic | Estimated time |
|---|---|---|
| 0 | Programming from zero (only if you have never programmed) | 1–3 months |
| 1 | Foundations: math, Python, ML basics | 2–4 months |
| 2 | Deep learning | 1.5–3 months |
| 3 | LLMs and transformers | 1.5–2.5 months |
| 4 | Prompt engineering | 2–4 weeks |
| 5 | Retrieval-Augmented Generation (RAG) | 3–5 weeks |
| 6 | Tool use and function calling | 2–4 weeks |
| 7 | Agent architectures: planning, memory, multi-agent | 1–2 months |
| 8 | Frameworks and protocols | 1–2 months |
| 9 | Evaluation and safety | 3–6 weeks |
| 10 | Deploying real agents | 1–2 months |

**Ground rules from the research and addendum**

- **Time figures:** all time estimates are rough *estimates*, assuming roughly **8–10 hours/week**, unless they are marked as the provider's own figure.
- **Total path (estimate):** about **10–20 months** if you do Stages 1–10 one after another at 8–10 hrs/week, or about **11–23 months** including Stage 0. Because Stages 4–10 overlap, you may finish sooner, but the addendum has no source for how much sooner, so it doesn't state a shorter total. (This corrects the original figure of ~9–15 months.)
- **Where to start:** the addendum's prerequisite check (editorial) says to skip Stage 0 if you can already write a short program that loops over a list, uses `if`/`else`, defines functions and reads a file. Otherwise, start at Stage 0.
- **"Editorial":** items marked *(editorial)* are Lucy's own suggestions or reasoning in the addendum, not statements taken from a source.
- **Overlap:** the path is cumulative, but **Stages 4–10 overlap heavily in practice**. Start building small agents early instead of waiting for "mastery" of the earlier stages.
- **Links:** every link in the research and the addendum was checked on **16 Oct 2026**. Links whose content couldn't be confirmed were removed.
- **"Paid":** this means the resource costs money. Prices are not quoted because they change, so check the provider page.

**How the corrected total is calculated (from the addendum)**

| | Minimum | Maximum |
|---|---|---|
| Month-based stages (1, 2, 3, 7, 8, 10) | 2 + 1.5 + 1.5 + 1 + 1 + 1 = **8 mo** | 4 + 3 + 2.5 + 2 + 2 + 2 = **15.5 mo** |
| Week-based stages (4, 5, 6, 9) | 2 + 3 + 2 + 3 = **10 wk ≈ 2.3 mo** | 4 + 5 + 4 + 6 = **19 wk ≈ 4.4 mo** |
| **Done strictly one after another** | **≈ 10.3 mo** | **≈ 19.9 mo** |
| **Plus Stage 0 (1–3 months)** | **≈ 11.3 mo** | **≈ 22.9 mo** |

> **Gap:** The addendum gives a recommended order for resources within Stage 0 only. For Stages 1–10, neither the research nor the addendum says which resource to take first.

---

## Stage 0 — Programming from Zero

*Added by the addendum. Who it's for: anyone who has never written code. Use the prerequisite check in the Overview to decide whether to skip it.*

### 0.1 Key concepts and definitions

**Programming topics (from the CS50P course description)**
- Functions, variables, conditionals, loops, exceptions, debugging, unit tests, libraries, regular expressions, classes and file I/O.

**Prerequisite skills (the editorial skip test)**
- Writing a short program that loops over a list, uses `if`/`else`, defines functions and reads a file.

> **Gap:** The addendum lists these topics but defines none of them. A beginner learns what each one means from the Stage 0 resources themselves.

### 0.2 Explanation

Stage 0 fills a hole in the original path. Stage 1's main Python resource, the official Python Tutorial, is written for people who already program. Python.org's wiki has a separate page for newcomers: "If you've never programmed before, the tutorials on this page are recommended for you; they don't assume that you have previous experience."

Stage 0 builds the core programming skills that every later stage assumes. Kaggle Learn's Python and pandas courses then serve as a short bridge into Stage 1's data and ML work.

### 0.3 Important facts, dates and figures

- **Time estimate:** 1–3 months *(estimate)*. The addendum found no provider-stated duration for CS50P.
- **CS50's Introduction to Programming with Python (CS50P)**, by Harvard's David J. Malan:
  - "Designed for students with or without prior programming experience."
  - "No software required except for a web browser."
  - Free as OpenCourseWare, with a paid verified certificate offered.
- **Automate the Boring Stuff with Python** (Al Sweigart) is free to read under a Creative Commons license, with a paid print copy. The Python wiki describes it as "Practical Programming for Total Beginners."
- **The Python wiki** notes that the wiki is being archived.

**Recommended order within Stage 0 (editorial)**
1. CS50P, for structured lessons and problem sets.
2. Automate the Boring Stuff, for practical projects.
3. The Kaggle Python and pandas courses.
4. Then the official Python Tutorial (Stage 1) as a reference.

### 0.4 Examples (hands-on projects, editorial)

1. A file-renaming script.
2. A CSV summary tool.
3. A tiny text-adventure game using functions and classes.

### 0.5 Recommended resources

| Resource | Type | What the source says |
|---|---|---|
| [Python wiki – "Python for New Programmers" (BeginnersGuide/NonProgrammers)](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers) | Free | "If you've never programmed before, the tutorials on this page are recommended for you; they don't assume that you have previous experience." The page notes the wiki is being archived. Python.org points to this page in contrast to its Programmers page; the official Tutorial is for people who already program. |
| [CS50's Introduction to Programming with Python (Harvard, David J. Malan)](https://cs50.harvard.edu/python/) | Free (OpenCourseWare); paid verified certificate offered | "Designed for students with or without prior programming experience." Covers functions, variables, conditionals, loops, exceptions, debugging, unit tests, libraries, regular expressions, classes and file I/O. "No software required except for a web browser." |
| [Automate the Boring Stuff with Python (Al Sweigart)](https://automatetheboringstuff.com/) | Free to read under a Creative Commons license; print copy paid | The Python wiki above describes it as "Practical Programming for Total Beginners." |
| [Kaggle Learn – Python micro-course](https://www.kaggle.com/learn) | Free | Already in the original path. Good as a short bridge into pandas and ML. |

---

## Stage 1 — Foundations: Math, Python and ML Basics

### 1.1 Key concepts and definitions

**Linear algebra**
- Vectors, matrices, dot products, matrix multiplication, linear transformations, eigenvalues/eigenvectors, PCA.

**Calculus**
- Derivatives, partial derivatives, gradients, the chain rule, gradient descent.

**Probability and statistics**
- Distributions (binomial, Gaussian), expectation, Bayes' rule, MLE/MAP, hypothesis testing.

**Python**
- Data structures, functions, classes, modules, exceptions, virtual environments/pip, JSON, NumPy/pandas.

**Machine learning (ML) basics**
- Supervised vs. unsupervised learning; linear and logistic regression; train/dev/test splits; over/underfitting; decision trees and ensembles; evaluation metrics.

**Definitions from the addendum**

| Term | Definition (source) |
|---|---|
| **PCA (principal component analysis)** | "A linear dimensionality reduction technique with applications in exploratory data analysis, visualization and data preprocessing." (Wikipedia) |
| **MLE (maximum likelihood estimation)** | "A method of estimating the parameters of an assumed probability distribution, given some observed data… by maximizing a likelihood function." (Wikipedia) |
| **MAP (maximum a posteriori) estimate** | "The mode of the posterior density… employs an augmented optimization objective which incorporates a prior… MAP estimation is therefore a regularization of maximum likelihood estimation." (Wikipedia) |
| **Precision / recall** | "Performance metrics that apply to data retrieved from a collection, corpus or sample space." (Wikipedia) |

> **Gap:** The other Stage 1 terms (for example vectors, eigenvalues and Bayes' rule) still have no sourced definitions. The addendum points to the 3Blue1Brown and Coursera math resources in this stage, which cover these topics.

### 1.2 Explanation

The research gives four reasons this foundation matters for agentic AI:

1. **Linear algebra underlies representation and search.** Embeddings, attention and similarity search are all linear algebra.
2. **Calculus underlies learning.** Training a model is calculus plus optimization.
3. **Probability underlies model outputs.** An LLM's output is a probability distribution over tokens.
4. **Python is the working language.** Almost every agent framework and LLM SDK is Python-first.

Without this base, you can't debug or evaluate these systems well.

### 1.3 Important facts, dates and figures

- **Time estimate:** 2–4 months, or less if you already code in Python.
- **Mathematics for Machine Learning and Data Science Specialization:** the provider says "12 weeks … at 5 hours a week."
- **Machine Learning Specialization (Andrew Ng):** beginner level, 3 courses, using NumPy, scikit-learn and TensorFlow. The provider says "2 months at 10 hours a week."
- **Deep Learning book, Part I:** Chapters 2–5 cover linear algebra, probability, numerical computation and ML basics, at a rigorous level.
- **The Python Tutorial (official docs):** the docs say it is aimed at people who already program but are new to Python.

**If you have never programmed:** the official Python Tutorial targets people who already program. Do Stage 0 first; its resources are written for complete beginners.

### 1.4 Examples (hands-on projects)

1. Implement linear regression with gradient descent in pure NumPy, then check it against scikit-learn.
2. Do a PCA on a small dataset from scratch (eigendecomposition) and plot the result.
3. Build a CLI Python app that reads a CSV or JSON file, cleans it with pandas, and trains a classifier. Report precision, recall and F1.

### 1.5 Recommended resources

| Resource | Type | Notes |
|---|---|---|
| [3Blue1Brown – Linear Algebra (Essence of LA)](https://www.3blue1brown.com/?topic=linear-algebra) | Free | Visual intuition for vectors and transformations. |
| [The Python Tutorial (official docs)](https://docs.python.org/3/tutorial/) | Free | The docs say it is aimed at people who already program but are new to Python. It covers control flow, data structures, classes, venv/pip. |
| [Kaggle Learn](https://www.kaggle.com/learn) | Free | Short, hands-on micro-courses (Python, pandas, intro ML). |
| [Mathematics for Machine Learning and Data Science Specialization (DeepLearning.AI / Coursera)](https://www.coursera.org/specializations/mathematics-for-machine-learning-and-data-science) | Paid (financial aid available) | Linear algebra, calculus, probability and statistics, with Python labs. Provider figure: "12 weeks … at 5 hours a week." |
| [Machine Learning Specialization (Andrew Ng, DeepLearning.AI + Stanford Online / Coursera)](https://www.coursera.org/specializations/machine-learning-introduction) | Paid (financial aid available) | Beginner level, 3 courses, NumPy/scikit-learn/TensorFlow. Provider figure: "2 months at 10 hours a week." |
| [Deep Learning book, Part I (Goodfellow, Bengio, Courville)](https://www.deeplearningbook.org/) | Free online (print edition paid) | Chapters 2–5 cover linear algebra, probability, numerical computation and ML basics, all at a rigorous level. |

**Replacements for removed resources (from the addendum).** Two resources were removed during link checking: O'Reilly's "Hands-On Machine Learning" page (it returned 403) and Coursera's Deep Learning Specialization page (its content couldn't be confirmed). Two already-verified free resources fill their roles:
- **Instead of *Hands-On Machine Learning*:** [Dive into Deep Learning](https://d2l.ai/), a free interactive book with code (page title confirmed: "Dive into Deep Learning 1.0.3 documentation"), plus Kaggle Learn.
- **Instead of the Coursera Deep Learning Specialization:** fast.ai's [Practical Deep Learning for Coders](https://course.fast.ai/) (free, 9 lessons of about 90 minutes each).

The addendum adds no paid replacement because Lucy couldn't confirm one.

---

## Stage 2 — Deep Learning

### 2.1 Key concepts and definitions

**Network building blocks**
- Neurons and MLPs; activation functions.

**Training mechanics**
- Backpropagation; loss functions (cross-entropy); SGD/Adam; regularization (weight decay, dropout).

**Architectures and representations**
- CNNs and RNNs (studied "for context"); embeddings; transfer learning.

**Tooling**
- PyTorch tensors and training loops.

**Definitions from the addendum**

| Term | Definition (source) |
|---|---|
| **MLP (multilayer perceptron)** | "A kind of modern feedforward neural network consisting of fully connected neurons with nonlinear activation functions, organized in layers." (Wikipedia) |
| **SGD (stochastic gradient descent)** | "An iterative method for optimizing an objective function… replaces the actual gradient by an estimate thereof, calculated from a randomly selected subset of the data." (Wikipedia) |
| **CNN (convolutional neural network)** | "A type of feedforward neural network that learns features via filter optimization… the de-facto standard… [for] computer vision… only recently replaced—in some cases—by… the transformer." (Wikipedia) |
| **RNN (recurrent neural network)** | "Designed for processing sequential data… the output of a neuron at one time step is fed back as input… at the next time step." (Wikipedia) |

**What "for context" means (editorial):** CNNs and RNNs are background for understanding why transformers replaced earlier designs. You don't need to master them for agent work.

### 2.2 Explanation

LLMs are deep neural networks. Once you understand how training, loss and backpropagation work, you can reason about:

- fine-tuning,
- embeddings,
- tokenization quirks, and
- model behaviour.

### 2.3 Important facts, dates and figures

- **Time estimate:** 1.5–3 months.
- **fast.ai – Practical Deep Learning for Coders:** 9 lessons of about 90 minutes each, using PyTorch, fastai, Hugging Face Transformers and Gradio. Prerequisite, quoted from the site: "The only prerequisite is that you know how to code (a year of experience is enough), preferably in Python, and that you have at least followed a high school math course." (At about 9 × 90 minutes, that is roughly 13.5 hours of lessons, not counting practice.)

- **Karpathy – Neural Networks: Zero to Hero:** builds backprop (micrograd) and then language models up to GPT, from scratch in code.
- **Takeaway for beginners (addendum):** fast.ai expects some coding experience, so a non-coder should do Stage 0/Stage 1 first.
- **Deep Learning book, Part II:** a theory reference for feedforward nets, regularization, optimization and CNNs/RNNs.

### 2.4 Examples (hands-on projects)

1. Build micrograd following Karpathy, then train a tiny MLP with it.
2. Fine-tune a pretrained image or text classifier (fast.ai lessons 1–2) and deploy it as a Gradio demo.
3. Write a full PyTorch training loop by hand, with a validation split and early stopping.

### 2.5 Recommended resources

| Resource | Type | Notes |
|---|---|---|
| [fast.ai – Practical Deep Learning for Coders](https://course.fast.ai/) | Free | 9 lessons of about 90 minutes each, using PyTorch, fastai, Hugging Face Transformers and Gradio. Prerequisite, quoted from the site: "The only prerequisite is that you know how to code (a year of experience is enough), preferably in Python, and that you have at least followed a high school math course." |
| [Andrej Karpathy – Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) | Free | Builds backprop (micrograd) and then language models up to GPT, from scratch in code. |
| [3Blue1Brown – Neural Networks](https://www.3blue1brown.com/?topic=neural-networks) | Free | Visual intuition for backprop and, later, transformers. |
| [Dive into Deep Learning (d2l.ai)](https://d2l.ai/) | Free | Interactive book with runnable code. |
| [Deep Learning book, Part II](https://www.deeplearningbook.org/) | Free online | Theory reference for feedforward nets, regularization, optimization and CNNs/RNNs. |

**Tools and techniques used in the projects (from the addendum)**
- **micrograd:** "A tiny Autograd engine… Implements backpropagation (reverse-mode autodiff) over a dynamically built DAG and a small neural networks library on top of it with a PyTorch-like API… about 100 and 50 lines of code respectively." (GitHub: karpathy/micrograd)
- **Early stopping:** "A form of regularization used to avoid overfitting when training a model with an iterative method, such as gradient descent… rules provide guidance as to how many iterations can be run before the learner begins to over-fit." (Wikipedia)
- **Gradio:** "An open-source Python package that allows you to quickly build a demo or web application for your machine learning model, API, or any arbitrary Python function… No JavaScript, CSS, or web hosting experience needed!" (Gradio Quickstart)

---

## Stage 3 — LLMs and Transformers

### 3.1 Key concepts and definitions

**Input representation**
- Tokenization; embeddings; positional encoding.

**The transformer mechanism**
- Self-attention (Q/K/V); multi-head attention.

**Architecture families**
- Encoder vs. decoder vs. encoder–decoder.

**Generation**
- Next-token prediction; sampling (temperature, top-p); context windows.

**Training stages and adaptation**
- Pretraining vs. post-training (SFT, preference tuning); fine-tuning and PEFT/LoRA.

**Ecosystem**
- The Hugging Face ecosystem (Transformers, Datasets, Tokenizers).

**Definitions from the addendum**
- **Q/K/V (query, key, value):** for each word, self-attention creates "a Query vector, a Key vector, and a Value vector… by multiplying the embedding by three matrices that we trained."
  - Each score is "the dot product of the query vector with the key vector."
  - The scores are divided by √d_k and passed through a softmax.
  - The softmax weights the value vectors, which are then summed. (The Illustrated Transformer)
- **Fine-tuning:** "Adapting a computational model trained for one task to perform a different, usually more specific, task… a form of transfer learning." (Wikipedia)
- **PEFT (Parameter-Efficient Fine-Tuning):** "A library for efficiently adapting large pretrained models… without fine-tuning all of a model's parameters… PEFT methods only fine-tune a small number of (extra) model parameters." (Hugging Face PEFT docs)
- **LoRA (Low-Rank Adaptation):** "Freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters." (Hu et al., arXiv 2106.09685)
- **SFT (supervised fine-tuning) and preference tuning:** *AI Engineering* lists "Supervised Finetuning" and "Preference Finetuning" under Post-Training in Chapter 2 (table of contents).
- **Temperature and top-p:** listed under "Sampling Strategies" in *AI Engineering* Chapter 2 (table of contents).

> **Gap:** There's still no sourced explanation of how temperature and top-p change a model's output. SFT and preference finetuning are only named in a table of contents, with no checked definition.

### 3.2 Explanation

The research calls the LLM the **"brain" of every agent**. An LLM's strengths and limits shape every design decision you make later, especially:

- **context windows**, which limit how much the model can take in at once;
- **hallucination**; and
- **how reliably the model produces structured output.**

### 3.3 Important facts, dates and figures

- **2017:** Vaswani et al. published *Attention Is All You Need*, the original Transformer paper.
- **Dec 2024:** Chip Huyen's *AI Engineering* (O'Reilly) was published. Chapter 2 covers foundation models (sampling, post-training, structured outputs). This book comes up again in later stages.
- **Hugging Face LLM Course:** covers Transformers, Datasets and Tokenizers, then fine-tuning and reasoning models. The provider says each chapter takes about 1 week at 6–8 hrs. Prerequisite (course page): it "Requires a good knowledge of Python" and "Is better taken after an introductory deep learning course".
- **Time estimate:** 1.5–2.5 months.

- **Hugging Face LLM Course length:** the course page describes Chapters 1–4, 5–8, 9 and 10–12, so there are **12 chapters**. At the provider's figure of about 1 week per chapter at 6–8 hrs/week, that works out to about **12 weeks, or roughly 72–96 hours** (the addendum's arithmetic).

### 3.4 Examples (hands-on projects)

1. Implement a single self-attention head and a tiny character-level GPT, following Karpathy.
2. Load an open model with Hugging Face `transformers`, compare greedy decoding with temperature/top-p sampling, and look at the tokenization.
3. LoRA fine-tune a small model on a narrow task and compare it with prompting alone.

### 3.5 Recommended resources

| Resource | Type | Notes |
|---|---|---|
| [Attention Is All You Need (Vaswani et al., 2017)](https://arxiv.org/abs/1706.03762) | Free paper | The original Transformer paper. |
| [The Illustrated Transformer (Jay Alammar)](https://jalammar.github.io/illustrated-transformer/) | Free | Step-by-step visual walkthrough of self-attention, multi-head attention, positional encoding and the decoder. |
| [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) | Free | Transformers, Datasets and Tokenizers, then fine-tuning and reasoning models. Provider figure: each chapter is about 1 week at 6–8 hrs. Prerequisite (course page): it "Requires a good knowledge of Python" and "Is better taken after an introductory deep learning course". |
| [Stanford CS224N – NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) | Free materials | University-level NLP and deep learning course. |
| [Karpathy – Zero to Hero (GPT lectures)](https://karpathy.ai/zero-to-hero.html) | Free | Builds a GPT-style model from scratch. |
| [AI Engineering – Chip Huyen (O'Reilly, Dec 2024)](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) | Paid book | Ch. 2 covers foundation models (sampling, post-training, structured outputs). This book is used again in later stages. |

---

## Stage 4 — Prompt Engineering

### 4.1 Key concepts and definitions

**Prompt structure**
- Clear instructions; system vs. user prompts; role prompting.

**Prompting techniques**
- Zero-shot and few-shot prompting; chain-of-thought / "time to think"; structured output (XML or JSON); prompt chaining.

**Engineering discipline**
- Building evals *before* you optimize; prompt versioning.

**Security**
- Defensive prompting against injection.

**Definitions from the addendum**
- **Zero-shot vs. few-shot:** zero-shot gives no examples; few-shot gives a few worked examples in the prompt. *AI Engineering* Chapter 5 groups both under "In-Context Learning: Zero-Shot and Few-Shot."
- **Standard few-shot (from the ReAct paper's prompt appendix):** question–answer exemplars only.
- **Chain-of-thought (from the same appendix):** exemplars that include "Let's think step by step" reasoning before the answer.
- **"Time to think":** *AI Engineering* Chapter 5 covers this under "Give the Model Time to Think" (table of contents).
- The DAIR.AI Prompt Engineering Guide and Anthropic's prompt engineering overview cover these techniques in more depth.

### 4.2 Explanation

**Prompts are code.** In an agent, the system prompt and the tool descriptions *are* the program.

**Measure first.** Anthropic's prompt-engineering guide recommends defining success criteria, and a way to test against them, *before* you start prompt engineering. This is why "building evals before you optimize" is on the concept list.

### 4.3 Important facts, dates and figures

- **Time estimate:** 2–4 weeks, then ongoing practice.
- **Anthropic's prompt engineering overview** links to best practices, a metaprompt generator and interactive tutorials.
- **Huyen's *AI Engineering*, Ch. 5,** covers prompting best practices, defensive prompt engineering, jailbreaking and prompt injection.

### 4.4 Examples (hands-on projects)

1. Build a small eval set (20–50 cases) for an extraction task. Iterate on the prompt and track the score for each prompt version.
2. Get structured JSON out reliably and validate it with Pydantic.
3. Red-team your own prompt with injection attempts and document what defenses you added.

### 4.5 Recommended resources

| Resource | Type | Notes |
|---|---|---|
| [Prompt Engineering Guide (DAIR.AI)](https://www.promptingguide.ai/) | Free | Techniques, papers, model-specific guides. |
| [Anthropic – Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) | Free | Links to best practices, a metaprompt generator, and interactive tutorials. |
| [Anthropic courses (GitHub)](https://github.com/anthropics/courses) | Free | Anthropic's educational notebooks, including the prompt-engineering tutorial. |
| [AI Engineering (Huyen), Ch. 5](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) | Paid | Prompting best practices, defensive prompt engineering, jailbreaking and prompt injection. |

**Tools and practices used in the projects (from the addendum)**
- **Pydantic:** "The most widely used data validation library for Python… Define how data should be in pure, canonical Python 3.10+; validate it with Pydantic." (Pydantic docs)
- **Red team:** "A group that simulates an adversary… then reports back so that the organization can improve their defenses." (Wikipedia) The OWASP GenAI Security Project also has an "AI Red Teaming" initiative, listed in its site menu.

---

## Stage 5 — Retrieval-Augmented Generation (RAG)

### 5.1 Key concepts and definitions

**Memory types**
- Parametric vs. non-parametric memory.

**Indexing**
- Chunking; embeddings; vector indexes and ANN search (HNSW, FAISS).

**Retrieval**
- BM25 and hybrid search; re-ranking; query rewriting.

**Generation quality**
- Citations/grounding.

**RAG evaluation**
- Retrieval recall; faithfulness; answer relevance.

**Definition given in the research**
- **RAG** lets a model use private or fresh knowledge without retraining.

**Definitions from the addendum**
- **Parametric vs. non-parametric memory:** the RAG paper calls the pre-trained seq2seq model "parametric memory." It calls the "dense vector index of Wikipedia, accessed with a pre-trained neural retriever" "non-parametric memory."
- **Chunking:** in the RAG paper, "Each Wikipedia article is split into disjoint 100-word chunks, to make a total of 21M documents."
- **Nearest-neighbour search and ANN (approximate nearest neighbour) search:**
  - Nearest-neighbour search means "finding the point in a given set that is closest to a given point" (Wikipedia).
  - ANN algorithms "return approximately top k nearest neighbors to trade off a little accuracy lost for a huge speedup" (Weng 2023).
- **HNSW:** "An algorithm for approximate nearest neighbor search" (Wikipedia). Weng says it "builds hierarchical layers of these small-world graphs… The layers in the middle create shortcuts to speed up search."
- **FAISS (Facebook AI Similarity Search):** "applies vector quantization by partitioning the vector space into clusters and then refining the quantization within clusters" (Weng). The RAG paper built its index "using FAISS… with a Hierarchical Navigable Small World approximation."
- **BM25:** "A ranking function used by search engines to estimate the relevance of documents to a given search query," based on the probabilistic retrieval framework of Robertson, Spärck Jones and others (Wikipedia). The RAG paper calls it a "word overlap-based BM25 retriever."
- **Hybrid search (editorial):** combining sparse/keyword retrieval (BM25) with dense/embedding retrieval.
- **recall@k (editorial, following the Wikipedia precision/recall entry):** the share of the relevant documents that appear in the top *k* results.
- **Faithfulness and answer relevance:** these are Ragas metrics.

> **Gap:** Only the Ragas landing page was checked, so the notes give no exact formulas for faithfulness or answer relevance.

### 5.2 Explanation

RAG solves a practical problem: it gives a model **private or fresh knowledge without retraining it**. The original RAG paper showed that **swapping the retrieval index updates what the model knows**.

The same pieces matter later. Agent "long-term memory" is usually built from the same components (embeddings, vector stores, retrieval), which connects Stage 5 directly to Stage 7.

### 5.3 Important facts, dates and figures

- **2020:** Lewis et al. published "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks," the paper that introduced RAG.
- **RAG paper details (from the addendum):**
  - Wikipedia was split into 100-word chunks, giving 21M documents.
  - The index was built with FAISS using an HNSW approximation.
  - In its comparison of BM25 and dense retrieval, each won on different tasks; BM25 was best on FEVER.
- **LlamaIndex:** the framework docs are at `developers.llamaindex.ai`. The old URL `docs.llamaindex.ai/en/stable/` still resolves.
- **Ragas:** a library for evaluating RAG and LLM apps. It is used again in Stage 9.
- **Huyen's *AI Engineering*, Ch. 6,** covers RAG architecture, retrieval algorithms and optimization.
- **Time estimate:** 3–5 weeks.

### 5.4 Examples (hands-on projects)

1. Build "chat with your docs" from scratch: chunk the docs, embed them, store them in FAISS or a vector DB, retrieve, and generate answers with citations.
2. Compare dense, BM25 and hybrid retrieval on 30 hand-labeled questions. Measure recall@k.
3. Add a re-ranker and run a Ragas-style faithfulness eval.

### 5.5 Recommended resources

| Resource | Type | Notes |
|---|---|---|
| [Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (2020)](https://arxiv.org/abs/2005.11401) | Free paper | The paper that introduced RAG. |
| [Sentence Transformers (SBERT) docs](https://www.sbert.net/) | Free | Computing embeddings and doing semantic search. |
| [LlamaIndex framework docs](https://developers.llamaindex.ai/python/framework/) | Free (open source) | Data and RAG-focused framework. The old URL `docs.llamaindex.ai/en/stable/` still resolves. |
| [Ragas docs](https://docs.ragas.io/en/stable/) | Free (open source) | Library for evaluating RAG and LLM apps. |
| [AI Engineering (Huyen), Ch. 6](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) | Paid | RAG architecture, retrieval algorithms and optimization. |

**Note on Huyen's Chapter 6:** the same chapter is cited here and in Stage 7, and that's correct. Chapter 6 is titled **"RAG and Agents"** and has sub-sections for both (O'Reilly table of contents).

---

## Stage 6 — Tool Use and Function Calling

### 6.1 Key concepts and definitions

**Defining tools**
- Tool and function definitions written with **JSON Schema**.

**The tool-calling loop (as defined in the research)**
- **request → tool call → execute → return output → final answer.**
- OpenAI's guide describes tool calling as a **multi-step conversation between your app and the model**.

**Controls**
- `tool_choice`; parallel tool calls; strict/structured outputs; error handling.

**Tool design**
- Designing good tools: the **"agent-computer interface" (ACI)**.
- **"Poka-yoke" tools:** mistake-proof tools (from Anthropic's "Building effective agents," Appendix 2).

**Details from the OpenAI function-calling guide (via the addendum)**
- **`tool_choice`** has five settings:
  - **Auto:** "Call zero, one, or multiple functions" (the default).
  - **Required:** "Call one or more functions."
  - **Forced:** call exactly one specific function.
  - **`allowed_tools`:** restrict calls to a subset.
  - **`none`:** imitates passing no functions.
- **Strict mode:** "Setting `strict` to `true` will ensure function calls reliably adhere to the function schema, instead of being best effort."
  - It requires `additionalProperties: false`, and every field must be listed as `required`.
  - You mark a field as optional by adding `null` as a type option.
- **JSON Schema:** "The vocabulary that enables JSON data consistency, validity, and interoperability" (json-schema.org). The OpenAI guide's `get_weather` example uses `type`, `properties`, `enum`, `required` and `additionalProperties`.

### 6.2 Explanation

Tools are what let an LLM ***act***, not just produce text. The model asks for a tool call, your application runs the tool and returns the output, and the model then writes its final answer. This is why the research calls the process a multi-step conversation rather than a single request.

Tool design deserves as much care as prompt design. Anthropic reports that while building its SWE-bench agent, it **spent more time optimizing tools than the overall prompt**.

### 6.3 Important facts, dates and figures

- **OpenAI's function calling guide** describes a **5-step** tool-calling flow, strict mode, `tool_choice`, parallel calls, and best practices. One of these is aiming for **fewer than 20 functions** available at once.
- **Anthropic's SWE-bench agent:** more effort went into tools than into the overall prompt.
- **Time estimate:** 2–4 weeks.

**Benchmarks and research named in this stage (from the addendum)**
- **SWE-bench (Jimenez et al., Oct 2023):** "An evaluation framework consisting of 2,294 software engineering problems drawn from real GitHub issues." Anthropic refers to "SWE-bench Verified" for agents that solve real GitHub issues.
- **Toolformer (Schick et al., Feb 2023):** "A model trained to decide which APIs to call, when to call them, what arguments to pass." In the authors' framing, LMs "can teach themselves to use external tools via simple APIs." (The addendum notes the abstract was truncated when it was checked.)
- **API-Bank (Li et al., Apr 2023):** "A benchmark… for tool-augmented LLMs."
  - Weng adds that it "contains 53 commonly used API tools… and 264 annotated dialogues that involve 568 API calls."
  - It evaluates at three levels: call, retrieve and plan.

### 6.4 Examples (hands-on projects)

1. Write a raw tool-calling loop with no framework, using 3 tools (calculator, web search, file read). Add retries and handle malformed arguments.
2. Build a "SQL analyst" that inspects the schema, writes queries, runs them read-only, and explains the results.
3. Measure tool-selection accuracy as you go from 3 to 20 tools. (This connects to OpenAI's advice to keep fewer than 20 functions available at once.)

### 6.5 Recommended resources

| Resource | Type | Notes |
|---|---|---|
| [OpenAI – Function calling guide](https://developers.openai.com/api/docs/guides/function-calling) | Free docs (API usage paid) | The 5-step tool-calling flow, strict mode, tool_choice, parallel calls, and best practices such as aiming for fewer than 20 functions available at once. |
| [Anthropic – Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | Free | How to design tools for agents. |
| [Anthropic – Building effective agents, Appendix 2 "Prompt engineering your tools"](https://www.anthropic.com/engineering/building-effective-agents) | Free | Covers ACI design and "poka-yoke" (mistake-proof) tools. |
| [Toolformer / API-Bank summaries in Lilian Weng's "LLM Powered Autonomous Agents"](https://lilianweng.github.io/posts/2023-06-23-agent/) | Free | Research background on tool-augmented LLMs. |

---

## Stage 7 — Agent Architectures: Planning, Memory, Multi-Agent

### 7.1 Key concepts and definitions

**Workflows vs. agents (Anthropic's distinction)**
- There are five workflow patterns:
  1. Prompt chaining
  2. Routing
  3. Parallelization
  4. Orchestrator–workers
  5. Evaluator–optimizer

**Planning**
- Task decomposition; CoT (chain-of-thought, see Stage 4); Tree of Thoughts.
- **ReAct:** the "reasoning + acting" paradigm, which **interleaves thought → action → observation**.
- Reflexion / self-reflection.

**Memory**
- **Short-term memory** = the context window.
- **Long-term memory** = a vector store (built from the RAG components in Stage 5).
- Memory streams, with retrieval scored by **recency, importance and relevance** (from Generative Agents).

**Multi-agent systems**
- Handoffs; manager/specialist structures; agents-as-tools.

**Control**
- Stopping conditions; human-in-the-loop checkpoints.

**Definitions from the addendum** (Anthropic, "Building effective agents," unless noted)
- **Workflows** are "systems where LLMs and tools are orchestrated through predefined code paths."
- **Agents** are "systems where LLMs dynamically direct their own processes and tool usage."
- **The five workflow patterns:**
  1. **Prompt chaining:** each LLM call processes the output of the previous one, with optional programmatic "gates."
  2. **Routing:** classify the input and send it to a specialized follow-up.
  3. **Parallelization:** either "sectioning" (independent subtasks) or "voting" (the same task run several times).
  4. **Orchestrator–workers:** a central LLM breaks down tasks dynamically, delegates them, and synthesizes the results.
  5. **Evaluator–optimizer:** one LLM generates and another evaluates and gives feedback, in a loop.
- **Tree of Thoughts** (Yao et al., May 2023): "Extends CoT by exploring multiple reasoning possibilities at each step… creating a tree structure," searched with BFS or DFS (Weng 2023).
- **Reflexion** (Shinn et al., Mar 2023): "A framework to equip agents with dynamic memory and self-reflection capabilities." Reflections are added to working memory, up to three of them (Weng).
- **Generative Agents** (Park et al., Apr 2023): 25 LLM-controlled characters live in a Sims-like sandbox.
  - A **memory stream** is "a long-term memory module (external database) that records a comprehensive list of agents' experience in natural language."
  - Retrieval scores memories by recency, importance and relevance.
  - A reflection step turns memories into higher-level inferences (Weng).

### 7.2 Explanation

Architecture decides an agent's **reliability, cost and latency**. Anthropic's guiding principle is **"finding the simplest solution possible, and only increasing complexity when needed."**

Lilian Weng identifies three core challenges for LLM agents:

1. **finite context**,
2. **long-horizon planning**, and
3. **the reliability of natural-language interfaces.**

The memory design follows a split: the context window holds short-term information, and a vector store holds long-term information, retrieved by recency, importance and relevance.

### 7.3 Important facts, dates and figures

- **2023:** Lilian Weng published "LLM Powered Autonomous Agents," a canonical survey of planning, memory and tool use.
- **Dec 2024:** Anthropic published "Building effective agents." The page itself notes that parts of the tooling landscape have changed since then.
- **ReAct (Yao et al.):** reports **absolute success-rate gains of 34% on ALFWorld and 10% on WebShop** over imitation/RL baselines.
- **Hugging Face AI Agents Course:** free, with a free certificate. It covers agent fundamentals, then smolagents / LlamaIndex / LangGraph, use cases and a final benchmark. The provider says it takes about **3–4 hrs/week per chapter**.
- **Huyen's *AI Engineering*, Ch. 6 "RAG and Agents" (Agents sections):** tools, planning, agent failure modes, memory.
- **Time estimate:** 1–2 months.

- **ReAct date:** arXiv 2210.03629 dates the paper to **Oct 2022**. Weng cites it as "ICLR 2023."
- **ALFWorld:** "A synthetic text-based game designed to align with the embodied ALFRED benchmark," with 6 task types in a simulated household. The baseline was **BUTLER**, "an imitation learning agent trained on 10^5 expert trajectories."
- **WebShop:** "An online shopping website environment with 1.18M real-world products and 12k human instructions." The baselines were IL (1,012 human trajectories) and IL+RL.
- **Hugging Face AI Agents Course structure:**
  - Units 0–4: Onboarding, Agent Fundamentals, Frameworks, Use Cases, Final Assignment.
  - 3 bonus units: function-calling fine-tuning, observability & evaluation, and agents in Pokémon games.
  - At the provider's 3–4 hrs/week per chapter, the five main units come to about **15–20 hrs** (the addendum's arithmetic).

> **Gap:** The original ALFWorld and WebShop papers weren't checked. These benchmarks are described here only through the ReAct paper.

### 7.4 Examples (hands-on projects)

1. Implement all five workflow patterns from the Anthropic post as small scripts.
2. Build a ReAct research agent with a step budget and a reflection step. Log each trajectory.
3. Add long-term memory (vector store plus recency/importance scoring) to a personal assistant agent.
4. Build a 3-agent system (planner → researcher → writer) and compare it with a single agent on the same tasks.

### 7.5 Recommended resources

| Resource | Type | Notes |
|---|---|---|
| [Anthropic – Building effective agents (Dec 2024)](https://www.anthropic.com/engineering/building-effective-agents) | Free | Defines the workflow patterns and when to use agents. The page itself notes that parts of the tooling landscape have changed since it was published. |
| [Lilian Weng – LLM Powered Autonomous Agents (2023)](https://lilianweng.github.io/posts/2023-06-23-agent/) | Free | Canonical survey of planning, memory and tool use. |
| [ReAct paper (Yao et al.)](https://arxiv.org/abs/2210.03629) | Free paper | The reasoning + acting paradigm. Reports absolute success-rate gains of 34% on ALFWorld and 10% on WebShop over imitation/RL baselines. |
| [Hugging Face AI Agents Course](https://huggingface.co/learn/agents-course) | Free (free certificate) | Agent fundamentals, then smolagents / LlamaIndex / LangGraph, use cases and a final benchmark. Provider figure: about 3–4 hrs/week per chapter. |
| [AI Engineering (Huyen), Ch. 6 "RAG and Agents" (Agents sections)](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) | Paid | Tools, planning, agent failure modes, memory. |

---

## Stage 8 — Frameworks and Protocols

### 8.1 Key concepts and definitions

**Orchestration**
- Graph or state-machine orchestration; durable state and checkpoints.

**Agent coordination and control**
- Handoffs; guardrails; sessions.

**Observability**
- Tracing.

**Protocols**
- **MCP (Model Context Protocol)** clients and servers. MCP is a free open standard, described as **"Like a USB-C port for AI applications."**

**Judgment**
- Know when *not* to use a framework.

**Definitions from the addendum**
- **MCP roles** (MCP architecture overview):
  - **Host:** the AI application, such as Claude Desktop or VS Code. It "coordinates and manages one or multiple MCP clients" and creates one client per server.
  - **MCP client:** "maintains a connection to an MCP server and obtains context from an MCP server for the MCP host to use."
  - **MCP server:** "a program that provides context to MCP clients."
  - **Transports:** local servers use STDIO; remote servers use Streamable HTTP.
- **Durable state:** LangGraph is "a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents," focused on "durable execution, streaming, human-in-the-loop" (LangGraph overview).
- **Guardrails:** the OpenAI Agents SDK describes them as running "input validation and safety checks in parallel with agent execution, and fail fast when checks do not pass."

> **Gap:** There's still no formal, sourced definition of a "checkpoint."

### 8.2 Explanation

**What frameworks give you:** they speed up the plumbing.

**What they cost you:** Anthropic warns that frameworks **"create extra layers of abstraction that can obscure the underlying prompts and responses"** and suggests starting with the LLM APIs directly.

**The research's advice:**
1. Learn **one framework deeply** and survey the rest.
2. Learn **MCP**, because MCP is how tools are increasingly plugged into agents.

### 8.3 Important facts, dates and figures

- **AutoGen (Microsoft)** has four parts:
  - **AgentChat:** for conversational single- and multi-agent apps.
  - **Core:** for event-driven, scalable systems.
  - **Studio:** a no-code UI.
  - **Extensions:** including an MCP workbench.
- **CrewAI:** open source, with an Enterprise tier. It covers agents, crews, flows, guardrails and memory.
- **OpenAI Agents SDK (Python):** free and open source under the **MIT License** ("Copyright (c) 2025 OpenAI"). Model API usage is billed per token; OpenAI's pricing page lists model prices "per 1M tokens." The SDK "uses the Responses API by default for OpenAI models." It provides agents, handoffs/agents-as-tools, guardrails, sessions, MCP tool calling and built-in tracing. Install it with `pip install openai-agents`.
- **LangGraph:** stateful, graph-based agent orchestration.
- **LlamaIndex:** strong for data- and RAG-centric agents.
- **DeepLearning.AI short courses:** many 1–2 hr framework-specific courses.
- **Time estimate:** 1–2 months.

### 8.4 Examples (hands-on projects)

1. Re-implement your Stage 7 research agent in LangGraph and in the OpenAI Agents SDK. Compare lines of code, debuggability and traces.
2. Build an MCP server that exposes your own tools (e.g. notes or a database) and connect it to an MCP-capable client.
3. Build a CrewAI or AutoGen multi-agent crew for a content pipeline, with a human-approval step.

### 8.5 Recommended resources

| Resource | Type | Notes |
|---|---|---|
| [LangGraph overview (LangChain docs)](https://docs.langchain.com/oss/python/langgraph/overview) | Free (open source) | Stateful, graph-based agent orchestration. |
| [DeepLearning.AI – AI Agents in LangGraph](https://www.deeplearning.ai/courses/ai-agents-in-langgraph/) | Free short course | Intermediate, 1h42m, 9 video lessons, 6 code examples. Instructors: Harrison Chase (LangChain founder) and Rotem Weiss (Tavily founder). Covers LangGraph's components and agentic search. Enrolment is free; a graded accomplishment requires PRO. |
| [LlamaIndex framework](https://developers.llamaindex.ai/python/framework/) | Free (open source) | Strong for data- and RAG-centric agents. |
| [AutoGen (Microsoft)](https://microsoft.github.io/autogen/stable/) | Free (open source) | AgentChat for conversational single- and multi-agent apps; Core for event-driven, scalable systems; Studio is a no-code UI; extensions include an MCP workbench. |
| [CrewAI docs](https://docs.crewai.com/) | Free OSS (Enterprise tier exists) | Agents, crews, flows, guardrails, memory. |
| [DeepLearning.AI – Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/courses/multi-ai-agent-systems-with-crewai/) | Free short course | Beginner, 3h1m, 18 video lessons, 7 code examples. Instructor: João Moura. Covers designing a team of agents to automate multi-step tasks, such as tailoring a resume or event planning. |
| [OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/) | Free, open source (MIT); model API usage billed per token | Agents, handoffs/agents-as-tools, guardrails, sessions, MCP tool calling, built-in tracing. `pip install openai-agents`. |
| [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) | Free open standard | "Like a USB-C port for AI applications". Build servers and clients. |
| [Hugging Face MCP Course](https://huggingface.co/learn/mcp-course) | Free | "Study Model Context Protocol in theory, design, and practice," use MCP SDKs, take part in challenges, and earn a certificate of completion. |
| [DeepLearning.AI short courses catalog](https://www.deeplearning.ai/courses/) | Free | Many 1–2 hr framework-specific courses. |

**Which framework should a beginner start with?**
- Anthropic advises starting "by using LLM APIs directly."
- LangGraph's own docs say it "is very low-level" and recommend LangChain's prebuilt agents "if you are just getting started with agents or want a higher-level abstraction."
- **Suggested order (editorial):** raw APIs first, then the OpenAI Agents SDK or LangChain agents, then LangGraph when you need durable, stateful control.

> **Gap:** The addendum found no independent, sourced comparison of the frameworks, so the suggested order above is Lucy's editorial judgment.

---

## Stage 9 — Evaluation and Safety

### 9.1 Key concepts and definitions

**Evaluation**
- Task success rates; trajectory/step-level evals; tool-call accuracy.
- LLM-as-judge (and its limits); human evals.
- Regression suites; cost and latency budgets; observability/tracing.

**Safety and security: the OWASP Top 10 for LLMs (2025)**

All 10 risks, from the official OWASP 2025 list (via the addendum):

| ID | Risk | OWASP's own summary (list-page text, truncated, except LLM07, LLM08 and LLM10, which are quoted in full from their detail pages) |
|---|---|---|
| LLM01:2025 | Prompt Injection | "occurs when user prompts alter the…" |
| LLM02:2025 | Sensitive Information Disclosure | "can affect both the LLM and its application…" |
| LLM03:2025 | Supply Chain | "LLM supply chains are susceptible to various vulnerabilities…" |
| LLM04:2025 | Data and Model Poisoning | "occurs when pre-training, fine-tuning, or embedding data is…" |
| LLM05:2025 | Improper Output Handling | "insufficient validation, sanitization, and…" |
| LLM06:2025 | Excessive Agency | "An LLM-based system is often granted a degree of agency…" |
| LLM07:2025 | System Prompt Leakage | "The system prompt leakage vulnerability in LLMs refers to the risk that the system prompts or instructions used to steer the behavior of the model can also contain sensitive information that was not intended to be discovered." "When discovered, this information can be used to facilitate other attacks. It's important to understand that the system prompt should not be considered a secret, nor should it be used as a security control." ([LLM07 detail page](https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/)) |
| LLM08:2025 | Vector and Embedding Weaknesses | "Vectors and embeddings vulnerabilities present significant security risks in systems utilizing Retrieval Augmented Generation (RAG) with Large Language Models (LLMs). Weaknesses in how vectors and embeddings are generated, stored, or retrieved can be exploited by malicious actions (intentional or unintentional) to inject harmful content, manipulate model outputs, or access sensitive information." ([LLM08 detail page](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/)) |
| LLM09:2025 | Misinformation | "Misinformation from LLMs poses a core vulnerability…" |
| LLM10:2025 | Unbounded Consumption | "Unbounded Consumption occurs when a Large Language Model (LLM) application allows users to conduct excessive and uncontrolled inferences, leading to risks such as denial of service (DoS), economic losses, model theft, and service degradation. The high computational demands of LLMs, especially in cloud environments, make them vulnerable to resource exploitation and unauthorized usage." ([LLM10 detail page](https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/)) |

**Defensive practices**
- Least privilege; sandboxing; human approval for irreversible actions; guardrails.

**Direct vs. indirect prompt injection** (OWASP LLM01 page)
- *Direct* injections "occur when a user's prompt input directly alters the behavior of the model."
- *Indirect* injections "occur when an LLM accepts input from external sources, such as websites or files." One example, from a project: malicious instructions planted in a document that a RAG agent retrieves.
- Both kinds can be intentional or unintentional.
- OWASP notes that RAG and fine-tuning "do not fully mitigate prompt injection vulnerabilities" and that jailbreaking is "a form of prompt injection."

> **Gap:** The summaries for LLM02–LLM06 and LLM09 are still truncated list-page text. Only LLM01 (prompt injection), LLM07, LLM08 and LLM10 have full, checked descriptions; the other six risks have no complete definitions.

### 9.2 Explanation

Evaluation and safety matter more for agents than for single LLM calls because **agents compound errors across steps and take real actions**.

Anthropic notes agents bring **"higher costs, and the potential for compounding errors"** and recommends **"extensive testing in sandboxed environments."**

**A warning about LLM judges (the ChemCrow case, cited by Weng):**
- **What ChemCrow is** (Bran et al., Apr 2023): it augments an LLM "with 13 expert-designed tools to accomplish tasks across organic synthesis, drug discovery, and materials design." It was implemented in LangChain using a ReAct/MRKL-style loop.
- **What happened:** it was compared with **GPT-4**. "LLM-based evaluation concluded that GPT-4 and ChemCrow perform nearly equivalently, [but] human evaluations with experts… showed that ChemCrow outperforms GPT-4 by a large margin."
- **The lesson:** don't rely blindly on LLM judges.

### 9.3 Important facts, dates and figures

- **OWASP Top 10 for LLM & GenAI Apps** is dated **2025** and works as a threat-model checklist.
- **Inspect**, from the **UK AI Security Institute**, is an open-source framework for LLM and agent evaluations.
- **Langfuse** offers open-source tracing, evals and prompt management, with a paid cloud option.
- **Hugging Face Agents Course, Bonus Unit 2,** covers Agent Observability & Evaluation. Direct link (title confirmed as "AI Agent Observability & Evaluation"): https://huggingface.co/learn/agents-course/bonus-unit2/introduction
- **Huyen's *AI Engineering*, Ch. 3–4 & 10,** cover evaluation methodology, AI-as-a-judge, guardrails and monitoring.
- **Time estimate:** 3–6 weeks, then continuous.

### 9.4 Examples (hands-on projects)

1. Build an eval harness for your agent: 50+ tasks with pass/fail checks, cost and latency tracking, run in CI on every prompt change.
2. Run an indirect-prompt-injection test: plant malicious instructions in a document your RAG agent retrieves, then add defenses and measure again.
3. Implement least-privilege tools plus a human-approval gate for destructive actions, and record "excessive agency" test cases.

### 9.5 Recommended resources

| Resource | Type | Notes |
|---|---|---|
| [OWASP Top 10 for LLM & GenAI Apps (2025)](https://genai.owasp.org/llm-top-10/) | Free | Threat model checklist. |
| [Inspect (UK AI Security Institute)](https://inspect.aisi.org.uk/) | Free (open source) | Framework for LLM and agent evaluations. |
| [Ragas](https://docs.ragas.io/en/stable/) | Free (open source) | RAG and LLM app evaluation metrics. |
| [Langfuse docs](https://langfuse.com/docs) | Free OSS / paid cloud | Open-source tracing, evals and prompt management. |
| [Hugging Face Agents Course – Bonus Unit 2: Agent Observability & Evaluation](https://huggingface.co/learn/agents-course) | Free | Direct unit link: https://huggingface.co/learn/agents-course/bonus-unit2/introduction |
| [AI Engineering (Huyen), Ch. 3–4 & 10](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) | Paid | Evaluation methodology, AI-as-a-judge, guardrails, monitoring. |

---

## Stage 10 — Deploying Real Agents

### 10.1 Key concepts and definitions

**Serving**
- Serving agents behind an API (FastAPI); containerization (Docker); async/streaming responses.

**Reliability and long-running work**
- Durable state and resumable runs; queues for long-running tasks.

**Security and cost control**
- Secrets management; rate limiting and cost caps. These map to OWASP **LLM10 (unbounded consumption)**.

**Performance**
- Model routing and caching.

**Operations**
- Tracing and monitoring in production; user feedback loops.

**Change management**
- Versioning prompts, tools and models.

**What the addendum could source**
- **Model routing:** *AI Engineering* Chapter 10 has the step "Add Model Router and Gateway" (table of contents only). Anthropic's routing workflow sends "easy/common questions to smaller, cost-efficient models… and hard/unusual questions to more capable models."
- **Message queue:** a component "used for inter-process communication… [using] a queue for messaging" (Wikipedia).
- **Caching:** "A hardware or software component that stores data so that future requests for that data can be served faster" (Wikipedia). *AI Engineering* Chapter 10 has "Reduce Latency with Caches." The OpenAI function-calling guide notes that `allowed_tools` lets you "maximize savings from prompt caching."

> **Gap:** There's no sourced explanation of specific model-router algorithms, and no recommended queue products. The addendum checked no page about any queueing tool, so none are named.

### 10.2 Explanation

**A demo agent and a production agent are very different things.**

Huyen's *AI Engineering*, Ch. 10, builds up a production architecture in five numbered steps. (The table of contents labels them as steps, for example "Step 1. Enhance Context" and "Step 3. Add Model Router and Gateway.")

1. Enhance context.
2. Add guardrails.
3. Add a model router and gateway.
4. Cache to cut latency.
5. Add agent patterns.

**Then, as follow-on topics rather than a numbered step:** monitoring/observability, and user feedback.

Several of these steps use ideas from earlier stages: guardrails (Stages 8–9), agent patterns (Stage 7), and tracing and monitoring (Stages 8–9).

The *AI Engineering* table of contents lists "Step 1. Enhance Context" and "Step 3. Add Model Router and Gateway." Chapter 6 (RAG and Agents) is the context-building chapter.

> **Gap:** The full text of *AI Engineering* is paywalled, so Huyen's exact definitions of "enhance context" and "gateway" couldn't be verified.

### 10.3 Important facts, dates and figures

- **Time estimate:** 1–2 months for a first production-grade capstone. Mastery comes from shipping and iterating.
- **Anthropic's two highlighted agent use cases:** customer support and coding agents.
- **OpenAI Agents SDK:** production-oriented runtime features, including sessions, tracing, human-in-the-loop and sandbox agents. It is free and open source (MIT); model API usage is billed per token.
- **Huyen's *AI Engineering*, Ch. 9–10:** inference optimization, architecture, monitoring, user feedback.

### 10.4 Examples (capstone projects)

1. **Customer-support agent:** RAG over a knowledge base, tools for order lookup and refund *requests* gated by human approval, an eval suite, deployed with FastAPI + Docker, with tracing and per-conversation cost caps. Anthropic names customer support as a strong agent use case.
2. **Coding/ops agent in a sandbox:** reads the repo, runs tests and proposes patches as PRs (never pushing directly), with test pass rate as the eval. Anthropic's other highlighted use case is coding agents.
3. **MCP-powered personal assistant:** connects to 2–3 MCP servers, with memory, a scheduled background job, and a dashboard of traces and evals.

Each capstone uses earlier stages: human-approval gates and least privilege (Stage 9), RAG (Stage 5), MCP (Stage 8), memory (Stage 7) and evals (Stage 9).

### 10.5 Recommended resources

| Resource | Type | Notes |
|---|---|---|
| [FastAPI docs](https://fastapi.tiangolo.com/) | Free | Python API framework for serving agents. |
| [Docker – Get started](https://docs.docker.com/get-started/) | Free | Containerize and ship. |
| [OpenAI Agents SDK – sessions, tracing, human-in-the-loop, sandbox agents](https://openai.github.io/openai-agents-python/) | Free, open source (MIT); model API usage billed per token | Production-oriented runtime features. |
| [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) | Free | Durable, stateful orchestration. |
| [Langfuse](https://langfuse.com/docs) | Free OSS / paid cloud | Production tracing and monitoring. |
| [AI Engineering (Huyen), Ch. 9–10](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) | Paid | Inference optimization, architecture, monitoring, user feedback. |

> **Gap:** There's still no checked resource for secrets management (the Wikipedia lookup returned nothing) and no cloud hosting guide beyond Docker. Caching and queues are covered only by the general definitions in 10.1.

---

## Pacing Summary (All Estimates)

| Stage | Estimate |
|---|---|
| 0. Programming from zero (optional) | 1–3 months |
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

- **Total (estimate):** about 10–20 months if Stages 1–10 are done one after another at 8–10 hrs/week, or about 11–23 months including Stage 0. Overlap between Stages 4–10 may shorten this, but the research has no source for how much.

---

## Overall Summary

The path has an optional on-ramp and five logical phases:

0. **On-ramp (Stage 0, only if you have never programmed).** Beginner-first resources (CS50P, Automate the Boring Stuff, Kaggle Learn) teach basic programming before Stage 1's resources, which assume you can already code.
1. **Foundations (Stages 1–3).**
   - Linear algebra, calculus, probability and Python explain how models represent data (embeddings), learn (gradient-based optimization) and produce output (probability distributions over tokens).
   - Deep learning explains training and backpropagation.
   - The transformer (introduced in 2017) is the architecture behind the LLM, which the research calls the "brain" of every agent.
2. **Steering and grounding the model (Stages 4–5).**
   - In an agent, prompts and tool descriptions *are* the program, so define success criteria and evals before you optimize.
   - RAG (introduced in 2020) gives the model private or fresh knowledge without retraining. Its components also make up agent long-term memory.
3. **Acting (Stages 6–7).**
   - Tool calling turns an LLM into an actor, through a multi-step loop between your app and the model.
   - Architecture choices (workflows vs. agents, planning methods such as ReAct, memory, multi-agent setups) determine reliability, cost and latency.
   - The guiding rule: use the simplest solution that works, and add complexity only when needed.
4. **Building with leverage (Stage 8).**
   - Frameworks speed up the plumbing but can hide the prompts and responses underneath, so start with raw APIs.
   - Learn one framework deeply, and learn MCP.
5. **Making it trustworthy and real (Stages 9–10).**
   - Agents compound errors and take real actions. That calls for rigorous evals (without relying blindly on LLM judges), the OWASP LLM Top 10 threat model, least privilege, sandboxing and human approval for irreversible actions.
   - Production adds serving, containers, durable state, cost caps, routing, caching, monitoring and feedback loops.
   - Mastery comes from shipping and iterating.

Across the whole path, the research's advice is to **start building small agents early**, because Stages 4–10 overlap heavily in practice. Done strictly in sequence, the path takes about 10–20 months (about 11–23 months with Stage 0) at 8–10 hrs/week.

---

## Glossary

*Definitions come from the research and the addendum, with the source in brackets. Items marked (editorial) are Lucy's own wording, not a quote from a source. The stage number shows where each term is taught.*

| Term | Definition | Stage |
|---|---|---|
| **Agent** | "Systems where LLMs dynamically direct their own processes and tool usage." [Anthropic] | 7 |
| **Agent-computer interface (ACI)** | The design of good tools for agents. [Anthropic, via the research] | 6 |
| **ANN (approximate nearest neighbour) search** | Algorithms that "return approximately top k nearest neighbors to trade off a little accuracy lost for a huge speedup." [Weng] | 5 |
| **API-Bank** | "A benchmark… for tool-augmented LLMs," with 53 API tools, 264 annotated dialogues and 568 API calls, evaluated at three levels (call, retrieve, plan). [Li et al.; Weng] | 6 |
| **BM25** | "A ranking function used by search engines to estimate the relevance of documents to a given search query." [Wikipedia] | 5 |
| **Caching** | "A hardware or software component that stores data so that future requests for that data can be served faster." [Wikipedia] | 10 |
| **Chain-of-thought** | Prompt exemplars that include "Let's think step by step" reasoning before the answer. [ReAct paper appendix] | 4, 7 |
| **ChemCrow** | An LLM augmented "with 13 expert-designed tools to accomplish tasks across organic synthesis, drug discovery, and materials design." [Bran et al.; Weng] | 9 |
| **Chunking** | Splitting documents into pieces for retrieval. For example, the RAG paper split each Wikipedia article into "disjoint 100-word chunks." [Lewis et al.] | 5 |
| **CNN (convolutional neural network)** | "A type of feedforward neural network that learns features via filter optimization." [Wikipedia] | 2 |
| **Durable execution / stateful agents** | What LangGraph is built for: "long-running, stateful agents," focused on "durable execution, streaming, human-in-the-loop." [LangGraph overview] | 8 |
| **Early stopping** | "A form of regularization used to avoid overfitting when training a model with an iterative method, such as gradient descent." [Wikipedia] | 2 |
| **FAISS (Facebook AI Similarity Search)** | "Applies vector quantization by partitioning the vector space into clusters and then refining the quantization within clusters." [Weng] | 5 |
| **Few-shot / zero-shot prompting** | Few-shot gives a few worked examples in the prompt; zero-shot gives none. [addendum, following *AI Engineering* Ch. 5] | 4 |
| **Fine-tuning** | "Adapting a computational model trained for one task to perform a different, usually more specific, task… a form of transfer learning." [Wikipedia] | 3 |
| **Generative Agents** | A study in which 25 LLM-controlled characters live in a Sims-like sandbox, using a memory stream with retrieval by recency, importance and relevance. [Park et al.; Weng] | 7 |
| **Gradio** | "An open-source Python package that allows you to quickly build a demo or web application for your machine learning model, API, or any arbitrary Python function." [Gradio Quickstart] | 2 |
| **Guardrails** | Running "input validation and safety checks in parallel with agent execution, and fail fast when checks do not pass." [OpenAI Agents SDK] | 8, 9 |
| **HNSW** | "An algorithm for approximate nearest neighbor search" [Wikipedia] that "builds hierarchical layers of these small-world graphs." [Weng] | 5 |
| **Hybrid search** | Combining sparse/keyword retrieval (BM25) with dense/embedding retrieval. (editorial) | 5 |
| **JSON Schema** | "The vocabulary that enables JSON data consistency, validity, and interoperability." [json-schema.org] | 6 |
| **LoRA (Low-Rank Adaptation)** | "Freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture." [Hu et al.] | 3 |
| **Long-term / short-term memory** | Long-term memory is a vector store; short-term memory is the context window. [research] | 7 |
| **MAP (maximum a posteriori) estimate** | "The mode of the posterior density… a regularization of maximum likelihood estimation." [Wikipedia] | 1 |
| **MCP (Model Context Protocol)** | A free open standard, "Like a USB-C port for AI applications." [modelcontextprotocol.io] | 8 |
| **MCP host / client / server** | Host: the AI application, which "coordinates and manages one or multiple MCP clients." Client: "maintains a connection to an MCP server and obtains context." Server: "a program that provides context to MCP clients." [MCP architecture overview] | 8 |
| **Memory stream** | "A long-term memory module (external database) that records a comprehensive list of agents' experience in natural language." [Weng] | 7 |
| **Message queue** | A component "used for inter-process communication… [using] a queue for messaging." [Wikipedia] | 10 |
| **micrograd** | "A tiny Autograd engine" that implements backpropagation over a dynamically built DAG, with a small neural-network library on top. [karpathy/micrograd] | 2 |
| **MLE (maximum likelihood estimation)** | "A method of estimating the parameters of an assumed probability distribution, given some observed data… by maximizing a likelihood function." [Wikipedia] | 1 |
| **MLP (multilayer perceptron)** | "A kind of modern feedforward neural network consisting of fully connected neurons with nonlinear activation functions, organized in layers." [Wikipedia] | 2 |
| **Nearest-neighbour search** | "Finding the point in a given set that is closest to a given point." [Wikipedia] | 5 |
| **Parametric / non-parametric memory** | In the RAG paper, the pre-trained seq2seq model is "parametric memory"; the dense vector index of Wikipedia is "non-parametric memory." [Lewis et al.] | 5 |
| **PCA (principal component analysis)** | "A linear dimensionality reduction technique with applications in exploratory data analysis, visualization and data preprocessing." [Wikipedia] | 1 |
| **PEFT (Parameter-Efficient Fine-Tuning)** | A library whose methods "only fine-tune a small number of (extra) model parameters." [Hugging Face PEFT docs] | 3 |
| **Poka-yoke tools** | Mistake-proof tools. [Anthropic, via the research] | 6 |
| **Precision / recall** | "Performance metrics that apply to data retrieved from a collection, corpus or sample space." [Wikipedia] | 1, 5 |
| **Prompt injection (direct / indirect)** | Direct: "a user's prompt input directly alters the behavior of the model." Indirect: "an LLM accepts input from external sources, such as websites or files." [OWASP LLM01] | 4, 9 |
| **Pydantic** | "The most widely used data validation library for Python." [Pydantic docs] | 4 |
| **Q/K/V (query, key, value)** | Three vectors created for each word "by multiplying the embedding by three matrices that we trained"; attention scores are query–key dot products. [The Illustrated Transformer] | 3 |
| **RAG (retrieval-augmented generation)** | A method that lets a model use private or fresh knowledge without retraining. [research; Lewis et al.] | 5 |
| **ReAct** | The reasoning + acting paradigm, which interleaves thought → action → observation. [research; Yao et al.] | 7 |
| **recall@k** | The share of the relevant documents that appear in the top *k* results. (editorial) | 5 |
| **Red team** | "A group that simulates an adversary… then reports back so that the organization can improve their defenses." [Wikipedia] | 4 |
| **Reflexion** | "A framework to equip agents with dynamic memory and self-reflection capabilities." [Shinn et al.; Weng] | 7 |
| **RNN (recurrent neural network)** | "Designed for processing sequential data… the output of a neuron at one time step is fed back as input… at the next time step." [Wikipedia] | 2 |
| **SGD (stochastic gradient descent)** | "An iterative method for optimizing an objective function… replaces the actual gradient by an estimate thereof, calculated from a randomly selected subset of the data." [Wikipedia] | 2 |
| **Strict mode** | "Setting `strict` to `true` will ensure function calls reliably adhere to the function schema, instead of being best effort." [OpenAI] | 6 |
| **SWE-bench** | "An evaluation framework consisting of 2,294 software engineering problems drawn from real GitHub issues." [Jimenez et al.] | 6 |
| **Tool-calling loop** | Request → tool call → execute → return output → final answer; "a multi-step conversation between your app and the model." [research; OpenAI] | 6 |
| **`tool_choice`** | Controls whether and which functions the model may call. Its five settings are Auto (default), Required, Forced, `allowed_tools` and `none`. [OpenAI] | 6 |
| **Tool use (function calling)** | Letting an AI model call functions or services, such as a web search or a weather lookup. The model decides when to call a tool based on your request and the tool's description, and the result is fed back to it so it can answer. [Anthropic tool use overview] | 6 |
| **Toolformer** | "A model trained to decide which APIs to call, when to call them, what arguments to pass." [Schick et al.] | 6 |
| **Tree of Thoughts** | "Extends CoT by exploring multiple reasoning possibilities at each step… creating a tree structure." [Yao et al.; Weng] | 7 |
| **Workflow** | "Systems where LLMs and tools are orchestrated through predefined code paths." [Anthropic] | 7 |

---

## Review Questions

*Answer key: each question ends with the section(s) of these notes where the answer is found.*

### Stage 0 — Programming from zero
1. What is the addendum's prerequisite check for skipping Stage 0? *(See §Overview ("Where to start"); 0.1.)*
2. Why isn't the official Python Tutorial a good first resource for someone who has never programmed? *(See §0.2.)*
3. Name the three main Stage 0 resources in the recommended (editorial) order, and say what each one is used for. *(See §0.3.)*
4. What does CS50P say about prior experience and required software? *(See §0.3; 0.5.)*
5. Describe the three Stage 0 projects. *(See §0.4.)*

### Stage 1 — Foundations
1. Which three areas of mathematics does Stage 1 cover, and what does the research say each one contributes to understanding LLMs and agents? *(See §1.1; 1.2.)*
2. Why does the research say embeddings, attention and similarity search are "linear algebra"? *(See §1.2.)*
3. Who is the official Python Tutorial aimed at, and why does that matter for a complete beginner? *(See §1.3; 1.5.)*
4. What is the provider's time figure for the Machine Learning Specialization, and how many courses does it contain? *(See §1.3.)*
5. Describe the three Stage 1 hands-on projects and the evaluation metrics the third one reports. *(See §1.4.)*
6. Define PCA and explain how MAP estimation relates to MLE. *(See §1.1.)*

### Stage 2 — Deep learning
1. Why does understanding backpropagation and loss help when you work with LLMs? *(See §2.2.)*
2. How many lessons does fast.ai's course have, and roughly how long is each? What prerequisite does the site state, and what does it mean for someone who has never coded? *(See §2.3.)*
3. What does Karpathy's "Zero to Hero" build, in order? *(See §2.3.)*
4. Which architectures does the research say to study only "for context," and what does the addendum say that means? *(See §2.1.)*
5. What is micrograd, and what problem does early stopping address? *(See §2.5.)*

### Stage 3 — LLMs and transformers
1. What paper introduced the Transformer, who wrote it, and when? *(See §3.3.)*
2. Name three properties of LLMs that the research says drive later agent design decisions. *(See §3.2.)*
3. Name two sampling settings listed in Stage 3, and say which project compares them with greedy decoding. *(See §3.1; 3.4.)*
4. The concept list contrasts pretraining with post-training. Which two post-training methods does it name in parentheses? *(See §3.1.)*
5. What does Chapter 2 of Huyen's *AI Engineering* cover? *(See §3.3.)*
6. Explain how query, key and value vectors are used to compute attention, and how LoRA reduces the number of trainable parameters. *(See §3.1.)*

### Stage 4 — Prompt engineering
1. Explain the claim that in an agent, "the system prompt and the tool descriptions *are* the program." *(See §4.2.)*
2. What does Anthropic's guide recommend you do *before* starting prompt engineering? *(See §4.2.)*
3. How big an eval set does the first Stage 4 project suggest, and what should you track across prompt versions? *(See §4.4.)*
4. Which library does the research suggest for validating structured JSON output? *(See §4.4; 4.5.)*
5. What is the difference between zero-shot and few-shot prompting? *(See §4.1.)*

### Stage 5 — RAG
1. What problem does RAG solve, according to the research? *(See §5.2.)*
2. What did the original RAG paper (Lewis et al., 2020) show about swapping the retrieval index? *(See §5.2.)*
3. Name the three RAG evaluation dimensions listed in the key concepts. *(See §5.1.)*
4. Which three retrieval approaches does the second project compare, and what metric does it use? *(See §5.4; 5.1.)*
5. How does RAG relate to agent long-term memory? *(See §5.2.)*
6. In the RAG paper, what was parametric memory and what was non-parametric memory? *(See §5.1.)*

### Stage 6 — Tool use and function calling
1. Write out the five stages of the tool-calling loop described in the research. *(See §6.1.)*
2. How does OpenAI's guide describe tool calling? *(See §6.1.)*
3. What did Anthropic find about tools vs. prompts while building its SWE-bench agent? *(See §6.2.)*
4. How many functions does OpenAI's guide recommend having available at once? *(See §6.3.)*
5. What does "poka-yoke" mean when applied to tools? *(See §6.1.)*
6. List the five `tool_choice` settings, and say what strict mode requires of a schema. *(See §6.1.)*

### Stage 7 — Agent architectures
1. List Anthropic's five workflow patterns. *(See §7.1.)*
2. What is ReAct, and what success-rate gains does the paper report on ALFWorld and WebShop? *(See §7.1; 7.3.)*
3. How does the research distinguish short-term from long-term memory, and which three factors are used for retrieval in Generative Agents-style memory? *(See §7.1.)*
4. Quote Anthropic's guiding principle about complexity. *(See §7.2.)*
5. What three core challenges does Lilian Weng identify? *(See §7.2.)*
6. How does Anthropic define a workflow, and how does it define an agent? *(See §7.1.)*

### Stage 8 — Frameworks and protocols
1. What warning does Anthropic give about frameworks, and what does it suggest starting with instead? *(See §8.2.)*
2. What analogy does the MCP site use to describe MCP? *(See §8.1.)*
3. Name the four parts of Microsoft AutoGen described in the research and what each does. *(See §8.3.)*
4. What features does the OpenAI Agents SDK provide, and how do you install it? *(See §8.3.)*
5. What strategy does the research recommend for learning frameworks? *(See §8.2.)*
6. Describe the roles of the MCP host, client and server, and the two transports. *(See §8.1.)*

### Stage 9 — Evaluation and safety
1. Why do agents need more rigorous evaluation than single LLM calls? *(See §9.2.)*
2. Name the OWASP 2025 LLM risks with the IDs LLM01, LLM06 and LLM10. *(See §9.1.)*
3. What does the ChemCrow example show about LLM-as-judge evaluation? *(See §9.2.)*
4. Which defensive practices does the research list alongside the OWASP Top 10? *(See §9.1.)*
5. Describe the indirect-prompt-injection test project. *(See §9.4.)*
6. Name OWASP risks LLM03, LLM04 and LLM09, and explain the difference between direct and indirect prompt injection. *(See §9.1.)*

### Stage 10 — Deploying real agents
1. List, in order, the five numbered steps of the production architecture in Huyen's *AI Engineering*, Ch. 10, and name the two follow-on topics that come after them. *(See §10.2.)*
2. Which OWASP risk do rate limiting and cost caps address? *(See §10.1.)*
3. Which two agent use cases does Anthropic highlight, and which capstones match them? *(See §10.3; 10.4.)*
4. What constraint does the coding/ops capstone put on how patches are delivered, and what metric does it use as its eval? *(See §10.4.)*
5. Which tools does the research recommend for serving and containerizing an agent? *(See §10.1; 10.5.)*

---

## References

There are 83 sources in total: sources 1–42 come from the original research, sources 43–79 were added by the addendum, sources 80–82 come from the addendum's "QA additions for notes," and source 83 comes from the addendum's "Beginner basics glossary." Both files say all links were checked on 16 Oct 2026.

### From the original research (1–42)

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

### Added by the addendum (43–79)

43. Python wiki – BeginnersGuide/NonProgrammers: https://wiki.python.org/moin/BeginnersGuide/NonProgrammers
44. CS50's Introduction to Programming with Python: https://cs50.harvard.edu/python/
45. Automate the Boring Stuff with Python: https://automatetheboringstuff.com/
46. Wikipedia – PCA: https://en.wikipedia.org/wiki/Principal_component_analysis
47. Wikipedia – MLE: https://en.wikipedia.org/wiki/Maximum_likelihood_estimation
48. Wikipedia – MAP: https://en.wikipedia.org/wiki/Maximum_a_posteriori_estimation
49. Wikipedia – MLP: https://en.wikipedia.org/wiki/Multilayer_perceptron
50. Wikipedia – SGD: https://en.wikipedia.org/wiki/Stochastic_gradient_descent
51. Wikipedia – CNN: https://en.wikipedia.org/wiki/Convolutional_neural_network
52. Wikipedia – RNN: https://en.wikipedia.org/wiki/Recurrent_neural_network
53. Wikipedia – Early stopping: https://en.wikipedia.org/wiki/Early_stopping
54. Wikipedia – Okapi BM25: https://en.wikipedia.org/wiki/Okapi_BM25
55. Wikipedia – Nearest neighbor search: https://en.wikipedia.org/wiki/Nearest_neighbor_search
56. Wikipedia – HNSW: https://en.wikipedia.org/wiki/Hierarchical_navigable_small_world
57. Wikipedia – Red team: https://en.wikipedia.org/wiki/Red_team
58. Wikipedia – Precision and recall: https://en.wikipedia.org/wiki/Precision_and_recall
59. Wikipedia – Fine-tuning (deep learning): https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)
60. Wikipedia – Message queue: https://en.wikipedia.org/wiki/Message_queue
61. Wikipedia – Cache (computing): https://en.wikipedia.org/wiki/Cache_(computing)
62. Hu et al. – LoRA: https://arxiv.org/abs/2106.09685
63. Yao et al. – Tree of Thoughts: https://arxiv.org/abs/2305.10601
64. Shinn et al. – Reflexion: https://arxiv.org/abs/2303.11366
65. Park et al. – Generative Agents: https://arxiv.org/abs/2304.03442
66. Schick et al. – Toolformer: https://arxiv.org/abs/2302.04761
67. Li et al. – API-Bank: https://arxiv.org/abs/2304.08244
68. Bran et al. – ChemCrow: https://arxiv.org/abs/2304.05376
69. Jimenez et al. – SWE-bench: https://arxiv.org/abs/2310.06770
70. karpathy/micrograd: https://github.com/karpathy/micrograd
71. Gradio Quickstart: https://gradio.app/guides/quickstart
72. Pydantic docs: https://pydantic.dev/docs/validation/latest/get-started/
73. Hugging Face PEFT docs: https://huggingface.co/docs/peft/index
74. JSON Schema: https://json-schema.org/
75. MCP architecture overview: https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture
76. OWASP LLM01:2025 Prompt Injection: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
77. OpenAI Agents SDK LICENSE (MIT): https://raw.githubusercontent.com/openai/openai-agents-python/main/LICENSE
78. OpenAI API pricing: https://developers.openai.com/api/docs/pricing
79. HF Agents Course – Bonus Unit 2: https://huggingface.co/learn/agents-course/bonus-unit2/introduction

### Added by the addendum's "QA additions for notes" (80–82)

80. OWASP LLM07:2025 System Prompt Leakage: https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/
81. OWASP LLM08:2025 Vector and Embedding Weaknesses: https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/
82. OWASP LLM10:2025 Unbounded Consumption: https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/

### Added by the addendum's "Beginner basics glossary" (83)

83. Anthropic – Tool use overview: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview

*Removed during checking (from the research):* O'Reilly's "Hands-On Machine Learning" page (returned 403, content not confirmed) and Coursera's Deep Learning Specialization page (returned 200, but the content couldn't be confirmed).

*Citation note:* works the original research named without citing them (Generative Agents, Tree of Thoughts, Reflexion, Toolformer, API-Bank, ChemCrow and SWE-bench), plus LoRA, now have arXiv citations (sources 62–69). The addendum says these were checked through the arXiv API. The ALFWorld and WebShop papers remain uncited; see the gap in Stage 7.
