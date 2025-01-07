import matplotlib.pyplot as plt
import os

payoff_matrix = {
    ("Cooperate", "Cooperate"): (3, 3),
    ("Cooperate", "Defect"): (0, 5),
    ("Defect", "Cooperate"): (5, 0),
    ("Defect", "Defect"): (1, 1),
}

def play_round(strategy1, strategy2, history1, history2):
    move1 = strategy1(history1, history2)
    move2 = strategy2(history2, history1)
    payoff1, payoff2 = payoff_matrix[(move1, move2)]
    return move1, move2, payoff1, payoff2

def simulate_game(strategy1, strategy2, rounds=100, filename="cumulative_payoff.png"):
    history1, history2 = [], []
    total_payoff1, total_payoff2 = 0, 0
    payoffs1, payoffs2 = [], []

    print(f"\n{'Round':^10}{'Player 1 Move':^20}{'Player 2 Move':^20}{'Payoff (P1, P2)':^20}")
    print("-" * 70)

    for i in range(rounds):
        move1, move2, payoff1, payoff2 = play_round(strategy1, strategy2, history1, history2)
        history1.append(move1)
        history2.append(move2)
        total_payoff1 += payoff1
        total_payoff2 += payoff2
        payoffs1.append(total_payoff1)
        payoffs2.append(total_payoff2)

        print(f"{i+1:^10}{move1:^20}{move2:^20}{str((payoff1, payoff2)):^20}")

    print("\nFinal Results:")
    print(f"Player 1 Total Payoff: {total_payoff1}")
    print(f"Player 2 Total Payoff: {total_payoff2}")

    # Plotting cumulative payoffs
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, rounds+1), payoffs1, label='Player 1')
    plt.plot(range(1, rounds+1), payoffs2, label='Player 2')
    plt.xlabel('Round')
    plt.ylabel('Cumulative Payoff')
    plt.title('Payoff Over Time')
    plt.legend()
    plt.grid(True)

    # Create the directory if it doesn't exist
    save_dir = os.path.join(os.path.dirname(__file__), '..', 'docs', 'visuals')
    os.makedirs(save_dir, exist_ok=True)

    # Save the plot to the specified directory
    save_path = os.path.join(save_dir, filename)
    plt.savefig(save_path)
    plt.show()
    
    return total_payoff1, total_payoff2
