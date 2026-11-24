import unittest
from rsa import *

class TestRSA(unittest.TestCase):

    # 素数判定のテスト
    def test_prime(self):
        self.assertEqual(is_prime(7), True)
        self.assertEqual(is_prime(10), False)
        self.assertEqual(is_prime(1), False)

    # 鍵生成のテスト
    def test_key(self):
        public_key, private_key = generate_keys()

        self.assertEqual(public_key[1], private_key[1])

    # 暗号化と復号のテスト
    def test_encrypt(self):
        public_key, private_key = generate_keys()

        message = "Hello World"

        cipher = encrypt_text(message, public_key)
        decoded = decrypt_text(cipher, private_key)

        self.assertEqual(decoded, message)

    # 文字列変換のテスト
    def test_text(self):
        message = "Hello"

        numbers = text_to_numbers(message)
        decoded = numbers_to_text(numbers)

        self.assertEqual(decoded, message)


if __name__ == "__main__":
    unittest.main()