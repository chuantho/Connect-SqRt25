import datetime;
import time;

class GameTimer():
    """Create GameTimer to calculate player's turns as well as the match time."""
    def __init__(self):
        pass

    def start(self):
        """Start the timer."""
        self.start_time = datetime.datetime.now()
        return self.start   
    
    def stop(self):
        """Stops the timer."""
        self.stop = datetime.datetime.now()
        return message + str(self.stop - self.start)
      
    def elapsed(self, message="Elapsed: "):
        """Gets the elapsed time from the time start was added."""
        # Return statement to integrate with the view rather than print
        return message + str(datetime.datetime.now() - self.start_time)  
    
    def player_time(self): 
        # Returns true
        count = 0;
        self.start_time = datetime.datetime.now()
        # 15 seconds before player loses their turn
        while(count <=15):
            count=count+1;
            time.sleep(1);
        self.stop = datetime.datetime.now()
        return True;
        

