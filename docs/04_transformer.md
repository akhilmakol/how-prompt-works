# 04. Transformer Blocks

## What is a transformer block?

A transformer block is a reusable unit that combines:

- layer normalization
- self-attention
- residual connection
- feed-forward network

Our mini GPT stacks a few of these blocks in sequence.

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

Imagine the sentence:

```text
Risk management helps a bank balance growth, safety, and profitability.
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

That layering is what gives transformers expressive power.
