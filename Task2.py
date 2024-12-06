import random

population = [
    {"individual": "11000101", "fitness": 10},
    {"individual": "10111011", "fitness": 13},
    {"individual": "11110111", "fitness": 20},
    {"individual": "01100001", "fitness": 15},
]

total_fitness = sum(ind["fitness"] for ind in population)
cumulative_fitness = 0
for i in population:
    i["fitness_ratio"] = i["fitness"] / total_fitness
    cumulative_fitness += i["fitness_ratio"]
    i["cumulative_fitness"] = cumulative_fitness

random_pick = random.random()

selected = None
for i in population:
    if random_pick <= i["cumulative_fitness"]:
        selected = i
        i["selected"] = "Yes"
        break
    else:
        i["selected"] = "No"

print(f"Random Pick: {random_pick:.3f}")
print(f"{'Individual':<15} {'Fitness':<10} {'Fitness Ratio':<15} {'Cumulative Fitness':<20} {'Selected':<10}")
for i in population:
    print(
        f"{i['individual']:<15} {i['fitness']:<10} {i['fitness_ratio']:<15.3f} {i['cumulative_fitness']:<20.3f} {i.get('selected', 'No'):<10}"
    )
