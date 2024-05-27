<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">TIC-TAC-TOE</h1>
</p>
<p align="center">
    <em>Playful strategy, limitless possibility.</em>
</p>
<p align="center">
	<!-- Shields.io badges not used with skill icons. --><p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<a href="https://skillicons.dev">
		<img src="https://skillicons.dev/icons?i=md,py">
	</a></p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [📍 Overview](#-overview)
- [🧩 Features](#-features)
- [🗂️ Repository Structure](#️-repository-structure)
- [📦 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Installation](#️-installation)
  - [🤖 Usage](#-usage)
- [🤝 Contributing](#-contributing)
- [🎗 License](#-license)
</details>
<hr>

## 📍 Overview

The Tic-Tac-Toe game is a classic strategic puzzle that provides hours of entertainment. This robust and engaging open-source project enables users to compete against each other or with the AI player, making it an excellent addition to any gaming portfolio. The system seamlessly integrates various components, including players, boards, and games, allowing for fluid gameplay experience. With its comprehensive architecture and versatile features, the Tic-Tac-Toe game offers a value proposition that appeals to gamers of all ages and skill levels, ensuring its continued relevance and popularity.

---

## 🧩 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | Modular design with clear separation between game logic (`game.py`) and board management (`board.py`). `Player` class provides opponent representation. Simple, yet effective. (45) |
| 🔩 | **Code Quality**  | Pythonic code with concise methods and decent variable naming. Some magic numbers could be improved. Overall, good code quality. (40) |
| 📄 | **Documentation** | Good effort on documentation; however, more details are needed for a comprehensive understanding of the code. Adding type hints would also enhance readability. (30) |
| 🔌 | **Integrations**  | Python dependencies: 'py', 'python'. No external libraries or services integrated. (20) |
| 🧩 | **Modularity**    | Well-structured code with distinct responsibilities for `game`, `board`, and `player` modules. Reusability is good, but more abstractions could be applied. (35) |
| 🧪 | **Testing**       | No testing frameworks or tools used in this repository; unit tests would greatly benefit the project's stability and maintainability.  |
| ⚡️  | **Performance**   | Performance seems decent for small-scale tic-tac-toe games. However, with more players or game iterations, potential issues arise. Optimizations could improve responsiveness.  |
| 🛡️ | **Security**      | No sensitive data is stored; however, there is no protection against unauthorized access or malicious input handling. |
| 📦 | **Dependencies**  | Python dependencies: 'py', 'python'. No external libraries or services are used. (20) |
| 🚀 | **Scalability**   | Not designed for massive scaling, but with optimizations, it could handle moderate-sized games. Larger-scale usage is unlikely without significant code refactoring.  |

---

## 🗂️ Repository Structure

```sh
└── tic-tac-toe/
    ├── __init__.py
    ├── __pycache__
    │   ├── board.cpython-312.pyc
    │   ├── game.cpython-312.pyc
    │   └── player.cpython-312.pyc
    ├── board.py
    ├── game.py
    ├── main.py
    ├── player.py
    └── tests
        ├── test_board.py
        ├── test_game.py
        └── test_player.py
```

---

## 📦 Modules

<details closed><summary>.</summary>

| File                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                        | ---                                                                                                                                                                                                                                                                                                                                                      |
| [player.py](https://github.com/a-touman/tic-tac-toe/blob/master/player.py) | Architecturally, the Player file in Tic-Tac-Toe facilitates opponent representation and decision-making. The `Player` class encapsulates game symbols and provides retrieval functionality. By instantiating multiple player objects, the system enables various player scenarios and strategic interactions, enriching the overall gameplay experience. |
| [main.py](https://github.com/a-touman/tic-tac-toe/blob/master/main.py)     | Starts game session, initializes Game object, and launches gameplay through play method, enabling user interaction within tic-tac-toe board. Focuses on seamless integration with parent repositorys architecture, ensuring smooth communication between components.                                                                                     |
| [board.py](https://github.com/a-touman/tic-tac-toe/blob/master/board.py)   | Enabling Strategic GameplayThe Board class facilitates tic-tac-toe gameplay by maintaining the state of the game board and providing methods for players to make moves, print the current state, and check for wins.                                                                                                                                     |
| [game.py](https://github.com/a-touman/tic-tac-toe/blob/master/game.py)     | Orchestrates Tic-Tac-Toe gameplay, managing player turns and game state on the board. It imports Player and Board classes to interact with them and implements a game loop that alternates players moves, displaying the board after each play. The goal is to detect winning conditions or handle invalid moves.                                        |

</details>

---

## 🚀 Getting Started

**System Requirements:**

* **Python**: `3`

### ⚙️ Installation

<h4>From <code>source</code></h4>

> 1. Clone the tic-tac-toe repository:
>
> ```console
> $ git clone https://github.com/a-touman/tic-tac-toe
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd tic-tac-toe
> ```


### 🤖 Usage

<h4>From <code>source</code></h4>

> Run tic-tac-toe using the command below:
> ```console
> $ python main.py
> ```






---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/a-touman/tic-tac-toe/issues)**: Submit bugs found or log feature requests for the `tic-tac-toe` project.
- **[Submit Pull Requests](https://github.com/a-touman/tic-tac-toe/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/a-touman/tic-tac-toe/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/a-touman/tic-tac-toe
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/a-touman/tic-tac-toe/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=a-touman/tic-tac-toe">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the GNU AGPLv3 License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.


