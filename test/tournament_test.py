import unittest
import datetime
from main.tournament_handler import TournamentHandler
from model.player import Player
from model.tournament import Tournament


class TournamentTest(unittest.TestCase):
    """
    Class used to test implementations of tournament project.
    """

    def test_01_clean_database(self):
        """
        Method that tests cleaning of the database     
        """
        tournament_handler = TournamentHandler()

        tournament_handler.delete_ranks()
        print "Removing all ranks."

        tournament_handler.delete_matches()
        print "Removing all matches."

        tournament_handler.delete_players()
        print "Removing all players."

        tournament_handler.delete_tournaments()
        print "Removing all tournaments."

        print "-----------------------------------------"

    def test_02_create_tournament(self):
        """
        Method that tests creation of a tournament in 
        database
        """
        tournament_handler = TournamentHandler()

        tournament = Tournament('CSGO Major - One Vs One 2017',
                                datetime.datetime.now(),
                                datetime.datetime.now())

        tournament_handler.create_tournament(tournament)

        self.assertTrue(tournament_handler.get_tournament() is not None,
                        "The tournament were not created.")

        print "Created tournament: [" + tournament.name[0] + "]"

        print "-----------------------------------------"

    def test_03_create_players(self):
        """
        Method that tests creation of players in database
        """
        tournament_handler = TournamentHandler()

        players = [
            Player('FALLEN "O VERDADEIRO"', datetime.datetime.now()),
            Player('COLDZERA', datetime.datetime.now()),
            Player('FNX', datetime.datetime.now()),
            Player('DEV1CE', datetime.datetime.now()),
            Player('COGU', datetime.datetime.now()),
            Player('OLOFMEISTER', datetime.datetime.now()),
            Player('GUARDIAN', datetime.datetime.now()),
            Player('S1MPLE', datetime.datetime.now()),
            Player('NIKO', datetime.datetime.now()),
            Player('FER', datetime.datetime.now()),
            Player('TACO', datetime.datetime.now()),
            Player('KIOSHIMA', datetime.datetime.now()),
            Player('XYP9X', datetime.datetime.now()),
            Player('DUPREEH', datetime.datetime.now()),
            Player('FLUSHA', datetime.datetime.now()),
            Player('SNAX', datetime.datetime.now())
        ]

        for player in players:
            tournament_handler.create_player(player)
            print "Player [" + player.name + "] created."

        self.assertTrue(len(tournament_handler.get_all_players()) > 0,
                        "The players were not created.")

        print "-----------------------------------------"

    def test_04_register_players(self):
        """
        Method that tests registering of players in tournament with 
        0 points initially         
        """
        tournament_handler = TournamentHandler()

        tournament = tournament_handler.get_tournament()

        players = tournament_handler.get_all_players()

        for player in players:
            tournament_handler.register_player(tournament, player,
                                               datetime.datetime.now())
            print "Player [" + player[1] + "] registered in tournament."

        self.assertTrue(len(tournament_handler.
                            get_all_registered_players(tournament)) > 0,
                        "The players were not registered.")

        print "-----------------------------------------"

    def test_05_count_players(self):
        """
        Method that tests if there are players registered in tournament         
        """
        tournament_handler = TournamentHandler()

        tournament = tournament_handler.get_tournament()

        player_number = tournament_handler.count_players(tournament)

        self.assertTrue(player_number > 0, "The number of registered must"
                                           "be greater than zero.")

        print "There are [" + str(player_number) + "] players registered " \
                                                   "in tournament."

        print "-----------------------------------------"

    def test_06_create_matches(self):
        """
        Method that tests match creation and swiss pairings         
        """
        tournament_handler = TournamentHandler()

        tournament = tournament_handler.get_tournament()

        for round_num in range(4):
            player_ranks = tournament_handler.player_ranks(tournament)
            swiss_pairings = tournament_handler.swiss_pairings(player_ranks)

            self.assertTrue(len(swiss_pairings) > 0, "Swiss pairings can not "
                                                     "be empty.")

            for swiss_pair_num in range(len(swiss_pairings)):
                self.assertTrue(len(swiss_pairings[swiss_pair_num]) == 2,
                                "Swiss pairings must have two elements.")

                winner = swiss_pairings[swiss_pair_num][0]
                loser = swiss_pairings[swiss_pair_num][1]

                tournament_handler.create_match(tournament, winner, loser,
                                                round_num + 1,
                                                datetime.datetime.now())

                print "Round [" + str(round_num + 1) + "], Game [" + \
                      str(swiss_pair_num + 1) + "], Winner [" \
                      + winner[0] + "], Loser [" + loser[0] + "]"
            print

        print "-----------------------------------------"

    def test_07_check_rank(self):
        """
        Method that tests if ranking points are correct        
        """
        tournament_handler = TournamentHandler()

        tournament = tournament_handler.get_tournament()

        player_ranks = tournament_handler.player_ranks(tournament)
        for player_rank in player_ranks:
            print "[" + player_rank[0] + "], points: " + str(player_rank[4])

        self.assertTrue(tournament_handler
                        .get_num_of_players_by_points(tournament, 0) == 1,
                        "Just one player must have 0 points.")
        self.assertTrue(tournament_handler
                        .get_num_of_players_by_points(tournament, 1) == 4,
                        "Just four players must have 1 points.")
        self.assertTrue(tournament_handler
                        .get_num_of_players_by_points(tournament, 2) == 6,
                        "Just six player must have 2 points.")
        self.assertTrue(tournament_handler
                        .get_num_of_players_by_points(tournament, 3) == 4,
                        "Just four player must have 3 points.")
        self.assertTrue(tournament_handler
                        .get_num_of_players_by_points(tournament, 4) == 1,
                        "Just one player must have 4 points.")

        print "-----------------------------------------"

    def test_08_check_winner(self):
        """
        Method that tests if the player really is the winner         
        """
        tournament_handler = TournamentHandler()

        tournament = tournament_handler.get_tournament()

        winner = tournament_handler.player_ranks(tournament)[0]

        self.assertTrue(winner[4] == 4, "The winner must have 4 points.")

        print "The winner of [" + tournament[1] + "] is [" + winner[0] + \
              "], congratulations!"

if __name__ == '__main__':
    unittest.main()