import unittest

from src.tokenizer import WordTokenizer


class TokenizerTests(unittest.TestCase):
    def test_encode_includes_known_tokens(self) -> None:
        tokenizer = WordTokenizer().fit("bank loan savings account")
        encoded = tokenizer.encode("bank loan", add_special_tokens=False)
        expected = [tokenizer.token_to_id["bank"], tokenizer.token_to_id["loan"]]
        self.assertEqual(encoded, expected)


if __name__ == "__main__":
    unittest.main()
