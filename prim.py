def span_tree(nodes, edges, N):

	INF = 10000000
	selected_node = [0, 0, 0, 0, 0, 0, 0]
	no_edge = 0
	selected_node[0] = True
	nd = N

	# printing for edge and weight
	print("Edge : Weight\n")
	while no_edge < nodes - 1:
		
		minimum = INF
		a = 0
		b = 0

		for m in range(nodes):
			if selected_node[m]:
				for n in range(nodes):
					if (not selected_node[n]) and edges[m][n]:
	# not in selected and there is an edge
						if minimum > edges[m][n]:
							minimum = edges[m][n]
							a = m
							b = n
		print(nd[int(a)] + "-" + nd[int(b)] + ":" + str(edges[a][b]))
		selected_node[b] = True
		no_edge += 1
	
def main():

	nodes = 7
	nd = ["a", "b", "c", "d", "e", "f", "g"]
	edges = [[0, 5, 3, 0, 0, 0, 0],
							[5, 0, 4, 6, 2, 0, 0],
							[3, 4, 0, 5, 0, 6, 0],
							[0, 6, 5, 0, 6, 6, 0],
							[0, 2, 0, 6, 0, 3, 5],
							[0, 0, 6, 6, 3, 0, 4],
							[0, 0, 0, 0, 5, 4, 0]]
	span_tree(nodes, edges, nd)

if __name__ == "__main__":
 main()