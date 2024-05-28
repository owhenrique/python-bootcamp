# Explorando conjuntos em Python

### Criando sets

Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.

```python
set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

set("abacaxi") # {'b', 'a', 'c', 'x', 'i'}

linguagens = {'python', 'java', 'python'} # {'java', 'python'}
```

### Acessando os dados

Conjuntos em Python não suportam indexação e nem fatiamento, caso queira acessar os seus valores é necessário converter o conjunto para lista.

```python
linguagens = {'python', 'java', 'python'} # {'java', 'python'}

linguagens = list(linguagens)

linguagens[0]
```

### Iterando em conjuntos

```python
carros = {'gol', 'fusca', 'voyage'}

for carro in carros:
	print(carro)
```

## Métodos da classe set

### Union

```python
conjunto_a = {1, 2}

conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) # {1, 2, 3, 4}
```

### Intersection

```python
conjunto_a = {1, 2, 3}

conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b) # {2, 3}
```

### Difference

```python
conjunto_a = {1, 2, 3}

conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}
```

### Symetric difference

```python
conjunto_a = {1, 2, 3}

conjunto_b = {2, 3, 4}

conjunto_a.symetric_difference(conjunto_b) # {1, 4}
```

### Subset

```python
conjunto_a = {1, 2, 3}

conjunto_b = {1, 2, 3, 4, 5}

conjuntos_a.issubset(conjunto_b) # True
conjuntos_b.issubset(conjunto_a) # False
```

### Superset

```python
conjunto_a = {1, 2, 3}

conjunto_b = {1, 2, 3, 4, 5}

conjuntos_a.issubset(conjunto_b) # False
conjuntos_b.issubset(conjunto_a) # True
```

### Disjoint

```python
conjunto_a = {1, 2, 3}

conjunto_b = {4, 5, 6}

conjunto_c = {0, 1}

conjuntos_a.isdisjoint(conjunto_b) # True
conjuntos_a.isdisjoint(conjunto_c) # False
```

### Add

```python
sorteio = {1, 23}

sorteio.add(32) # {1, 23, 32}
```

### Copy

```python
sorteio = {1, 23}

sorteio # {1, 23}
sorteio.copy()

sorteio # {1, 23}
```

### Discard

```python
sorteio = {1, 23}

sorteio.discard(1) # {23}
sorteio.discard(12) # {23}
```

### Pop

```python
sorteio = {1, 23}

sorteio.pop() # {23}
sorteio.pop() # {}
```

### Remove

```python
sorteio = {1, 23}

sorteio.remove(1) # {23}
sorteio.remove(12) # error
```

## Também temos alguns métodos semelhantes à listas

- `len`
- `in`