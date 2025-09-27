# 27 Sep 2025
# human vs computer
import random

com = random.choice(["rock", "paper", "scissors"])
print(f"com choose: {com}")

print("choose any of these")
print("1: rock")
print("2: paper")
print("3: scissors")
human = int(input())




def main():
    com_score = 0
    human_score = 0

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
        print("you lose")
    elif human == 2 and com == "scissors":
        com_score += 1
        print("you lose")
    elif human == 3 and com == "rock":
        com_score += 1
        print("you lose")

    print(f"com score: {com_score}")
    print(f"human score: {human_score}")



if __name__ == "__main__":
    main()
    
