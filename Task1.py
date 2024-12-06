import random

def fit(individual):
    sum = 0
    for bit in individual:
        sum += int(bit)
    return sum


def generate(size, length):
    pop = []
    fitness_scores = []
    for i in range(size):
        binary_bits = []               
        for bit_index in range(length):
            binary_bits.append(random.choice(['0', '1']))        
        individual = ''.join(binary_bits)           
        
        fitness = fit(individual)           
        pop.append(individual)             
        fitness_scores.append(fitness)      
        print(f"Individual {i + 1}: {individual}, Fitness: {fitness}")
    return pop, fitness_scores


def roulette_wheel_selection(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    fitness_ratios = [fitness / total_fitness for fitness in fitness_scores]
    pick = random.uniform(0, 1)
    
    cumulative_sum = 0
    index = 0

    

    while cumulative_sum < pick and index < len(population):
        cumulative_sum += fitness_ratios[index]
        index += 1
    
    return population[index - 1]     

def crossover(p1, p2):
    point = random.randint(1, len(p1) - 1)
    child1 = p1[:point] + p2[point:]
    child2 = p2[:point] + p1[point:]
    return child1, child2

def mutate(individual, mutation_rate=0.02):
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < mutation_rate:  
            individual[i] = '1' if individual[i] == '0' else '0'
    return ''.join(individual)

def genetic_algorithm(population_size, individual_length, mutation_rate, generations):
    population, _ = generate(population_size, individual_length)
    for generation in range(1, generations + 1):
        print(f"\nGeneration {generation}")
        
        fitness_scores = [fit(individual) for individual in population]
        for i, (individual, fitness) in enumerate(zip(population, fitness_scores), 1):
            print(f"Individual {i}: {individual}, Fitness: {fitness}")
        
        new_population = []
        while len(new_population) < population_size:
            parent1 = roulette_wheel_selection(population, fitness_scores)
            parent2 = roulette_wheel_selection(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            
            new_population.extend([child1, child2])
    
        population = new_population[:population_size]
    
    fitness_scores = [fit(individual) for individual in population]
    print("\nFinal Population:")
    for i, (individual, fitness) in enumerate(zip(population, fitness_scores), 1):
        print(f"Individual {i}: {individual}, Fitness: {fitness}")

    best_individual = max(zip(population, fitness_scores), key=lambda x: x[1])
    return best_individual


population_size = 10
individual_length = 8
mutation_rate = 0.03
num_generations = 3
numOfParents = 2

print("\t\t--------------Task1(1)--------------\n")
population, fitness_scores = generate(population_size, individual_length)


selected_parents = []
for _ in range(numOfParents):
    selected_individual = roulette_wheel_selection(population, fitness_scores)
    selected_parents.append(selected_individual)
print("\t\t--------------Task1(2)--------------\n")
print("\nParents:")
for i, parent in enumerate(selected_parents, 1):
    print(f"Parent {i}: {parent}")


parent1 = selected_parents[0]
parent2 = selected_parents[1]
child1, child2 = crossover(parent1, parent2)

print("\t\t--------------Task1(3)--------------\n")
print("\nAfter Crossover:")
print("Child 1: ", child1)
print("Child 2: ", child2)


child1 = mutate(child1, mutation_rate=mutation_rate)
child2 = mutate(child2, mutation_rate=mutation_rate)

print("\t\t--------------Task1(4)--------------\n")
print("\nAfter Mutation:")
print("Child 1: ", child1)
print("Child 2: ", child2)

print("\t\t--------------Task1(5)--------------\n")
best = genetic_algorithm(population_size, individual_length, mutation_rate, num_generations)
print(f"\nBest Individual: {best[0]}, Fitness: {best[1]}\n")


