# Tipos de operadores em Python

## Operadores aritméticos

- Soma: ‘+’, subtração: ‘-’
- Divisão: ‘/’, multiplicação: ‘*’
- Divisão inteira: ‘//’
- Módulo (resto da divisão): ‘%’
- Exponenciação: ‘**’

### Precedência dos operadores

1. Parêntesis
2. Expoêntes
3. Multiplicação e divisões (esquerda para a direita)
4. Somas e subtrações (esquerda para a direita)

## Operadores de comparação

### Igualdade

Retorna `true` quando a comparação for verdadeira e `false` quando não.

```python
saldo = 400
saque = 200
print(saldo == saque)
>>> False
```

### Diferença

Retorna `true` quando a comparação for verdadeira e `false` quando não.

```python
saldo = 400
saque = 200
print(saldo != saque)
>>> True
```

### Maior que / maior ou igual

Retorna `true` quando a comparação for verdadeira e `false` quando não.

```python
saldo = 400
saque = 200
print(saldo > saque)
>>> True

saldo = 400
saque = 200
print(saldo >= saque)
>>> True
```

### Menor que / menor ou igual

Retorna `true` quando a comparação for verdadeira e `false` quando não.

```python
saldo = 400
saque = 200
print(saldo > saque)
>>> False

saldo = 400
saque = 200
print(saldo >= saque)
>>> False
```

## Operadores de atribuição

### Atribuição simples

```python
saldo = 300

print(saldo)
>>> 300
```

### Atribuição com adição

```python
saldo = 300
saldo +=200

print(saldo)
>>> 500
```

> E assim como tenho atribuição com adição, temos atribuição com outros operadores. Por exemplo - `-=`, `*=`, `/=`, `//=`, `**=` e `%=`.
> 

## Operadores lógicos

> Operadores lógicos são utilizados em conjunto com operadores de comparação, para montar uma expressão lógica.
> 

### Operador `and`

```python
saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite
>>> False 
```

### Operador `or`

```python
saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite
>>> True 
```

### Operador `not`

```python
contatos_emergencia = []

not 1000 > 1500
>>> True

not contatos_emergencia // Lista vazia em python é considerado False
>>> True

not "saque 1500;" // A string é verdadeira pq tem valor
>>> False

not ""
>>> True
```

> Em python da pra negar valores dentro de uma sequência. Uma lista e uma string são sequências, uma lista é uma sequência de objetos e uma string é uma sequência de caracteres.
> 

### Parênteses

```python
saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque
>>> True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
>>> True
```

## Operadores de identidade

> São operadores utilizados para comparar de os dois objetos testados ocupam a mesma região de memória.
> 

```python
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 2000

curso is nome_curso // Ambos estão na mesma região de memória
>>> True

curso is not nome_curso
>>> False

saldo is limite // Ambos ocupam a mesma região de memória
>>> True
```

[https://pt.stackoverflow.com/questions/454193/como-o-python-gerencia-a-memória-durante-a-atribuição-de-diferentes-tipos](https://pt.stackoverflow.com/questions/454193/como-o-python-gerencia-a-mem%C3%B3ria-durante-a-atribui%C3%A7%C3%A3o-de-diferentes-tipos)

### Operadores de associação

> São operadores utilizados para verificar se um objeto está presente em uma sequência.
> 

```python
curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"Python" in curso
>>> True

"maçã" not in frutas
>>> True

200 in saques
>>> False

"Laranja" in frutas // o operador é "case sentive"
>>> False
```