from unittest import TestCase


class TestDobleImpar(TestCase):
    def test_dobleImpar(self):
        if (2 / 2) % 2 != 0:
            return print(2, "es el doble de ", 2 / 2, " que es impar")
