# Trabalhando com listas em Python

> Listas em Python são sequencias que podem armazenar qualquer tipo de objeto.
> 

```python
frutas = ['laranja', 'maca', 'uva']

frutas = []

letras = list('python') # cada letra será um elemento da lista

numeros = list(range(10))

carro = ['ferrari', 'f8', 4200000, 2020, 2900, 'sao paulo', True]

```

### Acesso direto

A lista é uma sequência, portanto podemos acessar seus dados utilizando índices. Contamos o índice de determinada sequência a partir do zero

```python
frutas = ['laranja', 'maca', 'uva']

frutas[0] # laranja
frutas[2] # uva
```

### índices negativos

Sequências suportam indexação negativa. A contagem começa em -1. 

```python
frutas = ['laranja', 'maca', 'uva']

frutas[-1] # uva
frutas[-3] # laranja
```

### Listas aninhadas

Listas podem armazenar todos os tipos de objetos em Python, portanto podemos ter listas que armazenam outras listas. Com isso podemos criar estruturas bidimensionais (tabelas), e acessar informações informando os índices de linha e coluna.

```python
matriz = [
	[1, 2, 3],
	[4, 5, 6],
]

matriz[0]      # [1, 2, 3]
matriz[0][0]   # 1
matriz[0][-1]  # 3
matriz[-1][-1] # 6
```

### Fatiamento

Além de acessar elementos diretamente, podemos extrair um conjunto de valor de uma sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursos de “pular” no acesso.

```python
lista = ['p', 'a', 'u', 'l', 'o']

lista[2:]   # ['u', 'l', 'o']
lista[0: 2] # ['p', 'a']
lista[::]   # ['p', 'a', 'u', 'l', 'o']
lista[::-1] # ['o', 'l', 'u', 'a', 'p']
```

### Iterar listas

```python
carros = ['gol', 'celta', 'palio']

for carro in carros:
	print(carro)
```

### Função enumerate

Às vezes é necessário saber qual índice do objeto dentro do laço `for`. Para isso podemos usar a função `enumerate.`

```python
carros = ['gol', 'celta', 'palio']

for indice, carro in enumerate(carros):
	print(f"Carro nº: {indice} é o {carro}.")
```

### Compressão de listas

A compressão de listas (list comprehension) oferece uma sintaxe mais curta quando você deseja: criar uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista aplicando algumas modificações nos elementos de uma lista existente.

```python
numeros = [1, 2, 3, 6, 7, 8, 12]
pare = []

for numero in numeros:
	if numero % 2:
		pares.append(numero)
```

```python
numeros = [1, 2, 3, 6, 7, 8, 12]
pares = [numero for numero in numero if numero % 2 == 0]

				# [retorno iteração condição]
```

Os únicos atributos necessarios são o retorno e a iteração. Para o exemplo acima `numero`é o retorno `for numero in numero` é a iteração e `if numero % 2 == 0` é a condição para retornar `numero`.

```python
numeros = [1, 2, 3, 6, 7, 8, 12]
quadrado = []

for numero in numeros:
	quadrado.append(numero**2)
```

```python
numeros = [1, 2, 3, 6, 7, 8, 12]
quadrado = [numero**2 for numero in numeros]
```

## Métodos da classe list

### Append

```python
lista = []
lista.append(1)
lista.append(10)
lista.append(100)
lista.append([1, 10, 100])

print(lista) # [1, 10, 100, [1, 10, 100]]
```

### Clear

```python
lista = [1, 10, 100, [1, 10, 100]]

lista.clear()
print(lista) # []
```

### Copy

```python
lista = [1, 10, 100, [1, 10, 100]]

l1 = lista.copy()        # oq é feito em l1 não reflete em lista

print(id(lista), id(l2)) # id's diferentes
```

### Count

```python
cores = ['vermelho', 'azul', 'amarelo', 'azul']

cores.count('vermelho') # 1
cores.count('azul')     # 2
cores.count('amarelo')  # 1
```

### Extend

```python
cores = ['vermelho', 'azul', 'amarelo', 'azul']

cores.extend(['verde', 'roxo']) # Junta duas listas, ao invés de colocar 
																# elemento por elemento

print(cores) # ['vermelho', 'azul', 'amarelo', 'azul', 'verde', 'roxo']
```

### Index

```python
cores = ['vermelho', 'azul', 'amarelo', 'azul']

cores.index('vermelho') # 0
cores.index('azul')     # 1 primeira ocorrencia do elemento
```

### Pop

```python
cores = ['vermelho', 'azul', 'amarelo', 'azul']

cores.pop()  # azul
cores.pop()  # amarelo
cores.pop(0) # vermelho
```

### Remove

```python
cores = ['vermelho', 'azul', 'amarelo', 'azul']

cores.remove('azul') # remove a primeira occorrencia

print(cores) # ['vermelho', 'amarelo', 'azul']
```

### Reverse

```python
cores = ['vermelho', 'azul', 'amarelo', 'azul']

cores.reverse()

print(cores) # ['azul', 'amarelo', 'azul', 'vermelho']
```

### Sort

```python
cores = ['vermelho', 'azul', 'amarelo', 'azul']
cores.sort() # ['amarelo', 'azul', 'azul', 'vermelho']

cores = ['vermelho', 'azul', 'amarelo', 'azul']
cores.sort(reverse=True) # ['vermelho', 'azul', 'azul', 'amarelo']

cores = ['vermelho', 'azul', 'amarelo', 'azul']
cores.sort(key=lambda x: len(x)) # ['azul', 'azul', 'amarelo', 'vermelho']

cores = ['vermelho', 'azul', 'amarelo', 'azul']
cores.sort(key=lambda x: len(x), reverse=True) # ['vermelho', 'amarelo', 'azul', 'azul']
```

> `lambda` é uma função anônima (função sem nome) e `x` é o argumento.
> 

### Len

```python
cores = ['vermelho', 'azul', 'amarelo', 'azul']

len(cores) # 4
```

### Sorted

```python
cores = ['vermelho', 'azul', 'amarelo', 'azul']

sorted(cores, key=lambda x: len(x))
```

> A diferenção é que o `sorted` é uma função built-en e o `sort` é um método do objeto list
>