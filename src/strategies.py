import numpy as np

def always_cooperate(history, opponent_history):
    return "Cooperate"

def always_defect(history, opponent_history):
    return "Defect"

def tit_for_tat(history, opponent_history):
    if not opponent_history:
        return "Cooperate"
    return opponent_history[-1]

def grudger(history, opponent_history):
    if "Defect" in opponent_history:
        return "Defect"
    return "Cooperate"

def random_strategy(history, opponent_history):
    return np.random.choice(["Cooperate", "Defect"])
