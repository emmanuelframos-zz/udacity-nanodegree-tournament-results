class Player:
    """
    Model class that represents a Player
    """
    def __init__(self, name, created_at):
        """
        Init function that assign properties
        :param name: Player name
        :param created_at: Creation date of the player in database
        """
        self.name = name
        self.created_at = created_at