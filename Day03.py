import numpy as np
from scipy.signal import convolve2d
import re

in_text = []
with open('Day03_input.txt', 'r') as f:
    in_text = f.readlines()

in_text = [line.strip() for line in in_text]
n_rows = len(in_text)
n_cols = len(in_text[0])


numbers_idx = [[m.span() for m in re.finditer(r'\b\d+\b', line)] for line in in_text]
numbers_dict = {}
for r in range(n_rows):
    for c in range(n_cols):
        for I in numbers_idx[r]:
            if (I[0] <= c) and (c < I[1]):
                numbers_dict[(r, c)] = int(in_text[r][I[0]:I[1]])

input_matrix = np.matrix([[char for char in line] for line in in_text])
numbers_mask = np.char.isdigit(input_matrix)
numbers_matrix = np.zeros((len(in_text), len(in_text[0])), dtype=np.int8)
numbers_matrix[np.where(numbers_mask)] = input_matrix[numbers_mask].astype('int8')
symbols_mask = np.invert(input_matrix == '.') * np.invert(numbers_mask)
symbols_matrix = np.zeros((len(in_text), len(in_text[0])), dtype=np.int8)
symbols_matrix[symbols_mask] = 1

# we do a convolution to determine which cells are in vicinity of a symbol
kernel = np.ones((3, 3), dtype=np.int8)
kernel[1, 1] = 0
possible_summands = convolve2d(symbols_matrix, kernel, mode='same')
mask = (possible_summands>0) * numbers_mask
mask_idx = np.array(np.where(mask)).T.tolist()

#remove horizontally adjacent indices. There should ALWAYS be a space between two numbers
mask_idx2 = []
for i, idx in enumerate(mask_idx):
    if i == 0: 
        mask_idx2.append(idx)
        continue
    if not(idx[1] == mask_idx[i-1][1]+1):
        mask_idx2.append(idx)

# now we can sum up the numbers
sum = 0
valid_nums = []
for idx in mask_idx2:
    sum += numbers_dict[(idx[0], idx[1])]
    valid_nums.append(numbers_dict[(idx[0], idx[1])])


