import random


def initial_points(player):
    """Roll dice twice and return total / if double points apply"""

    double = "no"

    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    # add the two dice rolls together
    total = roll_one + roll_two
    print(f"{player} - Roll 1: {roll_one} \t| Roll 2: {roll_two} \t| Total: {total} ")

    return total, double


# Intialise rounds points

double_user = "no"
user_start = "no"

# Roll the dice for the user and note if they got a double
initial_user = initial_points("User")
initial_comp = initial_points("Comp")

# Retrieve user points (first item returned from function)
user_points = initial_user[0]
comp_points = initial_comp[0]

# Let the user know if they qualify for double points
if initial_user[1] == "yes":
    double_user = "yes"
    print("Great news - if you win, you will earn double points!")

# assume user goes first...
first = "User"
second = "Computer"
player_1 = user_points
player_2 = comp_points

# if user has fewer points, they start the game
if user_points < comp_points:
    print("You start because your initial roll was less than the computer\n")

# if the user and computer roll equal points...
elif user_points == comp_points:
    print("The initial rolls were the same, the user starts!")

# if the computer has fewer points, switch the computer to 'player 1'
else:
    player_1, player_2 = player_2, player_1
    first, second = second, first

# Loop until we have a winner...
while player_1 < 13 and player_2 < 13:
    print()

    input("Press <enter> to continue this round\n"
          "")

    # first person rolls the die and score is updated
    player_1_roll = random.randint(1, 6)
    player_1 += player_1_roll

    print(f"{first}: Rolled a {player_1_roll} - has {player_1} points")

    # if the first person's score is over 13, end the round
    if player_1 >= 13:
        break

    # second person rolls the die (and score is updated)
    player_2_roll = random.randint(1, 6)
    player_2 += player_2_roll

    print(f"{second}: Rolled a {player_2_roll} - has {player_2} points")

    print(f"{first}: {player_1}  | {second} {player_2}")

print("\nFinal Points...")
print(f"{first}: {player_1}  | {second} {player_2}")


# reset user / computer points
if first == "User":
    user_points = player_1
    comp_points = player_2
else:
    user_points = player_2
    comp_points = player_1

if user_points > comp_points:
    winner = "User"
    round_feedback = "The user won!"
else:
    winner = "Computer"
    round_feedback = "The computer won"

if winner == "User" and double_user == "yes":
    user_points = user_points * 2

print("\nRound Results")
print(f"User Score: {user_points} | Computer Score: {comp_points}")
print(round_feedback)
print()

