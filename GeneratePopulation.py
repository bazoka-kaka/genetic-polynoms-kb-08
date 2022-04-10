import random

# fungsi untuk generate populasi baru
def Generate_Initial_Population(problem_size, population_size) -> list:
    """

    parameter
    ----------
    problem_size : int
        size problem, yakni jumlah lokasi/fasilitas

    population_size : int
        jumlah data yang kita inginkan di dalam list

    return
    ------
    list
        mereturn data list
    """

    population = []

    for i in range (population_size):

        # membuat list dengan size == problem size dan nilai random dari 0 - problem_size
        x = random.sample(range(problem_size), problem_size)
        population.append([x, 0])
    
    return population
