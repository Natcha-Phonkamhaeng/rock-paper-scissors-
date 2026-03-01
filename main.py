# 27 Sep 2025

import random

class Game:

    def __init__(self, com_score=None, human_score=None):
        self.com_score = 0
        self.human_score = 0


    def main_menu(self):
        print("choose any of these")
        print("1: rock")
        print("2: paper")
        print("3: scissors")
        

    def game_logic(self):
        com = random.choice(["rock", "paper", "scissors"])
        human = int(input())
        
        if human == 1 and com == "rock":
            self.com_score += 1
            self.human_score += 1
            print("even")
        elif human == 2 and com == "paper":
            self.com_score += 1
            self.human_score += 1
            print("even")
        elif human ==3 and com == "scissors":
            self.com_score += 1
            self.human_score += 1
            print("even")

        # human win logic
        elif human == 1 and com == "scissors":
            self.human_score += 1
            print("win")
        elif human == 2 and com == "rock":
            self.human_score += 1
            print("win")
        elif human == 3 and com == "paper":
            self.human_score += 1
            print("win")

        # human lose logic
        elif human == 1 and com == "paper":
            self.com_score += 1
            print("lose")
        elif human == 2 and com == "scissors":
            self.com_score += 1
            print("lose")
        elif human == 3 and com == "rock":
            self.com_score += 1
            print("lose")

    
    def main(self):
        while True:
            try:
                self.main_menu()
            except:
                print("please input number 1-3")

            self.game_logic()

            if self.com_score == 3 and self.human_score < 3:
                print("you lose")
                break
            elif self.human_score == 3 and self.com_score < 3:
                print("you won")
                break
            elif self.com_score == 3 and self.human_score == 3:
                print("DRAW!!")
                break

        print(f"com score: {self.com_score}")
        print(f"human score: {self.human_score}")

game = Game()

if __name__ == '__main__':
    game.main()


