import networkx as nx
import random
import MIS

size = 24
G = MIS.erdos_renyi(size=24, p=0.3)
G = MIS.random_geometric(size=24, k=0.3, connected=True)
G = MIS.random_bipartite(sizeA=int(size/2), sizeB=int(size/2), p=0.3, connected=True)

continuation_output = MIS.continuation(G)
lv_output = MIS.lotka_volterra(G, 1.3, [random.random() for node in G.nodes])
greedy_output = MIS.greedy(G)
exact_output = MIS.exact(G)

print(continuation_output)
print(lv_output)
print(greedy_output)
print(exact_output)

print(len(continuation_output))
print(len(lv_output))
print(len(greedy_output))
print(len(exact_output))


