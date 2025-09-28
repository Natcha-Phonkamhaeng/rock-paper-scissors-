# 27 Sep 2025
# human vs computer
import random

com_score = 0
human_score = 0

while True:

    com = random.choice(["rock", "paper", "scissors"])
    # for debugging purpose
    # print(f"com choose: {com}") 

    try:
        print("choose any of these")
        print("1: rock")
        print("2: paper")
        print("3: scissors")
        human = int(input())
    

        # even logic
        if human == 1 and com == "rock":
            com_score += 1
            human_score += 1
            print("even")
        elif human == 2 and com == "paper":
            com_score += 1
            human_score += 1
            print("even")
        elif human ==3 and com == "scissors":
            com_score += 1
            human_score += 1
            print("even")

        # human win logic
        elif human == 1 and com == "scissors":
            human_score += 1
            print("win")
        elif human == 2 and com == "rock":
            human_score += 1
            print("win")
        elif human == 3 and com == "paper":
            human_score += 1
            print("win")

        # human lose logic
        elif human == 1 and com == "paper":
            com_score += 1
            print("lose")
        elif human == 2 and com == "scissors":
            com_score += 1
            print("lose")
        elif human == 3 and com == "rock":
            com_score += 1
            print("lose")

        if com_score == 3 and human_score < 3:
            print("you lose")
            break
        elif human_score == 3 and com_score < 3:
            print("you won")
            break
        elif com_score == 3 and human_score == 3:
            print("DRAW!!")
            break

    except:
        print("please input number 1-3")

    print(f"com score: {com_score}")
    print(f"human score: {human_score}")
