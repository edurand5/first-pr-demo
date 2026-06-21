import sys


def mean(numbers):
    return sum(numbers) / len(numbers)


def stats(numbers):
    return {
        "count": len(numbers),
        "mean": mean(numbers),
        "min": min(numbers),
        "max": max(numbers),
    }


if __name__ == "__main__":
    nums = [float(x) for x in sys.argv[1:]]
    if not nums:
        print("Usage: python stats.py <num1> <num2> ...")
        sys.exit(1)
    result = stats(nums)
    for key, value in result.items():
        print(f"{key}: {value}")
