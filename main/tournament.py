from database.postgre_connection import PostgreConnection


class Tournament():
    """
    
    """

    def execute_not_read_only_query(self, query):
        connection = PostgreConnection.get_connection();

        cursor = connection.cursor()
        cursor.execute(query)

        connection.commit()

    def execute_read_only_query(self, query):
        connection = PostgreConnection.get_connection();

        cursor = connection.cursor()
        cursor.execute(query)

        return cursor.fetchall()


    def delete_players(self):
        """
        Remove all the players records from the database.
        :return: 
        """
        self.execute_not_read_only_query("DELETE FROM PLAYER")

    def delete_matches(self):
        """
        Remove all the matches records from the database.
        :return: 
        """
        self.execute_not_read_only_query("DELETE FROM MATCH")

    def count_players(self):
        """
        Returns the number of players currently registered.
        :return: 
        """

    def registerPlayer(self):
        """
        Adds a player to the tournament database.
        :return: 
        """
        print

    def playerStandings(self):
        """
        Returns a list of the players and their win records, sorted by wins. 
        :return: 
        """
        print()

    def report_match(self):
        """
        This is to simply populate the matches table and record the winner 
        and loser as (winner,loser) in the insert statement.
        :return: 
        """

    def swiss_pairings(self):
        """
        Returns a list of pairs of players for the next round of a match. 
        Here all we are doing is the pairing of alternate players from 
        the player standings table, zipping them up and appending them 
        to a list with values:(id1, name1, id2, name2)
        :return: 
        """