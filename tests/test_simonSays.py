from src.simonSays import simon_says


def test_simonSays():
    assert simon_says(["Simon says add 4", "Simon says add 6", "Then add 5"]) == 10

    assert (
        simon_says(
            [
                "Firstly, add 4",
                "Simeon says subtract 100",  # Look at the name closely :)
            ]
        )
        == 0
    )

    assert (
        simon_says(
            ["Susan says add 10", "Simon says add 3", "Simon says multiply by 8"]
        )
        == 24
    )
