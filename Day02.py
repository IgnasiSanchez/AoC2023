game_data = []
with open('Day02_input.txt', 'r') as f: 
    game_data = [x.strip() for x in f]

max_colors = {'red': 12, 'green': 13, 'blue': 14}

possible_games = []
possible_sum = 0
power_sets = []
power_sum = 0
for game in game_data:
    g = game.strip()
    g_id = g.split(':')[0]# save game id in case they are not sequential (I'm too lazy to check)
    g_reveals = g.split(':')[1].split(';')
    flag = 0 #this checks if the game is possible
    fewest_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for rev in g_reveals:
        r = rev.split(',')
        for col in r:
            n, c = col.strip().split(" ")
            n = int(n)
            if n > fewest_cubes[c]:
                fewest_cubes[c] = n
            if n > max_colors[c]:
                flag = 1
    power_sets.append(fewest_cubes)
    power_sum += fewest_cubes['red'] * fewest_cubes['green'] * fewest_cubes['blue']
    if not flag:
        id_num = int(g_id.split(' ')[1].strip())
        possible_games.append(id_num)
        possible_sum += id_num

print('Solution to part 1: ', possible_sum)
print('Solution to part 2: ', power_sum)