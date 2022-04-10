import random

def Generate_Distance_Or_Flow(size, upper_bound) -> dict:
    """dapatkan nilai random dari distance dan flows diantara location dan facilities
        
    Parameters
    ----------
    size : int
        panjang dari location/facility
    value_range : int
        batas atas untuk nilai dari distance/flow

    Returns
    -------
    """

    dictionary = {}
    for i in range(size):
        for j in range(size):
            
            if i == j: dictionary[i,j] = 0

            # karena merupakan one-one problem, maka mapping (1,2) == (2,1) jadi tidak perlu membuat duplikat dari mappings
            if (j,i) in dictionary: continue
            
            dictionary[i,j] = random.randrange(0, upper_bound)

    return dictionary


def Get_Distance_Or_Flow(i, j, dictionary) -> int:
    """return  nilai distance atau flow berdasarkan mapping (i, j)

    Parameters
    ----------
    i : int
        first location/facilty
    j : int
        second location/facility
    dictionary : dict
        dicttionary to search

    Returns
    -------
    int
        nilai intger dari dictionary berdasarkan mapping (i, j) 
    """

    if (i, j) not in dictionary:
        return dictionary[j, i]
    
    return dictionary[i, j]



def Chromosome_Cost(chromosome, distances, flows):
    """dapatkan nilai fitness score untuk kromosom tertentu menggunakan rumus minϕ∈Sn ∑ni=1 ∑nj=1 fij⋅dϕ(i)ϕ(j)
        
    Parameters
    ----------
    chromsome : list
        list of values
    distances : list
        list dari mapping jarak setiap data dalam populasi
    flows : list
        list dari mapping flow setiap data dalam populasi
         

    Returns
    -------
    int
        return cost untuk particular chromosome
    """
    searched_list = []
    cost = 0
    
    for j in chromosome:
            for k in chromosome:

                # karena problem adalah tipe 1-1 maka  mapping (1,2) == (2,1).
                if (k, j) in searched_list or (j, k) in searched_list: continue

                # cost = cost + flow(f1, f2) * distance(d1, d2) untuk setiap f1, f2, d1, d2.
                cost += Get_Distance_Or_Flow(j,k, distances) * Get_Distance_Or_Flow(chromosome[j], chromosome[k], flows)

                # append mapping to searched list to save time.
                # lakukan append mapping kedalam searched list untuk menghemat waktu
                searched_list.append((j, k))
    
    return cost


#flows = {(0,0) : 2, (0, 1) : 3, (0, 2): 0, (0, 3): 2, (1, 1): 0, (1,2):0, (1,3): 1, (2, 2): 0, (2, 3): 4, (3,3):0}
#distances = {(0,0): 0, (0, 1): 22, (0, 2): 53, (0, 3): 53, (1, 1): 0, (1, 2): 40, (1, 3): 62, (2, 2): 0, (2, 3): 55, (3, 3): 0}