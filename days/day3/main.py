from .input import example, example2, input
import re

def mul(input: str) -> int:
  [left, right] = input[4:-1].split(",")

  return int(left) * int(right)

def part1(input = input):
  matches: list[str] = re.findall(r"mul\(\d+,\d+\)", input, re.IGNORECASE | re.MULTILINE)

  return sum(map(mul, matches))

def part2(input = input):
  matches: list[(str, str, str)] = re.findall(r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))", input, re.IGNORECASE | re.MULTILINE)

  enable_mul = True
  result = 0

  for match in matches:
    if match[1] == "do()":
      enable_mul = True
      continue
    elif match[2] == "don't()":
      enable_mul = False
      continue

    if enable_mul:
      result += mul(match[0])

  return result
