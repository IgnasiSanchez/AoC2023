import regex as re

f = open("Day01_input.txt", "r")
lines = f.readlines()
f.close()

def convert_to_number(l):
    first = l[0]
    last = l[-1]
    return int(last) + 10*int(first)

nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
calibration_values = []
sum = 0
for w in lines:
    digits = []
    for d in re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', w, overlapped=True):
        if d in nums:
            digits.append(nums.index(d)+1)
        else:
            digits.append(int(d))
    calibration_values.append(convert_to_number(digits))
    sum = sum + convert_to_number(digits)
