# 07. Limitations

## This is a teaching model

Our mini GPT is useful for learning, but it is not a production banking model.

## Main limitations

### Small dataset

The corpus is tiny, so the model learns narrow patterns.

It may repeat training phrases rather than generalize strongly.

### Word-level tokenization

Modern LLMs often use subword tokenization, which handles rare words better.

Our tokenizer is easier to understand, but less flexible.

### Small context window

The model only sees a limited number of tokens at once.

It cannot track long documents or complex reports well.

### Greedy decoding only

Greedy decoding is simple, but it is not always the best choice for high-quality text generation.

### No real banking intelligence

The model does not understand regulation, credit policy, or accounting logic.

It only learns patterns from the sample text.

## Important caution

Because the project uses banking examples, it may look more authoritative than it really is.

It should not be used for:

- financial advice
- lending decisions
- compliance interpretation
- fraud scoring

Its purpose is education, not decision-making.
