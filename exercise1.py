class Player:

    def __init__(???):
        ???

    def __str__(???):
        ???

    def level_up(???):
        ???

    def collect_treasure(???):
        ???
 
    def restart(???):
        ???

    def do_battle(???):
        ???

def main():
    # Start the game
    player_1 = ???
    print(player_1)

    # Testing that the player can collect_treasure 9 times
    for i in range(9):
        player_1.collect_treasure()
    print(player_1)

    # This final treasure should cause the player to level up
    player_1.collect_treasure()
    print(player_1)

    # The player should level up again
    for i in range(10):
        player_1.collect_treasure()
    print(player_1)

    # Testing do_battle
    player_1.do_battle(9)
    print(player_1)

    # This final damage should cause a restart of the game
    player_1.do_battle(1)
    print(player_1)

# Run the game
main()
