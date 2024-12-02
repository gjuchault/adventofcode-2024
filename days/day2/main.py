from .input import example, input

def is_safe(line: list[int]) -> bool:
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

  return safe_line

def part1(input = input):
  lines = list(map(lambda l: list(map(int, l.split(" "))), input.splitlines()))

  result = 0

  for line in lines:
    result += 1 if is_safe(line) else 0

  return result

def part2(input = input):
  lines = list(map(lambda l: list(map(int, l.split(" "))), input.splitlines()))

  result = 0

  for initial_line in lines:
    # skip part 2 if line is already safe
    if is_safe(initial_line):
      result += 1
      continue

    for level_to_skip in range(len(initial_line)):
      # copy list, skipping unsafe element
      line = initial_line[:level_to_skip] + initial_line[level_to_skip + 1:]

      if is_safe(line):
        result += 1
        break

  return result
