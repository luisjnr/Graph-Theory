#grafo ponderado das cidades
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
		
def percurso(grafo, origem, destino): #traça a rota, calcula a distância e guarda as distâncias de ponto a ponto
	if origem not in grafo:
		print("Origem não existe.")
		return
		
	if destino not in grafo:
		print("Destino não existe.")
		return
		
	distancias = {} #guarda distancia ate o destino
	
	for cidade in grafo: #inicializa distancia
		distancias[cidade] = float("inf")
		
	distancias[origem] = 0
	nova_distancia = 0
	atual = None #cidade atual
	visitadas = set() #guarda cidades já visitadas
	anteriores = {} #guarda cidades anteriores a cidade atual
	
	while (len(visitadas)) < (len(grafo)): #loop para descobrir a rota	
		menor_distancia = float("inf")
		
		for cidade in distancias: 
			if cidade not in visitadas: #analisa se a cidade já foi visitada
				if distancias[cidade] < menor_distancia: #se não foi, analisa se a rota dessa cidade é menor que a menor distância
					menor_distancia = distancias[cidade] #se for, atualiza a menor distância e a cidade atual
					atual = cidade
		
		visitadas.add(atual)
		
		for vizinho, distancia in grafo[atual].items(): #vizinho guarda as cidades vizinhas, e a distância a distância kkk
			nova_distancia = distancias[atual] + distancia #atualiza a nova distância
			if nova_distancia < distancias[vizinho]: #verifica se a distância do vizinho é menor que a nova distância
				distancias[vizinho] = nova_distancia #se for menor, atualiza o dicionário distancias e o anteriores
				anteriores[vizinho] = atual
		
		if menor_distancia == float("inf"):
			break
	
	if distancias[destino] == float("inf"):
		print("Não existe conexão entre a origem e o destino.")
		return
	
	atual = destino
	caminho = []
	
	while atual != origem: #cria o caminho partindo do destino até a origem
		caminho.append(atual) #utilizando o dicionário anteriores que registrou
		atual = anteriores[atual] #as cidades da origem até o destino
		
	caminho.append(origem) 
	caminho.reverse() #reverte a lista caminho, para que fique na ordem de origem a destino
	
	print(f"\nOrigem: {origem} ---- Destino: {destino}")
	print("Rota encontrada: ")
	for i in range((len(caminho)-1)): #printa a rota de ponto a ponto, e sua distância por ponto
		print(f"{caminho[i]} ---{grafo[caminho[i]][caminho[i+1]]}KM--- {caminho[i+1]}")
		
	print(f"Distância total: {distancias[destino]}KM")
		
print("\nPercurso: ")
percurso(grafo, "Itacarambi", "Montes Claros")

def delete(grafo, origem, destino):
	if origem not in grafo:
		print("Origem não existe.")
	if destino not in grafo:
		print("Destino não existe.")
	del grafo[origem][destino]
	del grafo[destino][origem]
	return True

delete(grafo, "Itacarambi", "Januária") 

def conexo(grafo, origem): #analisa conexidade do grafo
	if origem not in grafo:
		print("Origem não existe.")
		return

	visitadas = set()
	pilha = [origem] #cria uma pilha com a origem

	while pilha: #quando a pilha fica vázia, encerra
		atual = pilha.pop() #tira um item da pilha e adiciona em atual
		visitadas.add(atual) #adiciona atual nas cidades visitadas

		for cidade in grafo[atual]: #busca vizinhos da cidade atual
			if cidade not in visitadas: #adiciona na pilha se ainda não foi visitada
				pilha.append(cidade)
	
	if(len(visitadas) == len(grafo)): #verifica se todas as cidades do grafo foram visitadas
		print("Grafo conexo")
	else:
		print("Grafo desconexo")

print("\nConexidade")				
conexo(grafo, "Itacarambi")

def componentes(grafo): #separa o grafo em componentes
	visitados = set()
	componentes = [] #armazena os componentes

	for cidade in grafo: #percorre as cidades do grafo e escolhe uma que não foi visitada
		if cidade not in visitados:	
			cidades = []
			pilha = [cidade] #guardas a cidade atual em uma pilha
				
			while pilha:
				atual = pilha.pop() #recebe uma cidade da pilha
				visitados.add(atual)
				cidades.append(atual)
						
				for vizinho in grafo[atual]: #procura vizinhos e adiciona na pilha, caso não tenham sido visitados
					if vizinho not in visitados:
						pilha.append(vizinho)
		
			componentes.append(cidades)
	cont = 0	
	for componente in componentes:
		print(componente)	
		cont += 1
	print(f"Quantidade total de componentes: {cont}")

print("\nComponentes: ")
componentes(grafo)
