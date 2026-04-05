# how-prompt-works

`how-prompt-works` is a visual, interactive, beginner-friendly repository that explains prompt engineering and a small GPT-style language model from first principles using banking fundamentals as the teaching domain.

This repository is built around two connected ideas:

1. A prompt is the instruction or context you give an AI model.
2. A language model transforms that prompt into tokens, attention patterns, and next-token predictions.

## Overview

The project includes:

- A clean PyTorch implementation of a tiny GPT-style model
- End-to-end training and greedy text generation
- A Streamlit app for token exploration, generation, and attention visualization
- Step-by-step docs that explain prompting and model internals with banking examples
- Lightweight notebooks and tests to support learning and verification

## What Is a Prompt?

A prompt is simply the input or instruction you give to an AI model to guide its response.

A prompt can be:

- A question: `What is AI?`
- A command: `Write a Python function`
- A scenario: `Act as a product manager and create a roadmap`

The quality of the prompt directly impacts the quality of the output.

## Prompt Engineering in This Project

This project uses banking-themed prompts so the ideas stay concrete and practical.

Examples:

- `Explain what a savings account is in simple terms.`
- `You are a senior banking analyst. Explain liquidity risk.`
- `Our company builds fintech apps. Suggest features for a mobile banking app.`
- `Return the answer in JSON with fields: product_name, benefit, risk`

## Types of Prompts

### 1. Zero-shot Prompt

No examples are given. Only a direct instruction.

Example:

```text
Explain a savings account in simple language.
```

Best for simple tasks. Less accurate for harder tasks.

### 2. One-shot Prompt

You give one example to guide the model.

Example:

```text
English: deposit -> Category: banking term
English: mortgage -> Category:
```

Useful when you want the model to follow one clear pattern.

### 3. Few-shot Prompt

You provide multiple examples.

Example:

```text
Term: savings account -> Category: deposit product
Term: mortgage -> Category: loan product
Term: credit card -> Category:
```

Great for structured outputs and improved accuracy.

### 4. Instruction-based Prompt

You give direct instructions.

Example:

```text
Write a LinkedIn post about AI in banking in a professional tone.
```

This is one of the most common prompt styles in real applications.

### 5. Role-based Prompt

You assign a role or persona to the model.

Example:

```text
You are a senior data engineer. Explain fraud monitoring pipelines in banking.
```

This often improves domain-specific responses.

### 6. Chain-of-Thought Prompt

You encourage step-by-step reasoning.

Example:

```text
Explain step by step how interest on a savings account is calculated.
```

Helpful for logic, reasoning, and multi-step thinking.

### 7. Contextual Prompt

You provide relevant background information.

Example:

```text
Our company builds fintech apps for first-time borrowers. Suggest features for a loan application assistant.
```

This produces more relevant and tailored output.

### 8. Conversational Prompt

You use a back-and-forth format.

Example:

```text
User: I want help choosing a bank account.
AI: What matters most to you: low fees, high interest, or easy mobile access?
```

Useful for dynamic interactions.

### 9. Output-constrained Prompt

You define the desired response format.

Example:

```text
Return the answer in JSON with fields: product_name, benefit, risk
```

Important for automation, APIs, and agents.

### 10. Creative Prompt

You use prompting for ideation or storytelling.

Example:

```text
Write a short story about an AI banker teaching children about saving money.
```

Great for creative generation.

## Best Prompt Pattern

The strongest prompts often combine multiple prompt types.

Example:

```text
You are a fintech product manager.
Create a roadmap for an AI chatbot for loan applications.
Target users are first-time borrowers.
Output in table format.
```

This combines:

- role-based prompting
- instruction-based prompting
- contextual prompting
- output-constrained prompting

## Simple Framework to Write Better Prompts

Use this structure:

```text
[Role] + [Task] + [Context] + [Output Format]
```

Example:

```text
You are a fintech product manager.
Design a chatbot for loan applications.
Target users are first-time borrowers.
Output as a step-by-step flow.
```

## Why banking examples?

Banking is familiar, structured, and full of repeatable language patterns:

- `A savings account earns interest.`
- `A loan requires repayment over time.`
- `A central bank influences rates.`

These patterns make it easier to understand both prompt design and language model behavior.

## Model Architecture

The model follows a minimal GPT-style decoder-only design:

1. Word tokenizer converts text into integer token IDs.
2. Token embeddings map IDs into vectors.
3. Positional embeddings inject order information.
4. Causal self-attention lets each token attend only to current and previous tokens.
5. Transformer blocks combine attention, feed-forward layers, residual connections, and layer normalization.
6. A final linear layer projects hidden states to vocabulary logits.
7. Greedy decoding generates the next token one step at a time.

## Repository layout

```text
how-prompt-works/
|-- app/ui.py
|-- src/
|-- docs/
|-- visuals/
|-- data/sample.txt
|-- notebooks/
|-- tests/
`-- assets/
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Train the model

```bash
python -m src.train
```

This reads [data/sample.txt](data/sample.txt), trains a small language model, and saves `model.pth` in the repository root.

## Generate text

```bash
python -m src.generate --prompt "a bank offers" --max-new-tokens 20
```

## Run the Streamlit demo

```bash
streamlit run app/ui.py
```

The app includes:

- Text generation
- Tokenization explorer
- Attention heatmap visualization

If `model.pth` is missing, the app automatically trains a fresh model using the sample banking corpus.

## Learning path

Read the docs in order:

1. [docs/01_intro.md](docs/01_intro.md)
2. [docs/02_tokens_embeddings.md](docs/02_tokens_embeddings.md)
3. [docs/03_attention.md](docs/03_attention.md)
4. [docs/04_transformer.md](docs/04_transformer.md)
5. [docs/05_training.md](docs/05_training.md)
6. [docs/06_inference.md](docs/06_inference.md)
7. [docs/07_limitations.md](docs/07_limitations.md)
8. [docs/08_real_world_llms.md](docs/08_real_world_llms.md)

## Visual references

The files in [visuals/](visuals) are text-based placeholders that describe what each final diagram should illustrate:

- `cover.png`
- `pipeline.png`
- `tokenization.png`
- `embeddings.png`
- `attention.png`
- `transformer.png`
- `training.png`
- `inference.png`

## Tests

Run:

```bash
python -m unittest discover -s tests -v
```

The tests validate:

- Tokenizer encoding behavior
- Attention output shape
- Model forward pass shape and loss computation

## Streamlit demo use cases

The app is useful for teaching prompt engineering with banking scenarios such as:

- comparing simple and detailed prompts
- exploring how prompt wording changes generated output
- visualizing how prompt tokens are encoded
- inspecting attention for phrases like `the central bank sets rates`

## License

This repository uses the MIT License in [LICENSE](LICENSE).
