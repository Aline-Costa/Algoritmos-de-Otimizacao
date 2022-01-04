import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose


def imprimir_voos(agenda):
    id_voo = -1
    total_preco = 0
    for i in range(len(agenda) // 2):
        nome = localizacoes_pessoas[i][0]
        origem = localizacoes_pessoas[i][1]
        id_voo += 1
        ida = voos[(origem, destino)][agenda[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(destino, origem)][agenda[id_voo]]
        total_preco += volta[2]
        print('%10s%10s %5s-%5s %3s %5s-%5s %3s' % (nome, origem, ida[0], ida[1], ida[2], volta[0], volta[1], volta[2]))
    print('Preço total: ', total_preco)


def fit(agenda):
    id_voo = -1
    total_preco = 0
    for i in range(len(agenda) // 2):
        origem = localizacoes_pessoas[i][1]
        id_voo += 1
        ida = voos[(origem, destino)][agenda[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(destino, origem)][agenda[id_voo]]
        total_preco += volta[2]
  
    return total_preco


def hill_climb(problema):
    solucao, custo = mlrose.hill_climb(problema, random_state=5)
    return solucao, custo


def simulated_annealing(problema):
    solucao, custo = mlrose.simulated_annealing(problema, schedule=mlrose.decay.GeomDecay(init_temp=10000), random_state=5)
    return solucao, custo


def generic_algorithm(problema):
    solucao, custo = mlrose.genetic_alg(problema, pop_size=500, mutation_prob=0.2, random_state=5)
    return solucao, custo



localizacoes_pessoas = [('Lisboa', 'LIS'),
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'),
           ('Dublin', 'DUB'),
           ('Bruxelas', 'BRU'),
           ('Londres', 'LHR')]
voos = {}

for linha in open('flights.txt'):
    origem, destino, saida, chegada, preco = linha.split(',')
    voos.setdefault((origem, destino), [])
    voos[(origem, destino)].append((saida, chegada, int(preco)))

fitness = mlrose.CustomFitness(fit)
problema = mlrose.DiscreteOpt(length=12, fitness_fn=fitness, maximize = False, max_val = 10)

solucao_hill_climb, custo_hill_climb = hill_climb(problema)
solucao_simulated_annealing, custo_simulated_annealing = simulated_annealing(problema)
solucao_generic_algorithm, custo_generic_algorithm = generic_algorithm(problema)

print("\nAlgoritmo Hill Climb \n\nSolução: ",solucao_hill_climb, "\nCusto" ,custo_hill_climb, "\nVoos:" )
imprimir_voos(solucao_hill_climb)

print("\nAlgoritmo Simulated_Annealing \n\nSolução: ",solucao_simulated_annealing, "\nCusto" ,custo_simulated_annealing, "\nVoos:")
imprimir_voos(solucao_simulated_annealing)

print("\nAlgoritmo Generic Algorithm \n\nSolução: ",solucao_generic_algorithm, "\nCusto" ,custo_generic_algorithm, "\nVoos:")
imprimir_voos(solucao_generic_algorithm)



