import unittest
from main.tournament import Tournament


class TournamentTest(unittest.TestCase):
    """
    Class used to validate implementations of tournament project.
    """

    def test_count(self):
        """
        Test the query that returns the number of players currently registered.
        :return: 
        """
        Tournament().count_players()

    def test_standings_before_matches(self):
        """
        Test the query that returns a list of the players 
        and their win records. 
        :return: 
        """
        Tournament().player_standings()

    def test_report_matches(self):
        """
        Test the population query at matches table.
        :return: 
        """
        Tournament().report_matches()

    def test_pairings(self):
        """
        Test the swiss pairing query.
        :return: 
        """
        Tournament().swiss_pairings()

if __name__ == '__main__':
    unittest.main()