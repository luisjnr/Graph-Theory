matriz_adj = [
	[0, 1],
	[1, 0]
]

def matriz_para_dicionario(matriz):
	dict_adj = {}
	
	for i, linha in enumerate(matriz):
		vizinhos = []
		
		for j, valor in enumerate(linha):
			if valor == 1:
				vizinhos.append(j)
		
		dict_adj[i] = vizinhos
	
	return dict_adj
	
for vertice, vizinhos in matriz_para_dicionario(matriz_adj).items():
	print(f"Vértice {vertice} conecta com: {vizinhos}")
	
