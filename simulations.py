import networkx as nx
from Class_wrDCJ_Node import Node
from Class_extremities_and_adjacencies import Extremities_and_adjacencies
from Class_Network_wrDCJ import Network
from Class_GraphTheory_weighted import GraphTheory
from Class_Evolve import Node_evolve
import copy
import GenomeEvolve


number_of_simulations = 100

results = []
genomeB = [[1, 2,3,4, 5,6,7],[8,9, 10, 11, 12], [13, 14, 15, 16, 17], [18, 19, 20, 21]]
get_adjacencies = Extremities_and_adjacencies()
adjacencies_genomeB = get_adjacencies.adjacencies_ordered_and_sorted(genomeB)

for i in range(0, number_of_simulations):
    genomeB_copy = copy.deepcopy(genomeB)
    genomeA = get_adjacencies.adjacencies_to_genome(GenomeEvolve.evolve_genome(genomeB_copy))
    print(genomeB)
    print(genomeA)
    adjacencies_genomeA = get_adjacencies.adjacencies_ordered_and_sorted(genomeA)
    # Create start and target node
    start_node = Node(adjacencies_genomeA)
    target_node = Node(adjacencies_genomeB)

    # Construct entire network
    construct_network = Network(start_node, target_node, adjacencies_genomeB)
    network = construct_network.build_network()

    # graph = GraphTheory(network)

    paths = list(construct_network.get_all_shortest_paths(network, start_node, target_node))

    new_shortest_paths = (list(nx.all_shortest_paths(network, start_node, target_node, weight='weight')))
    rDCJ_shortest_paths = (list(nx.all_shortest_paths(network, start_node, target_node)))
    print(len(new_shortest_paths))
    print(len(rDCJ_shortest_paths))

    j = 1
    tot_b_trl = 0
    tot_u_trl = 0
    tot_inv = 0
    tot_trp1 = 0
    tot_trp2 = 0
    tot_fus = 0
    tot_fis = 0
    ave_b_trl = 0
    ave_u_trl = 0
    ave_inv = 0
    ave_trp1 = 0
    ave_trp2 = 0
    ave_fus = 0
    ave_fis = 0

    for path in new_shortest_paths:

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
                # print(get_adjacencies.adjacencies_to_genome(current.state))
                pass
            else:
                x = path[i - 1].children.index(current)
                operation_type = path[i - 1].children_operations[x][1]
                if operation_type == 'b_trl':
                    b_trl += 1
                elif operation_type == 'u_trl':
                    u_trl += 1
                elif operation_type == 'inv':
                    inv += 1
                elif operation_type == 'trp1':
                    trp1 += 1
                elif operation_type == 'trp2':
                    trp2 += 1
                elif operation_type == 'fus':
                    fus += 1
                elif operation_type == 'fis':
                    fis += 1

            i += 1
        # print('Path ', j )
        # print('inv: ', inv, '  trp1: ', trp1, '  trp2: ', trp2, '  b_trl: ', b_trl, '  u_trl: ', u_trl, '  fus: ', fus,
        #    '  fis: ', fis)
        tot_b_trl += b_trl
        tot_u_trl += u_trl
        tot_inv += inv
        tot_trp1 += trp1
        tot_trp2 += trp2
        tot_fus += fus
        tot_fis += fis
        j += 1

    # print('Totals')
    # print('inv: ', tot_inv, '  trp1: ', tot_trp1, '  trp2: ', tot_trp2, '  b_trl: ', tot_b_trl, '  u_trl: ', tot_u_trl, '  fus: ', tot_fus,
    #          '  fis: ', tot_fis)

    ave_b_trl = tot_b_trl / len(new_shortest_paths)
    ave_u_trl = tot_u_trl / len(new_shortest_paths)
    ave_inv = tot_inv / len(new_shortest_paths)
    ave_trp1 = tot_trp1 / len(new_shortest_paths)
    ave_trp2 = tot_trp2 / len(new_shortest_paths)
    ave_fus = tot_fus / len(new_shortest_paths)
    ave_fis = tot_fis / len(new_shortest_paths)

    print()
    print('Averages')
    print('inv: ', ave_inv, '  trp1: ', ave_trp1, '  trp2: ', ave_trp2, '  b_trl: ', ave_b_trl, '  u_trl: ', ave_u_trl,
          '  fus: ', ave_fus,
          '  fis: ', ave_fis)

    number_of_operations = ave_b_trl + ave_fis + ave_fus + ave_inv + ave_trp1 + (ave_trp2 * 2) + ave_u_trl

    results.append(
        [number_of_operations, len(new_shortest_paths), ave_inv, ave_trp1, ave_trp2, ave_b_trl, ave_u_trl, ave_fus,
         ave_fis])
    network.clear()

'''
get_adjacencies = Extremities_and_adjacencies()
adjacencies_genomeB = get_adjacencies.adjacencies_ordered_and_sorted(genomeB)

results = []
#for i in range(0, 10):
    genomeB = [[1, 2,3,4, 5,6,7],[8,9, 10, 11, 12], [13, 14, 15]]
    get_adjacencies = Extremities_and_adjacencies()
    adjacencies_genomeB = get_adjacencies.adjacencies_ordered_and_sorted(genomeB)
    adjacencies_genomeB_copy = copy.deepcopy(adjacencies_genomeB)
    genome = Node_evolve(state=adjacencies_genomeB_copy)
    print(get_adjacencies.adjacencies_to_genome(genome.state))
    print()
    genome.evolve(num_inv=1, num_b_trl=1, num_fis=1, num_fus=1, num_trp1=1, num_trp2=0, num_u_trl=1)
    print()
    adjacencies_genomeA = genome.state
    print(get_adjacencies.adjacencies_to_genome(genome.state))
    print('-----------')

    print(get_adjacencies.adjacencies_to_genome(adjacencies_genomeB))
    print(get_adjacencies.adjacencies_to_genome(adjacencies_genomeA))



    #Create start and target node
    start_node = Node(adjacencies_genomeA)
    target_node = Node(adjacencies_genomeB)

    #Construct entire network
    construct_network = Network(start_node, target_node, adjacencies_genomeB)
    network = construct_network.build_network()

    #graph = GraphTheory(network)



    paths = list(construct_network.get_all_shortest_paths(network, start_node, target_node))

    new_shortest_paths = (list(nx.all_shortest_paths(network, start_node, target_node, weight='weight')))
    rDCJ_shortest_paths = (list(nx.all_shortest_paths(network, start_node, target_node)))
    print(len(new_shortest_paths))
    print(len(rDCJ_shortest_paths))


    j = 1
    tot_b_trl = 0
    tot_u_trl = 0
    tot_inv = 0
    tot_trp1 = 0
    tot_trp2 = 0
    tot_fus = 0
    tot_fis = 0
    ave_b_trl = 0
    ave_u_trl = 0
    ave_inv = 0
    ave_trp1 = 0
    ave_trp2 = 0
    ave_fus = 0
    ave_fis = 0

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


            i+=1
        #print('Path ', j )
        #print('inv: ', inv, '  trp1: ', trp1, '  trp2: ', trp2, '  b_trl: ', b_trl, '  u_trl: ', u_trl, '  fus: ', fus,
          #    '  fis: ', fis)
        tot_b_trl += b_trl
        tot_u_trl += u_trl
        tot_inv += inv
        tot_trp1 += trp1
        tot_trp2 += trp2
        tot_fus += fus
        tot_fis += fis
        j+=1

    #print('Totals')
    #print('inv: ', tot_inv, '  trp1: ', tot_trp1, '  trp2: ', tot_trp2, '  b_trl: ', tot_b_trl, '  u_trl: ', tot_u_trl, '  fus: ', tot_fus,
    #          '  fis: ', tot_fis)

    ave_b_trl = tot_b_trl/len(new_shortest_paths)
    ave_u_trl = tot_u_trl/len(new_shortest_paths)
    ave_inv = tot_inv/len(new_shortest_paths)
    ave_trp1 = tot_trp1/len(new_shortest_paths)
    ave_trp2 = tot_trp2/len(new_shortest_paths)
    ave_fus = tot_fus/len(new_shortest_paths)
    ave_fis = tot_fis/len(new_shortest_paths)

    print()
    print('Averages')
    print('inv: ', ave_inv, '  trp1: ', ave_trp1, '  trp2: ', ave_trp2, '  b_trl: ', ave_b_trl, '  u_trl: ', ave_u_trl, '  fus: ', ave_fus,
              '  fis: ', ave_fis)

    number_of_operations = ave_b_trl+ave_fis+ave_fus+ave_inv+ave_trp1+(ave_trp2*2)+ave_u_trl

    results.append([number_of_operations, len(new_shortest_paths), ave_inv, ave_trp1, ave_trp2, ave_b_trl, ave_u_trl, ave_fus, ave_fis])
    network.clear()
'''


simulation_average = []
average_number_of_operations = 0
average_number_of_paths = 0
average_number_of_inv = 0
average_number_of_trp1 = 0
average_number_of_trp2 = 0
average_number_of_b_trl = 0
average_number_of_u_trl = 0
average_number_of_fus = 0
average_number_of_fis = 0
for element in results:
    print(element)
    average_number_of_operations+=element[0]
    average_number_of_paths+=element[1]
    average_number_of_inv+=element[2]
    average_number_of_trp1+=element[3]
    average_number_of_trp2+=element[4]
    average_number_of_b_trl+=element[5]
    average_number_of_u_trl+=element[6]
    average_number_of_fus+=element[7]
    average_number_of_fis+=element[8]

average_number_of_operations=average_number_of_operations/number_of_simulations
average_number_of_paths=average_number_of_paths/number_of_simulations
average_number_of_inv=average_number_of_inv/number_of_simulations
average_number_of_trp1=average_number_of_trp1/number_of_simulations
average_number_of_trp2=average_number_of_trp2/number_of_simulations
average_number_of_b_trl=average_number_of_b_trl/number_of_simulations
average_number_of_u_trl=average_number_of_u_trl/number_of_simulations
average_number_of_fus=average_number_of_fus/number_of_simulations
average_number_of_fis=average_number_of_fis/number_of_simulations

print()
print('average_number_of_operations: ', average_number_of_operations)
print('average_number_of_paths: ', average_number_of_paths)
print('average_number_of_inv: ', average_number_of_inv)
print('average_number_of_trp1: ', average_number_of_trp1)
print('average_number_of_trp2: ', average_number_of_trp2)
print('average_number_of_b_trl: ', average_number_of_b_trl)
print('average_number_of_u_trl: ', average_number_of_u_trl)
print('average_number_of_fus: ',average_number_of_fus)
print('average_number_of_fis: ', average_number_of_fis)