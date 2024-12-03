from sys import argv
from days.day1 import main as day1
from days.day2 import main as day2
from days.day3 import main as day3

def main():
    if len(argv) < 2:
        print("Usage: uv run main.py [day]")
        return

    day = argv[1]

    match day:
        case "1":
            print("⭐️ Part 1", day1.part1())
            print("⭐️ Part 1", day1.part2())
        case "2":
            print("⭐️ Part 1", day2.part1())
            print("⭐️ Part 2", day2.part2())
        case "3":
            print("⭐️ Part 1", day3.part1())
            print("⭐️ Part 2", day3.part2())

if __name__ == "__main__":
    main()
