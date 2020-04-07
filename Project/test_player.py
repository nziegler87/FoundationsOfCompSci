from player import Player
import unittest
import os

class Player_Test(unittest.TestCase):

    def test_init(self):
        player = Player("nate")
        self.assertEqual(player.name, "nate")
        self.assertEqual(player.filename, "")
        self.assertEqual(player.score, 0)
        self.assertEqual(player.color, "")

    def test_increase_score(self):
        player = Player("nate")

        # increase score by one from 0
        player.increase_score()
        self.assertEqual(player.score, 1)

        player = Player("nate")

        # increase score 20 times, from 0
        for i in range(20):
            player.increase_score()
        self.assertEqual(player.score, 20)

        player = Player("nate")

        # increase score 5 times, from 5
        player.score = 5
        for i in range(5):
            player.increase_score()
        self.assertEqual(player.score, 10)

    def test_set_filename(self):
        # create a player object but don't call set_filename method
        player = Player("Nate")
        self.assertEqual(player.filename, "")
        self.assertNotEqual(player.filename, "Nate.txt")

        # call set_filename method, which should update filename attribute
        player.set_filename()
        self.assertEqual(player.filename, "Nate.txt")

    def test_initialize_score(self):
        player = Player("nofile")
        player.set_filename()
        
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
        player.set_filename()

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
