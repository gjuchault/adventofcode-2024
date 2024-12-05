from typing import Literal
import re
import numpy as np
from .input import example, example2, input

def hor(input: list[list[str]]) -> list[str]:
  return list(map(lambda x: ''.join(x), input))

def ver(input: list[list[str]]) -> list[str]:
  return list(map(lambda x: ''.join(x), zip(*input)))

def diag(input: list[list[str]], dir: Literal["ltr", "rtl"]) -> list[str]:
  arr: np.ndarray[np.ndarray[str]] = np.array(input) if dir == "ltr" else np.rot90(np.array(input))

  all_diags: list[str] = []

  for i in range(len(input[0])):
    all_diags.append(''.join(np.diag(arr, i).tolist()))
    if i != 0:
      all_diags.append(''.join(np.diag(arr, -1 * i).tolist()))

  return all_diags

def part1(input = input):
  grid: list[list[str]] = list(map(list, input.splitlines()))

  result = 0

  for line in hor(grid) + ver(grid) + diag(grid, "ltr") + diag(grid, "rtl"):
    result += len(re.findall(r'XMAS', line)) + len(re.findall(r'SAMX', line))

  return result

def part2(input = input):
  grid: list[list[str]] = list(map(list, input.splitlines()))
  
  all_a_coords: list[(int, int)] = []

  def get_char(x: int, y: int) -> str:
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y]):
      return ""
    return grid[y][x]

  for y in range(len(grid)):
    for x in range(len(grid[y])):
      char = grid[y][x]
      if char != "A":
        continue

      mas_diag_ltr = (get_char(x - 1, y - 1) == "M" and get_char(x + 1, y + 1) == "S")
      mas_diag_ltr_rev = (get_char(x - 1, y - 1) == "S" and get_char(x + 1, y + 1) == "M")
      mas_diag_rtl = (get_char(x + 1, y - 1) == "M" and get_char(x - 1, y + 1) == "S")
      mas_diag_rtl_rev = (get_char(x + 1, y - 1) == "S" and get_char(x - 1, y + 1) == "M")

      if (mas_diag_ltr or mas_diag_ltr_rev) and (mas_diag_rtl or mas_diag_rtl_rev):
        all_a_coords.append((x, y))

  return len(set(all_a_coords))
