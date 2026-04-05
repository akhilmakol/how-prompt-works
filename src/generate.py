from __future__ import annotations

import argparse
from pathlib import Path
from typing import Tuple

import torch

from src.model import MiniGPTConfig, MiniGPTModel
from src.tokenizer import WordTokenizer
from src.train import MODEL_PATH, train_model


def load_model_and_tokenizer(model_path: Path = MODEL_PATH) -> Tuple[MiniGPTModel, WordTokenizer]:
    if not model_path.exists():
        train_model(model_path=model_path)
    checkpoint = torch.load(model_path, map_location="cpu")
    tokenizer = WordTokenizer.from_dict(checkpoint["tokenizer"])
    config = MiniGPTConfig(**checkpoint["config"])
    model = MiniGPTModel(config)
    model.load_state_dict(checkpoint["model_state_dict"])
    model.eval()
    return model, tokenizer


def generate_text(prompt: str, max_new_tokens: int = 20, model_path: Path = MODEL_PATH) -> str:
    model, tokenizer = load_model_and_tokenizer(model_path)
    input_ids = torch.tensor([tokenizer.encode(prompt, add_special_tokens=True)], dtype=torch.long)
    generated_ids = model.generate(input_ids, max_new_tokens=max_new_tokens)[0].tolist()
    return tokenizer.decode(generated_ids)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate text from the mini GPT model.")
    parser.add_argument("--prompt", type=str, default="a bank offers", help="Seed prompt for generation.")
    parser.add_argument("--max-new-tokens", type=int, default=20, help="Number of tokens to generate.")
    args = parser.parse_args()

    text = generate_text(prompt=args.prompt, max_new_tokens=args.max_new_tokens)
    print(text)


if __name__ == "__main__":
    main()
