# o return encerra a execução da função corrente, voltando exatamente para o 
# ponto onde ela foi chamada. print mostra a variável no terminal, podendo ser string, int, etc.
while True:
	try:
		pedido = int(input('Digite um número positivo inteiro: '))

		if pedido < 0:
			print('Digite um número positivo')
			continue
	except ValueError:
		print('O número não é inteiro')
		continue
		
	print(f'A soma de todos os números naturais até {pedido} é:', sum(range(1, pedido + 1)), '\n\nTente Novamente🤓👇')