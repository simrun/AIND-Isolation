"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload

from sample_players import center_score, improved_score


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def testMiniMaxCenter(self):
        time_left = lambda: 1000

        player1 = game_agent.MinimaxPlayer(1, center_score)
        player2 = game_agent.MinimaxPlayer(1, center_score)

        game = isolation.Board(player1, player2, 9, 9)
        game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1,
                             1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 31]

        assert(player1 == game.active_player)

        self.assertFalse(player1.get_move(game, time_left) == (2,2))

    def testMiniMaxImproved(self):
        time_left = lambda: 1000

        player1 = game_agent.MinimaxPlayer(1, improved_score)
        player2 = game_agent.MinimaxPlayer(1, improved_score)

        game = isolation.Board(player1, player2, 9, 9)
        game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
                             1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 24]

        assert(player1 == game.active_player)

        self.assertFalse(player1.get_move(game, time_left) == (7,0))

if __name__ == '__main__':
    unittest.main()
