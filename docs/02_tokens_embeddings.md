# 02. Tokens and Embeddings

## Tokenization

A language model cannot read raw text directly. It first breaks text into smaller pieces called tokens.

In this project, the tokenizer is word-level.

Example:

```text
The bank approves a loan.
```

Becomes:

```text
["the", "bank", "approves", "a", "loan", "."]
```

Then each token gets an integer ID.

Possible example:

```text
"bank" -> 12
"loan" -> 19
```

## Why tokenize?

Neural networks work with numbers, not raw words.

Tokenization is the bridge between natural language and computation.

## Embeddings

An embedding is a learned vector representation of a token.

Instead of treating `bank` as just the integer `12`, the model learns a dense vector such as:

```text
[0.14, -0.82, 0.37, ...]
```

This vector can capture relationships:

- `loan` may be close to `credit`
- `deposit` may be close to `savings`
- `rate` may be close to `interest`

## Positional embeddings

Word order matters.

These two sentences use similar words but mean different things:

```text
The bank approved the loan.
The loan approved the bank.
```

Token embeddings alone do not tell us order, so we add positional embeddings.

That helps the model distinguish early tokens from later tokens in the sequence.

## Banking example

Consider:

```text
A mortgage is a long term loan.
```

The tokenizer produces tokens.
The embedding layer turns each token into a vector.
The positional embedding says where each token appears.

Together, they form the model input.
