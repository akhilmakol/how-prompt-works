# Medium Article Draft

## Prompt Engineering and LLMs, Explained with Banking Fundamentals

Large language models can feel mysterious at first, especially when terms like prompts, embeddings, attention, logits, and transformers are introduced all at once. This project breaks that story into smaller pieces by using a tiny GPT-style model and a familiar domain: banking fundamentals.

Why banking? Because banking language is structured and easy to reason about. Sentences such as "A savings account earns interest" or "A loan requires repayment" make it easier to observe how a model learns patterns.

The repository walks through:

- prompt engineering
- tokenization
- embeddings
- self-attention
- transformer blocks
- training with cross-entropy
- greedy autoregressive inference

It also includes a Streamlit app so learners can interact with the model instead of only reading about it.

One of the key lessons is that prompting is not separate from model internals. A prompt is simply the input that starts the whole process. Once you write that prompt, the model tokenizes it, embeds it, applies attention across it, and predicts the next token.

For example, these prompts are not equally strong:

- "Explain a loan"
- "You are a banking tutor. Explain a loan to a first-time borrower in simple bullet points."

The second prompt gives the model a role, a task, a user context, and an output style. That is why prompt engineering matters.

The big lesson is that modern LLMs are larger and more capable, but the first-principles pipeline is still the same:

1. write a prompt
2. convert text to tokens
3. map tokens to vectors
4. mix context with attention
5. train to predict the next token
6. generate one token at a time

That is what `how-prompt-works` is designed to make intuitive.
