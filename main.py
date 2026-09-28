# 1 = Snake

# -1 = Water
# 0 = Gun
import random
computer = random.choice([-1, 0, 1])

youstr = input("Enter your choice (s/w/g): ")

youdict = {
    "s": 1,
    "w": -1,
    "g": 0
}

reversedict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

you = youdict[youstr]

print(f"You chose {reversedict[you]}")
print(f"Computer chose {reversedict[computer]}")

if computer == you:
    print("Match Draw!")
elif computer == -1 and you == 1:
    print("You Win!")
elif computer == -1 and you == 0:
    print("You Lose!")
elif computer == 1 and you == -1:
    print("You Lose!")
elif computer == 1 and you == 0:
    print("You Win!")
elif computer == 0 and you == -1:
    print("You Win!")
elif computer == 0 and you == 1:
    print("You Lose!")
else:
    print("Something went wrong!")