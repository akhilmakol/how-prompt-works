# 03. Attention

## The core idea

Attention helps a token decide which earlier tokens matter most.

When reading:

```text
Higher policy rates can slow borrowing.
```

the token `borrowing` should pay attention to:

- `rates`
- `policy`
- `slow`

Those words provide the context needed to predict or interpret the sentence.

## Why self-attention is useful

In ordinary reading, meaning often depends on relationships across the sentence.

Banking example:

```text
The central bank raised rates because inflation stayed high.
```

The word `raised` is closely tied to:

- `central bank`
- `rates`
- `inflation`

Self-attention lets the model connect those words, even if they are not adjacent.

## Scaled dot-product attention

The mechanism uses three learned views of each token:

- Query: what this token is looking for
- Key: what this token offers
- Value: the information this token carries

The model compares queries with keys to decide attention scores.

Then it uses those scores to blend the values.

## Causal masking

In a GPT-style model, a token is only allowed to attend to current and previous tokens.

That matters because during generation, the future has not happened yet.

Example prompt:

```text
a customer repays
```

The model can use `a`, `customer`, and `repays`, but it must not peek at future words.

## Intuition

Attention is like asking:

```text
For this word, which earlier words should I focus on most?
```

That question is one of the main reasons transformers work so well.
