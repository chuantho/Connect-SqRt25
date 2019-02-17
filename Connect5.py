

# M of MVC
class BoardModel:
    """Class responsible for storing the game state : tokens placed on game board"""
    
    
    def __init__(self, num_rows, num_columns):
        """Initialize an empty game board with given rows and columns"""
        
        self.rows = num_rows
        self.columns = num_columns
        self.board = []
        
        for row in range(num_rows):
            self.board.append([])
            for column in range(num_columns):
                self.board[row].append(0)    # Set every cell to value 0 to represent an empty tile
             
                   
    def get_board(self):
        """Return the current board state"""
        return self.board
    
    
    def get_rows(self):
        """Return the number of rows of the game board"""
        return self.rows
    
        
    def get_columns(self):
        """Return the number of columns of the game board"""
        return self.columns
                   
                
                
                   
if __name__ == "__main__":

    model = BoardModel(19, 19)      # Create a new 19x19 game board

    for row in range(model.get_rows()):     # print the game board to text
        print(model.get_board()[row])