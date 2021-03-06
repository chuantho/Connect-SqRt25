
# Connect SQRT(25)

Connect SQRT(25), based on the japanese game Gomoku, is a 2+ player board game. 
Players alternate by claiming tiles on a 19 x 19 board. The goal of the game is to create a chain of 5 tiles in any direction (horizontal, vertical, or diagonal).


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
You must install Python (3.6 or later) and PyGame to play Connect SQRT(25). 
You can install the prerequisites based on your current system configuration by clicking on the following links:
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
* In the unzipped file, run the file named ```Connect5.py``` in your favourite python IDE.

### For ```MAC OS X```
Open Terminal
The following commands will install Connect SQRT(25) on your Desktop. You can replace ```Desktop``` with any other directory you choose to install the game directory in.
```bash
$ cd ~/Desktop
$ git clone https://github.com/chuantho/Connect-SqRt25.git
$ cd Connect-SqRt25/
$ python3 Connect5.py ## This command will launch the game.
```

## How to Play
* The user is prompted with a player selection menu.
* The user selects between 1 to 8 players and clicks ```Start playing``` to play.
* The game is initialized with an empty 19 x 19 board.
* Each player is assigned a random color.
* On their turn, each player can click on an empty tile of the board to claim it and replace it with a tile of their color. 
* Once a tile is claimed, it cannot be changed.
* The first player to claim 5 tiles in any direction (horizontal, vertical, or diagonal) wins the game.
* The game continues until a player wins or quits the game.

### Screenshots
<img width="390" alt="Menu" src="https://user-images.githubusercontent.com/47638467/54785474-b7dbfc00-4bfc-11e9-8010-72b3789f3042.png">
<img width="390" alt="EmptyGrid" src="https://user-images.githubusercontent.com/47638467/54714607-b7bdfc80-4b27-11e9-92d9-3beb86d3d28c.png">
<img width="390" alt="ManyPlayers" src="https://user-images.githubusercontent.com/47638467/54714741-1d11ed80-4b28-11e9-9d62-898463ac6640.png">
<img width="390" alt="WinMove" src="https://user-images.githubusercontent.com/47638467/54714723-0ec3d180-4b28-11e9-9191-2686984959af.png".>
<img width="390" alt="Win animation" src="https://user-images.githubusercontent.com/47638467/54785479-b90d2900-4bfc-11e9-9b1f-8ae64bd25ea3.png">

### Game Features
* Player selection menu
* Single-player option
* Multi-player option (2-8 players)
* In-game prompts and messages
* Win animations

## Documentation

### Directory Structure
The README and LICENSE are placed at the root of the directory.
All of the source code files are placed in the ```src``` directory. 
All images used in the application are replaced in the ```src/assets``` directory.
All game screenshots are placed in the ```screenshots``` directory.

### Major Classes 
* GameModel is responsible for storing the game state including the board, tokens and list of players and colors.
* GameView is responsible for graphically representing the game state using the GameModel.
* GameController is responsible for taking user input from the GameView and modifying the GameModel.
* GameMenu is responsible for showing the menu, allowing player selection and starting the game.

### Major Functions
* ```Model.is_won(player, row, column)``` : Checks if the ```player``` won the game by looping over every possible direction (horizontal, vertical, diagonal) from the tile at position ```board[row][column]```. Returns ```True``` if the player has claimed 5 or more consecutive tiles. 
* ```View.update()``` : Traverses the ```board``` in ```Model``` to find the claimed tiles and uses the ```player_list``` dictionary in ```Model``` to translate each claimed tile from a ```player_number``` to a ```color``` to represent on the graphical interface.
* ```Controller.play()``` : Loops over the ```mouse_events``` until a player wins the game or quits. If the player clicks on an unclaimed tile, the tile is claimed by the player and the tile is assigned their ```player_number``` in the ```Model```. After every move, ```View.update()``` is called to update the graphical representation and ```Model.is_won()``` is called to check if the game is won. If the game is won, ```View``` plays a special win animation and the game is done. If the game is not won, the game continues with the next player. 

### Flow of execution
1. The ```Connect5.py``` file is run.
2. A ```Menu``` object is initialized. The ```Menu``` initializes a graphical interface to allow the user to select the number of players for the game.
3. ```Connect5``` creates players according to the number of players selected in ```Menu```. Each player is assigned a random color and is added to the ```player_list``` dictionary which maps each ```player_number``` to a ```color```.
4. A ```Model``` object is initialized. The ```Model``` takes the ```player_list``` dictionary and stores it. The ```Model``` initializes the empty ```board```.
5. A ```View``` object is initialized. The ```View``` takes a ```Model``` object in its constructor to observe any changes that occur in the ```board```. The ```View``` initializes a graphical interface and displays the empty ```board``` in ```Model```. When the ```Model``` changes, ```View``` updates itself with its ```update()``` method which traverses the ```board``` in ```Model``` to find the claimed tiles and uses the ```player_list``` dictionary in ```Model``` to translate each claimed tile from a ```player_number``` to a ```color```, to represent on the ```View```.
6. A ```Controller``` object is initialized. The ```Controller``` takes a ```View``` object in its constructor to extract ```mouse_events``` when the user clicks on the ```View```. 
7. The ```Controller.play()``` method is called and the game begins.  The ```current_player``` is initialized to the first player in the ```player_list```. The ```play()``` loop continues until ```current_player``` wins or quits. ```current_player``` changes to the next player in ```player_list``` after every move.

### Extend Our Game
* Player versus computer variation
	* Add a one player option in the start menu to allow a single player to play with a computer. We are representing a 19x19 board in our game using a list of lists in ```GameModel``` class located in ```src/Connect5.py```. You can implement your own AI to play with the player by extracting the board from ```GameModel``` class using the ```get_board()``` method.

* Implement GameRounds
	* Add a rounds option in the start menu to allow the player to choose how many rounds they would like to play the game. Inside of the main of ```src/Connect5.py``` the ```GameRounds``` class would be constructed. The ```GameView``` and the number of rounds chosen in the start menu would be sent as arguments for the newly constructed class. The class would then run the game up to the number of specified rounds.

* Implement GameTimer
	* Add a feature for timed games. The game timer would be set so that once the timer is up, the person that is most favoured to win will be determined as the winner. The timer would be called in the main of ```src/Connect5.py``` and the method will be made in the ```GameModel``` class.Implement the GameTimer by creating an instance of GameTimer located in src/GameTimer.py. From the GameTimer instance, call the ```player_time()``` method to calculate the time a player can take before their turn is over. This timer will automatically reset to  when the player's turn ends. To calculate the length of the match, call the ```start()``` function when the game starts  and ```end()``` function when the ```Model.is_won()``` function returns ```True```.
	
* Implement TurnTimer
	* Add a feature for timed turns. The turn timer would be set so that once the turn timer is up, the player's piece is randomly placed. The timer would be called in the main of ```src/Connect5.py``` and the time count itself would be stored in the main. The method that randomizes the tile placement will be made in the ```GameModel``` class. Turn timer is currently implemented in a separate branch, however an unknown bug is causing a delay in the game when tiles are claimed. The reason is likely due to the ```sleep``` call in the function. 

## Built With

* [Python 3.6](https://www.python.org/)
* [PyGame](https://www.pygame.org/)

## Authors

* **Shubham Sharma** - [shub-sharma](https://github.com/shub-sharma)
* **Alexandre Gagne** - [salemalex11](https://github.com/salemalex11)
* **Anthony Chu** - [chuantho](https://github.com/chuantho)
* **Hameza Abubeker** - [Hameza-A](https://github.com/Hameza-A)
* **Jason Chabra** - [JasonChabra](https://github.com/JasonChabra)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
