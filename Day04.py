import numpy as np

input = open('Day04_input.txt', 'r').readlines()

win = np.zeros((100, len(input)))
games = np.zeros((100, len(input)))
for i, line in enumerate(input):
    gameId, game = line.strip().split(':')
    winningNumbers, roll = game.strip().split('|')
    winningNumbers = [int(n) for n in winningNumbers.strip().split(' ') if not (n=='')]
    roll = [int(n) for n in roll.strip().split(' ') if not(n=='')]
    win[winningNumbers, i] = 1
    games[roll, i] = 1

points = np.ones((1,100)).dot(win * games)
score = np.sum(2**(points[0][points[0]>0]-1))
print("Solution to part 1:", score)

copies = np.ones((len(input),))
for i in range(len(input)):
    copies[(i+1):(i+1+int(points[0][i]))] += copies[i]

print("Solution to part 2:", np.sum(copies))