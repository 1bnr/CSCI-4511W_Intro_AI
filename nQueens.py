import timeit
from search import *

def fitness(q):
    non_attacking = 0
    for row1 in range(len(q)):
        for row2 in range(row1 + 1, len(q)):
            col1 = int(q[row1])
            col2 = int(q[row2])
            row_diff = row1 - row2
            col_diff = col1 - col2

            if col1 != col2 and row_diff != col_diff and row_diff != -col_diff:
                non_attacking += 1

    return non_attacking

def ga_nQueens(nXn, fit_thresh):
    print("runnning")
    # Queens Problem
    gene_pool = range(nXn)
    population = init_population(100, gene_pool, nXn)
    solution = genetic_algorithm(population, fitness, gene_pool=gene_pool, f_thres=fit_thresh)
    print(solution)
    print('fitness: %s / %s, %% %.2f' %(fitness(solution), fit_thresh ,100 * float(fitness(solution)) / fit_thresh))

def dfts_nQueens(nXn):
    solution = depth_first_tree_search(NQueensProblem(nXn))
    print(solution.state)

def bfts_nQueens(nXn):
    solution = breadth_first_tree_search(NQueensProblem(nXn))
    print(solution.state)


sizes = [8, 10, 12, 13, 14]

if __name__ == '__main__':
#    for n in sizes:
#        mytimer(dfts_nQueens(n), 1)
#    for n in sizes:
#        mytimer(bfts_nQueens(n), 1)
    for n in sizes:
        t = timeit.timeit('dfts_nQueens(n)' 'from __main__ import dfts_nQueens, sizes, n', number=1)
        print("runtime average: %s" % (t))
    for n in sizes:
        t = timeit.timeit('bfts_nQueens(n)' 'from __main__ import dfts_nQueens, sizes, n', number=1)
        print("runtime average: %s" %(t))
    for n in sizes:
        t = timeit.timeit('ga_nQueens(n,sum(range(n)))', 'from __main__ import ga_nQueens, sizes, n', number=10)
        print("runtime average: %s" %(t/10))
#        mytimer(ga_nQueens(n,sum(range(n))), 1)
#    dfts_nQueens(19)
#    bfts_nQueens(12)
#    ga_nQueens(10, 45)