matriz_incidencia = [
	[1, 1, 0, 0],
	[1, 0, 1, 0],
	[0, 1, 1, 1],
	[0, 0, 0, 1]
]

def matriz_para_incidencia(matriz, coluna):
	if(coluna > (len(matriz[0]) - 1) or coluna < 0):
		return 
	print(f"Aresta {coluna}")
	for i, linha in enumerate(matriz):
		if(linha[coluna] == 1):
			print(f"Vértice {i}: [{linha[coluna]}]")

matriz_para_incidencia(matriz_incidencia, 2)
