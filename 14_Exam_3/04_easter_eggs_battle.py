eggs_one = int(input())
eggs_two = int(input())

winner = input()

while winner != "End":

    if winner == "one":
        eggs_two -= 1

    elif winner == "two":
        eggs_one -= 1

    if eggs_two == 0:
        print(f"Player two is out of eggs. Player one has {eggs_one} eggs left.")
        break

    elif eggs_one == 0:
        print(f"Player one is out of eggs. Player two has {eggs_two} eggs left.")
        break

    winner = input()

else:
    print(f"Player one has {eggs_one} eggs left.")
    print(f"Player two has {eggs_two} eggs left.")
