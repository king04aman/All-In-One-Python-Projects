# Text-Based Adventure Game

Welcome to the **Text-Based Adventure Game**! This Python game is a simple interactive adventure where players explore rooms, collect items, and engage in combat with opponents like goblins and dragons. Each decision you make will affect your inventory and how you handle future challenges.

## Features

- **Two distinct types of doors**: Players can choose between doors, which may lead to hidden items such as swords or shields.
- **Combat System**: Engage in battle with different opponents:
  - **Goblin**: A weak opponent that requires strategy.
  - **Dragon**: A formidable final boss with special attacks.
- **Inventory Management**: Pick up and use items like swords and shields to aid in combat.
- **Game Save & Load**: Your progress is automatically saved, so you can load it later and continue from where you left off.

## Gameplay

- Players start the game by entering their name.
- You are presented with two doors to choose from, each leading to different experiences.
- Items like swords and shields can be found to help you in combat.
- Random encounters with goblins and dragons will test your decision-making skills.
- The game automatically saves your progress, allowing you to resume your adventure later.

## How to Play

1. **Choose a door**: When prompted, choose either the left or right door. Each door may contain hidden treasures like a sword or shield.
2. **Make choices**: Decide whether to pick up items or face challenges.
3. **Combat**: Engage in combat with either a goblin or dragon. Use your sword and shield to protect yourself or defeat enemies.
4. **Save your progress**: The game will automatically save after each major action.
5. **Reload your game**: If you exit the game, you can load it from the last saved point when you return.

## Setup and Installation

1. Ensure you have Python 3 installed on your machine.
2. Clone this repository to your local machine.
3. Navigate to the project directory.
4. Run the text_adventure_game.py file.


## Code Overview

The game is built using Python, and its logic is divided into several components:

- **Opponent Class**: The base class for both weak and strong opponents. Handles basic attack logic.
- **WeakOpponent Class**: A class for weaker opponents like the goblin. Overrides the attack method to reflect weaker attacks.
- **FinalBoss Class**: A subclass of Opponent designed for more challenging enemies like the dragon, with special powers.
- **Combat and Exploration**: Players can choose doors, explore rooms, collect items, and engage in combat.
- **Saving and Loading**: The game state is saved to a file (`game_save.txt`), and players can load this file to continue their progress.

## Error Handling

The game is designed with basic error handling using `try-except` blocks:
- If there are issues with file saving or loading, an error message is displayed.
- Combat logic is wrapped in error handling to prevent crashes due to unexpected input.

Enjoy your adventure!
