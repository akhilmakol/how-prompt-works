# 05. Training

## The training objective

This model learns by predicting the next token in a sequence.

If the input is:

```text
A bank accepts deposits from
```

the target next token may be:

```text
customers
```

## Training data

We train on [data/sample.txt](/C:/dev/how-prompt-works/data/sample.txt), which contains short banking-fundamental statements.

Examples include:

- deposits
- interest
- loans
- inflation
- regulation
- fraud detection

## Sliding windows

The training script creates fixed-length windows of tokens.

For each window:

- input = tokens 1 to N
- target = tokens 2 to N+1

This teaches the model to shift forward by one token.

## Loss function

We use cross-entropy loss.

Cross-entropy measures how far the predicted probability distribution is from the correct next token.

If the model predicts:

- `customers` with high probability when `customers` is correct, loss gets lower
- `inflation` when `customers` is correct, loss gets higher

## Optimization

We use AdamW to update the model parameters.

During training:

1. run the input through the model
2. compute logits
3. compute loss
4. backpropagate gradients
5. update weights

## Banking example

Sentence:

```text
A loan allows a customer to borrow money.
```

At one step, the model may see:

```text
A loan allows a customer to borrow
```

and learn that `money` is a strong next-token candidate.
