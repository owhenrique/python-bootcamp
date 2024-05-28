# Dominando funções em Python

Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros, esses parâmetros podem ou não ter valores padrão. Usar funções torna o código mais legível e possibilita o reaproveitamento de código. Programar baseado em funções, é o mesmo que dizer que estamos programando de maneira estruturada. 

```python
def exibir_mensagem():
	print('olá mundo')
	
def exibir_mensagem_2(nome):
	print(f'seja bem vindo {nome}')
	
def exibir_mensagem_3(nome='antonio'): # desta forma passar o argumento se torna
	print(f'seja bem vindo {nome}')      # opcional, caso não seja passado, não
	                                     # retornará erro    
exibir_mensagem()
exibir_mensagem_2(nome='paulo')
exibir_mensagem_3()
exibir_mensagem_3(nome='maria')
```

### Retornando valores

Para retornar um valor, utilizamos a palavra reservada `return`. Toda função em Python retorna `None` por padrão. Diferente de outras linguagens de programação, em Python uma função pode retornar mais de um valor.

```python
def calcular_total(numeros):
	return sum(numeros)
	
def retorna_antecessor_esucessor(numero):
	antecessor = numero - 1
	sucessor = numero + 1
	
	# Este return irá retornar uma tupla, pois, uma tupla é uma estrutura imutável
	# e o retorno é de multiplos valores
	return antecessor, sucessor
	
print(calcular_total([1, 2, 3]))
print(retorna_antecessor_e_sucessor(10))
```

### Argumentos nomeados

```python
def salvar_carro(marca, modelo, ano, placa):
	print(f'carro inserido com sucesso {marca}/{modelo}/{ano}/{placa})
	
salvar_carro('fiat', 'palio', 2000, 'abc-1234')
salvar_carro(marca='fiat', modelo='palio', ano='2000', placa='abc-1234')

# A forma abaixo passa os argumentos como dicionário, e os ** são necessários 
# para que na interpretação do código o compilador entenda que este dicionário
# contem argumentos da função
salvar_Carro(**{
	'marca': 'fiat', 
	'modelo': 'palio', 
	'ano': 2000, 
	'placa': 'abc-1234'
})

```

### Args e kwargs

Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos (*args e **kwargs), o método recebe os valores como tupla e dicionário respectivamente.

> Os nomes `args` (tupla) e `kwargs` (dicionário) são apenas convenções. Poderiam ser utilizados outros nomes para representar isso.
> 

```python
def exibir_poema(data_extenso, *args, **kwargs):
	texto = "\n".join(args)
	meta_dados = "\n".join([f'{chave.title()}: {valor}' for chave, valor in 
	kwargs.items()])
	mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
	print(mensagem)
	
exibir_poema(
	'Sexta, 26 de agosto, 2024',
	'Zen of Python', 
	'Beautiful is better then ugly.', 
	author='tim peters',
	ano=1999
)

# então em texto eu estou inserindo uma tupla (argumentos dentro de um paratênsis)
# separados por virgulas:
#	 Zen of Python 
#	 Beautiful is better then ugly.

# em meta_dados estou inserindo argumentos na estrutura (chave:valor):
# author: tim peters
# ano: 1999
```

## Parâmetros especiais

Por padrão, argumentos podem ser passados para uma função Python tanto por posição quanto explicitamente pelo nome. Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pela qual argumentos possam ser passados, assim um desenvolvedor precisa apenas olhar para a definção da função para determinar se os itens são passados **por posição, por posição e nome ou por nome.**

### Positional only

```python
# antes da barra os parametros só podem ser nomeados por posição
# após eles podem ser por posição ou por nome
def criar_carro(modelo, ano, placa, /, marca, motor, combustível):
	print(modelo, ano, placa, marca, motor, combustível)
	
criar_carro('palio', 1999, 'abc-1234', marca='fiat', 
	motor='1.0', combustivel='gasolina')
```

### Keyword only

```python
# após o asterisco, os parametros só podem ser passados por nome
def criar_carro(*, modelo, ano, placa, marca, motor, combustível):
	print(modelo, ano, placa, marca, motor, combustível)
	
criar_carro(modelo='palio', ano=1999, placa='abc-1234', marca='fiat', 
	motor='1.0', combustivel='gasolina')
```

### Keyword and positional only

```python
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustível):
	print(modelo, ano, placa, marca, motor, combustível)
	
criar_carro('palio', 1999, 'abc-1234', marca='fiat', 
	motor='1.0', combustivel='gasolina')
```

## Objetos de primeira classe

Em Python tudo é objeto, dessa forma **funções também objetos o que as tornam objetos** de primeira classe. Com isso podemos **atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em estruturas de dados** (tuplas, listas, dicionários, etc) e usar como valor de retorno para uma função (closures).

```python
def somar(a, b):
	return a + b
	
def subtrair(a, b)
	return a - b
	
def exibir_resultado(a, b, funcao):
	resultado = funcao(a, b)
	print(f'o resultado da operacao entre {a} e {b} e {resultado})
	
exibir_resultado(a, b somar)
exibir_resultado(a, b subtrair)

op = somar
print(op(1, 2))
```

### Escopo local e escopo global

Python trabalha com escopo local e global, dentro do bloco da função o escopo é local. Portanto alterações feitas ali em objetos imutáveis serão perdidas quando o método terminar de ser executado. Para usar objetos globais utilizamos a palavra-chave **global,** que informa ao interpretador que o a variável está sendo manipulada no escopo local é global. ****Essa **NÃO é uma boa prática e deve ser evitada.**

```python
salario = 2000
lista = [1]

def salario_bonus(bonus):
	global salario
	salario += bonus
	return salario
	
def acresce_lista(lista):
	# listas são objetos imutáveis e, dentro da função, todas as operações serão
	# refletidas no objeto fora do escopo
	lista.append(2)
	
	# caso queira fazer uma alteração local na lista, utilize uma cópia
	nova_lista = lista.copy()
	nova_lista.append(2)
	
salario_bonus(500)
```