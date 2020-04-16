from unittest import TestCase
from pacote.modulo import soma as s


class TestSoma(TestCase):
    def test_soma(self):
        res = s(1,3)
        self.assertEqual(4,res)
        