from src.strategies import always_cooperate, always_defect, tit_for_tat, grudger, random_strategy

def test_always_cooperate():
    assert always_cooperate([], []) == "Cooperate"

def test_always_defect():
    assert always_defect([], []) == "Defect"

def test_tit_for_tat():
    assert tit_for_tat([], []) == "Cooperate"
    assert tit_for_tat([], ["Defect"]) == "Defect"

def test_grudger():
    assert grudger([], []) == "Cooperate"
    assert grudger([], ["Defect"]) == "Defect"
