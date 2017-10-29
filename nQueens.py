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

def ga_nQueens(nXn, fit_thresh, p, m):
    # Queens Problem
    gene_pool = range(nXn)
    population = init_population(p, gene_pool, nXn)
    solution = genetic_algorithm(population, fitness, gene_pool=gene_pool, f_thres=fit_thresh, pmut=p)
#    print(solution)
    print("{0:.2f}".format(100 * float(fitness(solution)) / fit_thresh))

def dfts_nQueens(nXn, fit_thresh):
    solution = depth_first_tree_search(NQueensProblem(nXn))
    #print(solution.state)
    #print('fitness: %s / %s, %% %.2f' %(fitness(solution.state), fit_thresh ,100 * float(fitness(solution.state)) / fit_thresh))

def bfts_nQueens(nXn, fit_thresh):
    solution = breadth_first_tree_search(NQueensProblem(nXn))
    #print(solution.state)
    #print('fitness: %s / %s, %% %.2f' %(fitness(solution.state), fit_thresh ,100 * float(fitness(solution.state)) / fit_thresh))

def bfs_nQueens(nXn, fit_thresh):
    solution = breadth_first_search(NQueensProblem(nXn))

#sizes = [8, 10, 12, 13, 14, 15, 16, 17, 18, 20]
sizes = [30]
popsize = [100, 200, 300]
mutation = [0.05, 0.1, 0.15, 0.2, 0.25]
if __name__ == '__main__':
    # test the gentic algorithm
    print("Genetic Algorithm Tree Search Test 10x each n x n")
    for n in sizes:
        print("%s x %s" %(n, n))
        t = timeit.timeit('ga_nQueens(n,sum(range(n)),100, 0.1)', 'from __main__ import ga_nQueens, sizes, n', number=10)
        print("{0:.6f}".format(round(t/10,6)))

#    for ppn in popsize:
#        for mf in mutation:
#            print("pop: %s,mut: %s" %(ppn, mf))
#            t = timeit.timeit('ga_nQueens(13,sum(range(13)),ppn, mf)', 'from __main__ import ga_nQueens, ppn, mf', number=10)
#            print("{0:.6f}".format(round(t/10,6)))

    #test depth_first_tree_search
    print("Depth First Tree Search Test 1x each n x n")
    for n in sizes:
        t = timeit.timeit('dfts_nQueens(n,sum(range(n)))', 'from __main__ import dfts_nQueens, sizes, n', number=1)
        print("%s x %s" %( n, n))
        print("%.6f" %t)
    #test breadth_first_tree_search
#    print("Breadth First Tree Search Test 1x each n x n")
#    for n in sizes:
#        t = timeit.timeit('bfts_nQueens(n,sum(range(n)))', 'from __main__ import bfts_nQueens, sizes, n', number=1)
#        print("%s x %s" %(n, n))
#        print("%.6f" %t)

#    print("Breadth First Search Test 1x each n x n")
#    for n in [10]:
#        t = timeit.timeit('bfs_nQueens(n,sum(range(n)))', 'from __main__ import bfs_nQueens, sizes, n', number=1)
#        print("%s x %s" %(n, n))
#        print("%.6f" %t)
