# Building AI Agents from Zero: A Beginner's Edition

*A friendly companion to the main study notes (`agentic-ai-notes.md`). It is written for readers who have never written a line of code. Every fact comes from Lucy's research file (`agentic-ai-learning-path.md`), her research addendum (`agentic-ai-research-addendum.md`, including its "Beginner basics glossary") and the main notes. Nothing else.*

---

## How to Use These Notes

**What this path is.** It's a step-by-step learning path, Stage 0 to Stage 10. It starts with your very first program and ends with building and launching AI agents that do real work.

**A few basic words first** (from Lucy's beginner glossary):
- **AI (artificial intelligence):** computer systems that can do tasks we normally link to human intelligence, such as learning, reasoning, solving problems, perceiving things and making decisions. It's also the name of the research field that builds such systems.
- **Model:** the thing machine learning (explained in Stage 1) produces. It's a mathematical "machine" that takes some input and returns an output, such as a prediction. Google describes it as "the set of parameters and structure needed for a system to make predictions."
- **LLM (large language model):** an AI model trained on a huge amount of text so it can generate, summarize, translate and analyze language. LLMs power chatbots such as ChatGPT, Claude, Gemini and Grok.
- **Agent (AI agent):** software that can reason about what you ask, plan steps and take actions for you, such as searching, running tools or sending requests, rather than only replying with text. Anthropic, whose guides the research uses often, puts it this way: agents are "systems where LLMs dynamically direct their own processes and tool usage." In other words, the AI decides for itself what to do next and which tools to use.

**How long it takes.** Plan for **about 11–23 months** if you start at Stage 0, or **about 10–20 months** if you can already code and start at Stage 1. That assumes 8–10 hours a week and doing the stages one after another. All of these times are rough estimates. Stages 4–10 overlap a lot in practice, so you may finish sooner, but the sources don't say how much sooner.

**One big tip from the research.** Start building small agents early. Don't wait until you feel you've "mastered" the earlier stages.

**How to read each stage.** Every stage has the same five parts:
1. What it is
2. Why it matters
3. Key ideas in plain words
4. A simple example
5. Beginner-friendly resources

**Three labels you'll see:**
- *Analogy:* an everyday comparison to help you picture an idea. Analogies are only teaching aids. They don't add facts.
- *(editorial):* Lucy's own suggestion rather than a fact from a source.
- **Gap:** something the sources don't cover.

**Two more notes:**
- "Paid" means a resource costs money. The sources don't list prices, because prices change.
- The links were all checked on 16 Oct 2026.

---

## Stage 0 — Your Very First Steps in Programming

### What it is
Stage 0 is for **anyone who has never written code**. **Code** (short for *source code*) is the human-readable text instructions that programmers write, which a computer then runs. You learn to write simple programs in **Python**, a popular programming language designed to be easy to read and write. Most AI tools are built for it. **Time:** about 1–3 months (estimate).

**Should you skip it?** The test is Lucy's own (editorial). Skip Stage 0 if you can already write a short program that:
- goes through a list of items one by one,
- makes a choice using "if … else …",
- defines its own functions, and
- reads a file.

If that sounds like a foreign language, start here. That's exactly what this stage is for.

### Why it matters
Almost every tool used to build AI agents is "Python-first," according to the research. And the official Python Tutorial, used in Stage 1, says it is aimed at people who *already* program. Stage 0 gets you ready for it.

*Analogy:* It's like learning the alphabet before writing an essay. Every later stage assumes you can already "write."

### Key ideas in plain words
The CS50 Python course lists the topics a beginner learns:

> functions, variables, conditionals, loops, exceptions, debugging, unit tests, libraries, regular expressions, classes and file I/O.

Don't worry if these words mean nothing yet. Learning them *is* Stage 0. One of them has a sourced plain definition: a **library** is ready-made code that other people wrote and you can reuse in your own program, so you don't start from scratch.

> **Gap:** Apart from "library," the sources list these topics but don't define them. You'll learn what each one means inside the Stage 0 courses.

**Suggested order (editorial):**
1. CS50P (the CS50 Python course), for structured lessons and problem sets.
2. Automate the Boring Stuff, for practical projects.
3. The Kaggle Python and pandas courses.
4. Then the official Python Tutorial (Stage 1), as a reference.

### A simple example
Lucy suggests three starter projects (editorial):
- a script that renames files,
- a CSV summary tool, and
- a tiny text-adventure game.

### Beginner-friendly resources
- [Python wiki – "Python for New Programmers" (BeginnersGuide/NonProgrammers)](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers) — Free. "If you've never programmed before, the tutorials on this page are recommended for you; they don't assume that you have previous experience." (The page notes the wiki is being archived.)
- [CS50's Introduction to Programming with Python (Harvard, David J. Malan)](https://cs50.harvard.edu/python/) — Free (a paid verified certificate is offered). "Designed for students with or without prior programming experience." "No software required except for a web browser."
- [Automate the Boring Stuff with Python (Al Sweigart)](https://automatetheboringstuff.com/) — Free to read online; the print copy is paid. The Python wiki calls it "Practical Programming for Total Beginners."
- [Kaggle Learn – Python micro-course](https://www.kaggle.com/learn) — Free. A short bridge into data work.

---

## Stage 1 — Foundations: Math, Python and Machine-Learning Basics

### What it is
Stage 1 has three parts:
- **Math:** linear algebra, calculus, and probability and statistics.
- **More Python:** including tools for working with data, and **pip**, Python's tool for installing libraries ("packages"). pip downloads them from a public online collection called PyPI.
- **The basics of machine learning (ML):** a part of AI where a program learns patterns from data, instead of a person writing every rule by hand. It then uses those patterns to handle new data it has never seen. Stage 1 covers things like supervised vs. unsupervised learning and how to evaluate a model.

**Time:** about 2–4 months (estimate), or less if you already code in Python.

### Why it matters
The research gives a clear reason for each part:
- **Linear algebra:** "embeddings, attention and similarity search" are all linear algebra. An **embedding** turns something like a word or a document into a list of numbers. Things with similar meanings end up with similar numbers, so a computer can compare them. (You'll meet these ideas again in Stages 3 and 5.)
- **Calculus:** training a model is calculus plus optimization.
  - **Training** means showing a model many examples so it gradually adjusts its internal numbers until its outputs are good. Each example may be used anywhere from a few times to billions of times.
  - Those internal numbers are its **parameters** (or **weights**). A weight is a value the model multiplies an input by. Training finds good weights.
- **Probability:** an LLM's outputs are "probability distributions over tokens."
  - A **token** is the small chunk of text an LLM actually reads and writes. It can be a whole word, part of a word, a single character, or even a byte.
  - Usage and limits are usually counted in tokens, not words. (Google's glossary gives the example "dogs like cats" as three word tokens.)
- **Python:** almost every agent tool is Python-first.

Without this base, you can't debug or evaluate these systems well.

*Analogy:* This stage is the foundation of a house. You don't see it once the house is built, but everything above rests on it.

### Key ideas in plain words
**Data words**
- **Dataset:** a collection of data, often arranged like a spreadsheet. Each row is one record, and each column is one kind of information (for example, height or weight).
- **Example:** one row of a dataset: the input values, and sometimes the correct answer.
- **Label:** the "correct answer" attached to an example. For instance, "spam" or "not spam" for an email.

**Math and measurement words**
- **PCA (principal component analysis):** a math technique that shrinks data down to fewer dimensions. It's used to explore data, to make pictures (visualizations) of it, and to prepare it for later work.
- **MLE (maximum likelihood estimation):** a way to estimate the settings of a probability pattern from data you've observed. It picks the settings that make that data most likely.
- **MAP (maximum a posteriori) estimation:** a variant of MLE that also builds in a "prior." The source calls it "a regularization of maximum likelihood estimation."
- **Precision and recall:** measures of how well a system performs when it pulls items out of a collection.

> **Gap:** Many Stage 1 words still have no sourced definition, including vector, matrix, derivative, gradient, eigenvalue, Bayes' rule, supervised vs. unsupervised learning and regression. The research points to the 3Blue1Brown videos and the Coursera math courses to learn them.

### A simple example
One project in the research: build a small **command-line (CLI)** Python app. A command line, or terminal, is a way of using a computer by typing text commands one line at a time, instead of clicking buttons. The app reads a data file (CSV or **JSON**), cleans it up with pandas, trains a "classifier," and reports its precision, recall and F1.
- **JSON** is a common, human-readable text format for storing and sending data as name–value pairs (e.g. `"city": "Paris"`). AI tools use it a lot.

- **F1 score:** one number that combines precision and recall. It is their *harmonic mean*, a kind of average that weights the two equally; when precision and recall are close, F1 is roughly their average. *Source 58: Wikipedia, "Precision and recall" (F-measure section).*

### Beginner-friendly resources
- [3Blue1Brown – Linear Algebra (Essence of LA)](https://www.3blue1brown.com/?topic=linear-algebra) — Free. Visual intuition for vectors and transformations.
- [Kaggle Learn](https://www.kaggle.com/learn) — Free. Short, hands-on micro-courses (Python, pandas, intro ML).
- [Machine Learning Specialization (Andrew Ng, DeepLearning.AI + Stanford Online / Coursera)](https://www.coursera.org/specializations/machine-learning-introduction) — Paid (financial aid available). Beginner level, 3 courses. Provider figure: "2 months at 10 hours a week."
- [Mathematics for Machine Learning and Data Science Specialization (DeepLearning.AI / Coursera)](https://www.coursera.org/specializations/mathematics-for-machine-learning-and-data-science) — Paid (financial aid available). Provider figure: "12 weeks … at 5 hours a week."

---

## Stage 2 — Deep Learning

### What it is
Stage 2 covers **neural networks**: their building blocks, how they're trained, and the PyTorch tools used to train them. A **neural network** is a kind of model loosely inspired by how brain cells connect. It's built from layers of simple connected units. A "deep" neural network has many layers. **Time:** about 1.5–3 months (estimate).

### Why it matters
The research says **LLMs are deep neural networks**. Once you know how training works, you can reason about how a model behaves and how it can be adjusted.

### Key ideas in plain words
**Types of network**
- **MLP (multilayer perceptron):** a kind of neural network made of connected "neurons," arranged in layers.
- **CNN (convolutional neural network):** a network that learns features by tuning filters. It has long been the standard for computer vision. In some cases it has recently been replaced by the transformer (Stage 3).
- **RNN (recurrent neural network):** a network built for data that comes in a sequence. What it produces at one step is fed back in at the next step.
- *(editorial)* You study CNNs and RNNs mostly "for context," to understand why transformers replaced earlier designs. You don't need to master them for agent work.

**How networks learn**
- **SGD (stochastic gradient descent):** a step-by-step method for improving a model. Each step uses an estimate worked out from a randomly chosen part of the data, instead of all of it.
- **Early stopping:** rules that tell you how many training rounds you can run before the model starts to "over-fit."
  - **Overfitting** is when a model memorizes its training data too closely, so it does poorly on new data. Lucy's glossary compares it to a student who memorized the practice test but can't answer new questions.

  *Analogy:* Early stopping is like a kitchen timer that tells you when to take the cake out. Leave it in too long and it's spoiled.

**Tools**
- **micrograd:** a tiny engine by Andrej Karpathy that implements backpropagation, with a small neural-network library on top. They are about 100 and 50 lines of code.
- **Gradio:** a free Python package for quickly building a demo or web app for a model. You need no web-design or hosting experience.

> **Gap:** The sources still don't define "neuron," "training loop," "loss" or "backpropagation" in plain words. The Stage 2 courses teach them.

### A simple example
In the fast.ai course, you adjust an existing image or text classifier for your own task. Then you share it as a Gradio web demo that anyone can try.

### Beginner-friendly resources
- [fast.ai – Practical Deep Learning for Coders](https://course.fast.ai/) — Free. 9 lessons of about 90 minutes each. Prerequisite, quoted from the site: "The only prerequisite is that you know how to code (a year of experience is enough), preferably in Python, and that you have at least followed a high school math course."

  **Beginner takeaway (from Lucy's addendum):** fast.ai expects some coding experience, so a non-coder should do Stage 0/Stage 1 first.
- [3Blue1Brown – Neural Networks](https://www.3blue1brown.com/?topic=neural-networks) — Free. Visual intuition for how networks learn.
- [Andrej Karpathy – Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) — Free. Builds everything from scratch in code, up to a GPT-style language model.

---

## Stage 3 — LLMs and Transformers

### What it is
This stage explains how LLMs (large language models, defined at the top of these notes) work inside. Its centerpiece is the **transformer**, from the 2017 paper *Attention Is All You Need* (Vaswani et al.), which the research calls "the original Transformer paper." **Time:** about 1.5–2.5 months (estimate).

### Why it matters
The research calls the LLM **the "brain" of every agent**. Its strengths and limits shape every later design choice. Three matter most:
- **Its context window.** This is the maximum number of tokens a model can take into account at one time, including your conversation and any documents. Anything beyond that limit, the model can't "see." The research also calls the context window the model's short-term memory.
- **Hallucination.** This is when an AI states something false or made-up as if it were fact. Google's example is a model claiming Barack Obama died in 1865.
- **How reliably it gives answers in a fixed format.**

### Key ideas in plain words
**Attention: Query, Key and Value (Q/K/V)**
- For each word, the transformer makes three vectors: a **query**, a **key** and a **value**.
- It scores how well each word's query matches every word's key.
- It uses those scores to blend the values together.

*Analogy:* Think of a library. Your **query** is what you're looking for. The **keys** are the labels on the books. The **values** are what's inside them. Books whose labels match your question best get the most of your attention.

**Training stages and using a model**
- **Pretraining:** the first, very large training stage. Here a language model reads a huge amount of unlabeled text and learns to predict the next word.
- **Fine-tuning:** taking a model that was already trained for one job and training it a bit more, so it does a narrower, more specific job.
- **Inference:** *using* a trained model, as opposed to training it. For an LLM, inference means taking your prompt (see Stage 4) and generating a response.
- **Temperature:** a setting that controls how random a model's output is. Higher means more varied and surprising; lower means more predictable.

**Adjusting a model cheaply**
- **PEFT (Parameter-Efficient Fine-Tuning):** methods that adjust only a small number of a model's parameters, not all of them.
- **LoRA (Low-Rank Adaptation):** a PEFT-style method. It "freezes" the original model and adds small trainable pieces to each layer. That greatly cuts down how much has to be trained.

*Analogy:* LoRA is like adding sticky notes to a textbook instead of reprinting the whole book.

**Facts and figures**
- **Hugging Face LLM Course:** 12 chapters, about 1 week each at 6–8 hours. That's roughly 12 weeks, or 72–96 hours in total (Lucy's arithmetic from the provider's figure).

> **Gap:** The sources still don't explain the "top-p" setting, or what "supervised fine-tuning" means beyond its name.

### A simple example
A project from the research: load a free, open model and compare its answers under different generation settings. While you're at it, look at how it splits text into pieces (tokenization).

### Beginner-friendly resources
- [The Illustrated Transformer (Jay Alammar)](https://jalammar.github.io/illustrated-transformer/) — Free. A step-by-step visual walkthrough.
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) — Free. Provider figure: each chapter is about 1 week at 6–8 hrs. Prerequisite (course page): it "Requires a good knowledge of Python" and "Is better taken after an introductory deep learning course".
- [Attention Is All You Need (Vaswani et al., 2017)](https://arxiv.org/abs/1706.03762) — Free paper. The original Transformer paper. It's advanced, so save it for later.

---

## Stage 4 — Prompt Engineering

### What it is
Stage 4 covers **prompt engineering**: the skill of writing and structuring prompts so a generative AI model produces the output you want.
- A **prompt** is any text you give an LLM as input to steer what it does. It can be one short phrase or something as long as a whole novel.
- **Generative AI** is AI that *creates* new things (text, images, audio, video or computer code) by learning the patterns in the data it was trained on.

The research's key ideas include clear instructions, giving examples, step-by-step reasoning, structured output and defending against attacks. **Time:** about 2–4 weeks (estimate), then ongoing practice.

### Why it matters
- **The instructions are the program.** The research says that in an agent, the system prompt and the tool descriptions *are* the program.
- **Measure before you tinker.** Anthropic's guide recommends deciding what "success" looks like, and how you'll test for it, *before* you start adjusting prompts.

*Analogy:* Write the answer key before you grade the test. Otherwise you can't tell whether a change helped.

### Key ideas in plain words
**Ways to prompt**
- **Zero-shot prompting:** you ask without giving any examples.
- **Few-shot prompting:** you include a few worked examples in the prompt.

  *Analogy:* Few-shot prompting is like showing a new coworker two filled-in forms before asking them to fill one out.
- **Chain-of-thought:** examples that show step-by-step reasoning ("Let's think step by step") before the answer.

**Tools and practices**
- **Pydantic:** a widely used Python tool for checking that data has the shape you expect.
- **Red team:** a group that plays the attacker and then reports back, so defenses can be improved.

> **Gap:** The sources don't define "system prompt" vs. "user prompt," "role prompting" or "prompt versioning."

### A simple example
A project from the research:
1. Write 20–50 test cases for a task, such as pulling details out of text.
2. Change your prompt a little at a time.
3. Keep score for each version, so you can see which one works best.

### Beginner-friendly resources
- [Prompt Engineering Guide (DAIR.AI)](https://www.promptingguide.ai/) — Free. Techniques, papers, model-specific guides.
- [Anthropic – Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) — Free. Links to best practices and interactive tutorials.
- [Anthropic courses (GitHub)](https://github.com/anthropics/courses) — Free. Includes a prompt-engineering tutorial.

---

## Stage 5 — RAG: Letting the AI Look Things Up

### What it is
**RAG (retrieval-augmented generation)** lets a model use private or up-to-date information without being retrained. It was introduced in a 2020 paper by Lewis et al. **Time:** about 3–5 weeks (estimate).

### Why it matters
- **New knowledge without retraining.** The original RAG paper showed that swapping the collection the model searches changes what the model knows.
- **The basis of agent memory.** An agent's "long-term memory" is usually built from the same parts.

### Key ideas in plain words
**Two kinds of memory (terms from the RAG paper)**
- **Parametric memory:** the knowledge stored inside the trained model itself.
- **Non-parametric memory:** a separate, searchable index of documents. In the paper, this was a searchable version of Wikipedia.

*Analogy:* An open-book exam. Parametric memory is what the student has memorized. Non-parametric memory is the book on the desk. Swap the book, and the student can answer different questions.

**Preparing documents**
- **Chunking:** splitting documents into pieces. The RAG paper cut each Wikipedia article into 100-word chunks, making 21 million documents.

**Searching**
- **Nearest-neighbour search:** finding the item in a collection that is closest to a given one.
- **ANN (approximate nearest neighbour) search:** search that gives up a little accuracy for a big gain in speed. Lucy's source describes ANN *algorithms* doing this. An **algorithm** is a precise, step-by-step set of instructions that solves a problem and finishes after a limited number of steps, much like a recipe.

  *Analogy:* ANN search is like asking a librarian for "about the right shelf" rather than checking every single book.
- **HNSW and FAISS:** two techniques used for this kind of fast approximate search. The RAG paper used both together.
- **BM25:** a ranking method search engines use to judge how relevant a document is to a search query. The RAG paper calls it "word overlap-based."
- **Hybrid search (editorial):** combining keyword search (like BM25) with meaning-based search.
- **recall@k (editorial):** of all the relevant documents, the share that show up in the top *k* results.

> **Gap:** The sources still don't define "vector database" in plain words. They also give no formulas for the RAG-checking measures "faithfulness" and "answer relevance." (Embeddings are defined in Stage 1.)

### A simple example
The research's main project is "chat with your docs." You split your documents into chunks, store them so they can be searched, find the chunks that match a question, and have the model answer while citing those chunks.

### Beginner-friendly resources
*"Open source" means software published together with its source code, so anyone can use, study, change and share it, subject to its license (for example, MIT).*

- [Sentence Transformers (SBERT) docs](https://www.sbert.net/) — Free. For meaning-based ("semantic") search.
- [LlamaIndex framework docs](https://developers.llamaindex.ai/python/framework/) — Free (open source). A framework focused on data and RAG.
- [Ragas docs](https://docs.ragas.io/en/stable/) — Free (open source). For checking how well a RAG system works.

---

## Stage 6 — Tools: Letting the AI Take Action

### What it is
**Tool calling** (also called function calling) lets an LLM use tools, such as a calculator, a web search or a file reader. Lucy's beginner glossary calls this **tool use**: letting an AI model call functions or services, such as a web search or a weather lookup. The model decides when to call a tool based on your request and the tool's description, and the result is fed back to it so it can answer.

Two words you'll meet here:
- An **API (application programming interface)** is a defined way for one program to talk to another and use its services. For example, your code can send a prompt to an AI company's API and get the model's answer back.
- An **API key** is a secret code that identifies you to an API and proves you're allowed to use it, much like a password for your program. Keep it private.

**Time:** about 2–4 weeks (estimate).

### Why it matters
Tools are what let an LLM ***act***, not just talk. Tools matter as much as prompts: Anthropic says that while building an agent for SWE-bench, it spent more time improving the tools than the overall prompt. (**SWE-bench** is a test made of 2,294 real software problems taken from GitHub.)

### Key ideas in plain words
**The tool-calling loop.** The research describes five steps:
1. Your app sends a request to the model.
2. The model asks for a tool.
3. Your app runs the tool.
4. Your app sends the result back.
5. The model gives its final answer.

OpenAI calls this "a multi-step conversation between your app and the model."

*Analogy:* A chef (the model) asks a kitchen assistant (your app) to fetch an ingredient. The assistant brings it back, and the chef finishes the dish.

**Describing a tool**
- **JSON Schema:** a standard way to describe exactly what information a tool needs.

  *Analogy:* JSON Schema is like a form with labeled boxes.
- **Strict mode:** a setting that makes the model's tool requests reliably match that description, instead of being "best effort."

  *Analogy:* Strict mode is a form that won't accept a missing box.

**Controlling tool use**
- **`tool_choice`:** a setting that controls tool use. It has five settings:
  - **Auto** (the default): the model decides whether to use zero, one or several tools.
  - **Required:** the model must use at least one tool.
  - **Forced:** the model must use one specific tool.
  - **`allowed_tools`:** the model may only use a chosen subset of the tools.
  - **`none`:** works as if the model had no tools at all.
- **Keep the list short.** OpenAI's guide suggests aiming for fewer than 20 tools available at once.

**Designing good tools**
- **"Poka-yoke" tools:** tools designed to be mistake-proof.

  *Analogy:* Poka-yoke is like a plug that only fits into the socket one way.

### A simple example
A project from the research: build a tool-using loop by hand with three tools (a calculator, web search and a file reader). Add retries for when something goes wrong.

### Beginner-friendly resources
- [OpenAI – Function calling guide](https://developers.openai.com/api/docs/guides/function-calling) — Free docs (API usage paid). The 5-step flow and best practices.
- [Anthropic – Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents) — Free. How to design tools for agents.

---

## Stage 7 — How Agents Plan, Remember and Work in Teams

### What it is
This stage covers agent "architecture": how you organize an AI system's planning, memory and teamwork. **Time:** about 1–2 months (estimate).

### Why it matters
Architecture decides how **reliable, costly and fast** an agent is. Anthropic's advice: **"finding the simplest solution possible, and only increasing complexity when needed."**

Lilian Weng, whose 2023 survey the research relies on, names three core challenges:
- finite context,
- planning over long tasks, and
- the reliability of natural-language interfaces.

### Key ideas in plain words
**Workflows vs. agents (Anthropic's definitions)**
- A **workflow** follows "predefined code paths": the steps are fixed in advance.
- An **agent** decides its own steps and tool use as it goes.

*Analogy:* A workflow is following a recipe card step by step. An agent is a cook who decides what to do next based on what's in the fridge.

**Anthropic's five workflow patterns**
1. **Prompt chaining:** each AI step works on the output of the step before.
2. **Routing:** sort the request first, then send it to the right specialist step.

   *Analogy:* Routing is like a receptionist sending you to the right desk.
3. **Parallelization:** split a job into parts that run at the same time ("sectioning"), or run the same job several times and compare ("voting").
4. **Orchestrator–workers:** a lead AI breaks the task down, hands out the pieces and combines the results.
5. **Evaluator–optimizer:** one AI drafts, another reviews and gives feedback, in a loop.

   *Analogy:* Evaluator–optimizer is like a writer and an editor passing a draft back and forth.

**Planning methods**
- **ReAct ("reasoning + acting"):** the agent repeats a cycle of thinking, acting and observing what happened. The ReAct paper (Oct 2022) reported **absolute** success-rate gains of 34% on a household text game (ALFWorld) and 10% on a shopping website test (WebShop), compared with baseline methods. "Absolute" means 34 and 10 percentage points, not a relative increase.
- **Tree of Thoughts:** explores several reasoning paths at each step, forming a tree.
- **Reflexion:** gives an agent memory and the ability to reflect on its own attempts.

**Memory**
- **Short-term memory** is the context window.
- **Long-term memory** is a searchable store (as in Stage 5).
- In the **Generative Agents** study, 25 AI-controlled characters lived in a Sims-like world. They kept a "memory stream," a running log of their experiences in plain language. They recalled memories by how recent, important and relevant they were.

*Analogy:* Short-term memory is the notepad on your desk. Long-term memory is the filing cabinet.

> **Gap:** The sources don't define "handoffs," "manager/specialist structures," "stopping conditions" or "human-in-the-loop checkpoints" in plain words. They describe the ALFWorld and WebShop tests only through the ReAct paper.

### A simple example
A project from the research: build a three-agent team (planner → researcher → writer) and compare it with a single agent on the same tasks.

### Beginner-friendly resources
- [Anthropic – Building effective agents (Dec 2024)](https://www.anthropic.com/engineering/building-effective-agents) — Free. Defines the workflow patterns and when to use agents.
- [Hugging Face AI Agents Course](https://huggingface.co/learn/agents-course) — Free, with a free certificate. Provider figure: about 3–4 hrs/week per chapter. The five main units come to about 15–20 hours (Lucy's arithmetic).
- [Lilian Weng – LLM Powered Autonomous Agents (2023)](https://lilianweng.github.io/posts/2023-06-23-agent/) — Free. A well-known survey of planning, memory and tool use.

---

## Stage 8 — Frameworks and MCP: Ready-Made Building Blocks

### What it is
**Frameworks** such as LangGraph, CrewAI, AutoGen and the OpenAI Agents SDK help with building agents. An **SDK (software development kit)** is a bundle of tools, installed as one package, that makes it easier to build software for a particular platform or service.

**MCP (Model Context Protocol)** is a free open standard. The research says it is how tools are increasingly plugged into agents. Its website describes it as **"Like a USB-C port for AI applications."**

*Analogy:* Think of one standard plug that many devices can use.

**Time:** about 1–2 months (estimate).

### Why it matters
- **The upside:** frameworks speed up the "plumbing."
- **The downside:** Anthropic warns they add layers that can hide what is really being sent to and from the model. It suggests starting "by using LLM APIs directly."
- **The advice:** learn one framework well, and learn MCP, because MCP is increasingly how tools get plugged into agents.

*Analogy:* A framework is like a meal kit. It saves time, but you don't always see what's in each packet.

### Key ideas in plain words
**The three MCP roles**
- **Host:** the AI app you use. It manages one or more clients.
- **MCP client:** keeps a connection to one server and fetches information from it for the host.
- **MCP server:** a program that provides information and tools to clients.

**Two framework features**
- **Guardrails** (in the OpenAI Agents SDK): safety checks that run alongside the agent and stop it quickly if a check fails.
- **LangGraph:** described as "very low-level." Its own docs suggest that beginners start with LangChain's ready-made agents instead.

**Suggested order for beginners (editorial)**
1. Start with raw LLM APIs.
2. Then try the OpenAI Agents SDK or LangChain agents.
3. Move to LangGraph when you need more control.

> **Gap:** The sources have no independent, side-by-side comparison of the frameworks. They also don't define "checkpoint" or "tracing" in plain words.

### A simple example
A project from the research: build an MCP server that offers your own tools (such as your notes), then connect it to an app that supports MCP.

### Beginner-friendly resources
- [DeepLearning.AI – Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/courses/multi-ai-agent-systems-with-crewai/) — Free short course. Beginner level, 3h1m, 18 video lessons.
- [Hugging Face MCP Course](https://huggingface.co/learn/mcp-course) — Free. Learn MCP "in theory, design, and practice," with a certificate of completion.
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) — Free open standard.
- [OpenAI Agents SDK (Python)](https://openai.github.io/openai-agents-python/) — Free, open source (MIT); model API usage billed per token.

---

## Stage 9 — Testing and Safety

### What it is
This stage teaches you to **measure** how well an agent works and to **protect** it from misuse. **Time:** about 3–6 weeks (estimate), then continuously.

### Why it matters
Agents take real actions, and their mistakes can add up over many steps. Anthropic warns of "higher costs, and the potential for compounding errors" and recommends "extensive testing in sandboxed environments."

**A cautionary tale: ChemCrow.** ChemCrow is an LLM given 13 expert-designed tools for organic synthesis, drug discovery and materials design. It was compared with GPT-4:
- When AI judges graded both, they said the two performed about the same.
- When human experts graded them, ChemCrow did far better.
- **The lesson:** don't trust AI judges blindly.

*Analogy:* It's like having a non-expert judge a cooking contest. The professional chefs might rank the dishes very differently.

### Key ideas in plain words
**The OWASP Top 10 for LLMs (2025).** OWASP publishes this threat-model checklist of ten risks:

| ID | Risk |
|---|---|
| LLM01 | Prompt Injection |
| LLM02 | Sensitive Information Disclosure |
| LLM03 | Supply Chain |
| LLM04 | Data and Model Poisoning |
| LLM05 | Improper Output Handling |
| LLM06 | Excessive Agency |
| LLM07 | System Prompt Leakage |
| LLM08 | Vector and Embedding Weaknesses |
| LLM09 | Misinformation |
| LLM10 | Unbounded Consumption |

**Prompt injection, the number-one risk, comes in two forms:**
- **Direct injection:** a user's own input changes how the model behaves.
- **Indirect injection:** the model takes in input from outside sources, such as websites or files, and that input changes its behavior.

OWASP adds that RAG and fine-tuning "do not fully mitigate" prompt injection.

*Analogy:* Indirect injection is like a note hidden inside a document your assistant reads, saying "ignore your boss and do this instead."

**Defenses the research lists:** least privilege, sandboxing, human approval for actions that can't be undone, and guardrails.

**Three risks explained in full** (quoted from OWASP's detail pages, via Lucy's addendum):
- **LLM07 System Prompt Leakage:** "The system prompt leakage vulnerability in LLMs refers to the risk that the system prompts or instructions used to steer the behavior of the model can also contain sensitive information that was not intended to be discovered." "When discovered, this information can be used to facilitate other attacks. It's important to understand that the system prompt should not be considered a secret, nor should it be used as a security control."
  - *In plain words:* the system prompt is the set of instructions used to steer the model. It can contain sensitive information, so OWASP says it shouldn't be treated as a secret or used as a security control.
- **LLM08 Vector and Embedding Weaknesses:** "Vectors and embeddings vulnerabilities present significant security risks in systems utilizing Retrieval Augmented Generation (RAG) with Large Language Models (LLMs). Weaknesses in how vectors and embeddings are generated, stored, or retrieved can be exploited by malicious actions (intentional or unintentional) to inject harmful content, manipulate model outputs, or access sensitive information."
  - *In plain words:* in RAG systems, weaknesses in how embeddings are made, stored or retrieved can be exploited to inject harmful content, manipulate the model's outputs or reach sensitive information.
- **LLM10 Unbounded Consumption:** "Unbounded Consumption occurs when a Large Language Model (LLM) application allows users to conduct excessive and uncontrolled inferences, leading to risks such as denial of service (DoS), economic losses, model theft, and service degradation. The high computational demands of LLMs, especially in cloud environments, make them vulnerable to resource exploitation and unauthorized usage."
  - *In plain words:* an LLM app lets users run too many uncontrolled inferences (uses of the model), which can lead to denial of service, economic losses, model theft and service degradation. Cost caps (Stage 10) help here.

> **Gap:** The sources fully define only four of the ten OWASP risks (LLM01, LLM07, LLM08 and LLM10). The rest have cut-off summaries. The sources also don't explain "least privilege" or "sandboxing" in plain words.

### A simple example
A project from the research:
1. Hide harmful instructions inside a document your RAG agent will read.
2. See whether the agent follows them.
3. Add defenses and test again.

### Beginner-friendly resources
- [OWASP Top 10 for LLM & GenAI Apps (2025)](https://genai.owasp.org/llm-top-10/) — Free. A checklist of threats.
- [Hugging Face Agents Course – Bonus Unit 2: Agent Observability & Evaluation](https://huggingface.co/learn/agents-course) — Free. Direct unit link: https://huggingface.co/learn/agents-course/bonus-unit2/introduction
- [Langfuse docs](https://langfuse.com/docs) — Free OSS / paid cloud. Open-source tracing, evals and prompt management. (**Cloud computing**, or "the cloud," means renting computers, storage and services over the internet on demand, instead of owning the machines yourself. The sources don't spell out "OSS.")

---

## Stage 10 — Launching Real Agents

### What it is
This stage takes an agent from a demo to production. **Time:** about 1–2 months (estimate) for a first production-grade project. After that, mastery comes from shipping and improving.

### Why it matters
The research says a demo agent and a production agent are very different things. Chip Huyen's book *AI Engineering* (Ch. 10) builds up a production design in five numbered steps:
1. Enhance context.
2. Add guardrails.
3. Add a model router and gateway.
4. Cache to cut waiting time.
5. Add agent patterns.

**Then:** monitor the agent and collect user feedback. These come after the five numbered steps, as follow-on topics rather than a step of their own.

*Analogy:* A demo is a home-cooked dinner for friends. Production is running a restaurant every night.

### Key ideas in plain words
- **Caching:** storing data so future requests for it can be answered faster.

  *Analogy:* Caching is like keeping the things you use most on the kitchen counter instead of in the basement.
- **Message queue:** a component that lets programs pass messages to each other through a queue.

  *Analogy:* A message queue is like the ticket line at a deli counter.
- **Model routing:** Anthropic's routing pattern sends easy, common questions to smaller, cheaper models and hard, unusual ones to more capable models.
- **Cost caps:** limits on spending. These help with OWASP risk LLM10, unbounded consumption.

> **Gap:** The sources still don't define "container," "secrets management" or "gateway" in plain words. They give no resource for secrets management or cloud hosting, and no specific queue products.

### A simple example
One capstone from the research is a **customer-support agent**. It:
- answers from a knowledge base (RAG),
- looks up orders, and
- *requests* refunds, which a human must approve.

It has a set of tests, and it runs with cost limits for each conversation. Anthropic names customer support as a strong use case for agents.

### Beginner-friendly resources
- [FastAPI docs](https://fastapi.tiangolo.com/) — Free. A Python framework for serving agents.
- [Docker – Get started](https://docs.docker.com/get-started/) — Free. Package your app and ship it.

---

## Plain-English Glossary

*Each entry restates a definition from the research or the addendum in simpler words. Entries marked (editorial) are Lucy's own wording.* *Entries with a "Source" note come from Lucy's "Beginner basics glossary," which paraphrases the Google Machine Learning Glossary, the Anthropic glossary or Wikipedia. The number in brackets is the stage where the term first appears or is taught.*

| Term | Plain-English meaning |
|---|---|
| **Agent (AI agent)** | Software that can reason about what you ask, plan steps and take actions for you, rather than only replying with text. *Source: Google ML Glossary; Wikipedia, "Intelligent agent".* Anthropic's version: an AI system that decides its own steps and which tools to use. [How to use, 7] |
| **AI (artificial intelligence)** | Computer systems that can do tasks we normally link to human intelligence, such as learning, reasoning, solving problems, perceiving things and making decisions. Also the research field that builds them. *Source: Wikipedia, "Artificial intelligence".* [How to use] |
| **Algorithm** | A precise, step-by-step set of instructions that solves a problem and finishes after a limited number of steps, much like a recipe. *Source: Wikipedia, "Algorithm".* [5] |
| **ANN (approximate nearest neighbour) search** | Search that gives up a little accuracy for a big gain in speed. [5] |
| **API (application programming interface)** | A defined way for one program to talk to another and use its services, such as sending a prompt to an AI company's API and getting the answer back. *Source: Wikipedia, "API".* [6] |
| **API key** | A secret code that identifies you to an API and proves you're allowed to use it, much like a password for your program. Keep it private. *Source: Wikipedia, "API key".* [6] |
| **BM25** | A ranking method search engines use to judge how relevant a document is to a query. [5] |
| **Caching** | Storing data so future requests for it can be answered faster. [10] |
| **Chain-of-thought** | Prompt examples that show step-by-step reasoning before the answer. [4] |
| **Chatbot** | A program or website you have a conversation with, by text or voice. Modern chatbots run on LLMs. *Source: Wikipedia, "Chatbot".* [How to use] |
| **ChemCrow** | An LLM given 13 expert-designed tools for chemistry tasks such as drug discovery. [9] |
| **Chunking** | Splitting documents into pieces, such as 100-word chunks. [5] |
| **Cloud computing ("the cloud")** | Renting computers, storage and services over the internet on demand, instead of owning the machines yourself. *Source: Wikipedia, "Cloud computing".* [9, 10] |
| **CNN (convolutional neural network)** | A neural network that learns features by tuning filters, long standard for computer vision. [2] |
| **Code (source code)** | The human-readable text instructions that programmers write, which a computer then runs. *Source: Wikipedia, "Source code".* [0] |
| **Command line / terminal (CLI)** | A way of using a computer by typing text commands, one line at a time, instead of clicking buttons. *Source: Wikipedia, "Command-line interface".* [1] |
| **Context window** | The maximum number of tokens a model can take into account at one time; anything beyond it, the model can't "see." The research also calls it the model's short-term memory. *Source: Wikipedia, "Context window"; Google ML Glossary.* [3, 7] |
| **Dataset** | A collection of data, often arranged like a spreadsheet: each row is one record and each column is one kind of information. *Source: Google ML Glossary; Wikipedia, "Data set".* [1] |
| **Direct prompt injection** | When a user's own input changes how the model behaves. [9] |
| **Early stopping** | Rules for how many training rounds to run before the model starts to over-fit. [2] |
| **Embedding** | A way of turning something like a word or document into a list of numbers, so things with similar meanings get similar numbers and can be compared. *Source: Wikipedia, "Embedding (machine learning)".* [1, 5] |
| **Evaluator–optimizer** | One AI drafts, another reviews and gives feedback, in a loop. [7] |
| **Example** | One row of a dataset: the input values, and sometimes the correct answer. *Source: Google ML Glossary.* [1] |
| **Few-shot prompting** | Giving the model a few worked examples in the prompt. [4] |
| **Fine-tuning** | Taking an already-trained model and training it a bit more so it does a narrower, more specific job. *Source: Wikipedia, "Fine-tuning (deep learning)".* [3] |
| **Generative Agents** | A study where 25 AI characters lived in a Sims-like world, with memory. [7] |
| **Generative AI** | AI that creates new things (text, images, audio, video or code) by learning patterns in the data it was trained on. *Source: Wikipedia, "Generative artificial intelligence" (Lucy notes the link redirects to the article "Generative AI").* [4] |
| **Git** | Software that tracks every version of your code over time, so you can undo changes and work with others. *Source: Wikipedia, "Git".* [not used in the stages] |
| **GPU (graphics processing unit)** | A computer chip first built for graphics. It can do many calculations at once, which makes it much faster than an ordinary processor for training and running AI. *Source: Wikipedia, "Graphics processing unit"; Google ML Glossary's "accelerator chip" entry. Caveat: Google's glossary has no standalone GPU entry, so this definition relies partly on Wikipedia.* [not used in the stages] |
| **Gradio** | A free Python package for quickly building a demo web app for a model. [2] |
| **Guardrails** | Input and safety checks that run alongside an agent and stop it quickly if a check fails. [8, 9] |
| **Hallucination** | When an AI states something false or made-up as if it were fact (Google's example: a model claiming Barack Obama died in 1865). *Source: Google ML Glossary; Wikipedia, "Hallucination (AI)".* [3] |
| **Hybrid search** | Combining keyword search with meaning-based search. (editorial) [5] |
| **Indirect prompt injection** | When outside input, such as a website or file, changes the model's behavior. [9] |
| **Inference** | Using a trained model, as opposed to training it. For an LLM, it means taking your prompt and generating a response. *Source: Google ML Glossary.* [3] |
| **JSON** | A common, human-readable text format for storing and sending data as name–value pairs (e.g. `"city": "Paris"`). *Source: Wikipedia, "JSON".* [1, 6] |
| **JSON Schema** | A standard way to describe exactly what data a tool needs. [6] |
| **Label** | The "correct answer" attached to an example, such as "spam" or "not spam" for an email. *Source: Google ML Glossary.* [1] |
| **Library** | Ready-made code that other people wrote and you can reuse in your own program. *Source: Wikipedia, "Library (computing)".* [0] |
| **LLM (large language model)** | An AI model trained on a huge amount of text so it can generate, summarize, translate and analyze language. LLMs power chatbots such as ChatGPT, Claude, Gemini and Grok. *Source: Wikipedia, "Large language model"; Google ML Glossary.* [How to use, 3] |
| **Long-term memory** | A searchable store an agent can look things up in. [7] |
| **LoRA (Low-Rank Adaptation)** | Freezing a model and adding small trainable pieces, so much less has to be trained. [3] |
| **Machine learning (ML)** | A part of AI where a program learns patterns from data, instead of a person writing every rule by hand, then uses them on new data. *Source: Google ML Glossary; Wikipedia, "Machine learning".* [1] |
| **MAP estimation** | A variant of MLE that also builds in a "prior." [1] |
| **MCP (Model Context Protocol)** | A free open standard, "Like a USB-C port for AI applications"; tools are increasingly plugged into agents through it. [8] |
| **MCP client** | Keeps a connection to one MCP server and fetches information for the host. [8] |
| **MCP host** | The AI app that manages one or more MCP clients. [8] |
| **MCP server** | A program that provides information and tools to MCP clients. [8] |
| **Memory stream** | A running log of an agent's experiences in plain language. [7] |
| **Message queue** | A component that lets programs pass messages to each other through a queue. [10] |
| **micrograd** | A tiny engine that implements backpropagation, with a small neural-network library on top. [2] |
| **MLE (maximum likelihood estimation)** | Estimating a probability pattern's settings by picking those that make the observed data most likely. [1] |
| **MLP (multilayer perceptron)** | A neural network of connected neurons arranged in layers. [2] |
| **Model** | The thing machine learning produces: a mathematical "machine" that takes an input and returns an output, such as a prediction. *Source: Google ML Glossary.* [How to use] |
| **Model routing** | Sending easy questions to smaller, cheaper models and hard ones to more capable models. [10] |
| **Nearest-neighbour search** | Finding the item in a collection that is closest to a given one. [5] |
| **Neural network** | A kind of model loosely inspired by how brain cells connect, built from layers of simple connected units. A "deep" one has many layers. *Source: Wikipedia, "Neural network (machine learning)"; Google ML Glossary.* [2] |
| **Non-parametric memory** | A separate searchable index of documents the model can consult. [5] |
| **Open source** | Software published together with its source code, so anyone can use, study, change and share it, subject to its license (e.g. MIT). *Source: Wikipedia, "Open source".* [5, 8] |
| **Orchestrator–workers** | A lead AI breaks down a task, hands out pieces and combines the results. [7] |
| **Overfitting** | When a model memorizes its training data too closely, so it does poorly on new data, like a student who memorized the practice test. *Source: Wikipedia, "Overfitting".* [2] |
| **OWASP Top 10 for LLMs** | A 2025 threat-model checklist of ten risks for LLM apps. [9] |
| **Parallelization** | Running parts of a job at the same time, or running the same job several times and comparing. [7] |
| **Parameters / weights** | The internal numbers a model learns during training. A weight is a value the model multiplies an input by. *Source: Google ML Glossary.* [1] |
| **Parametric memory** | Knowledge stored inside the trained model itself. [5] |
| **PCA (principal component analysis)** | A technique that shrinks data to fewer dimensions to explore, visualize or prepare it. [1] |
| **PEFT (Parameter-Efficient Fine-Tuning)** | Adjusting only a small number of a model's settings instead of all of them. [3] |
| **pip** | Python's tool for installing libraries ("packages"), downloaded from a public online collection called PyPI. *Source: Wikipedia, "pip (package manager)".* [1] |
| **Poka-yoke tool** | A tool designed to be mistake-proof. [6] |
| **Precision and recall** | Measures of how well a system performs when it pulls items out of a collection. [1] |
| **Pretraining** | The first, very large training stage, where a language model reads a huge amount of unlabeled text and learns to predict the next word. *Source: Anthropic glossary.* [3] |
| **Prompt** | Any text you give an LLM as input to steer what it does, from one short phrase to something as long as a novel. *Source: Google ML Glossary.* [4] |
| **Prompt chaining** | Each AI step works on the output of the step before. [7] |
| **Prompt engineering** | The skill of writing and structuring prompts so a generative AI model produces the output you want. *Source: Wikipedia, "Prompt engineering".* [4] |
| **Pydantic** | A Python tool for checking that data has the shape you expect. [4] |
| **Python** | A popular programming language designed to be easy to read and write. Most AI tools are built for it. *Source: Wikipedia, "Python (programming language)".* [0] |
| **Q/K/V (query, key, value)** | The three vectors the transformer makes for each word; query–key scores decide how the values are blended. [3] |
| **RAG (retrieval-augmented generation)** | Letting a model use private or fresh information without retraining. [5] |
| **ReAct** | An agent method that repeats a think → act → observe cycle. [7] |
| **recall@k** | Of all the relevant documents, the share that appear in the top *k* results. (editorial) [5] |
| **Red team** | A group that plays the attacker and reports back so defenses improve. [4] |
| **Reflexion** | A method that gives agents memory and the ability to reflect on their own attempts. [7] |
| **Repository (repo)** | The place where a project's files and their full version history are stored, for example a project on GitHub. *Source: Wikipedia, "Repository (version control)".* [not used in the stages] |
| **RNN (recurrent neural network)** | A network for sequences that feeds each step's output into the next step. [2] |
| **Routing** | Sorting a request and sending it to the right specialist step. [7] |
| **SDK (software development kit)** | A bundle of tools, installed as one package, that makes it easier to build software for a particular platform or service. *Source: Wikipedia, "Software development kit".* [8] |
| **SGD (stochastic gradient descent)** | Improving a model step by step, using estimates from random parts of the data. [2] |
| **Short-term memory** | The context window. [7] |
| **Strict mode** | A setting that makes the model's tool requests reliably match the tool's description. [6] |
| **SWE-bench** | A test of 2,294 real software problems taken from GitHub. [6] |
| **Temperature** | A setting that controls how random a model's output is: higher means more varied, lower means more predictable. *Source: Google ML Glossary.* [3] |
| **Token** | The small chunk of text an LLM reads and writes: a whole word, part of a word, a single character, or even a byte. Usage and limits are usually counted in tokens. *Source: Anthropic glossary; Google ML Glossary (which gives "dogs like cats" as three word tokens).* [1, 3] |
| **Tool calling** | Letting an LLM use tools through a multi-step conversation with your app. [6] |
| **Tool use (function calling)** | Letting an AI model call functions or services, such as a web search or a weather lookup. The model decides when to call a tool based on your request and the tool's description, and the result is fed back to it so it can answer. *Source: Anthropic tool use overview.* [6] |
| **`tool_choice`** | A setting that controls whether and which tools the model may use. [6] |
| **Training** | Showing a model many examples so it gradually adjusts its parameters until its outputs are good. *Source: Google ML Glossary.* [1] |
| **Transformer** | The architecture from the 2017 paper *Attention Is All You Need*. [3] |
| **Tree of Thoughts** | Exploring several reasoning paths at each step, forming a tree. [7] |
| **Workflow** | An AI system whose steps follow paths fixed in advance. [7] |
| **Zero-shot prompting** | Asking the model without giving any examples. [4] |

---

## Short Summary

- **Stage 0:** learn to program in Python.
- **Stages 1–3:** learn the math, the basics of machine learning and deep learning, and how LLMs (the "brain" of every agent) work.
- **Stages 4–5:** learn to instruct the model well, and let it look up information (RAG).
- **Stages 6–7:** give it tools so it can act, and organize its planning, memory and teamwork. Always use the simplest design that works.
- **Stage 8:** use frameworks and MCP to build faster.
- **Stage 9:** test carefully and defend against risks such as prompt injection.
- **Stage 10:** launch it for real.

**Time:** about **10–20 months** for Stages 1–10, or about **11–23 months** with Stage 0, at 8–10 hours a week. Start building small agents early.

---

## Easy Review Questions

### Stage 0
1. What four things should you be able to do before you skip Stage 0?
2. Which free course is "Designed for students with or without prior programming experience"?

### Stage 1
1. Which three areas of math does Stage 1 cover?
2. What do precision and recall measure?

### Stage 2
1. What does the research say LLMs are?
2. What does early stopping help you avoid?

### Stage 3
1. What is the name of the paper that introduced the transformer, and what year was it published?
2. In the library analogy, what plays the role of the query, the keys and the values?

### Stage 4
1. What's the difference between zero-shot and few-shot prompting?
2. What should you decide *before* you start adjusting prompts?

### Stage 5
1. What problem does RAG solve?
2. In the open-book-exam analogy, which part is parametric memory and which is non-parametric?

### Stage 6
1. Put the five steps of the tool-calling loop in order.
2. About how many tools does OpenAI suggest having available at once?

### Stage 7
1. What is the difference between a workflow and an agent?
2. Name the three steps in ReAct's repeating cycle.

### Stage 8
1. What everyday object does the MCP website compare MCP to?
2. What does Anthropic suggest starting with instead of a framework?

### Stage 9
1. What is the difference between direct and indirect prompt injection?
2. What does the ChemCrow story teach about AI judges?

### Stage 10
1. Name two things that help a real agent respond faster or cost less.
2. In the customer-support capstone, who must approve refund requests?

---

## References

This edition draws on 109 sources: the 42 from Lucy's original research (1–42), the 37 added in her addendum (43–79), and the 30 added by her "Beginner basics glossary" (80–109), 3 from her "QA additions for notes" (110–112), and 1 more from her beginner glossary (113). All were checked on 16 Oct 2026, according to the research.

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

### Added by Lucy's "Beginner basics glossary" (80–109)

80. Google Machine Learning Glossary: https://developers.google.com/machine-learning/glossary
81. Anthropic glossary: https://platform.claude.com/docs/en/about-claude/glossary
82. Wikipedia – Artificial intelligence: https://en.wikipedia.org/wiki/Artificial_intelligence
83. Wikipedia – Machine learning: https://en.wikipedia.org/wiki/Machine_learning
84. Wikipedia – Generative artificial intelligence: https://en.wikipedia.org/wiki/Generative_AI
85. Wikipedia – Algorithm: https://en.wikipedia.org/wiki/Algorithm
86. Wikipedia – Data set: https://en.wikipedia.org/wiki/Data_set
87. Wikipedia – Overfitting: https://en.wikipedia.org/wiki/Overfitting
88. Wikipedia – Neural network (machine learning): https://en.wikipedia.org/wiki/Neural_network_(machine_learning)
89. Wikipedia – Embedding (machine learning): https://en.wikipedia.org/wiki/Embedding_(machine_learning)
90. Wikipedia – Large language model: https://en.wikipedia.org/wiki/Large_language_model
91. Wikipedia – Chatbot: https://en.wikipedia.org/wiki/Chatbot
92. Wikipedia – Context window: https://en.wikipedia.org/wiki/Context_window
93. Wikipedia – Prompt engineering: https://en.wikipedia.org/wiki/Prompt_engineering
94. Wikipedia – Hallucination (AI): https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)
95. Wikipedia – Intelligent agent: https://en.wikipedia.org/wiki/Intelligent_agent
96. Wikipedia – Python (programming language): https://en.wikipedia.org/wiki/Python_(programming_language)
97. Wikipedia – Source code: https://en.wikipedia.org/wiki/Source_code
98. Wikipedia – Library (computing): https://en.wikipedia.org/wiki/Library_(computing)
99. Wikipedia – pip (package manager): https://en.wikipedia.org/wiki/Pip_(package_manager)
100. Wikipedia – Command-line interface: https://en.wikipedia.org/wiki/Command-line_interface
101. Wikipedia – JSON: https://en.wikipedia.org/wiki/JSON
102. Wikipedia – API: https://en.wikipedia.org/wiki/API
103. Wikipedia – API key: https://en.wikipedia.org/wiki/API_key
104. Wikipedia – Software development kit: https://en.wikipedia.org/wiki/Software_development_kit
105. Wikipedia – Open source: https://en.wikipedia.org/wiki/Open_source
106. Wikipedia – Git: https://en.wikipedia.org/wiki/Git
107. Wikipedia – Repository (version control): https://en.wikipedia.org/wiki/Repository_(version_control)
108. Wikipedia – Graphics processing unit: https://en.wikipedia.org/wiki/Graphics_processing_unit
109. Wikipedia – Cloud computing: https://en.wikipedia.org/wiki/Cloud_computing

### Added by Lucy's "QA additions for notes" (110–112)

110. OWASP LLM07:2025 System Prompt Leakage: https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/
111. OWASP LLM08:2025 Vector and Embedding Weaknesses: https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/
112. OWASP LLM10:2025 Unbounded Consumption: https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/

### Added by Lucy's "Beginner basics glossary" after QA (113)

113. Anthropic – Tool use overview: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview

*Caveats from Lucy:* the Generative AI link redirects to the article "Generative AI"; Google's glossary has no standalone GPU entry, so the GPU definition relies partly on Wikipedia and Google's "accelerator chip" entry; and the "dogs like cats" token example comes from the Google glossary. Source 59 (Wikipedia – Fine-tuning) is also cited by the beginner glossary and isn't listed twice.
