# Ampliando o conhecimento em POO

## Variáves de classe e variáveis de instância

Todos os objetos nascem o mesmo número de atributos de classe e de instância. Atributos de instância são diferentes para cada objeto (cada objeto tem um cópia), já os atributos de classe são compartilhados entre os objetos. 

```python
class Estudante:
	escola = "DIO"       # variável de classe
	
	def __init__(self, nome, numero):
		self.nome = nome
		self.numero = numero
		
	def __str__(self):
		return f"{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"
		
		
gui = Estudante("guilherme", 5466)
gi = Estudante("giovanna", 1799)
```

### Métodos de classe e métodos estáticos

Métodos de classe estão ligados à classe e não ao objeto. Eles têm acesso ao estado da classe, pois recebem um parâmetro que aponta para a classe e não para instância do objeto. Já os métodos estáticos não recebem um primeiro argumento explícito. Ele também é um método vinculado à classe e não ao objeto da classe. Este método não pode acessar ou modificar o estado da classe.

### Métodos de classe x métodos estáticos

- Um método de classe recebe um primeiro parâmetro que aponta para a classe, enquanto um método estático não.
- Um método de classe pode acessar ou modificar o estado da classe enquanto um método estático não pode acessá-lo ou modificá-lo.

### Quanto utilizar métodos de classe ou estáticos

- Geralmente usamos o método de classe para criar métodos de fábrica (métodos de fábrica são aqueles que retornam instâncias daquela classe, exemplo, temos uma classe Pessoa e um método de fábrica para a classe Pessoa. Este método irá retornar uma nova instância de Pessoa).
- Geralmente usamos métodos estáticos para criar funções utilitárias (exemplo, dentro da classe Pessoa eu quero criar uma função que valide se a pessoa é ou não maior de idade).

## Interfaces e Classes Abstratas

> Interfaces definem o que uma classe deve fazer e não como. Em outras palavras, uma interface é uma forma para implementar algo seguindo um padrão, por exemplo, uma interface de Lapiseira, idependete da sua forma, seu grafite, a Lapiseira deve permitir que seu usuário escreva, deve permitir que ao apertar um botão o grafite desca e deve permitir a recarga do grafite.
> 

O conceito de interface é definir um contrato, onde são declarados os métodos (o que deve ser feito) e suas respectivas assinaturas. Em Python utilizamos classes abstratas para criar contratos. Classes abstratas não podem ser instânciadas. 

### Criando classes abstratas com o módulo ABC

Por padrão o Python não fornece classes abstratas. O Python vem com um módulo que fornece a base para definir as classes abstratas chamado ABC. O ABC funciona decorando métodos da classe base como abstratos e, em seguida, registrando classes concretas como implementações da classe abstrata. Um método se torna abstrato quando decorado com `@abstractmethod` .

> **Métodos Abstratos** não vão ter corpos (lógica implementada) necessáriamente e as classes que extendem (classes filhas) vão ser obrigadas a implementá-lo.
>