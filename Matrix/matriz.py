matriz_adj = [
	[0, 1],
	[1, 0]
]

print("--- 1. MATRIZ DE ADJACÊNCIA ---")
for linha in matriz_adj:
		print(linha)
		
dict_adj = {
	0: [1],
	1: [0]
}

print("\n--- 2. DICIONÁRIO DE ADJACÊNCIA ---")
for vertice, vizinhos in dict_adj.items():
	print(f"Vértice {vertice} conecta com: {vizinhos}")

matriz_inc = [
	[1],
	[1]
]

print("\n--- 3. MATRIZ DE INCIDÊNCIA ---")
print("Aresta 0")
for i, linha in enumerate(matriz_inc):
	print(f"Vértice {i}: {linha}")
