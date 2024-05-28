# Programação Orientada a Objetos

Um **paradigma de programação** é um estilo de programação. É uma forma de se solucionar um problema. Por exemplo: 

- **Problema**: beber água
- **solução 1**: usar um copo pra beber água
- **solução 2**: usar uma garrafa para beber água

### Alguns paradigmas

- Imperativo ou procedural
- Funcional
- Orientado a eventos

### Paradigma Orientado a Objetos

O paradigma de programação orientada a objetos estrutura o código abstraindo problemas em objetos do mundo real, facilitando o entendimento do código e tornando-o mais mudular e extensível. Os dois conceitos chaves de POO são: **classes** e **objetos**.

## Classes e Objetos

As classes são algo abstrato que definem as características e métodos de um objeto (não podemos usá-la diretamente). Já os objetos possuem comportamentos e características que foram definidos nas classes.

```python
class Cachorro:
	def __init__(self, nome, cor, acordado=True):
		self.nome = nome
		self.cor = cor
		self.acordado = acordado
		
	def latir(self):
		print("auau")
	
	def dormir(self):
		self.acordado = False
		print("zzzZzzzZZZzzz...")
	

cao_1 = Cachorro("chappie", "amarelo", False)
cao_2 = Cachorro("aladim", "branco e preto")

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)
```

> `self` é uma referencia explícita para o objeto. Colocando `self`, queremos dizer que, esta é uma instância do objeto que foi passado (ele representa a instância do objeto).
> 

```python
def Bicicleta:
	def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
  def trocar_marcha(numero_marcha): # trocar_marcha(self, numero_marcha)
	  print("trocando marcha")
```

> `self` não é uma palavra reservada da linguagem, é apenas uma convenção, da forma que o método `trocar_marcha` foi escrito, o python entenderá que o `numero_marcha` é a instância do objeto e um não um atributo passado para a função.
> 

### Boas práticas

Ésta é uma boa prática de se escrever métodos:

```python
  def trocar_marcha(self, numero_marcha):
      print("trocando marcha...")

      def _trocar_marcha():
          if numero_marcha > self.marcha:
              print("marcha trocada...")
          else:
              print("marcha não trocada...")

      _trocar_marcha()
       
       
       
caloi.trocar_marcha(2)
```

## Construtores e Destrutores

### Método construtor

O método construtor sempre é executado quando uma nova instância da classe é criada. Nesse método incializamos o estado do nosso projeto. Para declarar o método construtor da classe, criamos um método com o nome `__init__`.

> Métodos `__alguma_coisa__` são métodos especiais.
> 

### Método destrutor

O método destrutor sempre é executado quando uma instância (objeto) é destruída. Destrutores em Python não são tão necessários quanto em C++ porque o Python tem um coletor de lixo que lida com o gerenciamento de memória automaticamente. Para declarar o método destrutor da classe, criamos um método com o nome `__del__`.

```python
def Bicicleta:
	def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
        print("Inicializando a instância da classe")
        
   def __del__(self):
			  print("Removendo a instância da classe")
			  
	caloi = Bicicleta("vermelho", "caloi", 2024, 1600)
	print(caloi.valor)
			  
	#  Print
	Inicializando a instância da classe
	1600
	Removendo a instância da classe
        
   
```

> `__init__` é o construtor e sempre será executado no início do processo de instanciação do objeto e o `__del__` é o oposto, ele sempre é executado no final. Utilizando a palavra reservada `del` conseguimos forçar a exclusão da instância antes do fim da instanciação do objeto.
>