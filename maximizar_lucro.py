import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose



def imprimir_solucao(solucao):
    for i in range(len(solucao)):
        if solucao[i] == 1:
            print('%s - %s' % (produtos[i][0], produtos[i][2]))


def fit(solucao):
    custo = 0
    espaco_utilizado = 0
    for i in range(len(solucao)):
        if solucao[i] == 1:
            custo += produtos[i][2]
            espaco_utilizado += produtos[i][1]
    if espaco_utilizado > espaco:
        custo = 1
    return custo


def hill_climb(problema):
    solucao, custo = mlrose.hill_climb(problema)
    return solucao, custo


def simulated_annealing(problema):
    solucao, custo = mlrose.simulated_annealing(problema)
    return solucao, custo


def generic_algorithm(problema):
    solucao, custo = mlrose.genetic_alg(problema, pop_size=500, mutation_prob=0.2)
    return solucao, custo



produtos = [('Refrigerador A', 0.751, 999.90),
            ('Celular', 0.0000899, 2911.12),
            ('TV 55', 0.400, 4346.99),
            ('TV 50', 0.290, 3999.90),
            ('TV 42', 0.200, 2999.00),
            ('Notebook A', 0.00350, 2499.90),
            ('Ventilador', 0.496, 199.90),
            ('Microondas A', 0.0424, 308.66),
            ('Microondas B', 0.0544, 429.90),
            ('Microondas C', 0.0319, 299.29),
            ('Refrigerador B', 0.635, 849.00),
            ('Refrigerador C', 0.870, 1199.89),
            ('Notebook B', 0.498, 1999.90),
            ('Notebook C', 0.527, 3999.00)]

espaco = 3 # espaço disponível no caminhão 3m^3

fitness = mlrose.CustomFitness(fit)
problema = mlrose.DiscreteOpt(length = 14, fitness_fn = fitness, maximize = True, max_val = 2)

solucao_hill_climb, custo_hill_climb = hill_climb(problema)
solucao_simulated_annealing, custo_simulated_annealing = simulated_annealing(problema)
solucao_generic_algorithm, custo_generic_algorithm = generic_algorithm(problema)

print("\nAlgoritmo Hill Climb \n\nSolução: ",solucao_hill_climb, "\nValor Total: " ,custo_hill_climb, "\nProdutos:" )
imprimir_solucao(solucao_hill_climb)

print("\nAlgoritmo Simulated_Annealing \n\nSolução: ",solucao_simulated_annealing, "\nValor Total: " ,custo_simulated_annealing, "\nProdutos:")
imprimir_solucao(solucao_simulated_annealing)

print("\nAlgoritmo Generic Algorithm \n\nSolução: ",solucao_generic_algorithm, "\nValor Total: " ,custo_generic_algorithm, "\nProdutos:")
imprimir_solucao(solucao_generic_algorithm)
