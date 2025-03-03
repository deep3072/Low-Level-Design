from game import SnakesAndLadder

class Demo:
    def run():
        game = SnakesAndLadder()
        game.initialize_game()
        game.play()

if __name__ == "__main__":
    Demo.run()