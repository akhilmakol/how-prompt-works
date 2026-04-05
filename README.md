# how-llm-works

`how-llm-works` is a visual, interactive, beginner-friendly repository that explains how prompting and a small GPT-style language model work from first principles using banking fundamentals as the teaching domain.

The project includes:

- A clean PyTorch implementation of a tiny GPT-style model
- End-to-end training and greedy text generation
- A Streamlit app for token exploration, generation, and attention visualization
- Step-by-step docs that explain the full pipeline with simple banking examples
- Lightweight notebooks and tests to support learning and verification

## Why banking examples?

Banking is familiar, structured, and full of repeatable language patterns:

- "A savings account earns interest."
- "A loan requires repayment over time."
- "A central bank influences rates."

Those patterns make it easier to see what tokenization, embeddings, attention, training, and inference are doing under the hood.

## Architecture

The model follows a minimal GPT-style decoder-only design:

1. Word tokenizer converts text into integer token IDs.
2. Token embeddings map IDs into vectors.
3. Positional embeddings inject order information.
4. Causal self-attention lets each token attend only to current and previous tokens.
5. Transformer blocks combine attention, feed-forward layers, residual connections, and layer normalization.
6. A final linear layer projects hidden states to vocabulary logits.
7. Greedy decoding generates the next token one step at a time.

## Repository layout

```text
how-llm-works/
├── app/ui.py
├── src/
├── docs/
├── visuals/
├── data/sample.txt
├── notebooks/
├── tests/
└── assets/
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Train the model

```bash
python -m src.train
```

This reads [data/sample.txt](/C:/dev/how-prompt-works/data/sample.txt), trains a small language model, and saves `model.pth` in the repository root.

## Generate text

```bash
python -m src.generate --prompt "a bank offers" --max-new-tokens 20
```

## Run the Streamlit demo

```bash
streamlit run app/ui.py
```

The app includes:

- Text generation
- Tokenization explorer
- Attention heatmap visualization

If `model.pth` is missing, the app automatically trains a fresh model using the sample banking corpus.

## Learning path

Read the docs in order:

1. [docs/01_intro.md](/C:/dev/how-prompt-works/docs/01_intro.md)
2. [docs/02_tokens_embeddings.md](/C:/dev/how-prompt-works/docs/02_tokens_embeddings.md)
3. [docs/03_attention.md](/C:/dev/how-prompt-works/docs/03_attention.md)
4. [docs/04_transformer.md](/C:/dev/how-prompt-works/docs/04_transformer.md)
5. [docs/05_training.md](/C:/dev/how-prompt-works/docs/05_training.md)
6. [docs/06_inference.md](/C:/dev/how-prompt-works/docs/06_inference.md)
7. [docs/07_limitations.md](/C:/dev/how-prompt-works/docs/07_limitations.md)
8. [docs/08_real_world_llms.md](/C:/dev/how-prompt-works/docs/08_real_world_llms.md)

## Visual references

The files in [visuals/](/C:/dev/how-prompt-works/visuals) are text-based placeholders that describe what each final diagram should illustrate:

- `cover.png`
- `pipeline.png`
- `tokenization.png`
- `embeddings.png`
- `attention.png`
- `transformer.png`
- `training.png`
- `inference.png`

## Tests

Run:

```bash
python -m unittest discover -s tests -v
```

The tests validate:

- Tokenizer encoding behavior
- Attention output shape
- Model forward pass shape and loss computation

## Streamlit deployment notes

This project is designed to be lightweight enough for demos and portfolios:

- Small dataset
- Small model configuration
- Auto-training behavior for first-time runs
- No external APIs required

## License

This repository uses the MIT License in [LICENSE](/C:/dev/how-prompt-works/LICENSE).
