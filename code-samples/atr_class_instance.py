class Estudante:
	escola = "DIO"                          # variável de classe
	
	def __init__(self, nome, numero):
		self.nome = nome                    # nome e numero são variáveis de instância
		self.numero = numero                # lembrar-se do self (instância)
		
	def __str__(self) -> str:
		return f"{self.nome} - {self.numero} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
        
gui = Estudante("guilherme", 5466)
gi = Estudante("giovanna", 1799)
mostrar_valores(gui, gi)
gui.numero = 5477
Estudante.escola = "Python"
Estudante.nome = "default"                  # não altera os nomes pois nomes são variáveis de instância
paulo = Estudante("paulo", 8899)
mostrar_valores(gui, gi, paulo)