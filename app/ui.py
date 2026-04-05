from __future__ import annotations

import os
from pathlib import Path

import streamlit as st
import torch

from src.generate import load_model_and_tokenizer
from src.train import MODEL_PATH, train_model


ROOT_DIR = Path(__file__).resolve().parents[1]
MPL_CONFIG_DIR = ROOT_DIR / ".mplconfig"
MPL_CONFIG_DIR.mkdir(exist_ok=True)
for stale_lock in MPL_CONFIG_DIR.glob("*.matplotlib-lock"):
    try:
        stale_lock.unlink(missing_ok=True)
    except PermissionError:
        pass
os.environ.setdefault("MPLCONFIGDIR", str(MPL_CONFIG_DIR))

import matplotlib.pyplot as plt


@st.cache_resource
def ensure_model():
    if not MODEL_PATH.exists():
        train_model()
    return load_model_and_tokenizer(MODEL_PATH)


def render_attention_heatmap(model, tokenizer, prompt: str) -> None:
    token_ids = tokenizer.encode(prompt or "a bank lends money", add_special_tokens=True)
    input_tensor = torch.tensor([token_ids], dtype=torch.long)
    _, _, attention_maps = model(input_tensor, return_attention=True)

    if not attention_maps:
        st.info("No attention maps were returned by the model.")
        return

    final_layer = attention_maps[-1][0, 0].detach().cpu().numpy()
    labels = [tokenizer.id_to_token[idx] for idx in token_ids]

    fig, ax = plt.subplots(figsize=(8, 6))
    heatmap = ax.imshow(final_layer, cmap="Blues", aspect="auto")
    ax.set_title("Attention Heatmap (final layer, head 0)")
    ax.set_xticks(range(len(labels)))
    ax.set_yticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.set_yticklabels(labels)
    fig.colorbar(heatmap, ax=ax)
    st.pyplot(fig)
    plt.close(fig)


def main() -> None:
    st.set_page_config(page_title="How LLM Works", layout="wide")
    st.title("How LLM Works")
    st.caption("A banking-themed, visual walkthrough of prompt engineering and a mini GPT-style model.")
    st.info(
        "Prompt framework used across this demo: [Role] + [Task] + [Context] + [Output Format]. "
        "Try prompts like 'You are a banking tutor. Explain savings accounts in 3 bullet points.'"
    )

    with st.spinner("Loading model and tokenizer..."):
        model, tokenizer = ensure_model()

    tab_generate, tab_tokenize, tab_attention = st.tabs(
        ["Text Generation", "Tokenization Explorer", "Attention Visualization"]
    )

    with tab_generate:
        st.subheader("Prompt Playground")
        st.markdown(
            "Test how different prompt styles change output. Start simple, then add role, context, or format."
        )
        prompt = st.text_input(
            "Prompt",
            value="You are a banking tutor. Explain what a bank offers.",
        )
        max_new_tokens = st.slider("Max new tokens", min_value=1, max_value=30, value=12)
        if st.button("Generate text", use_container_width=True):
            input_ids = torch.tensor([tokenizer.encode(prompt, add_special_tokens=True)], dtype=torch.long)
            generated = model.generate(input_ids, max_new_tokens=max_new_tokens)[0].tolist()
            output_text = tokenizer.decode(generated)
            st.success(output_text)

    with tab_tokenize:
        st.subheader("Prompt Tokenization Explorer")
        st.markdown("See how a banking prompt is broken into tokens before the model can process it.")
        sample_text = st.text_area(
            "Enter a prompt",
            value="You are a loan officer. Explain mortgage interest to a first-time homebuyer.",
            height=120,
        )
        tokens = tokenizer.tokenize(sample_text)
        token_ids = tokenizer.encode(sample_text, add_special_tokens=True)
        st.write("Tokens:", tokens)
        st.write("Token IDs:", token_ids)
        st.write("Decoded text:", tokenizer.decode(token_ids))

    with tab_attention:
        st.subheader("Prompt Attention Visualization")
        attention_prompt = st.text_input(
            "Prompt for attention map",
            value="the central bank sets rates to control inflation",
        )
        st.markdown(
            "This heatmap shows how one attention head in the final transformer layer distributes focus across "
            "tokens in a banking prompt."
        )
        render_attention_heatmap(model, tokenizer, attention_prompt)


if __name__ == "__main__":
    main()
