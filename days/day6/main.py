from typing import Literal
from pydantic import BaseModel, Field
from enum import Enum
import time
from .input import example, input

class Direction(Enum):
  UP = '^'
  RIGHT = '>'
  DOWN = 'v'
  LEFT = '<'

GuardCoords = tuple[int, int, Direction]

class MoveResult(BaseModel):
  result: Literal['move'] | Literal['blocked'] | Literal['out']
  new_coords: GuardCoords

def can_guard_move(grid: list[list[str]], guard_coords: GuardCoords) -> MoveResult:
  (x, y, direction) = guard_coords

  if direction == Direction.UP:
    y -= 1
  elif direction == Direction.RIGHT:
    x += 1
  elif direction == Direction.DOWN:
    y += 1
  elif direction == Direction.LEFT:
    x -= 1

  in_bounds = x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

  if in_bounds and grid[y][x] != '#':
    return MoveResult(result='move', new_coords=(x, y, direction))
  elif in_bounds:
    return MoveResult(result='blocked', new_coords=guard_coords)
  else:
    return MoveResult(result='out', new_coords=guard_coords)
  
def can_guard_rotate(grid: list[list[str]], guard_coords: GuardCoords) -> MoveResult:
  (x, y, direction) = guard_coords

  if direction == Direction.UP:
    return can_guard_move(grid, (x, y, Direction.RIGHT))
  elif direction == Direction.RIGHT:
    return can_guard_move(grid, (x, y, Direction.DOWN))
  elif direction == Direction.DOWN:
    return can_guard_move(grid, (x, y, Direction.LEFT))
  
  # left
  return can_guard_move(grid, (x, y, Direction.UP))

def part1(input = input):
  grid: list[list[str]] = list(map(list, input.splitlines()))

  all_coords: set[tuple[int, int]] = set()
  guard_coords: GuardCoords = (0, 0, Direction.UP)

  for y in range(len(grid)):
    for x in range(len(grid[y])):
      if grid[y][x] in ('^', 'v', '<', '>'):
        guard_coords = (x, y, Direction(grid[y][x]))
        break

  while True:
    all_coords.add((guard_coords[0], guard_coords[1]))
    can_guard_move_result = can_guard_move(grid, guard_coords)
    if can_guard_move_result.result == 'out':
      break

    if can_guard_move_result.result == 'blocked':
      can_guard_rotate_result = can_guard_rotate(grid, guard_coords)
      if can_guard_rotate_result.result == 'blocked':
        break
      guard_coords = can_guard_rotate_result.new_coords
    else:
      guard_coords = can_guard_move_result.new_coords

  return len(all_coords)

def part2(input = input):
  result = 0
  return result
