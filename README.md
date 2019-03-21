
# Connect SQRT(25)

Connect SQRT(25), based on Gomoku, is a two player japanese board game played on a 19x19 board. Players alternate by placing a stone on the board. The goal of the game is to create a chain of 5 stones in any direction (horizontal, vertical, or diagonal).

## Index
-  [Prerequisites](https://github.com/chuantho/Connect-SqRt25#prerequisites)
- [Installation](https://github.com/chuantho/Connect-SqRt25#installation)
    -  [For Linux/Debian](https://github.com/chuantho/Connect-SqRt25#for-linuxdebian-based-systems)
        - [Option 1: Clone the repo](https://github.com/chuantho/Connect-SqRt25#option-1-clone-the-repo)
        - [Option 2: Download the zipped file](https://github.com/chuantho/Connect-SqRt25#option-2-download-the-zipped-file)
    - [For Windows](https://github.com/chuantho/Connect-SqRt25#for-windows)
	- [For Mac OS X](https://github.com/chuantho/Connect-SqRt25#for-mac-os-x)
- [How to Play](https://github.com/chuantho/Connect-SqRt25#how-to-play)
- [Screenshots](https://github.com/chuantho/Connect-SqRt25#screenshots)
- [Game Features](https://github.com/chuantho/Connect-SqRt25#game-features)
- [Documentation](https://github.com/chuantho/Connect-SqRt25#documentation)
	- [Directory Structure](https://github.com/chuantho/Connect-SqRt25#directory-structure)
	- [Major Classes and Functions](https://github.com/chuantho/Connect-SqRt25#major-classes-and-functions)
	- [Extend Our Game](https://github.com/chuantho/Connect-SqRt25#extend-our-game)
- [Built With](https://github.com/chuantho/Connect-SqRt25#built-with)
- [Authors](https://github.com/chuantho/Connect-SqRt25#authors)
- [License](https://github.com/chuantho/Connect-SqRt25#license)

## Prerequisites
You must install Python 3.6 and PyGame to play Connect SQRT(25). You can install the prerequisites based on your current system configuration by clicking on the following links:
* [Python 3.6](https://www.python.org/downloads/release/python-360/)
* [PyGame](https://www.pygame.org/)

## Installation
### For `Linux/Debian` based systems
#### Option 1: Clone the repo
Open bash by pressing <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd>.
The following commands will install Connect SQRT(25) on your Desktop. You can replace ```Desktop``` with any other directory you choose to install the game directory in.
```bash
$ cd ~/Desktop
$ git clone https://github.com/chuantho/Connect-SqRt25.git
$ cd Connect-SqRt25/
$ chmod +x Connect5.py ## Change the Connect5.py's execute permissions
$ python3 Connect5.py ## This command will launch the game.
```
#### Option 2: Download the zipped file
Download the zipped file by clicking here
Download ```unzip``` if it isn't already installed on your system by typing the following command:
```bash
$ sudo apt-get install unzip
```
Open bash by pressing <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd>.
The following commands will install Connect SQRT(25) on your ```Desktop```. You can replace ```Desktop``` with any other directory you choose to install the game directory in.

### For ```Windows```
* Download the zip file by clicking here.
* Unzip the file via 7-Zip, WinRAR, or any other zip files software.
* In the unzipped file, run the executable named ```Connect5```.

#### For ```MAC OS X```
<TODO>


## How to Play
* The user selects either the 2 player or 2+ players option for the number of players that will play the game.
* The game is initialized with an empty grid.
* Each players is assigned a different color.
* The players click on certain cells of the grid board to fill it up with different colors. The grid cell color cannot change once it is assigned a color other than white.
* The player which gets 5 of the same colored cells in any direction (horizontal, vertical, or diagonal) wins the game.

### Screenshots
 <img width="130" alt="TwoPlayers" src="https://user-images.githubusercontent.com/47638467/54714760-2733ec00-4b28-11e9-82db-3d899d7af731.png">
 <img width="130" alt="EmptyGrid" src="https://user-images.githubusercontent.com/47638467/54714607-b7bdfc80-4b27-11e9-92d9-3beb86d3d28c.png">
<img width="130" alt="ManyPlayers" src="https://user-images.githubusercontent.com/47638467/54714741-1d11ed80-4b28-11e9-9d62-898463ac6640.png">
  <img width="130" alt="WinMove" src="https://user-images.githubusercontent.com/47638467/54714723-0ec3d180-4b28-11e9-9191-2686984959af.png".>
## Game Features
* Polished UI
* 2+ players option

## Documentation

### Directory Structure
All of the source code files are placed in the ```src``` directory. Any images used in the application is included in the ```src/assets``` directory.

### Major Classes and Functions
* Before entering the main game loop, a ```MenuView``` object is initialized in ```Connect5.py``` to determine the number of players that will be playing the game.
* Next, the ```BoardModel``` and ```BoardView``` objects are initialized. The ```BoardModel```class is responsible for setting up the game board and determining if a player has won through its method ```is_won(player, row, column)```. The ```BoardView``` class is responsible for updating the GUI seen by the user, so it takes a ```BoardModel``` object in its constructor to reflect any changes that occur within the ```BoardModel``` class. 
* The game loop in ```Connect5.py``` acts as the controller for our MVC design. It is responsible for extracting the click events from the user to determine where the next stone should be placed within the grid. The job of the game loop is to update the ```BoardView``` object on each user click event. The game loop also calls  the ```is_won(player, row, column)``` method on the ```BoardModel``` object to determine if a player has won the game. The loop terminates if a player wins or the game window is closed.

### Extend Our Game
* Player versus computer variation
	* Add a one player option in the start menu to allow a single player to play with a computer. We are representing a 19x19 board in our game using a list of lists in ```BoardModel``` class located in ```src/Connect5.py```. You can implement your own AI to play with the player by extracting the board from ```BoardModel``` class using the ```get_board()``` method.



## Built With

* [Python 3.6](https://www.python.org/)
* [PyGame](https://www.pygame.org/)

## Authors

* **Shubham Sharma** - [shub-sharma](https://github.com/shub-sharma)
* **Alexandre Gagne** - [salemalex11](https://github.com/salemalex11)
* **Anthony Chu** - [chuantho](https://github.com/chuantho)
* **Hameza Abubeker** - [Hameza-A](https://github.com/Hameza-A)
* **Jason Chabra** -[JasonChabra](https://github.com/JasonChabra)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
