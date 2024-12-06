from sys import argv
from days.day1 import main as day1
from days.day2 import main as day2
from days.day3 import main as day3
from days.day4 import main as day4
from days.day5 import main as day5

def main():
    if len(argv) < 2:
        print("Usage: uv run main.py [day]")
        return

    day = argv[1]
    part = argv[2] if len(argv) > 2 else "both"

    match day:
        case "1":
            print("⭐️ Part 1", day1.part1()) if part == "both" or part == "1" else None
            print("⭐️ Part 1", day1.part2()) if part == "both" or part == "2" else None
        case "2":
            print("⭐️ Part 1", day2.part1()) if part == "both" or part == "1" else None
            print("⭐️ Part 2", day2.part2()) if part == "both" or part == "2" else None
        case "3":
            print("⭐️ Part 1", day3.part1()) if part == "both" or part == "1" else None
            print("⭐️ Part 2", day3.part2()) if part == "both" or part == "2" else None
        case "4":
            print("⭐️ Part 1", day4.part1()) if part == "both" or part == "1" else None
            print("⭐️ Part 2", day4.part2()) if part == "both" or part == "2" else None
        case "5":
            print("⭐️ Part 1", day5.part1()) if part == "both" or part == "1" else None
            print("⭐️ Part 2", day5.part2()) if part == "both" or part == "2" else None

if __name__ == "__main__":
    main()
