#grafo ponderado
grafo = {
	"Manga": {
		"São João das Missões": 23
	},
	
	"São João das Missões": {
		"Manga": 23,
		"Itacarambi": 25
	},
	
	"Itacarambi": {
		"São João das Missões": 25,
		"Januária": 59
	},
	
	"Januária": {
		"Itacarambi": 59,
		"Pedras de Maria da Cruz": 15
	},
	
	"Pedras de Maria da Cruz": {
		"Januária": 15,
		"Lontra": 35
	},
	
	"Lontra": {
		"Pedras de Maria da Cruz": 35,
		"Japonvar": 12
	},
	
	"Japonvar": {
		"Lontra": 12,
		"Mirabela": 35
	},
	
	"Mirabela": {
		"Japonvar": 35,
		"Montes Claros": 67
	},
	
	"Montes Claros": {
		"Mirabela": 67,
		"Bocaiuva": 47
	},
	
	"Bocaiuva": {
		"Montes Claros": 47
	}
}

def matriz_adj(matriz, grafo): #cria uma matriz da adjacência a partir de uma ponderada
	for cidade in grafo:
		linha = []

		for destino in grafo:
			if destino in grafo[cidade]:
				linha.append(grafo[cidade][destino])
			else:
				linha.append(0)
		
		matriz.append(linha)

#representação computacional
matriz = [] 
matriz_adj(matriz, grafo)

print("Representação computacional:")

for linha in matriz:
    print(linha)

def vizinhos(grafo): #mostra vizinhos
	for cidade in grafo:
		linha = []
		for vizinhos in grafo[cidade]:
			linha.append(vizinhos)
		print(f"{cidade}, Vizinhos: {linha}")

print("\nCidades e seus vizinhos:")
vizinhos(grafo)

def grau(grafo): #mostra peso dos vértices
	for cidade in grafo:
		grau = 0
		for vizinhos in grafo[cidade]:
			grau += grafo[cidade][vizinhos]
		print(f"{cidade}, Grau: {grau}")

print("\nGrau dos vértices: ")
grau(grafo)

cidades = list(grafo.keys())

print(cidades.index("Itacarambi"))
