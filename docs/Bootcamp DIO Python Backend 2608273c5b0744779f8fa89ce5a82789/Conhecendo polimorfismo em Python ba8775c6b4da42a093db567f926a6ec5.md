# Conhecendo polimorfismo em Python

Na programação, polimorfismo significa o mesmo nome de função (assinaturas diferentes) sendo usado para tipos diferentes. Um exemplo de polimorfismo é a função len(), ela se comporta de maneira diferente a medida que argumentos de tipos diferentes são passados na sua chamada.

```python
len("python")
len([10, 20, 30])
```

### Mesmo método com comportamento diferente

Na herança, a classe filha herda os métodos da classe pai, mas é possível modificar um método em uma classe filha herdada da classe pai. Isso é particularmente útil nos casos que o método herdado da classe pai não se encaixa perfeitamente na classe filha.

```python
class Passaro:
	def voar(self): pass
	
class Pardal(Passaro):
	def voar(self):
		print("pardal voa")
		
class Avestruz(Passaro):
	def voar(self):
		print("avestruz nao voa")
		
def plano_de_voo(passaro):
	passaro.voar()
	
plano_de_voo(Pardal())
plano_de_voo(Avestruz())
```