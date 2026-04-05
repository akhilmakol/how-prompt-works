import unittest

import torch

from src.model import MiniGPTConfig, MiniGPTModel


class ModelTests(unittest.TestCase):
    def test_forward_pass_shape_and_loss(self) -> None:
        config = MiniGPTConfig(vocab_size=50, block_size=8, embed_dim=16, num_heads=4, num_layers=2, dropout=0.0)
        model = MiniGPTModel(config)
        inputs = torch.randint(0, 50, (3, 8))
        targets = torch.randint(0, 50, (3, 8))
        logits, loss, _ = model(inputs, targets=targets)
        self.assertEqual(tuple(logits.shape), (3, 8, 50))
        self.assertIsNotNone(loss)


if __name__ == "__main__":
    unittest.main()
