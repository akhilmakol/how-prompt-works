# 02. Tokens and Embeddings

## Start with a banking prompt

Let us begin with a realistic prompt:

```text
You are a banking tutor. Explain a savings account in simple words.
```

A language model cannot read this raw sentence directly. It must first turn the prompt into tokens.

## Tokenization

Tokenization means splitting text into smaller pieces called tokens.

In this project, the tokenizer is word-level.

Example:

```text
["you", "are", "a", "banking", "tutor", ".", "explain", "a", "savings", "account", "in", "simple", "words", "."]
```

Then each token gets an integer ID.

Possible example:

```text
"banking" -> 14
"savings" -> 21
"account" -> 9
```

## Why tokenization matters for prompt engineering

When you change a prompt, you change the tokens the model sees.

Compare:

```text
Explain a loan.
Explain a loan like I am a first-time borrower.
```

The second prompt gives the model more tokens and more context. That often leads to a more useful answer.

## Embeddings

An embedding is a learned vector representation of a token.

Instead of treating `bank` as just an ID, the model learns a dense vector such as:

```text
[0.14, -0.82, 0.37, ...]
```

These vectors help the model learn relationships such as:

- `loan` being related to `credit`
- `deposit` being related to `savings`
- `rate` being related to `interest`

## Positional embeddings

Word order matters.

These two prompts use similar words but mean different things:

```text
Explain how the bank approves the loan.
Explain how the loan approves the bank.
```

Token embeddings alone do not represent order, so we add positional embeddings.

That helps the model know which token came first, second, third, and so on.

## Banking tutorial example

Consider this prompt:

```text
You are a loan officer. Explain mortgage interest to a first-time homebuyer.
```

The full pipeline is:

1. tokenize the prompt
2. map each token to an embedding vector
3. add position information
4. send the result into the transformer

Together, those steps convert a human-written banking prompt into model-ready input.
