# Manipulando Strings

## Métodos úteis da classe string

### Maiúscula, minúscula e título

```python
curso = "pytHon"

print(curso.upper())
>>> PYTHON

print(curso.lower())
>>> python

print(curso.title())
>>> Python
```

### Eliminando espaços em branco

```python
curso = "   Python  "

print(curso.strip())
>>> "Python"

print(curso.lstrip())
>>> "Python  "

print(curso.rstrip())
>>> "   Python"
```

### Junções e centralização

```python
curso = "Python"

print(curso.center(10, "#"))
>>> "##Python##"

print(".".join(curso)) # Após cada item o join adiciona o caractere 
											 # passado na instrução do join
>>> "P.y.t.h.o.n"
```

## Interpolação de variáveis

### Old style `%`

```python
nome = "Paulo"
idade = 24
profissao = "estudante"
linguagem = "python"

print("Olá, eu me chamo %s. Eu tenho %d anos, faço %d e manjo de %s". % 
(nome, idade, profissão, linguagem))
>>> Olá, eu me chamo Paulo. Eu tenho 24 anos, faço estudante e manjo de python
```

### Método `format`

```python
nome = "Paulo"
idade = 24
profissao = "estudante"
linguagem = "python"

print("Olá, eu me chamo {}. Eu tenho {} anos, faço {} e manjo de {}". 
.format(nome, idade, profissão, linguagem))
>>> Olá, eu me chamo Paulo. Eu tenho 24 anos, faço estudante e manjo de python

print("Olá, eu me chamo {0}. Eu tenho {1} anos, faço {2} e manjo de {3}". 
.format(nome, idade, profissão, linguagem))
>>> Olá, eu me chamo Paulo. Eu tenho 24 anos, faço estudante e manjo de python

print("Olá, eu me chamo {nome}. Eu tenho {idade} anos, faço {profissao} e manjo de {linguagem}". 
.format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
>>> Olá, eu me chamo Paulo. Eu tenho 24 anos, faço estudante e manjo de python

pessoa = {
	"nome": "Paulo"
	"idade": 24
	"profissao": "estudante"
	"linguagem": "python"
}

print("Olá, eu me chamo {nome}. Eu tenho {idade} anos, faço {profissao} e manjo de {linguagem}". 
.format(**pessoa))
>>> Olá, eu me chamo Paulo. Eu tenho 24 anos, faço estudante e manjo de python
```

### Método `f-string`

```python
nome = "Paulo"
idade = 24
profissao = "estudante"
linguagem = "python"

print(f"Olá, eu me chamo {nome}. Eu tenho {idade} anos, faço {profissao} e manjo de {linguagem}")
>>> Olá, eu me chamo Paulo. Eu tenho 24 anos, faço estudante e manjo de python
```

### Formatar strings com `f-string`

```python
pi = 3.14159

print(f"valor de pi: {pi:.2f}")
>>> "valor de pi: 3.14"

print(f"valor de pi: {pi:10.2f}") # adiciona 10 casas à esquerda
>>> "valor de pi:           3.14" 
```

## Fatiamento de strings

Fatiamento de string é uma técnica utilizada para retornar substrings (partes da string original), informando inicio (start), fim (stop) e passo (step): [start: stop[, step]].

```python
nome = "Paulo Henrique"

nome[0]
>>> "P"

nome[:4]        # Aqui não informamos o start [:] e nem o step
								# informando apenas o stop, então ele para na posição 5
>>> "Paulo"

nome[6:]        # Aqui não informamos o stop [:] e nem o step
								# informando apenas o start, então ele começa na posição 7
>>> "Henrique"

nome[6:8]
>>> "Hen"

nome[6:13:2]
>>> "Hniu"

nome[:]
>>> "Paulo Henrique"

nome[::-1]
>>> 'euqirneH oluaP'
```

### String multi-linhas

```python
nome = "Paulo"

mensagem = f"""
Olá meu nome é {nome},
vlw chefe!
"""
>>> OLá meu nome é Paulo,
vlw chefe!
```