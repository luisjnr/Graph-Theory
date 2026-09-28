import os

from Transporte import (
    grafo,
    matriz_adj,
    vizinhos,
    grau,
    percurso,
    delete,
    conexidade,
    componentes
)

def menu():
	opc = int(input("1 - Representação computacional\n"
	"2 - Vizinhos\n3 - Grau\n4 - Percurso\n5 - Delete\n"
	"6 - Conexidade\n7 - Componentes\n8 - Encerrar\n"))
	os.system("clear")
	return opc

while True:
	match menu():
		case 1:	matriz_adj(grafo)
		case 2: vizinhos(grafo)	
		case 3:	grau(grafo)
		case 4: percurso(grafo, input("Digite a origem: "), input("Digite o destino: "))
		case 5: print(("Sucesso!\n" if delete(grafo, input("Digite a origem: "), input("Digite o destino: ")) 
		else "Falha.\n"))	
		case 6: conexidade(grafo, input("Digite a origem: "))
		case 7:	componentes(grafo)
		case 8: exit()
		case _:	print("Digite uma opção válida.")
		
