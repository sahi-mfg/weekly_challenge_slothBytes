from src.keyboard_shortcut import keyboard_shortcut


def test_keyboard_shortcut():
    assert (
        keyboard_shortcut("the egg and Ctrl + C Ctrl + V the spoon")
        == "the egg and the egg and the spoon"
    )
    assert keyboard_shortcut("WARNING Ctrl + V Ctrl + C Ctrl + V") == "WARNING WARNING"
    assert (
        keyboard_shortcut("The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V")
        == "The The Town The The Town"
    )
    assert keyboard_shortcut("Ctrl + C Ctrl + V Ctrl + C Ctrl + V") == ""
    assert (
        keyboard_shortcut("Ctrl + C Ctrl + V Ctrl + C Ctrl + V Ctrl + C Ctrl + V") == ""
    )
    assert (
        keyboard_shortcut(
            "Ctrl + C Ctrl + V Ctrl + C Ctrl + V Ctrl + C Ctrl + V Ctrl + C Ctrl + V"
        )
        == ""
    )
    assert (
        keyboard_shortcut(
            "Ctrl + C Ctrl + V Ctrl + C Ctrl + V Ctrl + C Ctrl + V Ctrl + C Ctrl + V Ctrl + C Ctrl + V"
        )
        == ""
    )
