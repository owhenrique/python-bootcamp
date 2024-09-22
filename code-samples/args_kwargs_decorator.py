def meu_decorador(funcao):
	def envelope(*args, **kwargs):                   # inner function
		print("faz algo antes de executar a funcao") # exemplo, autenticação
		funcao(*args, **kwargs)
		print("faz algo apos executar a funcao")
		
	return envelope

@meu_decorador	
def ola_mundo(nome):
	print(f"ola mundo {nome}")
	
ola_mundo('Paulo')