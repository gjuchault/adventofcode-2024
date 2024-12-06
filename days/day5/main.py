from typing import Literal, Union
from pydantic import BaseModel, Field, ValidationError
from math import floor
from .input import example, input

class ValidatedResult(BaseModel):
  validated: Literal[True]
  pages: list[int]

class NonValidatedResult(BaseModel):
  validated: Literal[False]
  pages: list[int]
  fixed_pages: list[int]

class PagesValidationResult(BaseModel):
  result: NonValidatedResult | ValidatedResult = Field(discriminator="validated")

def validate_page(pages: list[int], allowed_after: dict[int, set[int]]) -> PagesValidationResult:
  # print("starting validation of", pages)
  valid = True
  fixed_pages = pages.copy()

  for i in range(len(pages) - 1):
    # print("testing", pages[i], pages[i + 1], "valid so far", valid)
    if pages[i + 1] in (allowed_after.get(pages[i]) or []):
      continue
    
    valid = False
    fixed_pages[i], fixed_pages[i + 1] = fixed_pages[i + 1], fixed_pages[i]
    break

  if valid:
    # print("all good", pages)
    return PagesValidationResult(result=ValidatedResult(validated=True, pages=pages))
  else:
    # print(f"had to swap {pages[i]}, {pages[i + 1]}, fixing", pages, "into", fixed_pages)
    deep_fixed_pages = validate_page(fixed_pages, allowed_after)
    # if the last two pages are swapped, the last deep result is invalid so we take the fixed page
    if deep_fixed_pages.result.validated:
      return PagesValidationResult(result=NonValidatedResult(validated=False, pages=deep_fixed_pages.result.pages, fixed_pages=deep_fixed_pages.result.pages))
    # else, the last deep result is valid
    else:
      return PagesValidationResult(result=NonValidatedResult(validated=False, pages=deep_fixed_pages.result.pages, fixed_pages=deep_fixed_pages.result.fixed_pages))

def part1(input = input):
  [rawPairs, rawUpdates] = input.split("\n\n")
  pairs = list(map(lambda rawPair: list(map(int, rawPair.split("|"))), rawPairs.splitlines()))
  updates = list(map(lambda rawUpdate: list(map(int, rawUpdate.split(","))), rawUpdates.splitlines()))

  allowed_after: dict[int, set[int]] = {}

  for [before, after] in pairs:
    if (before in allowed_after):
      allowed_after[before].add(after)
    else:
      allowed_after[before] = set([after])

  result = 0

  for pages in updates:
    if validate_page(pages, allowed_after).result.validated:
      result += pages[floor(len(pages) / 2)]

  return result

def part2(input = input):
  [rawPairs, rawUpdates] = input.split("\n\n")
  pairs = list(map(lambda rawPair: list(map(int, rawPair.split("|"))), rawPairs.splitlines()))
  updates = list(map(lambda rawUpdate: list(map(int, rawUpdate.split(","))), rawUpdates.splitlines()))

  allowed_after: dict[int, set[int]] = {}

  for [before, after] in pairs:
    if (before in allowed_after):
      allowed_after[before].add(after)
    else:
      allowed_after[before] = set([after])

  result = 0

  for pages in updates:
    validation_result = validate_page(pages, allowed_after)
    if not validation_result.result.validated:
      fixed_pages = validation_result.result.fixed_pages
      result += fixed_pages[floor(len(fixed_pages) / 2)]

  return result
