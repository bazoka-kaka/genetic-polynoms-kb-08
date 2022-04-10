from utils import Get_Distance_Or_Flow

# harga fungsi untuk mendapat harga masing-masing kromosom
def Cost_Function(population, distances, flows) -> list:
    """

    parameter
    ---------
    populasi : list
        list data
    jarak : list
        list mapping jarak untuk masing-masing data di dalam populasi
    flow : list
        list flow mapping untuk masing-masing data di dalam populasi

    return
    ------
    list
        list data dengan skor fitness yang telah terupdate
    """
    for data in population:

        cost = 0

        searched_list = []

        for j in data[0]:
            for k in data[0]:

                # sejak permasalahannya adalah tipe 1-1, mapping (1, 2) == (2, 1)
                if (k, j) in searched_list or (j, k) in searched_list: continue

                # cost = cost + flow(f1, f2) * distance(d1, d2) untuk masing-masing f1, f2, d1, d2.
                cost += Get_Distance_Or_Flow(j,k, distances) * Get_Distance_Or_Flow(data[0][j], data[0][k], flows)

                # append mapping untuk list yang telah dicari untuk menghemat waktu
                searched_list.append((j, k))


        data[1] = cost

    return population


