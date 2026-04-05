# Medium Article Draft

## How LLMs Work, Explained with Banking Fundamentals

Large language models can feel mysterious at first, especially when terms like embeddings, attention, logits, and transformers are introduced all at once. This project breaks that story into smaller pieces by using a tiny GPT-style model and a familiar domain: banking fundamentals.

Why banking? Because banking language is structured and easy to reason about. Sentences such as "A savings account earns interest" or "A loan requires repayment" make it easier to observe how a model learns patterns.

The repository walks through:

- tokenization
- embeddings
- self-attention
- transformer blocks
- training with cross-entropy
- greedy autoregressive inference

It also includes a Streamlit app so learners can interact with the model instead of only reading about it.

The big lesson is that modern LLMs are larger and more capable, but the first-principles pipeline is still the same:

1. convert text to tokens
2. map tokens to vectors
3. mix context with attention
4. train to predict the next token
5. generate one token at a time

That is what `how-llm-works` is designed to make intuitive.
