def fatorial(n):
	if(n <= 1):
		return 1;
	return ((n-1) * fatorial(n-1))

def viagem(n):
	if(n == 0):
		return 0
	return (int)(fatorial(n) / 2)

print(viagem(5));
