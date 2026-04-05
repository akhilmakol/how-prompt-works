# 06. Inference

## What happens during inference?

Inference means using a trained model to generate text from a prompt.

We begin with a prompt such as:

```text
You are a banking tutor. Explain a savings account.
```

Then the model:

1. tokenizes the prompt
2. runs it through the transformer
3. predicts the next token
4. appends that token
5. repeats

## Prompt engineering view

Inference is where prompt engineering becomes visible.

Compare these prompts:

```text
Explain a loan.
You are a loan officer. Explain a loan to a first-time borrower in simple bullet points.
```

The second prompt gives the model:

- a role
- a task
- user context
- an output style

That usually produces a more targeted answer.

## Greedy decoding

This project uses greedy decoding.

That means at each step, we choose the single highest-probability token.

Example:

If the model predicts:

- `helps` -> 0.61
- `requires` -> 0.18
- `limits` -> 0.08

then greedy decoding selects `helps`.

## Benefits and tradeoffs

Greedy decoding is:

- simple
- deterministic
- easy to explain

But it can also:

- repeat phrases
- become predictable
- miss more creative continuations

## Banking tutorial example

Prompt:

```text
You are a central banking analyst. Explain why the central bank changes rates.
```

Possible continuation:

```text
the central bank influences interest rates and supports financial stability.
```

The model generates this one token at a time, not all at once.
