import random

# selection function
def Selection_Function(population) -> list:
    """Ambil data dengan fitness score paling sedikit dari sebuah populasi menggunakan teknik tournament selection 
        
    Parameters
    ----------
    population : list
        list of data

    Returns
    -------
    list
        data dengan fitness score paling sedikit dari sebuah populasi
    """

    # return random list size population_size/5 from population 
    random_k_list = random.sample(population, int(len(population)/5))

    # sort random list berdasarkan fitness score 
    random_k_list.sort(key = lambda x: x[1])
    
    #print("Fittest chromosome - ")
    #print(random_k_list[0])

    # return element pertama setelah sort
    return random_k_list[0]