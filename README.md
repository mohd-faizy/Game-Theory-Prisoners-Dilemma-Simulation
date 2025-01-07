[![author](https://img.shields.io/badge/author-mohd--faizy-red)](https://github.com/mohd-faizy)


# Game Theory - Prisoner's Dilemma Simulation

Welcome to the **Prisoner's Dilemma Simulation**, a Python-based project that delves into one of the most iconic problems in **Game Theory**. Through this simulation, you can explore how various strategies compete in multi-round games, gain insights into their effectiveness, and visualize the outcomes through engaging graphical representations. 🌟

---

## Why the Prisoner's Dilemma Matters 🤔

The **Prisoner's Dilemma** represents a situation where individuals face a choice to either cooperate for mutual benefit or defect for personal gain at the expense of others. Despite its simplicity, this problem highlights the complexities of trust, competition, and collaboration in human interactions, economic systems, and evolutionary biology.

### The Payoff Matrix 🧮

|               | Opponent: C | Opponent: D |
|---------------|-------------|-------------|
| **Player: C** | (3, 3)      | (0, 5)      |
| **Player: D** | (5, 0)      | (1, 1)      |

- **C** = Cooperate 🤝
- **D** = Defect ❌

Key Takeaways:

- Mutual cooperation yields moderate rewards for both players.
- Defecting provides a higher payoff if the opponent cooperates but risks low rewards if both defect.

---

## What is Game Theory? 🎲

**Game Theory** is the study of strategic interactions between rational decision-makers. It provides mathematical frameworks to analyze situations where the outcome for each participant depends on the choices of others. Game theory helps in understanding and predicting behaviors in competitive and cooperative environments.

### Applications of Game Theory 🌍

- **Economics**: Analyzing markets, auctions, and pricing strategies.
- **Politics**: Understanding alliances, voting systems, and conflict resolution.
- **Biology**: Exploring evolutionary strategies and species interactions.
- **Artificial Intelligence**: Designing algorithms for decision-making in multi-agent systems.
- **Business**: Developing competitive strategies, negotiation tactics, and collaboration frameworks.
- **Everyday Life**: From board games to complex societal issues, game theory helps explain interactions in a variety of contexts.

---

## Features 🚀

- **Pre-implemented strategies**:
  - Always Cooperate 🤝
  - Always Defect ❌
  - Tit-for-Tat 🔄
  - Grudger 😠
  - Random 🎲
- Multi-round simulation to observe long-term dynamics.
- Graphical visualization of cumulative payoffs 📊.
- Detailed comparison of strategies.

---

## Insights from the Simulation 💡

### Cooperation vs. Competition ⚔️

This simulation demonstrates how cooperation can lead to better outcomes over time, yet selfishness (defection) often seems tempting in the short term.

### Emergence of Stable Strategies 🔒

Some strategies, like **Tit-for-Tat** or **Grudger**, balance cooperation and retaliation, showing how trust and punishment work together to enforce stability in repeated interactions.

---

## Directory Structure 🗂️

```
Prisoners-Dilemma-Simulation/
├── README.md
├── LICENSE
├── requirements.txt
├── src/
│   ├── __init__.py 
│   ├── strategies.py
│   ├── game.py
├── docs/
│   ├── strategy_explanations.md
│   ├── visuals/
│       ├── sample_graph.png
├── tests/
│   ├── __init__.py
│   ├── test_strategies.py
│   ├── test_game.py
└── venv/
└── main.py
```

---

## Getting Started 🛠️

### Prerequisites 📋

- Python 3.8 or above.
- `pip` installed.

### Installation Steps 📥

1. **Clone the repository**:

    ```bash
    git clone https://github.com/mohd-faizy/Prisoners-Dilemma-Simulation.git
    cd Prisoners-Dilemma-Simulation
    ```

2. **Set up a virtual environment (optional but recommended)**:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the simulation**:

    Open the terminal in VSCode, navigate to the project folder, and execute:

    ```bash
    python main.py
    ```

---

## Usage 🖥️

1. **Run the program** to initiate the simulation:

    ```bash
    python src/main.py
    ```

2. **Output**:
    - Round-by-round moves and payoffs.
    - Graphical representation of cumulative payoffs.
    - Comparative analysis of strategies.

### Example Simulation 🎯

The following demonstrates **Tit-for-Tat** versus **Always Defect** for 100 rounds.

**Sample Output**:

```
Round 1: Player 1 (Cooperate), Player 2 (Defect), Payoffs: (0, 5)
Round 2: Player 1 (Defect), Player 2 (Defect), Payoffs: (1, 1)
...
Final Cumulative Payoffs:
- Player 1: 50
- Player 2: 100
```

---

## Strategies Implemented 🤖

| Strategy           | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Always Cooperate** | Always chooses "Cooperate" regardless of the opponent's moves.             |
| **Always Defect**   | Always chooses "Defect" regardless of the opponent's moves.                |
| **Tit-for-Tat**     | Starts with "Cooperate" and mimics the opponent's last move in subsequent rounds. |
| **Grudger**         | Cooperates until the opponent defects once, then defects forever.          |
| **Random**          | Randomly chooses between "Cooperate" and "Defect".                        |

---

## Visualization 📈

- The simulation generates **graphs** of cumulative payoffs for each strategy.
- Example graph from a 100-round game:

![Sample Graph](https://raw.githubusercontent.com/mohd-faizy/learn_python/refs/heads/main/docs/visuals/Grudger_vs_Random.png?token=GHSAT0AAAAAAC4TBXOE426EDPSLRNPWL45UZ35EXYA)

---

## Contributing 🤝

Contributions are welcome! Feel free to submit pull requests to improve strategies, optimize the code, or add features.

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request.

---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---



### $\color{skyblue}{\textbf{Connect with me:}}$

[<img align="left" src="https://cdn4.iconfinder.com/data/icons/social-media-icons-the-circle-set/48/twitter_circle-512.png" width="32px"/>][twitter]
[<img align="left" src="https://cdn-icons-png.flaticon.com/512/145/145807.png" width="32px"/>][linkedin]
[<img align="left" src="https://cdn-icons-png.flaticon.com/512/2626/2626299.png" width="32px"/>][Portfolio]

[twitter]: https://twitter.com/F4izy
[linkedin]: https://www.linkedin.com/in/mohd-faizy/
[Portfolio]: https://ai.stackexchange.com/users/36737/faizy?tab=profile

---

<img src="https://github-readme-stats.vercel.app/api?username=mohd-faizy&show_icons=true" width=380px height=200px />
