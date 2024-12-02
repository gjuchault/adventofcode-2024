from collections import Counter
from .input import example, input

def part1(input = input):
  lines = list(map(lambda l: list(map(int, l.split(" "))), input.splitlines()))

  result = 0

  for line in lines:
    direction = "asc" if line[1] - line[0] > 0 else "dsc"
    safe_line = True

    for i in range(len(line)):
      if i == 0:
        continue
      
      safe_direction = (line[i] - line[i - 1] > 0 and direction == "asc") or (line[i] - line[i - 1] < 0 and direction == "dsc")
      safe_gap = abs(line[i] - line[i - 1]) <= 3 and abs(line[i] - line[i - 1]) > 0

      if not safe_direction or not safe_gap:
        safe_line = False
        break
    
    if safe_line:
      result += 1

  return result

def part2(input = example):
  result = 0

  return result
