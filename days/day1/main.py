from collections import Counter
from .input import example, input

def part1(input = input):
  lines = list(map(lambda line: list(map(lambda num: int(num), line.split("   "))), input.splitlines()))

  sorted_columns = list(map(lambda col: sorted(col), zip(*lines)))
  left_col = list(sorted_columns[0])
  right_col = list(sorted_columns[1])

  result = 0

  for i in range(len(left_col)):
    result += abs(right_col[i] - left_col[i])

  return result

def part2(input = input):
  lines = list(map(lambda line: list(map(lambda num: int(num), line.split("   "))), input.splitlines()))

  left_col = list(map(lambda col: sorted(col), zip(*lines)))[0]
  right_col = list(map(lambda col: sorted(col), zip(*lines)))[1]

  right_occurrences = Counter(right_col)

  result = 0

  for i in range(len(left_col)):
    result += left_col[i] * right_occurrences[left_col[i]]

  return result
