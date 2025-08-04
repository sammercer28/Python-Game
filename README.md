# 🐧 Penguin Game (2D Python Arcade Game)

This is a **2D arcade-style game** I developed in my first year at college using **Python** and the **Pygame** library.  
The objective is to control a penguin, collect coins for points, and avoid falling fireballs that reduce your score.

---

## 🎮 Game Features
- **Player Character**  
  - A penguin that can move left and right across the screen.  

- **Collectibles & Obstacles**  
  - **Coins**: Earn points when collected.  
  - **Fireballs**: Lose points if hit.  

- **Score System**  
  - Real-time score tracking displayed on screen.  
  - High scores saved to `scores.txt` and displayed on a leaderboard.  

- **Pause Functionality**  
  - Press **P** to pause and **U** to unpause the game.  

- **Start Screen & Game Loop**  
  - Enter your player name at the start.  
  - Press **Enter** to begin playing.  

- **Sound Effects**  
  - Coin collection triggers a sound effect.  

---

## 🛠️ Technologies Used
- **Python 3**
- **Pygame** (for graphics, sound, and event handling)
- **Text File I/O** (for saving and displaying high scores)

---

## 🎯 Skills Demonstrated
- Python programming fundamentals  
- Event handling and game loop management in Pygame  
- Collision detection and movement mechanics  
- Implementing pause/play functionality  
- File handling for persistent high scores  
- Creating a leaderboard system  

---

## 📂 File Structure
- **`penguin_game.py`** → Main game code  
- **`scores.txt`** → Stores player names and scores  
- **`background.png`** → Background image  
- **`penguin.png`** → Player character image  
- **`coin.jfif`** → Coin sprite  
- **`fire.jfif`** → Fireball sprite  
- **`collectcoin.mp3`** → Coin collection sound effect  

---

## 🚀 How to Play
1. Install the required library:
   ```bash
   pip install pygame
2. Run the game and follow the controls:
   python penguin_game.py

    Controls:
    A   → Move Left
    D   → Move Right
    P   → Pause
    U   → Unpause
    ESC → Quit
    
    Gameplay:
    - Collect coins (+1 point).
    - Avoid fireballs (-1 point).
    - Scores are saved automatically to scores.txt.

## 🏆 High Score System
The top 5 high scores are displayed on screen after each round.

Scores are saved to scores.txt automatically.

Example scores.txt content:
  Alex 25
  Sam 19
  Jordan 11

## 📧 Contact
If you’d like to discuss this project or my other work, feel free to connect with me on LinkedIn or through the contact details on my CV.




