import networkx as nx
from Class_wrDCJ_Node import Node

from Class_extremities_and_adjacencies import Extremities_and_adjacencies
from Class_Network_wrDCJ import Network


from Class_GraphTheory_weighted import GraphTheory

#genomeA = [[1, 2, 3, 5, 6, 4, 7, -8, 9]]
#genomeB = [[1, 2,3 ,4,5,6,7, 8, 9]]
genomeA = [[1,3, 4, 2],[5,6,7]]
genomeB = [[1, 2,3 ,4], [5, 6, 7]]
#genomeA = [[1,-3,-2, 4, 5,6,9,7], [8, 10],[ 11, 12]]
#genomeB = [[1, 2,3 ,4 , 5, 6, 7], [8, 9, 10,11, 12]]
#genomeA = [[1, 6, 7, 4, 5, 2, 3, -8, 9]]
#genomeB = [[1, 2,3 ,4,5,6,7, 8, 9]]
#genomeA = [[1,5,6,7,2,3,4,8]]
#genomeB = [[1,2,3,4,5,6,7,8]]

#genomeA = [[1,-4,-3, -2,5,6,11], [-7,-10,8,9]]
#genomeB = [[1,2,3,4], [5,6,7,8,9], [10,11]]

#genomeA = [[1,-4, -3, 6,7, -2, 5, 8, -9, 10]]
#genomeA = [[1, -4, 6, -3, -2, 5, 7]]
#genomeA = [[1,-3,-2,4,5,6,7]]
#genomeB = [[1,2,3,4,5,6,7,8, 9, 10]]
#from genes to adjacencies
get_adjacencies = Extremities_and_adjacencies()
adjacencies_genomeA = get_adjacencies.adjacencies_ordered_and_sorted(genomeA)
adjacencies_genomeB = get_adjacencies.adjacencies_ordered_and_sorted(genomeB)

print('Adjacencies of the genomes: ')
print('Genome A: ', adjacencies_genomeA)
print('Genome B: ', adjacencies_genomeB)
print('____________________________________')
print()
print()




#Create start and target node
start_node = Node(adjacencies_genomeA)
target_node = Node(adjacencies_genomeB)

#Construct entire network
construct_network = Network(start_node, target_node, adjacencies_genomeB)




network = construct_network.build_network()

graph = GraphTheory(network)

#plot the entire network in hierarchical structure (saved as 'hierarchical_network_plot.png')
graph.plot_network(start_node)

#prints out metrics
metrics_on_degree_sequence= graph.metrics_on_degree_sequence()

#calcute different centrality measures
centrality_measures = graph.centrality_algorithms()
pagerank = centrality_measures[0]
c_degree = centrality_measures[1]
c_closeness = centrality_measures[2]
c_betweenness = centrality_measures[3]

#plot the 4 different centrality measure on one graph (saved as 'centrality_measures_plot.png')
graph.plot_centrality_measures(start_node, pagerank, c_degree, c_closeness, c_betweenness)



paths = list(construct_network.get_all_shortest_paths(network, start_node, target_node))
print('number of paths: ', len(paths))
for path in paths:
    print(path)
    for element in path:

        print('children: ', element.children)
        print('wieghts: ', element.children_weights)
        print()
        print(element.state)
        for child in element.children:
            print('         ', child.state)

        #print(element.children_weights)
        print()

new_shortest_paths = (list(nx.all_shortest_paths(network, start_node, target_node, weight='weight')))
print(len(paths))
print(len(new_shortest_paths))



rDCJ_shortest_paths = (list(nx.all_shortest_paths(network, start_node, target_node)))

'''
print()
i=0
for path in rDCJ_shortest_paths:
    i=i+1
    print('PATH ', i)
    for element in path:
        adj = element.state
        print(get_adjacencies.adjacencies_to_genome(adj))
    print()
print('***************')
print()
'''
i=0
for path in new_shortest_paths:
    i=i+1
    print('PATH ', i)
    for element in path:
        adj = element.state
        print(get_adjacencies.adjacencies_to_genome(adj))
    print()