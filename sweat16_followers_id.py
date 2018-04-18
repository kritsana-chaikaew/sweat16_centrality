import networkx as nx
import matplotlib.pyplot as plt
import pprint as pp
import json
import csv

with open('sweat16_followers_id.json') as f:
	content = f.readlines()

members = []
followers = []
member_followers = []
color = []
labels = {}

def degree_centrality(G):
	centrality = {}
	s = 1.0 / (len(G) - 1.0)
	centrality = {n: d * s for n, d in G.degree()}
	return centrality

for item in content:
	line = item.split(':')
	temp = line[0].split('"')
	members.append(temp[1])
	temp1 = line[1].split(',')
	for i in temp1:
		temp2 = i.strip()
		temp2 = temp2.strip("]}")
		followers.append(temp2)
	member_followers.append(followers)
	followers = []
G = nx.DiGraph()
G.add_nodes_from(members)

follower_nodes = []
mmm = 13
for k in range(mmm):
	for i in member_followers[k]:
		G.add_node(i)
		G.add_edge(i,members[k])
		follower_nodes.append(i)


for node in G.nodes():
	if node in members:
		labels[node] = node

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos,node_color="green",nodelist=follower_nodes, node_size=10)
nx.draw_networkx_nodes(G,pos,nodelist=members)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G,pos,labels,font_size=10,font_color = "yellow", node_size=200)
deg_c = degree_centrality(G)
with open('centrality.csv', 'w', newline='') as csvfile:
	fieldnames = ['name', 'degree centrality']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()

	deg_cen_dict = {}
	dict_for_write = {}
	for i in members:
		deg_cen_dict[i] = float(deg_c[i])
		dict_for_write['name'] = i
		dict_for_write['degree centrality'] = deg_cen_dict[i]
		writer.writerow(dict_for_write)
	pp.pprint(deg_cen_dict)

plt.axis('off')
plt.savefig("Graph2.png", format="PNG")
# plt.draw()
# plt.show()