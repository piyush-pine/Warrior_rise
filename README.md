
# Warrior Game

A Python class-based game that simulates a warrior's journey through battles and training. Track your warrior's level, experience, rank, and achievements as you rise from a "Pushover" to the "Greatest".

## Features
- Warrior levels from 1 to 100 based on experience points
- Rank system with 11 distinct ranks (from Pushover to Greatest)
- Battle mechanic with enemy levels affecting experience gain and fight intensity
- Training sessions to gain achievements and experience
- Battle rules preventing unfair fights against much stronger enemies

## How to Use

1. Clone this repository:
   ```
   git clone https://github.com/your_username/warrior-game.git
   cd warrior-game
   ```

2. Using the `Warrior` class:
   - Instantiate a warrior:  
     ```
     from warrior import Warrior

     bruce_lee = Warrior()
     ```
   - Train your warrior:  
     ```
     bruce_lee.training(["Defeated Chuck Norris", 9000, 1])
     ```
   - Battle enemies by specifying their level:  
     ```
     outcome = bruce_lee.battle(90)
     print(outcome)  # Fight result
     ```
   - Track the warrior's stats with:  
     ```
     print(bruce_lee.level)
     print(bruce_lee.rank)
     print(bruce_lee.achievements)
     ```

3. Run tests (if included):
   ```
   python -m unittest discover tests
   ```

## Requirements
- Python 3.6 or higher

## Project Structure
```
├── warrior.py          # Warrior class implementation
├── tests.py            # Tests for the Warrior class
└── README.md           # This file
```

## Contribution
Feel free to fork, create issues, and submit pull requests. Contributions to improve gameplay mechanics or extend functionality are welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

Enjoy training your warrior to become the greatest!
```
