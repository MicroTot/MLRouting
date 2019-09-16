import networkx as nx
import matplotlib.pyplot as plt
from classes.bfs import BfsTraverser
G = nx.Graph()
nodes=["Karen","J6","Gitaru","J1","J4","J7", "J8", "Loresho", "J9", "J10", "Lavi", "Parklands", "J11", "Kilimani", "J5", "J12", "CBD", "J2", "J3", "Langata", "J13", "IMARA", "Donholm", "Hillview", "Kasa", "Kahawa"]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes
#Add Edges and their weights
G.add_edge("Karen","J1",weight="2")
G.add_edge("Karen","J6",weight="4")
G.add_edge("J1","J4",weight="2")
G.add_edge("J6","Gitaru",weight="10")
G.add_edge("J6","J7",weight="6")
G.add_edge("J6","J4",weight="6")
G.add_edge("Gitaru","J7",weight="6")

G.add_edge("J7","J8",weight="7")
G.add_edge("J8","Loresho",weight="2")
G.add_edge("J8","J9",weight="3")
G.add_edge("J9","J10",weight="4")
G.add_edge("J9","Lavi",weight="7")
G.add_edge("J10","Parklands",weight="3")
G.add_edge("J10","J11",weight="7")
G.add_edge("Lavi","J11",weight="0.5")
G.add_edge("J11","Kilimani",weight="0.5")
G.add_edge("J5","Kilimani",weight="0.5")
G.add_edge("J4","J5",weight="9.7")
G.add_edge("Kilimani","J12",weight="2.3")
G.add_edge("J12","CBD",weight="1.5")
G.add_edge("J1","J2",weight="6")
G.add_edge("J2","J3",weight="5.4")
G.add_edge("J3","J12",weight="6.7")
G.add_edge("J2","Langata",weight="2.6")
G.add_edge("CBD","J13",weight="5.5")
G.add_edge("J13","IMARA",weight="3.9")
G.add_edge("IMARA","Donholm",weight="10.4")
G.add_edge("Hillview","Donholm",weight="20")
G.add_edge("Hillview","Kasa",weight="1.7")
G.add_edge("Kahawa","Kasa",weight="11.5")
G.add_edge("J3","J13",weight="6.2")



#position the nodes to resemble Nairobis map
G.node["Karen"]['pos']=(0,0)
G.node["J6"]['pos']=(0,2)
G.node["J1"]['pos']=(1,-2)
G.node["J4"]['pos']=(2,-2)
G.node["J7"]['pos']=(0,4)

G.node["J8"]['pos']=(1, 4)
G.node["Loresho"]['pos']=(1, 6)
G.node["J9"]['pos']=(2, 4)
G.node["J10"]['pos']=(3, 4)
G.node["Lavi"]['pos']=(2,2)
G.node["Parklands"]['pos']=(4,5)
G.node["J11"]['pos']=(3,2)
G.node["Kilimani"]['pos']=(4,0.7)
G.node["J5"]['pos']=(3,-2)
G.node["J12"]['pos']=(5,0)
G.node["CBD"]['pos']=(6.5,0)
G.node["J2"]['pos']=(1.5,-3)
G.node["J3"]['pos']=(2.6,-3)
G.node["Langata"]['pos']=(1.5,-4.5)
G.node["J13"]['pos']=(6.5,-2)
G.node["IMARA"]['pos']=(7.5,-3)
G.node["Donholm"]['pos']=(7.5,1)
G.node["Hillview"]['pos']=(7.5,2.5)
G.node["Kasa"]['pos']=(7.5,4.25)
G.node["Kahawa"]['pos']=(8.8,5.5)
G.node["Gitaru"]['pos']=(-1,3)

#store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')
#call BFS to return set of all possible routes to the goal
route_bfs = BfsTraverser()
routes = route_bfs.BFS(G,"Karen","IMARA")
print(route_bfs.visited)
route_list = route_bfs.visited
#color the nodes in the route_bfs
node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list,route_list[1:]))
#color the edges as well
#print(peru_colored_edges)
edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos,width=2,edge_color= edge_col)
nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)
plt.axis('off')
plt.show()


