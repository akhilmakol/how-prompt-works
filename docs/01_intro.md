# 01. Introduction

## What is this project?

This project explains how a small language model works by using simple banking statements as training data.

Instead of jumping straight into giant production LLMs, we start with a tiny system that still captures the key ideas:

- break text into tokens
- turn tokens into vectors
- let tokens attend to each other
- train the model to predict the next token
- generate text one token at a time

## Why prompts matter

A prompt is the starting text we give the model.

Example:

```text
a bank offers
```

The model reads that prompt, looks at patterns it learned during training, and predicts the most likely next token.

Because the model was trained on banking fundamentals, it may continue with words like:

- `deposits`
- `loans`
- `customers`

## Intuition

You can think of the model as a pattern-completion machine. It does not understand banking like a banker. It learns statistical relationships between words and phrases.

Example:

```text
A savings account helps people store money.
```

After seeing many examples like that, the model learns that `savings` often appears near `account`, `interest`, and `money`.

## What you will learn

By the end of this repository, you should be able to explain:

- what tokenization does
- what embeddings are
- how self-attention works
- why transformer blocks are powerful
- how next-token training works
- how inference differs from training

## Banking scenario used throughout

Our examples focus on common banking topics:

- savings accounts
- checking accounts
- loans
- interest rates
- central banking
- risk management
- fraud detection

That gives us a practical domain with clear vocabulary and repeatable sentence structure.
