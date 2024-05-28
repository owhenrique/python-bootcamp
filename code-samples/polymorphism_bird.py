class Passaro:
    def voar(self):
        print("voando...")
	
class Pardal(Passaro):
	def voar(self):
		return super().voar()
		
class Avestruz(Passaro):
	def voar(self):
		print("avestruz nao voa")
		
def plano_de_voo(objeto):
	objeto.voar()
	
plano_de_voo(Pardal())
plano_de_voo(Avestruz())