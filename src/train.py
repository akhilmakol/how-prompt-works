from __future__ import annotations

import random
from dataclasses import dataclass
from pathlib import Path
from typing import List, Sequence, Tuple

import numpy as np
import torch
from torch import optim

from src.model import MiniGPTConfig, MiniGPTModel
from src.tokenizer import WordTokenizer


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT_DIR / "data" / "sample.txt"
MODEL_PATH = ROOT_DIR / "model.pth"


@dataclass
class TrainingConfig:
    block_size: int = 24
    embed_dim: int = 64
    num_heads: int = 4
    num_layers: int = 2
    dropout: float = 0.1
    learning_rate: float = 3e-3
    epochs: int = 160
    seed: int = 7


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


def load_corpus(path: Path = DATA_PATH) -> str:
    return path.read_text(encoding="utf-8")


def build_tokenizer(text: str) -> WordTokenizer:
    tokenizer = WordTokenizer()
    tokenizer.fit(text)
    return tokenizer


def build_training_examples(token_ids: Sequence[int], block_size: int) -> Tuple[torch.Tensor, torch.Tensor]:
    windows_x: List[List[int]] = []
    windows_y: List[List[int]] = []

    for start in range(0, max(len(token_ids) - block_size, 0)):
        chunk = token_ids[start : start + block_size + 1]
        windows_x.append(chunk[:-1])
        windows_y.append(chunk[1:])

    if not windows_x:
        raise ValueError("Corpus is too small for the configured block size.")

    return torch.tensor(windows_x, dtype=torch.long), torch.tensor(windows_y, dtype=torch.long)


def train_model(
    data_path: Path = DATA_PATH,
    model_path: Path = MODEL_PATH,
    training_config: TrainingConfig | None = None,
) -> Tuple[MiniGPTModel, WordTokenizer, list[float]]:
    config = training_config or TrainingConfig()
    set_seed(config.seed)

    text = load_corpus(data_path)
    tokenizer = build_tokenizer(text)
    token_ids = tokenizer.encode(text, add_special_tokens=True)
    inputs, targets = build_training_examples(token_ids, block_size=config.block_size)

    model_config = MiniGPTConfig(
        vocab_size=tokenizer.vocab_size,
        block_size=config.block_size,
        embed_dim=config.embed_dim,
        num_heads=config.num_heads,
        num_layers=config.num_layers,
        dropout=config.dropout,
    )
    model = MiniGPTModel(model_config)
    optimizer = optim.AdamW(model.parameters(), lr=config.learning_rate)

    losses: list[float] = []
    model.train()
    for epoch in range(config.epochs):
        optimizer.zero_grad()
        _, loss, _ = model(inputs, targets=targets)
        if loss is None:
            raise RuntimeError("Loss was not computed during training.")
        loss.backward()
        optimizer.step()
        losses.append(float(loss.item()))

        if (epoch + 1) % 40 == 0:
            print(f"Epoch {epoch + 1}/{config.epochs} - loss: {loss.item():.4f}")

    checkpoint = {
        "model_state_dict": model.state_dict(),
        "tokenizer": tokenizer.to_dict(),
        "config": model_config.to_dict(),
        "losses": losses,
    }
    torch.save(checkpoint, model_path)
    return model, tokenizer, losses


if __name__ == "__main__":
    train_model()
