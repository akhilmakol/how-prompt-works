import unittest

import torch

from src.attention import MultiHeadSelfAttention


class AttentionTests(unittest.TestCase):
    def test_attention_output_shape(self) -> None:
        attention = MultiHeadSelfAttention(embed_dim=16, num_heads=4)
        x = torch.randn(2, 5, 16)
        output, weights = attention(x)
        self.assertEqual(tuple(output.shape), (2, 5, 16))
        self.assertEqual(tuple(weights.shape), (2, 4, 5, 5))


if __name__ == "__main__":
    unittest.main()
