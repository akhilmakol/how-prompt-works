from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import List, Optional, Tuple

import torch
from torch import nn

from src.embeddings import TokenPositionEmbedding
from src.transformer import TransformerBlock


@dataclass
class MiniGPTConfig:
    vocab_size: int
    block_size: int = 32
    embed_dim: int = 64
    num_heads: int = 4
    num_layers: int = 2
    dropout: float = 0.1

    def to_dict(self) -> dict:
        return asdict(self)


class MiniGPTModel(nn.Module):
    def __init__(self, config: MiniGPTConfig) -> None:
        super().__init__()
        self.config = config
        self.embedding = TokenPositionEmbedding(
            vocab_size=config.vocab_size,
            embed_dim=config.embed_dim,
            block_size=config.block_size,
        )
        self.dropout = nn.Dropout(config.dropout)
        self.blocks = nn.ModuleList(
            [
                TransformerBlock(
                    embed_dim=config.embed_dim,
                    num_heads=config.num_heads,
                    dropout=config.dropout,
                )
                for _ in range(config.num_layers)
            ]
        )
        self.ln_f = nn.LayerNorm(config.embed_dim)
        self.lm_head = nn.Linear(config.embed_dim, config.vocab_size)

    def forward(
        self,
        input_ids: torch.Tensor,
        targets: Optional[torch.Tensor] = None,
        return_attention: bool = False,
    ) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[List[torch.Tensor]]]:
        x = self.embedding(input_ids)
        x = self.dropout(x)

        attention_maps: List[torch.Tensor] = []
        for block in self.blocks:
            x, attn = block(x)
            if return_attention:
                attention_maps.append(attn)

        logits = self.lm_head(self.ln_f(x))

        loss = None
        if targets is not None:
            loss_fn = nn.CrossEntropyLoss()
            loss = loss_fn(logits.reshape(-1, logits.size(-1)), targets.reshape(-1))

        return logits, loss, attention_maps if return_attention else None

    @torch.no_grad()
    def generate(self, input_ids: torch.Tensor, max_new_tokens: int) -> torch.Tensor:
        self.eval()
        for _ in range(max_new_tokens):
            input_window = input_ids[:, -self.config.block_size :]
            logits, _, _ = self(input_window)
            next_token_logits = logits[:, -1, :]
            next_token = torch.argmax(next_token_logits, dim=-1, keepdim=True)
            input_ids = torch.cat([input_ids, next_token], dim=1)
        return input_ids
