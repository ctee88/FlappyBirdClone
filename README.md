# FlappyBirdClone
Play my version of the famous Flappy BIrd game!

# Features
- Player controls a bird to help it navigate through pipes

- Simple scoring system

- The game ends when if the bird touches the ground or collides with a pipe

# Requirements
- Created on Python 3.8

- Created using Python library - PyGame

- Developed on Windows 10. 

## Installing instructions for Windows 10
### Python 3.8
1) Locate the appropriate version of Python here:
- https://www.python.org/downloads/

2) Add the file to a known directory of your choice and execute the file. ((C:) drive most accessible)

3) Run the command prompt and access the directory you chose in the previous step.

4) Type ```python``` in to the terminal to check your version.
- Terminal should return: 
```
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32 
Type "help", "copyright", "credits" or "license" for more information. 
```

### PyGame

1) Once the appropriate version of Python has been installed, run the command prompt and simply type:
```
python -m pip install pygame
```
If you have any issues installing pygame, please refer to this video here: 
- https://www.youtube.com/watch?time_continue=39&v=AdUZArA-kZw&feature=emb_title

Tech With Tim does an amazing job covering the various methods of installing pygame. Check out his other content as well, he is an amazing educator!

# Usage
## Running the game
Access the directory of the flappy bird file through the command prompt and simple execute by typing:
```
python main.py
```

## Exiting the game
You can exit the game by clicking the 'X' button at the top right, or you can press 'Q' at anytime.

# Components
See the relevant files for more detailed annotations. My project is made up of many parts:

- main.py - Executable code to run the game is located here
- /images - Contained the images used as elements in the game. Sourced from: 
  1) https://opengameart.org/
  2) https://github.com/sourabhv/FlapPyBird/tree/master/assets/sprites 
  
# Limitations
- The game only works for the specified screen dimensions. If changed, the background and ground images used will not be drawn correctly.
- Static difficulty - remains unchanged as the game progresses.
- High score does not save in between executions of the game.
- No sounds (as of yet, I will try to implement this at a later date!).

