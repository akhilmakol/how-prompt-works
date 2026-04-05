from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List


TOKEN_PATTERN = re.compile(r"\w+|[^\w\s]", re.UNICODE)


@dataclass
class WordTokenizer:
    """A simple word-level tokenizer with special tokens."""

    token_to_id: Dict[str, int] = field(default_factory=dict)
    id_to_token: Dict[int, str] = field(default_factory=dict)

    pad_token: str = "<pad>"
    unk_token: str = "<unk>"
    bos_token: str = "<bos>"
    eos_token: str = "<eos>"

    def __post_init__(self) -> None:
        if not self.token_to_id:
            self._initialize_vocab()
        elif not self.id_to_token:
            self.id_to_token = {idx: token for token, idx in self.token_to_id.items()}

    def _initialize_vocab(self) -> None:
        special_tokens = [self.pad_token, self.unk_token, self.bos_token, self.eos_token]
        self.token_to_id = {token: idx for idx, token in enumerate(special_tokens)}
        self.id_to_token = {idx: token for token, idx in self.token_to_id.items()}

    @property
    def vocab_size(self) -> int:
        return len(self.token_to_id)

    def tokenize(self, text: str) -> List[str]:
        return TOKEN_PATTERN.findall(text.lower())

    def fit(self, text: str) -> "WordTokenizer":
        for token in self.tokenize(text):
            if token not in self.token_to_id:
                idx = len(self.token_to_id)
                self.token_to_id[token] = idx
                self.id_to_token[idx] = token
        return self

    def encode(self, text: str, add_special_tokens: bool = True) -> List[int]:
        tokens = self.tokenize(text)
        ids = [self.token_to_id.get(token, self.token_to_id[self.unk_token]) for token in tokens]
        if add_special_tokens:
            return [self.token_to_id[self.bos_token], *ids, self.token_to_id[self.eos_token]]
        return ids

    def decode(self, ids: List[int], skip_special_tokens: bool = True) -> str:
        tokens: List[str] = []
        special_tokens = {self.pad_token, self.unk_token, self.bos_token, self.eos_token}
        for idx in ids:
            token = self.id_to_token.get(int(idx), self.unk_token)
            if skip_special_tokens and token in special_tokens:
                continue
            tokens.append(token)

        text = " ".join(tokens)
        text = re.sub(r"\s+([.,!?;:])", r"\1", text)
        return text.strip()

    def to_dict(self) -> Dict[str, Dict[str, int]]:
        return {"token_to_id": self.token_to_id}

    def save(self, path: str | Path) -> None:
        Path(path).write_text(json.dumps(self.to_dict(), indent=2), encoding="utf-8")

    @classmethod
    def from_dict(cls, payload: Dict[str, Dict[str, int]]) -> "WordTokenizer":
        return cls(token_to_id=payload["token_to_id"])

    @classmethod
    def load(cls, path: str | Path) -> "WordTokenizer":
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        return cls.from_dict(payload)
