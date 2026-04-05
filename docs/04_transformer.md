# 04. Transformer Blocks

## What is a transformer block?

A transformer block is a reusable unit that helps the model process a prompt in stages.

Each block combines:

- layer normalization
- self-attention
- residual connection
- feed-forward network

Our mini GPT stacks a few of these blocks in sequence.

## Prompt engineering view

When you write a richer prompt, the transformer has more useful context to process.

Example:

```text
You are a banking risk analyst. Explain why liquidity and capital both matter for a bank.
```

The transformer block helps the model connect:

- the role: `banking risk analyst`
- the task: `explain`
- the concepts: `liquidity`, `capital`, `bank`

## Residual connections

Residual connections add the input back to the transformed output.

This helps the model:

- keep useful information
- train more stably
- support deeper networks

## Feed-forward network

After attention mixes information across tokens, the feed-forward network transforms each token representation independently.

You can think of it as a small reasoning step applied to every token vector.

## Banking intuition

Imagine the prompt:

```text
You are a banking tutor. Explain how risk management helps a bank balance growth, safety, and profitability.
```

Attention helps the token `balance` look at:

- `risk management`
- `bank`
- `growth`
- `safety`
- `profitability`

Then the feed-forward layer reshapes that mixed information into a richer internal representation.

## Why stacking blocks helps

Early layers may learn simpler relationships:

- `savings` relates to `interest`
- `loan` relates to `repayment`

Later layers can build on those patterns:

- interest rate changes affect borrowing behavior
- risk controls protect liquidity and capital
- role-based prompts influence explanation style

That layering is what gives transformers expressive power.
