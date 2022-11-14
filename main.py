# imports
from Chromosome import Chromosome
import random
# end of imports

# Parameters
n = 10
alfa = 1023
c = 0
l = 10
p_cross = 0.50 + 0.40  # YZ is 40 in my case
p_mut = 0.003 + 0.004  # YZ is 40 in my case
T = 1000
industry_output_graphic_name = "industry_output_graphic.pdf"  # Graph 1
variance_graphic_name = "variance_graphic.pdf"  # Graph 2
# End of Parameters

def print_chromosomes(chromosomes):
    for chromosome in chromosomes:
        print(chromosome)

def update_binary_quantity(chromosome):
    chromosome.A = format(chromosome.X, '010b')

def create_initial_population(chromosomes):
    for i in range(n):
        random_x = random.randint(0,alfa)
        chromosome = Chromosome()
        chromosome.X = random_x
        update_binary_quantity(chromosome)
        chromosomes.append(chromosome)

def get_initial_population(): # ilk jenerasyonu olusturup doner
    initial_generation = []
    create_initial_population(initial_generation)
    return initial_generation

def calculate_outputs(chromosomes):
    for chromosome in chromosomes:
        chromosome.q = chromosome.X * (alfa /(pow(2,l) - 1))

def calculate_and_get_price(chromosomes):
    ind_out = 0
    for chromosome in chromosomes:
        ind_out += chromosome.q
    
    price = alfa - ind_out
    return price

def calculate_relative_fitness_values(chromosomes, price):
    total_fitness = 0
    if price <= 0: # her birinin esit ve 0.1 olacak
        for chromosome in chromosomes:
            chromosome.fitness = 0.1
    else:
        for chromosome in chromosomes:
            chromosome.fitness = price * chromosome.q - c * chromosome.q
            total_fitness += chromosome.fitness

        for chromosome in chromosomes:
            chromosome.fitness = chromosome.fitness / total_fitness

def Recombination(chromosomes): # bu islem sonucu olusan yeni populasyonu donecek 

    chromosomes_recombination = []

    for i in range(n):
        number = random.uniform(0,1)
        if chromosomes[0].fitness >= number:
            chromosomes_recombination[i] = chromosomes[0]
            continue
        if chromosomes[0].fitness + chromosomes[1].fitness >= number:
            chromosomes_recombination[i] = chromosomes[1]
            continue
        if chromosomes[0].fitness + chromosomes[1].fitness + chromosomes[2].fitness  >= number:
            chromosomes_recombination[i] = chromosomes[2]
            continue
        if chromosomes[0].fitness + chromosomes[1].fitness + chromosomes[2].fitness + chromosomes[3].fitness >= number:
            chromosomes_recombination[i] = chromosomes[3]
            continue
        if chromosomes[0].fitness + chromosomes[1].fitness + chromosomes[2].fitness + chromosomes[3].fitness + chromosomes[4].fitness >= number:
            chromosomes_recombination[i] = chromosomes[4]
            continue
        if chromosomes[0].fitness + chromosomes[1].fitness + chromosomes[2].fitness + chromosomes[3].fitness + chromosomes[4].fitness + chromosomes[5].fitness >= number:
            chromosomes_recombination[i] = chromosomes[5]
            continue
        if chromosomes[0].fitness + chromosomes[1].fitness + chromosomes[2].fitness + chromosomes[3].fitness + chromosomes[4].fitness + chromosomes[5].fitness + chromosomes[6].fitness >= number:
            chromosomes_recombination[i] = chromosomes[6]
            continue
        if chromosomes[0].fitness + chromosomes[1].fitness + chromosomes[2].fitness + chromosomes[3].fitness + chromosomes[4].fitness + chromosomes[5].fitness + chromosomes[6].fitness + chromosomes[7].fitness >= number:
            chromosomes_recombination[i] = chromosomes[7]
            continue
        if chromosomes[0].fitness + chromosomes[1].fitness + chromosomes[2].fitness + chromosomes[3].fitness + chromosomes[4].fitness + chromosomes[5].fitness + chromosomes[6].fitness + chromosomes[7].fitness + chromosomes[8].fitness >= number:
            chromosomes_recombination[i] = chromosomes[8]
            continue
        if chromosomes[0].fitness + chromosomes[1].fitness + chromosomes[2].fitness + chromosomes[3].fitness + chromosomes[4].fitness + chromosomes[5].fitness + chromosomes[6].fitness + chromosomes[7].fitness + chromosomes[8].fitness + chromosomes[9].fitness >= number:
            chromosomes_recombination[i] = chromosomes[9]
            continue

    return chromosomes_recombination


# print_chromosomes(get_initial_population())

# eger fiyat negatif veya 0 cikarsa butun oyuncularin relative fitnesslari esit olarak dusunulecek

# simdilik boyle duruyor ancak q lari duzgun araliga getirebilmek icin fiyat hesaplamadan once her bir q degeri 5 e bolunebilir

# veya price negatif oldugu zaman -1 ile carpilabilir


pop = get_initial_population()

calculate_outputs(pop)

print_chromosomes(pop)
print()
print("*****************")
print()

price = calculate_and_get_price(pop)

print("price: " + str(price))

calculate_relative_fitness_values(pop, 100)

print_chromosomes(pop)

# Recombination metodu henuz test edilmedi yani stabil degil. Onu test et
