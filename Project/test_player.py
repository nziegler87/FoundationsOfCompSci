from player import Player
import unittest
import os

class Player_Test(unittest.TestCase):
    def test_init(self):
        player = Player("nate")
        self.assertEqual(player.name, "nate")
        self.assertEqual(player.filename, "nate.txt")
        self.assertEqual(player.score, 0)

    def test_increase_score(self):
        player = Player("nate")

        # increase score by one from 0
        player.increase_score()
        self.assertEqual(player.score, 1)

        player = Player("nate")

        # increase score by 20 from 0
        for i in range(20):
            player.increase_score()
        self.assertEqual(player.score, 20)

        player = Player("nate")

        # increase score by 5 from 5
        player.score = 5
        for i in range(5):
            player.increase_score()
        self.assertEqual(player.score, 10)

    def test_initialize_score(self):
        player = Player("nofile")
        
        # Initialize score from file with a non-existent file
        # where score goes back to zero
        if os.path.exists(player.filename):
            os.remove(player.filename)
        player.initialize_score()
        self.assertEqual(player.score, 0)

        # Initialize score from a file with value 10
        with open("nofile.txt", "w") as outfile:
            outfile.write('10')
        player.initialize_score()
        self.assertEqual(player.score, 10)
        os.remove(player.filename)

    def test_save_score(self):
        player = Player("testfile")

        # set player score to 100
        player.score = 100
        player.save_score()

        # open file and read value
        with open("testfile.txt", "r") as infile:
            score = int(infile.read().strip())
        self.assertEqual(score, 100)
        os.remove("testfile.txt")
        

def main():
    unittest.main(verbosity = 3)

main()
