class Observer:
    """
    An Observer is any object which inherits from the Observer class and
    implements the update() method.
    """

    def update(self):
        """
        Call update() on the class that inherits this class.

        Raises a NotImplementedError if update() is not implemented by a subclass.
        """
        raise NotImplementedError("Update method is not implmented.")
class Observable:
    """
    The Observable class keeps track of one or more Observer objects by
    attaching or detaching observers. Calling notify_observers() on the
    Observable object after any Observer changes its instance will update()
    all Observer objects.
    """

    def __init__(self):
        """Initialize Observer object with no observers.
        """
        self.observers = []

    def attach(self, o: Observer):
        """Add Observer o to the list of observers.
        """
        self.observers.append(o)


    def detach(self, o: Observer):
        """Remove Observer o from the list of observers.
        """
        self.observers.remove(o)


    def notify_observers(self):
        """Update all observers.
        """
        for o in self.observers:
            o.update(self)
