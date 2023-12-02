my_dict = {}
game_multiplier = []

total = 0

with open('input.txt', 'r') as file:
    for line in file:
        new_line = line.lstrip('Game ').strip()
        split_list = new_line.split(': ')

        # key = game ID number
        # value = the minigame in each game round
        game_id = split_list[0]
        games = split_list[1].split('; ')

        my_dict[game_id] = games

for game in my_dict:
    all_games_list = my_dict[game]

    to_add = True

    g_list, r_list, b_list = set(), set(), set()

    for each_game in all_games_list:
        games_list = each_game.split(',')

        g_marbles, r_marbles, b_marbles = 0, 0, 0

        for marbles in games_list:
            if 'green' in marbles:
                g_marbles = int(marbles.rstrip(' green').strip())
            if 'red' in marbles:
                r_marbles = int(marbles.rstrip(' red').strip())
            if 'blue' in marbles:
                b_marbles = int(marbles.rstrip(' blue').strip())

            g_list.add(g_marbles)
            r_list.add(r_marbles)
            b_list.add(b_marbles)

    max_green = max(g_list)
    max_red = max(r_list)
    max_blue = max(b_list)

    multiplier = max_green * max_red * max_blue
    game_multiplier.append(multiplier)

for one_game in game_multiplier:
    total += one_game
print(total)
