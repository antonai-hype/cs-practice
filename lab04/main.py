import sys

from stats import average_by_city, read_valid, warmest_city


def main():
    lines = sys.stdin.read().splitlines()
    records = read_valid(lines)
    averages = average_by_city(records)
    best = warmest_city(records)

    empty = sum(1 for line in lines if not line.strip())
    skipped = len(lines) - empty - len(records)

    print(len(records))
    print(skipped)
    print(f"{averages[best]:.1f}")


if __name__ == "__main__":
    main()    