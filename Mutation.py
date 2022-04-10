import random



# mendapatkan 2 indeks random dalam kromosom dan menukar nilai mereka.

def Mutation_Function(data) -> list:
    """modifikasi kromosom dalam data

    Parameters
    ----------
    gene : list
        data spesifik yang akan dimodifikasi

    Returns
    -------
    list
        returns data yang sudah dimodifikasi
    """

    chromosome = data[0]

    #print("\nKromosom sebelum modifikasi - ")
    #print(chromosome)

    randomNum1 = random.randint(0, len(chromosome) - 1)
    randomNum2 = random.randint(0, len(chromosome) - 1)

    # tukar nilai kedua index
    chromosome[randomNum1], chromosome[randomNum2] = chromosome[randomNum2], chromosome[randomNum1]

    #print("\nkromosomsetelah - ")
    #print(chromosome)

    return data