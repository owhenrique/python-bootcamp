# Conhecendo tuplas em Python

Tuplas são estruturas de dados parecidas com as listas, a principal diferença é que tuplas são imutáveis enquanto listas são mutáveis. Podemos criar tuplas através da classe `tuple`, ou colocando valores separados por virgula de parenteses. 

```python
frutas = ('laranja', 'pera', 'uva',)

letras = tuple('python')

numeros = ([1, 2, 3, 4])

pais = ('brasil', )
```

### Tuplas aninhadas

Tuplas podem armazenar todos os tipos de objetos em Python, portanto podemos ter tuplas que armazenam outras tuplas. Com isso podemos criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna.

```python
matriz =(
	(1, 2, 3),
	(4, 5, 6),
)

matriz[0] # (1, 2, 3)
matriz[0][0] # 1
```

Utilizamos tuplas quando temos certeza que não queremos alterar os valores de um objeto.

> Índices negativos, fatiamento, iteração, método enumerate, método count , método index e métodos len, funcionam da mesma forma que strings.
>