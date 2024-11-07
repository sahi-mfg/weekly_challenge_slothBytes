from src.countTrue import count_true


def test_count_true():
    assert count_true([True, True, True, True]) == 4
    assert count_true([False, False, False, False]) == 0
    assert count_true([False, True, True, False]) == 2
    assert count_true([True, False, True, False]) == 2
    assert count_true([True, True, False, False]) == 2
    assert count_true([]) == 0
