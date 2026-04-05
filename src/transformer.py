from __future__ import annotations

from typing import Tuple

import torch
from torch import nn

from src.attention import MultiHeadSelfAttention


class FeedForward(nn.Module):
    def __init__(self, embed_dim: int, dropout: float = 0.0) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(embed_dim, 4 * embed_dim),
            nn.GELU(),
            nn.Linear(4 * embed_dim, embed_dim),
            nn.Dropout(dropout),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


class TransformerBlock(nn.Module):
    """Attention + feed-forward with residual paths and layer norm."""

    def __init__(self, embed_dim: int, num_heads: int, dropout: float = 0.0) -> None:
        super().__init__()
        self.ln1 = nn.LayerNorm(embed_dim)
        self.attn = MultiHeadSelfAttention(embed_dim=embed_dim, num_heads=num_heads, dropout=dropout)
        self.ln2 = nn.LayerNorm(embed_dim)
        self.ffn = FeedForward(embed_dim=embed_dim, dropout=dropout)

    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        attn_output, attn_weights = self.attn(self.ln1(x))
        x = x + attn_output
        x = x + self.ffn(self.ln2(x))
        return x, attn_weights
