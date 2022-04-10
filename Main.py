import random
from GeneratePopulation import Generate_Initial_Population
from Mutation import Mutation_Function
from Crossover import Crossover_Function
from Selection import Selection_Function
from Fitness import Cost_Function
from utils import *

import sys


# genetic rep dari solusi
chromosome = [1, 2, 3, 4, 5] # di mana index == location dan chromosome[index] == facility

fitness_score = 700 # cost fungsi untuk kromosom ini secara partikular

data = [[chromosome], fitness_score] # data adalah sebuah list yang mengandung kromosom dan fitness_score

def GeneticAlgorithm(problem_size, population_size, distances, flows, number_of_iterations):

    # Get dictionary that generates random value for flows and distance between locations and facilities
    # mendapat dictionary yang melakukan generasi value random untuk flow dan jarak antara lokasi dan fasilitas

    # generate populasi awal
    population = Generate_Initial_Population(problem_size, population_size)

    
    solution = int(sys.maxsize)
    next_generation = []
    n = 0


    while n < number_of_iterations:

        # mendapat harga fungsi untuk masing-masing data di populasi
        population = Cost_Function(population=population, distances=distances, flows=flows)

        # mengurutkan populasi berdasarkan skor fitness
        population.sort(key = lambda x: x[1])

        # mendapat data yang paling fit
        fittest_data = list.copy(population[0])


        # mengecek data yang paling fit dan menprintnya
        if fittest_data[1] < solution:
            result = list.copy(fittest_data)
            solution = fittest_data[1]
            print("\nSolution for iteration - " + str(n))
            print(result)


        while len(next_generation) < len(population):

            # gunakan fungsi seleksi untuk mendapatkan 2 kromosom yang fit
            data1 = Selection_Function(population)
            data2 = Selection_Function(population)

            # corssover 2 kromosom
            crossed_over_data = Crossover_Function(data1, data2)

            # mutasi kedua kromosom
            offspring1 = Mutation_Function(crossed_over_data[0])
            offspring2 = Mutation_Function(crossed_over_data[1])

            # tambahkan hasil ke generasi berikutnya
            next_generation.append(offspring1)
            next_generation.append(offspring2)

        # ulangi iterasi dengan generasi baru
        population = next_generation
        next_generation = []
        n+=1
    
    
    # print hasil akhir
    print("Final solution after " + str(n) +" iterations = ")
    print(result)

    return result
    

# sebuah fungsi pembantu untuk membantu generasi jarak dan flow random
distances = Generate_Distance_Or_Flow(6, 20)
flows = Generate_Distance_Or_Flow(6, 4)

# test run sebuah contoh dengan input_size 6, population_size 30 dan melakukan 1000 iterasi
GeneticAlgorithm(6, 30, distances, flows, 1000)