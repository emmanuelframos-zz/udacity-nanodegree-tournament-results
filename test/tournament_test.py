import unittest
from main.tournament import Tournament

class TournamentTest(unittest.TestCase):
    """
    Class used to validate implementations of main project
    """
    def test_count(self):
        """
        
        :return: 
        """
        #Tournament().count_players();
        Tournament().delete_players();

    def test_standings_before_matches(self):
        """
        
        :return: 
        """
        print "test_standings_before_matches"

    def test_report_matches(self):
        """
        
        :return: 
        """
        print "test_report_matches"

    def test_pairings(self):
        """
        
        :return: 
        """
        print "test_pairings"

if __name__ == '__main__':
    unittest.main()