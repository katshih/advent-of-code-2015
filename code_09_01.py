import networkx as nx

inputFile = open("advent-of-code-2015-inputs/input_09_test.txt", "r")
inputDat = inputFile.readlines()
inputFile.close()

cityGraph = nx.Graph()
for l in inputDat:
    startPoint = l.split()[0]
    endPoint = l.split()[2]
    distance = l.split()[-1]
    cityGraph.add_edge(startPoint, endPoint, weight = distance)
    
nx.algorithms.approximation.traveling_salesman.traveling_salesman_problem(cityGraph)
