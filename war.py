from GAME import Game
import time


def war():
    game = Game()
    game.play()
    winner = game.getWinner()
    if winner == None:
        print("Tie game!")
    else:
        print("\nWinner = " + winner.getName())
        time.sleep(1)
        print("\nThanks for playing...")


if __name__ == "__main__":
    war()
