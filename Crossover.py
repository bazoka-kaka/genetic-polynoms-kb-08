import random
from iteration_utilities import duplicates

# fungsi crossover
def Crossover_Function(data1, data2):
    """
    Parameter
    ---------
    data1 : list
        data list mengandung skor kromosom and fitness
    data2 : list
        data list mengandung skor kromosom and fitness 

    return values
    -------------
    list
        mengembalikan list yang mengandung 2 data dengan kromosom yang telah termodifikasi
    """
    # untuk fungsi ini, kami memodifikasi fungsi uniform crossover untuk menyelesaikan problem duplikasi setelah crossover

    data1[1] = 0
    data2[1] = 0
    chromosome1 = list.copy(data1[0])
    chromosome2 = list.copy(data2[0])

    # untuk  masing-masing index di kedua kromosom, gunakan satu pelemparan koin untuk menentukan index mana yang di cross over
    for i in range(len(chromosome1)):

        cointoss = random.randrange(2)
        if cointoss == 0:
            chromosome1[i], chromosome2[i] = chromosome2[i], chromosome1[i]

    # menemukan duplikasi setelah cross over
    dupes_in_ch1 = list(duplicates(chromosome1))
    dupes_in_ch2 = list(duplicates(chromosome2))

    # menghandle duplikasi jika ada yang ditemukan
    for i in dupes_in_ch1:
        if i in chromosome1: chromosome1.remove(i)
        chromosome2.append(i)
    
    for i in dupes_in_ch2:
        if i in chromosome2: chromosome2.remove(i)
        chromosome1.append(i)

    # mengganti kromosom yang telah termodifikasi di data
    data1[0] = chromosome1
    data2[0] = chromosome2

    return [data1, data2]
