import sys

if len(sys.argv) > 1:
    scores = list(map(int, sys.argv[1:]))
else:
    scores = [78, 85, 90, 66, 80]
    print("No scores provided. Using default values:", scores)

total = sum(scores)
average = total / len(scores)

maximum = max(scores)
minimum = min(scores)

print(f"Scores entered: {scores}")
print(f"Sum of scores: {total}")
print(f"Average score: {average:.2f}")
print(f"Maximum score: {maximum}")
print(f"Minimum score: {minimum}")
