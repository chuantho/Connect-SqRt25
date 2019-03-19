class Token:
        """
        Initialize the Token.
        
        Args:
            player_id (int): the player id that owns self
            color (str): the color of self
            x_coord (int): the x-coordinate of self
            y_coord (int): the y-coordinate of self
        """
        def __init__(self, player_id, color, x_coord, y_coord):
            self.player_id = player_id
            self.color = color
            self.x_coord = x_coord
            self.y_coord = y_coord

        def get_player_id(self):
            """Return the player id of self."""
            return self.player_id

        def get_color(self):
            """Return the color of self."""
            return self.color

        def get_x_coord(self):
            """Return the x-coordinate of self."""
            return self.x_coord

        def get_y_coord(self):
            """Return the y-coordinate of self."""
            return self.y_coord
