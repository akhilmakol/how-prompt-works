from __future__ import annotations

import torch
from torch import nn


class TokenPositionEmbedding(nn.Module):
    """Combines learned token embeddings and positional embeddings."""

    def __init__(self, vocab_size: int, embed_dim: int, block_size: int) -> None:
        super().__init__()
        self.token_embedding = nn.Embedding(vocab_size, embed_dim)
        self.position_embedding = nn.Embedding(block_size, embed_dim)

    def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
        batch_size, seq_len = input_ids.shape
        positions = torch.arange(seq_len, device=input_ids.device).unsqueeze(0).expand(batch_size, seq_len)
        token_vectors = self.token_embedding(input_ids)
        position_vectors = self.position_embedding(positions)
        return token_vectors + position_vectors
