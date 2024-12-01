from sys import argv
from days.day1 import main as day1

def main():
    if len(argv) < 2:
        print("Usage: uv run main.py [day]")
        return

    day = argv[1]

    match day:
        case "1":
            print("⭐️ Part 1", day1.part1())
            print("⭐️ Part 1", day1.part2())

if __name__ == "__main__":
    main()
