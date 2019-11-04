import networkx as nx
from Class_wrDCJ_Node import Node

from Class_extremities_and_adjacencies import Extremities_and_adjacencies
from Class_Network_wrDCJ import Network


from Class_GraphTheory_weighted import GraphTheory

#genomeA = [[1, 2, 3, 5, 6, 4, 7, -8, 9]]
#genomeB = [[1, 2,3 ,4,5,6,7, 8, 9]]
#genomeA = [[1,4, 5, 2, 3,-6,7]]
#genomeB = [[1, 2,3 ,4], [5, 6, 7]]
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

#genomeA =[[-7, 16, -6], [-12, -11, -10, -9, -8, 1, 2, -3, 4, 5, -13], [-17, -15, -14]]


#genomeB = [[1, 2,3,4, 5,6,7],[8,9, 10, 11, 12], [13, 14, 15,16, 17]]


genomeA =[[1, 8, -10, -9, -5, -4, 11, 12, -15, -14, -3], [-7, -6, -13], [2]]
genomeB = [[1, 2,3,4, 5,6,7],[8,9, 10, 11, 12], [13, 14, 15]]
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
#graph.plot_network(start_node)

#prints out metrics
#metrics_on_degree_sequence= graph.metrics_on_degree_sequence()

#calcute different centrality measures
#centrality_measures = graph.centrality_algorithms()
#pagerank = centrality_measures[0]
##c_degree = centrality_measures[1]
#c_closeness = centrality_measures[2]
#c_betweenness = centrality_measures[3]

#plot the 4 different centrality measure on one graph (saved as 'centrality_measures_plot.png')
#graph.plot_centrality_measures(start_node, pagerank, c_degree, c_closeness, c_betweenness)



paths = list(construct_network.get_all_shortest_paths(network, start_node, target_node))
'''
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
'''
new_shortest_paths = (list(nx.all_shortest_paths(network, start_node, target_node, weight='weight')))
rDCJ_shortest_paths = (list(nx.all_shortest_paths(network, start_node, target_node)))
print(len(new_shortest_paths))
print(len(rDCJ_shortest_paths))




''''

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

i=0
for path in new_shortest_paths:
    i=i+1
    print('PATH ', i)
    for element in path:
        adj = element.state
        print(get_adjacencies.adjacencies_to_genome(adj))
    print()

'''
j = 1
tot_b_trl = 0
tot_u_trl = 0
tot_inv = 0
tot_trp1 = 0
tot_trp2 = 0
tot_fus = 0
tot_fis = 0
for path in new_shortest_paths:
    print()
    i = 0
    b_trl = 0
    u_trl = 0
    inv = 0
    trp1 = 0
    trp2 = 0
    fus = 0
    fis = 0
    while i < len(path):

        current = path[i]
        if i == 0:
            #print(get_adjacencies.adjacencies_to_genome(current.state))
            pass
        else:
            x = path[i-1].children.index(current)
            operation_type = path[i-1].children_operations[x][1]
            if operation_type == 'b_trl':
                b_trl+=1
            elif operation_type == 'u_trl':
                u_trl+=1
            elif operation_type == 'inv':
                inv+=1
            elif operation_type == 'trp1':
                trp1+=1
            elif operation_type == 'trp2':
                trp2+=1
            elif operation_type == 'fus':
                fus+=1
            elif operation_type =='fis':
                fis+=1
            #print(operation_type)


            #print(get_adjacencies.adjacencies_to_genome(current.state))

        i+=1
    print('Path ', j )
    print('inv: ', inv, '  trp1: ', trp1, '  trp2: ', trp2, '  b_trl: ', b_trl, '  u_trl: ', u_trl, '  fus: ', fus,
          '  fis: ', fis)
    tot_b_trl += b_trl
    tot_u_trl += u_trl
    tot_inv += inv
    tot_trp1 += trp1
    tot_trp2 += trp2
    tot_fus += fus
    tot_fis += fis
    j+=1

print('Totals')
print('inv: ', tot_inv, '  trp1: ', tot_trp1, '  trp2: ', tot_trp2, '  b_trl: ', tot_b_trl, '  u_trl: ', tot_u_trl, '  fus: ', tot_fus,
          '  fis: ', tot_fis)
