# 08. Real-World LLMs

## How real-world LLMs differ

Production LLMs are much larger and more capable than this project.

They usually include:

- billions of parameters
- large-scale training corpora
- subword tokenizers
- advanced optimization methods
- better hardware and distributed training

## What stays the same

Even very large models still rely on the same core ideas:

- prompt input
- tokenization
- embeddings
- attention
- transformer layers
- next-token prediction

That is why learning with a tiny model is valuable.

## Prompt engineering in real systems

In real applications, prompts often combine:

- role instructions
- task instructions
- examples
- formatting constraints
- retrieved context

For a banking assistant, a real prompt might look like:

```text
You are a banking support assistant.
Summarize the following customer complaint in three bullet points.
Highlight any possible fraud signals.
Return the result as JSON.
```

This combines role-based, instruction-based, contextual, and output-constrained prompting.

## Why prompt engineering matters in larger models

Large models are better at following nuanced prompts because they have:

- broader world knowledge
- richer internal representations
- stronger instruction-following behavior
- more training on human-preference data

But even in advanced systems, prompt quality still matters.

## Beyond this repository

If you continue learning, explore:

- subword tokenization
- batching and mini-batch training
- sampling methods like top-k and temperature
- larger datasets
- evaluation metrics
- retrieval-augmented generation
- prompt templates and system prompts

## Final takeaway

A real LLM is much bigger than this toy project, but the first-principles story is the same.

Prompt quality shapes the input. The transformer processes the tokens. The model predicts one token at a time.

That is the main goal of this repository: make the big idea understandable.
