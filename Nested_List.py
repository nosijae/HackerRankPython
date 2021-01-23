arr = []
scores = set()
second_lowest_names = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    arr.append([name, score])
    scores.add(score)

second_score = sorted(scores)[1]

for name, score in arr:
    if score == second_score:
        second_lowest_names.append(name)

for name in sorted(second_lowest_names):
    print(name, end='\n')
