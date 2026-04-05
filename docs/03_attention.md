# 03. Attention

## Attention starts with the prompt

Suppose the prompt is:

```text
You are a banking tutor. Explain why higher policy rates slow borrowing.
```

Not every token matters equally when the model predicts the next word.

Attention helps the model decide which earlier tokens deserve the most focus.

## The core idea

When reading:

```text
higher policy rates slow borrowing
```

the token `borrowing` should pay attention to:

- `rates`
- `policy`
- `slow`

Those words provide the context needed to interpret the phrase.

## Why self-attention is useful for prompts

Prompt engineering is often about giving the model the right context.

Example prompt:

```text
You are a central banking analyst. Explain why inflation can lead to higher rates.
```

In this prompt, the later tokens should connect with earlier tokens such as:

- `central`
- `banking`
- `inflation`
- `higher`
- `rates`

Self-attention lets the model connect those words even when they are not adjacent.

## Scaled dot-product attention

The mechanism uses three learned views of each token:

- Query: what this token is looking for
- Key: what this token offers
- Value: the information this token carries

The model compares queries with keys to compute attention scores.

Then it uses those scores to blend the values into a context-aware representation.

## Causal masking

In a GPT-style model, a token is only allowed to attend to current and previous tokens.

That matters because during generation, the future has not happened yet.

Example prompt fragment:

```text
a customer repays
```

The model can use `a`, `customer`, and `repays`, but it must not peek at future words such as `loan` if that token has not been generated yet.

## Banking tutorial example

Prompt:

```text
You are a banking tutor. Explain how a central bank sets rates to control inflation.
```

If the model is predicting the next token after `control`, attention may focus strongly on:

- `central`
- `bank`
- `rates`
- `inflation`

That is one reason detailed prompts often work better than short ones: they give attention more useful material to work with.

## Intuition

Attention is like asking:

```text
For this word in this prompt, which earlier words matter most?
```

That question is one of the main reasons transformers work so well.
