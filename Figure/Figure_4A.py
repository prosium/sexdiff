import networkx as nx
import matplotlib.pyplot as plt
import os


plt.figure(figsize = (10, 9))

inputfile = open("input.txt")
g1 = nx.Graph()

allnodes = []
inputfile.readline()
for line in inputfile:
	elms = line.strip().split("\t")
	# print(elms)
	target1 = elms[2]
	target2 = elms[3]
	g1.add_node(target1)
	g1.add_node(target2)

inputfile.seek(0)
inputfile.readline()
for line in inputfile:
	elms = line.strip().split("\t")
	target1 = elms[2]
	target2 = elms[3]
	target3 = elms[5] # C and E

	if elms[7] == "Co_Occurence":
		g1.add_edge(target1, target2, color="tab:green")

	if elms[7] == "Mutually_Exclusive":
		g1.add_edge(target1, target2, color="tab:purple")


pos=nx.circular_layout(g1)

edges = g1.edges()

colors_edges = [g1[u][v]['color'] for u,v in edges]

nx.draw(g1, pos, with_labels = True, 
	edge_color=colors_edges, node_color="white",
	font_size=23, width=3)


# plt.show()
plt.autoscale()
plt.savefig("test.svg", bbox_inches='tight')
