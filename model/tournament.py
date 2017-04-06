class Tournament:
    """
    Model class that represents a Tournament
    """
    def __init__(self, name, start_at, created_at):
        """
        Init function that assign properties
        :param name: Tournament name
        :param start_at: Tournament start date
        :param created_at: Creation date of the tournament in database
        """
        self.name = name,
        self.start_at = start_at,
        self.created_at = created_at