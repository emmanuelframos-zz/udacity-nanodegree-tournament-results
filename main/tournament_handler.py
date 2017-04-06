from database.dao import DAO


class TournamentHandler:
    """
    Class that contains all operations to realize a tournament.
    """

    @classmethod
    def get_tournament(cls):
        """
        Returns the tournament 
        :return: Tournament
        """
        return DAO.execute_fetch_one("SELECT * FROM  TOURNAMENT")

    @classmethod
    def create_tournament(cls, tournament):
        """
        Create the tournament
        :param tournament: Tournament        
        """
        DAO.execute_not_read_only_query("INSERT INTO TOURNAMENT "
                                        "(NAME, START_AT, CREATED_AT) "
                                        "VALUES (%s, %s, %s)",
                                        (tournament.name, tournament.start_at,
                                         tournament.created_at))

    @classmethod
    def delete_tournaments(cls):
        """
        Remove all tournament from the database.
        """
        DAO.execute_not_read_only_query("DELETE FROM TOURNAMENT")

    @classmethod
    def get_all_players(cls):
        """
        Returns the all players currently registered.
        :return: List of Player
        """
        return DAO.execute_fetch_all("SELECT * FROM PLAYER ")

    @classmethod
    def count_players(cls, tournament):
        """
        Returns the number of players currently registered.
        :return: Long
        """
        return DAO.execute_fetch_one("SELECT COUNT(*) FROM RANK "
                                     "WHERE ID_TOURNAMENT = %s ",
                                     ([tournament[0]]))[0]

    @classmethod
    def create_player(cls, player):
        """
        Create a player in database
        :param player: Player        
        """
        DAO.execute_not_read_only_query("INSERT INTO PLAYER (NAME, CREATED_AT)"
                                        " VALUES (%s, %s)",
                                        (player.name, player.created_at))

    @classmethod
    def register_player(cls, tournament, player, created_at):
        """
        Register a player in a tournament
        :param tournament: Tournament 
        :param player: Player
        :param created_at: Creation date        
        """
        DAO.execute_not_read_only_query(
            "INSERT INTO RANK (ID_TOURNAMENT, ID_PLAYER, POINTS, CREATED_AT) "
            "VALUES (%s, %s, %s, %s)",
            (tournament[0], player[0], 0, created_at))

    @classmethod
    def get_all_registered_players(cls, tournament):
        """
        Return all registered players
        :param tournament: Tournament
        :return: List of registered players
        """
        return DAO.execute_fetch_all("SELECT * FROM RANK "
                                     "WHERE ID_TOURNAMENT = %s",
                                     ([tournament[0]]))

    @classmethod
    def delete_players(cls):
        """
        Remove all the players records from the database.
        """
        DAO.execute_not_read_only_query("DELETE FROM PLAYER")

    @classmethod
    def create_match(cls, tournament, winner, loser, round, date):
        """
        Builds a dictionary having:
        KEY = Query
        VALUE = Params        
        :param tournament: Tournament 
        :param winner: Winner of match
        :param loser: Loser of match        
        :param round: Round number
        :param date: Match date        
        """
        queries = {"INSERT INTO MATCH (ID_TOURNAMENT, WINNER, LOSER, ROUND, "
                   "DATE) VALUES (%s, %s, %s, %s, %s)":
                       (tournament[0], winner[3], loser[3], round, date),
                   "UPDATE RANK SET POINTS = (POINTS + 1) WHERE ID_TOURNAMENT"
                   " = %s AND ID_PLAYER = %s":  (tournament[0], winner[3])}

        DAO.execute_not_read_only_queries(queries=queries)

    @classmethod
    def delete_matches(cls):
        """
        Remove all the matches records from the database.        
        """
        DAO.execute_not_read_only_query("DELETE FROM MATCH")

    @classmethod
    def delete_ranks(cls):
        """
        Remove all the ranks records from the database.        
        """
        DAO.execute_not_read_only_query("DELETE FROM RANK")

    @classmethod
    def player_ranks(cls, tournament):
        """
        Returns a list of the players and their win records, sorted by wins. 
        :return: List of rank
        """
        return DAO.execute_fetch_all("SELECT P.NAME, R.* FROM RANK R"
                                     " JOIN PLAYER P ON R.ID_PLAYER = P.ID "
                                     "WHERE ID_TOURNAMENT = %s "
                                     "ORDER BY POINTS DESC",
                                     ([tournament[0]]))

    @classmethod
    def swiss_pairings(self, players):
        """
        Returns a list of pairs of players for the next round of a match. 
        Receive a ordered list by wins and create the pairs base in it.
        :return: A list of ranking pairs
        """
        swiss_pairings = []
        player_index = 0
        for index in range(len(players) / 2):
            swiss_pairings.append(
                [players[player_index],
                 players[player_index + 1]])
            player_index += 2

        return swiss_pairings

    @classmethod
    def get_num_of_players_by_points(cls, tournament, points):
        """
        Get the number of players based on points
        :param tournament: Tournament
        :param points: Points
        :return: Long
        """
        return DAO.execute_fetch_one("SELECT COUNT(*) FROM RANK "
                                     "WHERE ID_TOURNAMENT = %s "
                                     "AND POINTS = %s",
                                     (tournament[0], points))[0]