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
    # Queens Problem
    gene_pool = range(nXn)
    population = init_population(100, gene_pool, nXn)
    solution = genetic_algorithm(population, fitness, gene_pool=gene_pool, f_thres=fit_thresh)
#    print(solution)
    print('fitness: %s / %s, %% %.2f' %(fitness(solution), fit_thresh ,100 * float(fitness(solution)) / fit_thresh))

def dfts_nQueens(nXn, fit_thresh):
    solution = depth_first_tree_search(NQueensProblem(nXn))
    #print(solution.state)
    #print('fitness: %s / %s, %% %.2f' %(fitness(solution.state), fit_thresh ,100 * float(fitness(solution.state)) / fit_thresh))

def bfts_nQueens(nXn, fit_thresh):
    solution = breadth_first_tree_search(NQueensProblem(nXn))
    #print(solution.state)
    #print('fitness: %s / %s, %% %.2f' %(fitness(solution.state), fit_thresh ,100 * float(fitness(solution.state)) / fit_thresh))


sizes = [8, 10, 12, 13, 14, 15, 16, 17, 18, 20]

if __name__ == '__main__':
    # test the gentic algorithm
    print("Genetic Algorithm Tree Search Test 10x each n x n")
    for n in sizes:
        t = timeit.timeit('ga_nQueens(n,sum(range(n)))', 'from __main__ import ga_nQueens, sizes, n', number=10)
        print("%s x %s" %(n, n))
        print("runtime average: " + "{0:.6f}".format(round(t/10,6)))
    #test depth_first_tree_search
    print("Depth First Tree Search Test 1x each n x n")
    for n in sizes:
        t = timeit.timeit('dfts_nQueens(n,sum(range(n)))', 'from __main__ import dfts_nQueens, sizes, n', number=1)
        print("%s x %s" %( n, n))
        print("%.6f" %t)
    #test breadth_first_tree_search
    print("Breadth First Tree Search Test 1x each n x n")
    for n in sizes:
        t = timeit.timeit('bfts_nQueens(n,sum(range(n)))', 'from __main__ import bfts_nQueens, sizes, n', number=1)
        print("%s x %s" %(n, n))
        print("%.6f" %t)
