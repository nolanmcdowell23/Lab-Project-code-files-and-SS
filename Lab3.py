import random

num_trials = 1_000_000

num_dice = int(input("How many dice are you rolling? "))
num_sides = int(input("How many sides does each die have? "))

total_of_highest = 0

for trial in range(num_trials):
    highest = 0

    for die in range(num_dice):
        roll = random.randint(1, num_sides)
        if roll > highest:
            highest = roll

    total_of_highest += highest

average_highest = total_of_highest / num_trials

print(f"Average highest roll: {average_highest:.3f}")




total_of_sums = 0

for trial in range(num_trials):
    running_sum = 0
    lowest = 7

    for die in range(4):
        roll = random.randint(1, 6)
        running_sum += roll
        if roll < lowest:
            lowest = roll

    total_of_sums += running_sum - lowest

average_sum = total_of_sums / num_trials
print(f"Average sum of 4d6 after dropping the lowest: {average_sum:.3f}")