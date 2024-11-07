import unittest

from src.keyboard_shortcut import keyboard_shortcut


class TestKeyboard_shortcut(unittest.TestCase):
    def setUp(self) -> None:
        self.keyboard_shortcut = keyboard_shortcut()

    def test_keyboard_shortcut(self):
        self.assertEqual(
            self.keyboard_shortcut.keyboard_shortcut(
                "the egg and Ctrl + C Ctrl + V the spoon"
            ),
            "the egg and the egg and the spoon",
        )
        self.assertEqual(
            self.keyboard_shortcut.keyboard_shortcut(
                "WARNING Ctrl + V Ctrl + C Ctrl + V"
            ),
            "WARNING WARNING",
        )
        self.assertEqual(
            self.keyboard_shortcut.keyboard_shortcut(
                "The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V"
            ),
            "The The Town The The Town",
        )
