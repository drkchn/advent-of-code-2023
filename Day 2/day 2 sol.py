my_dict = {}
red_start = 12
green_start = 13
blue_start = 14
possible_games = []

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

        if (red_start < r_marbles) or (green_start < g_marbles) or (blue_start < b_marbles):
            to_add = False
            continue

    if to_add:
        possible_games.append(game)

for one_game in possible_games:
    total += int(one_game)
print(total)
