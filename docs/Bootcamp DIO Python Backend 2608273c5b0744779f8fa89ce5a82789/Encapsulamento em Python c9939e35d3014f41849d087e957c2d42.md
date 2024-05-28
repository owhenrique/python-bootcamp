# Encapsulamento em Python

O encapsulamento descreve a ideia de agrupar dados e os métodos que manipulam esses dados em uma unidade. Isso impõe restrições ao acesso direto a variáveis e métodos e pode evitar a modificação acidental de dados. Para evitar alterações acidentais, a variável de um objeto só pode ser alterada pelo método desse objeto.

> Em um **diagrama de classes**, o sinal de `-` identifica o atributo privado e o sinal de `+` identifica atributos públicos.
> 

### Recursos públicos e privados

> Em Python não existem palavras reservadas para definir se um atributo é público ou privado, o interpretador não irá garantir a proteção do recursos. Então usam-se convenções para isto. Todos os recursos são públicos, a menos que o nome seja iniciado por um _.
> 

### Público

Pode ser acessado de fora da classe.

### Privado

Só pode ser acessado pela classe.

```python
class Conta:
	def __init__(self, saldo=0)
		self._saldo = saldo
	
	def depositar(self, valor):
		pass
	
	def sacar(self, valor):
		pass
```

## Properties

Com o property() do Python, você pode criar atributos gerenciados em suas classes. Você pode usar atributos gerenciados, também conhecidos como propriedades, quando precisar modificar sua implementação interna sem alterar a API pública da classe.

> Basicamente, o `@property` pega um método e transforma em uma propriedade. Dizer que a property é computada, significa dizer que ela pode ter uma ação para montar o valor de uma variável. Por exemplo, dentro de um property poderiamos fazer uma conexão com o banco de dados e recuperar o valor.
> 

```python
class Foo:
	def __init_(self, x=None):
		self._x = x
	
	@property                # decorator
	def x(self):
		return self._x or 0
		
	@x.setter                # setter para o property
	def x(self, value):
		_x = self._x or 0
		_value = value or 0
		self._x = _x + _value
		
	@x.deleter               # deleter para o property
	def x(self):
		self._x = -1
		
foo = Foo(10)
print(foo.x)              # sem o property não seria possivel fazer isto,
foo.x = 10								# pois o x é um método, seria necessario ()
```

> Basicamente, o **decorator**, é uma função que é executada antes da sua função. Sua sintaxe é colocar um `@` antes do nome.
>