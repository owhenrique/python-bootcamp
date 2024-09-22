# Decoradores em Python

Funções em Python são objetos de primeira classe, isso significa que, elas podem passadas e usadas como argumento.

```python
def dizer_oi(nome):
	return f"oi {nome}"
	
def incentivar_aprender(nome):
	return f"Oi {nome}, vamos aprender juntos"
	
def mensagem(funcao_mensagem, nome):
	return funcao_mensagem(nome)
	
	
mensagem(dizer_oi, 'Paulo')               # oi Paulo
mensagem(incentivar_aprender, 'Maria')    # Oi Maria, vamos aprender juntos

```

### Inner functions

É possível definir funções dentro de outras funções, essas funções são chamadas de `inner functions`. 

```python
def pai():
	print("escrevendo da pai() funcao")
	
	def filho1():
		print("escrevendo da filho1() funcao")
		
	def filho2():
		print("escrevendo da filho2() funcao")
		
	filho2()
	filho1()
	
	
pai()
```

> Python permite que use funções como valores de retorno
> 

```python
def calcular(operacao):
	def somar(a, b):
		return a+b
		
	def subtrair(a,b):
		return a-b
		
		
	if operacao == "+":
		return somar
		
	else:
		return subtrair
		
resultado = calcular("+")(1,3)
print(resultado)
```

## Decorador simples

```python
def meu_decorador(funcao):
	def envelope():          # inner function
		print("faz algo antes de executar a funcao") # exemplo, autenticação
			funcao()
		print("faz algo apos executar a funcao")
		
	return envelope
	
def ola_mundo():
	print("ola mundo")
	
ola_mundo = meu_decorador(ola_mundo) # para decorar uma função
ola_mundo()
```

> O Python permite que você use decoradores de mais simples com o símbolo @.
> 

```python
@meu_decorador
def ola_mundo():
	print("ola mundo")

ola_mundo()
```

### Funções de decoração com argumentos

Podemos usar *args e **kwargs na função interna, com isso ela aceitará um número arbitário de argumentos posicionais e de palavra-chave.

```python
def duplicar(func):
	def envelope(*args, **kwargs):
		func(*args, **kwargs)
		func(*args, **kwargs)
		
	return envelope
	
@duplicar
def aprender(tecnologia):
	print(f"estou aprendendo {tecnologia}")
	
aprender("Python")
```

O decorador pode decidir se retonar o valor da função decorada ou não. Para que o valor seja retornado a função de **envelope** deve retornar o valor da função decorada.

```python
def meu_decorador(funcao):
	def envelope(*args, **kwargs):          # inner function
		print("faz algo antes de executar a funcao") # exemplo, autenticação
		resultado = funcao(*args, **kwargs)
		print("faz algo apos executar a funcao")
		return resultado
		
	return envelope
	
@meu_decorador
def ola_mundo(nome):
	print(f"ola mundo {nome}")
	return nome.upper()

resultado = ola_mundo('Paulo')
print(resultado)

# ola mundo Paulo
# PAULO
```

### Introspecção

É a capacidade de um objeto saber sobre seus próprios atributos em tempo de execução.

```python
import functools

def meu_decorador(funcao):
	@functools.wraps
	def envelope(*args, **kwargs):          # inner function
		resultado = funcao(*args, **kwargs)
		return resultado
		
	return envelope
	
@meu_decorador
def ola_mundo(nome):
	print(f"ola mundo {nome}")
	return nome.upper()

print(ola_mundo.__name__)

# ola_mundo
# antes da instrospecção ela se perderia e printaria 'envelope', o decorador
```