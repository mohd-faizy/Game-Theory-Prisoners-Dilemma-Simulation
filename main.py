import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import (
    always_cooperate,
    always_defect,
    tit_for_tat,
    grudger,
    random_strategy,
    simulate_game,
)

def compare_strategies(strategies, rounds=100):
    results = {}
    strategy_names = list(strategies.keys())

    for i, name1 in enumerate(strategy_names):
        for j, name2 in enumerate(strategy_names):
            if i < j:
                print(f"\n{'-' * 40}")
                print(f"Simulating: {name1} vs {name2}")
                print(f"{'-' * 40}")
                filename = f"{name1}_vs_{name2}.png"
                payoff1, payoff2 = simulate_game(strategies[name1], strategies[name2], rounds, filename)
                results[(name1, name2)] = (payoff1, payoff2)

    print("\nOverall Results:")
    print(f"{'Strategy 1':<20}{'Strategy 2':<20}{'Player 1 Payoff':<20}{'Player 2 Payoff':<20}")
    print("-" * 80)

    for (name1, name2), (payoff1, payoff2) in results.items():
        print(f"{name1:<20}{name2:<20}{payoff1:<20}{payoff2:<20}")

if __name__ == "__main__":
    strategies = {
        "Always Cooperate": always_cooperate,
        "Always Defect": always_defect,
        "Tit-for-Tat": tit_for_tat,
        "Grudger": grudger,
        "Random": random_strategy,
    }
    compare_strategies(strategies, rounds=100)
